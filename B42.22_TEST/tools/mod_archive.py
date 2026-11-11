#!/usr/bin/env python3
"""Generate the B42.22_TEST mod archive from the live test lab.

The documentation lives in Grsh_PZ_Modpack/B42.22_TEST, while the actual
profile and mod library live in the sibling A004/B42.22_TEST lab.  This keeps
the repository free of mod binaries and avoids a second, drifting copy.

Usage (from B42.22_TEST):
  python tools/mod_archive.py --profile b422-batch2
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LAB_DEFAULT = ROOT.parent.parent / "B42.22_TEST"
CATALOG = ROOT / "tools" / "mod_catalog.json"
TIMES = ROOT / "tools" / "workshop_times.json"
GAME_VERSION = (42, 22, 0)

BLOCK_COMMENT = re.compile(r"/\*.*?\*/", re.S)
LINE_COMMENT = re.compile(r"//[^\n]*")
MODULE_RE = re.compile(r"^\s*module\s+([A-Za-z0-9_]+)", re.M)
ITEM_RE = re.compile(r"^[ \t]*item[ \t]+([A-Za-z_][A-Za-z0-9_]*)[ \t]*(?:\{|$)", re.M)
VEHICLE_RE = re.compile(r"^\s*vehicle\s+([A-Za-z0-9_]+)\s*\{?", re.M)
RECIPE_RE = re.compile(r"^\s*(?:craftRecipe|recipe)\s+([A-Za-z0-9_]+)", re.M)
PROP_RE = r"^\s*{key}\s*=\s*(.+?)\s*,?\s*$"
BAD_NAME = re.compile(r'[<>:\"/\\|?*\s]+')

README_GROUPS = [
    ("核心框架与渲染", {
        "ZombieBuddy", "Viewpoint", "ViewpointRightClick", "ViewpointRoofs",
        "ViewpointBarricade",
    }),
    ("角色与外观", {"AimohPmxPreview", "VariableSkinSFW", "VariableSkinFix"}),
    ("界面、库存与制作", {
        "NeatUI_Framework", "Neat_Crafting", "Project_Cook", "CleanUI",
        "CleanHotBar", "BetterSorting", "ProximityInventory",
        "P4TidyUpMeister", "MapLegendUI", "B42SandboxOptions",
    }),
    ("工具与调试", {"DebugMenu", "WhereAmI"}),
    ("性能优化", {"PzPerformanceFixes", "SuPerfCore"}),
    ("KI5 载具系列", {
        "damnlib", "YetAnotherPZLib", "KI5trailers", "isoContainers",
        "92amgeneralM998", "70dodge", "91range", "88chevyS10", "92nissanGTR",
        "84mercW460", "87fordB700", "90fordF350ambulance", "86fordE150",
        "78amgeneralM35A2", "82jeepJ10",
    }),
    ("玩法与移动", {"Ladders Collapsible"}),
    ("修复与兼容", {"FixNaNStats"}),
    ("汉化", {"LaoYuTranslationJava", "B42ModTrans_CN_As1", "B42Trans_CN_As1"}),
]


def vtuple(text: str) -> tuple[int, int, int]:
    parts = [int(x) for x in re.findall(r"\d+", text or "")[:3]]
    return tuple(parts + [0] * (3 - len(parts)))  # type: ignore[return-value]


def parse_info(path: Path) -> dict:
    out: dict = OrderedDict()
    try:
        text = path.read_text(encoding="utf-8-sig", errors="replace")
    except OSError:
        return out
    for line in text.splitlines():
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        key, value = key.strip().lower(), value.strip()
        if key and value:
            out[key] = value
    return out


def read_info(folder: Path) -> dict:
    """Prefer the newest mod.info compatible with B42.22.

    A package can contain many version folders.  Taking the first mod.info
    makes CleanUI look like a 42.12 mod even though the active copy is 42.22.
    """
    infos = sorted(folder.rglob("mod.info"))
    parsed = [(p, parse_info(p)) for p in infos]
    if not parsed:
        return {}
    compatible = []
    for path, info in parsed:
        lo = vtuple(info.get("versionmin", ""))
        hi = vtuple(info.get("versionmax", ""))
        if lo <= GAME_VERSION and (hi == (0, 0, 0) or GAME_VERSION <= hi):
            compatible.append((lo, str(path), path, info))
    if compatible:
        _, _, chosen_path, chosen = max(compatible, key=lambda x: x[0])
    else:
        _, _, chosen_path, chosen = max(
            [(vtuple(i.get("versionmin", "")), str(p), p, i) for p, i in parsed],
            key=lambda x: x[0],
        )
    out = dict(chosen)
    # Fill missing presentation fields, but never borrow another version's bounds.
    for path, info in parsed:
        if path == chosen_path:
            continue
        for key, value in info.items():
            if key not in out and key not in {"versionmin", "versionmax"}:
                out[key] = value
    return out


def strip_comments(text: str) -> str:
    return LINE_COMMENT.sub("", BLOCK_COMMENT.sub("", text))


def script_facts(folder: Path) -> dict:
    items: "OrderedDict[str, dict]" = OrderedDict()
    vehicles: list[str] = []
    recipes: list[str] = []
    for f in sorted(folder.rglob("*.txt")):
        if "scripts" not in f.parts:
            continue
        try:
            text = strip_comments(f.read_text(encoding="utf-8-sig", errors="replace"))
        except OSError:
            continue
        module = "Base"
        m = MODULE_RE.search(text)
        if m:
            module = m.group(1)
        recipes += [x.group(1) for x in RECIPE_RE.finditer(text)]
        vehicles += [x.group(1) for x in VEHICLE_RE.finditer(text)]
        for m in ITEM_RE.finditer(text):
            block = text[m.end():m.end() + 900].split("}", 1)[0]
            disp = re.search(PROP_RE.format(key="DisplayName"), block, re.M)
            typ = re.search(PROP_RE.format(key="Type"), block, re.M) or re.search(
                PROP_RE.format(key="ItemType"), block, re.M
            )
            items.setdefault(f"{module}.{m.group(1)}", {
                "display": disp.group(1).strip().strip('"') if disp else "",
                "type": typ.group(1).strip().strip('"') if typ else "",
            })
    return {"items": items, "vehicles": vehicles, "recipes": recipes}


def dir_stats(folder: Path) -> dict:
    out = Counter()
    for f in folder.rglob("*"):
        if not f.is_file():
            continue
        out["files"] += 1
        try:
            out["bytes"] += f.stat().st_size
        except OSError:
            pass
        suffix = f.suffix.lower()
        if suffix == ".lua":
            out["lua"] += 1
        elif suffix in (".png", ".dds", ".jpg", ".tga"):
            out["textures"] += 1
        elif suffix in (".fbx", ".x", ".obj", ".glb", ".gltf"):
            out["models"] += 1
        if "client" in f.parts and suffix == ".lua":
            out["lua_client"] += 1
        if "server" in f.parts and suffix == ".lua":
            out["lua_server"] += 1
        if "Translate" in f.parts:
            out["translate"] += 1
        if suffix == ".java":
            out["java"] += 1
        if suffix in (".jar", ".class"):
            out["jar"] += 1
    for key in ("files", "bytes", "lua", "textures", "models",
                "lua_client", "lua_server", "translate", "java", "jar"):
        out.setdefault(key, 0)
    return out


def human(size: int) -> str:
    value = float(size)
    for unit in ("B", "KB", "MB", "GB"):
        if value < 1024 or unit == "GB":
            return f"{value:.0f} {unit}" if unit == "B" else f"{value:.1f} {unit}"
        value /= 1024.0
    return f"{value:.1f} GB"


def pick_root(lib: Path, wid: str, folder: str) -> Path:
    candidate = lib / wid / "mods" / folder
    return candidate if candidate.is_dir() else lib / wid


def catalog_key(wid: str, folder: str, duplicate_wids: set[str]) -> str:
    return f"{wid}-{folder.lower()}" if wid in duplicate_wids else wid


def sanitize(text: str) -> str:
    text = text.replace("&", "and")
    text = re.sub(r"[<>:\"/\\|?*\[\](),'`]+", "", text)
    text = re.sub(r"\s+", "_", text.strip())
    return re.sub(r"_+", "_", text).strip("_")


def file_name(row: dict) -> str:
    original = sanitize(row["info"].get("name") or row["folder"])
    brief = sanitize(row["cat"].get("brief") or "无简介")
    return f"{row['wid']}_{original}_{brief}.md"


def dist_label(value: str) -> str:
    return {"both": "both（双端）", "client": "client（仅客户端）",
            "server": "server（仅服务端）"}.get(value, value)


def read_times() -> dict[str, str]:
    if not TIMES.is_file():
        return {}
    return json.loads(TIMES.read_text(encoding="utf-8"))


def readme_group(folder: str) -> str:
    for name, folders in README_GROUPS:
        if folder in folders:
            return name
    return "其他"


def render_doc(row: dict, profile: str) -> str:
    info, stats, facts, cat = row["info"], row["stats"], row["facts"], row["cat"]
    name = info.get("name") or row["folder"]
    cn = cat.get("cn") or name
    title = f"{cn}（{name}）" if cn != name else name
    req = (info.get("require") or "").replace("\\", " ").strip()
    bad = (info.get("incompatible") or "").replace("\\", " ").strip()
    java_txt = ""
    if stats["java"] or stats["jar"]:
        java_txt = f"；Java 源码 {stats['java']}、jar/class {stats['jar']}"
    lines = [
        f"# {title}",
        "",
        f"**{cat.get('brief', '')}** · 分类：{cat.get('cat', '-')} · "
        f"`{row['wid']}` · {'启用' if row['enabled'] else '禁用'} · "
        f"加载位次 {row['load'] or '未列'}",
        "",
        "## 它做什么",
        "",
        cat.get("what", "（待补：这个 mod 的作用）"),
        "",
        "## 概览",
        "",
        "| 项 | 值 |",
        "| --- | --- |",
        f"| 工作坊 ID | `{row['wid']}` |",
        f"| mod id | `{info.get('id', '-')}` |",
        f"| 文件夹 | `{row['folder']}` |",
        f"| 版本 / 适配 | `{info.get('versionmin', '-')}` … `{info.get('versionmax', '-')}` |",
        f"| 作者 | {info.get('author', '-')} |",
        f"| 工作坊更新时间 | {row['updated']} |",
        f"| 分发端 | {dist_label(row['distribution'])} |",
        f"| 体积 / 文件 | {human(stats['bytes'])} · {stats['files']:,} 文件"
        f"（lua {stats['lua']}，client {stats['lua_client']}，server {stats['lua_server']}；"
        f"贴图 {stats['textures']}；模型 {stats['models']}；翻译 {stats['translate']}{java_txt}） |",
        "",
        "## 依赖与冲突",
        "",
        f"- 需要：{('`' + req + '`') if req else '无'}",
        f"- 互斥：{('`' + bad + '`') if bad else '无'}",
        f"- 被依赖：{('、'.join('`' + x + '`' for x in row['required_by'])) if row['required_by'] else '无（叶子节点）'}",
        "",
        "## 内容清单",
        "",
    ]
    items = facts["items"]
    if items:
        lines += [f"脚本物品 **{len(items)}** 条：", ""]
        if len(items) <= 60:
            lines += ["| 完整 id | 显示名 | 类型 |", "| --- | --- | --- |"]
            lines += [
                f"| `{key}` | {value['display'] or '-'} | {value['type'] or '-'} |"
                for key, value in items.items()
            ]
        else:
            by_type = Counter(value["type"] or "?" for value in items.values())
            lines += ["按类型：" + "，".join(f"{t} × {n}" for t, n in by_type.most_common()), ""]
            lines += ["前 40 条：", "", "| 完整 id | 显示名 |", "| --- | --- |"]
            lines += [
                f"| `{key}` | {value['display'] or '-'} |"
                for key, value in list(items.items())[:40]
            ]
            lines.append(f"| … | 其余 {len(items) - 40} 条见脚本原件 |")
    else:
        if facts["vehicles"] or facts["recipes"]:
            lines.append("没有独立脚本物品；载具和配方见下。")
        else:
            lines.append("没有脚本物品（Lua / 模型 / 补丁类 mod）。")
    vehicles = sorted(set(facts["vehicles"]))
    if vehicles:
        lines += ["", f"载具脚本 {len(vehicles)} 条：" + "，".join(f"`{x}`" for x in vehicles)]
    recipes = sorted(set(facts["recipes"]))
    if recipes:
        shown = "，".join(f"`{x}`" for x in recipes[:30])
        suffix = f" … 其余 {len(recipes) - 30} 条" if len(recipes) > 30 else ""
        lines += ["", f"配方 {len(recipes)} 条：{shown}{suffix}"]

    lines += ["", "## 双端与联机", "", cat.get("mp", "-"), ""]
    if row["distribution"] == "client":
        lines.append("**当前 profile：client-only（仅客户端）。** 服务端 `Mods=` 不含此条；"
                     "联机进服后客户端会按服务端列表重载，因此该项在服务器内不会保留。")
    else:
        lines.append(f"当前 profile：{dist_label(row['distribution'])}。")
    auto = [
        "客户端有 lua" if stats["lua_client"] else
        ("客户端无 lua，但带 Java 源码补丁" if stats["java"] else "客户端无 lua（纯资源）"),
        "服务端有 lua" if stats["lua_server"] else "服务端无 lua（只挂载）",
    ]
    lines += ["", "本机文件构成：" + "；".join(auto) + "。"]

    lines += ["", "## 实测与排查", "", cat.get("note", "（暂无专项记录）")]
    lines += ["", "```", "cd A004/B42.22_TEST",
              "python lab.py check --profile b422-batch2",
              f"grep -a '{row['folder']}' runs/<trial>/console.log", "```"]

    desc = (info.get("description") or "").strip()
    lines += ["", "## 作者原话", "", "```", desc[:1000] if desc else "（mod.info 未提供描述）", "```"]
    lines += ["", "## 来源", "",
              f"- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id={row['wid']}`",
              f"- 本地快照（测试台）：`A004/B42.22_TEST/workspace/mods_library/{row['wid']}/mods/{row['folder']}`",
              f"- 档案生成：`python tools/mod_archive.py --profile {profile}`", ""]
    return "\n".join(lines) + "\n"


def render_index(rows: list[dict], profile: str, total_items: int, total_size: int) -> str:
    lines = [
        f"# B42.22_TEST 包 mod 档案索引（{profile}）",
        "",
        f"共 {len(rows)} 个条目（启用 {sum(1 for r in rows if r['enabled'])}，"
        f"禁用 {sum(1 for r in rows if not r['enabled'])}），"
        f"合计 {human(total_size)}、脚本物品 {total_items:,} 条。",
        "结构见 [_TEMPLATE.md](_TEMPLATE.md)；文件名为 `<steam_id>_<模组原名>_<模组中文介绍>.md`。",
        "",
        "> 体积、文件数、物品数按测试台本地包**完整目录**统计；同一个 mod 若带多个版本目录，"
        "实际加载只取匹配 B42.22 的一档。",
        "",
        "| # | 中文名 | mod | 工作坊 ID | 分类 | 分发 | 体积 | 物品 | 状态 | 档案 |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        cat = row["cat"]
        cn = (cat.get("cn") or row["folder"]).replace("|", "/")
        name = (row["info"].get("name") or row["folder"]).replace("|", "/")
        lines.append(
            f"| {row['idx']} | {cn} | {name} | `{row['wid']}` | {cat.get('cat', '-')} | "
            f"{row['distribution']} | {human(row['stats']['bytes'])} | "
            f"{len(row['facts']['items'])} | {'启用' if row['enabled'] else '禁用'} | "
            f"[查看]({file_name(row)}) |"
        )
    lines += [
        "",
        "## 查物品 id",
        "",
        "- 直接 `grep -r 'Base.某id' mod_archives/`，命中文件就是加它的 mod。",
        "- 改了 profile 或更新了 mod：`python tools/mod_archive.py --profile b422-batch2` 重跑。",
        "",
    ]
    return "\n".join(lines) + "\n"


def render_readme(rows: list[dict], total_items: int, total_size: int, profile: str) -> str:
    enabled = sum(1 for r in rows if r["enabled"])
    client_only = [r for r in rows if r["distribution"] == "client"]
    grouped: dict[str, list[dict]] = {name: [] for name, _ in README_GROUPS}
    grouped["其他"] = []
    for row in rows:
        grouped.setdefault(readme_group(row["folder"]), []).append(row)

    lines = [
        "# B42.22_TEST · 42 Mod 联机测试包",
        "",
        "这是 **A004/B42.22_TEST** 的文档副本，记录当前 B42.22 联机测试包的 42 个条目：",
        "它们做什么、依赖谁、加了哪些物品/载具/配方、哪一端加载、以及本机实测注意事项。",
        "这里只放档案，不含 mod 本体；实际运行库在 `A004/B42.22_TEST`。",
        "",
        "## 当前包",
        "",
        f"- 游戏版本：`B42.22`（profile `gameVersion=42.22.0`）",
        f"- 条目：**{len(rows)}**（启用 {enabled}，禁用 {len(rows) - enabled}）",
        f"- 双端：**Client 42 / Server 38**；服务端不加载的 4 条是 "
        + "、".join(f"`{r['folder']}`" for r in client_only) + "。",
        "- 世界名 / 服务器名：`b422batch2`；入口：`A004/B42.22_TEST/start-client.bat`、`start-server.bat`。",
        f"- 体积：{human(total_size)}；脚本物品：{total_items:,} 条。",
        "- 三个汉化包均为 `both`，服务端 `Mods=` 末尾依次是 "
        "`LaoYuTranslationJava`、`B42ModTrans_CN`、`B42Trans_CN`。",
        "",
        "## 目录",
        "",
        "```",
        "B42.22_TEST/",
        "├── README.md              # 本文件：包说明 + 按类别索引",
        "├── mod_archives/          # 一个 mod 一份档案",
        "│   ├── INDEX.md           # 42 条简表",
        "│   ├── _TEMPLATE.md       # 固定骨架与通用规则",
        "│   └── <steam_id>_<原名>_<中文简介>.md",
        "└── tools/",
        "    ├── mod_archive.py     # 从 A004/B42.22_TEST 生成档案",
        "    ├── mod_catalog.json    # 人工简介、分类、排查注记",
        "    └── workshop_times.json # 工作坊更新日期快照",
        "```",
        "",
        "## 模组索引（按类别）",
        "",
        "类别只表示用途，不代表加载顺序；实际顺序看 profile 的 `loadOrder`。",
        "",
    ]
    for group_name in [name for name, _ in README_GROUPS] + ["其他"]:
        items = grouped.get(group_name, [])
        if not items:
            continue
        lines += [
            f"### {group_name}（{len(items)} 个）",
            "",
            "| 中文名 | 原名 | 工作坊 ID | 分发 | 体积 | 物品 | 档案 |",
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
        for row in sorted(items, key=lambda x: (x["cat"].get("cn") or x["folder"]).casefold()):
            cn = (row["cat"].get("cn") or row["folder"]).replace("|", "/")
            name = (row["info"].get("name") or row["folder"]).replace("|", "/")
            lines.append(
                f"| {cn} | {name} | [`{row['wid']}`](https://steamcommunity.com/sharedfiles/filedetails/?id={row['wid']}) | "
                f"{row['distribution']} | {human(row['stats']['bytes'])} | "
                f"{len(row['facts']['items'])} | [查看](mod_archives/{file_name(row)}) |"
            )
        lines.append("")
    lines += [
        "## 三条通用规则",
        "",
        "1. **双端一致**：标记 `both` 的模组客户端和服务端都要装；少一边会因 mod 列表校验失败而连不上。"
        "当前 4 条 `client` 只装客户端，进服后会被服务端 `Mods=` 列表丢弃，这是已知行为。",
        "2. **依赖在前**：`ZombieBuddy`、`NeatUI_Framework`、`damnlib`、`YAPZLib`、`Viewpoint` "
        "必须排在依赖它的内容之前；汉化包放最后。",
        "3. **汉化垫底**：`LaoYuTranslationJava` → `B42ModTrans_CN` → `B42Trans_CN`，"
        "否则翻译文件会被后加载的模组覆盖。",
        "",
        "## 怎么读单个档案",
        "",
        "每份档案固定为：它做什么 → 概览（版本/作者/体积/更新时间）→ 依赖与冲突 → "
        "内容清单（物品 id / 载具 / 配方）→ 双端与联机 → 实测与排查 → 作者原话 → 来源。",
        "骨架和遍历结论见 [`mod_archives/_TEMPLATE.md`](mod_archives/_TEMPLATE.md)。",
        "",
        "## 重新生成与校验",
        "",
        "```",
        "cd Grsh_PZ_Modpack/B42.22_TEST",
        "python tools/mod_archive.py --profile b422-batch2",
        "cd ../../../B42.22_TEST",
        "python lab.py check --profile b422-batch2",
        "```",
        "",
        "生成器只扫描 `A004/B42.22_TEST/workspace/mods_library` 和 profile，"
        "不会复制、修改或上传任何 mod 文件。",
        "",
        "## 免责声明",
        "",
        "所有模组版权归各自作者所有；本目录只记录整合信息、版本与兼容性结论，不分发模组文件。"
        "遇到问题先看对应档案的「实测与排查」，再回创意工坊页面确认版本。",
        "",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--profile", default="b422-batch2")
    ap.add_argument("--lab", default=str(LAB_DEFAULT))
    ap.add_argument("--out", default=str(ROOT / "mod_archives"))
    args = ap.parse_args()

    lab = Path(args.lab).resolve()
    profile_path = lab / "workspace" / "defs" / args.profile / "pack.json"
    pack = json.loads(profile_path.read_text(encoding="utf-8"))
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))["mods"]
    times = read_times()
    mods = pack.get("mods", [])
    load_order = pack.get("loadOrder") or []
    duplicate_wids = {wid for wid, count in Counter(str(m["workshopId"]) for m in mods).items() if count > 1}

    rows: list[dict] = []
    for idx, mod in enumerate(mods, 1):
        wid = str(mod["workshopId"])
        folder = mod.get("folder") or mod.get("modId")
        root = pick_root(lab / "workspace" / "mods_library", wid, folder)
        info = read_info(root) if root.is_dir() else {}
        key = catalog_key(wid, folder, duplicate_wids)
        entry = catalog.get(key) or catalog.get(wid) or {}
        rows.append({
            "idx": idx,
            "wid": wid,
            "folder": folder,
            "enabled": mod.get("enabled", True),
            "distribution": mod.get("distribution", "both"),
            "info": info,
            "stats": dir_stats(root) if root.is_dir() else dir_stats(Path(".")),
            "facts": script_facts(root) if root.is_dir() else {"items": {}, "vehicles": [], "recipes": []},
            "load": (load_order.index(folder) + 1) if folder in load_order else None,
            "cat": entry,
            "updated": times.get(wid, "-"),
        })

    by_id = {r["info"].get("id"): r for r in rows if r["info"].get("id")}
    for row in rows:
        rid = row["info"].get("id")
        row["required_by"] = [
            other["folder"] for other in rows
            if other is not row and rid and re.search(rf"\b{re.escape(rid)}\b", other["info"].get("require", ""))
        ]

    out = Path(args.out).resolve()
    out.mkdir(parents=True, exist_ok=True)
    for old in out.glob("*.md"):
        if old.name != "_TEMPLATE.md":
            old.unlink()

    used: set[str] = set()
    for row in rows:
        name = file_name(row)
        if name in used:
            stem, suffix = name.rsplit(".", 1)
            name = f"{stem}_{row['idx']}.{suffix}"
        used.add(name)
        (out / name).write_text(render_doc(row, args.profile).rstrip() + "\n", encoding="utf-8")

    total_items = sum(len(r["facts"]["items"]) for r in rows)
    total_size = sum(r["stats"]["bytes"] for r in rows)
    (out / "INDEX.md").write_text(
        render_index(rows, args.profile, total_items, total_size).rstrip() + "\n",
        encoding="utf-8",
    )
    (ROOT / "README.md").write_text(
        render_readme(rows, total_items, total_size, args.profile).rstrip() + "\n",
        encoding="utf-8",
    )

    missing = [r["folder"] for r in rows if not r["cat"]]
    print(f"wrote {len(rows)} docs + INDEX.md -> {out}")
    print(f"items={total_items} size={human(total_size)}")
    if missing:
        print("catalog 缺条目:", missing)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
