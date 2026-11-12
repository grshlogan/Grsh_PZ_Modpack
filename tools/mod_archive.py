#!/usr/bin/env python3
"""Generate the B42.22 inventory from the sibling A004 lab without launching it.

The default archive view covers b422-compat, a superset of the daily b422-main.
Every entry identifies its daily/candidate status; documentation is not activation.
No mod binaries or profile credentials are copied into this repository.

Usage (from Grsh_PZ_Modpack):
  python tools/mod_archive.py
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LAB_DEFAULT = ROOT.parent
CATALOG = ROOT / "tools" / "mod_catalog.json"
TIMES = ROOT / "tools" / "workshop_times.json"
GAME_VERSION = "42.22.2"

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
        "ViewpointBarricade", "ViewpointFences3D", "ViewpointLivingProps",
        "aparosa_vpmo_RaccoonCityB42", "ViewpointDLSS", "ViewpointVisualFixes",
        "PV-modmapbakefix", "ProjectViewpointShelves", "PZVoxelStudioViewpoint",
        "BasileDoors3D", "ViewpointInteriors",
    }),
    ("角色与外观", {"AimohPmxPreview", "VariableSkinSFW", "VariableSkinFix",
                    "VariableSkinBoobBounce", "VariableSkinBoobBounceViewpoint"}),
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
    ("修复与兼容", {
        "FixNaNStats", "ProjectViewpoint-KI5VehiclePartsFix",
        "ViewpointVehicleShellFix", "ViewpointPartPaint", "ViewpointKI5Materials",
    }),
    ("房车兼容候选", {"GridVansHost", "GridVans", "DeadWorksVehicleFramework",
                       "aparosa_DWVFTweaks", "DeadWorksNomadRV", "DeadWorksDaleRV"}),
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


def read_info(folder: Path, overlay: Path | None = None,
              game_version: str = GAME_VERSION) -> dict:
    """Match the deployment tool's version directory, then apply metadata Overlay."""
    target = vtuple(game_version)
    candidates = [folder / "mod.info", folder / "common" / "mod.info"]
    candidates += [p for p in folder.glob("*/mod.info")
                   if re.fullmatch(r"\d+(?:\.\d+)*", p.parent.name)
                   and vtuple(p.parent.name) <= target]
    chosen_path = max((p for p in candidates if p.is_file()), default=None,
                      key=lambda p: (vtuple(p.parent.name)
                                     if re.fullmatch(r"\d+(?:\.\d+)*", p.parent.name)
                                     else (-1, -1, -1), p.parent.name == "common"))
    if chosen_path is None:
        return {}
    base = parse_info(chosen_path)
    relative = chosen_path.relative_to(folder)
    patched = overlay / relative if overlay else None
    out = parse_info(patched) if patched and patched.is_file() else dict(base)
    # Only presentation fields may fall back to common/root metadata.
    for other in (folder / "common" / "mod.info", folder / "mod.info"):
        for key, value in parse_info(other).items():
            if key in {"name", "author", "description", "modversion"}:
                out.setdefault(key, value)
    out["_base_versionmin"] = base.get("versionmin", "")
    out["_base_versionmax"] = base.get("versionmax", "")
    out["_info_path"] = relative.as_posix()
    out["_overlay"] = relative.as_posix() if patched and patched.is_file() else ""
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
        f"归属：**{'日常组合' if row['baseline'] else '兼容候选（未运行验收）'}**；档案视图 `{profile}`。",
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
        f"| Mod 版本 | `{info.get('modversion', '-')}` |",
        f"| 原件适配 | `{info.get('_base_versionmin') or '-'}` … `{info.get('_base_versionmax') or '-'}` |",
        f"| 当前生效适配 | `{info.get('versionmin', '-')}` … `{info.get('versionmax', '-')}`"
        + ("（Overlay 放行，非上游正式支持） |" if info.get('_overlay') else "（原件） |"),
        f"| 元数据来源 | `{info.get('_info_path', '-')}` |",
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
    if not row["baseline"]:
        lines += ["", "**planned：仅完成依赖、版本与补丁指纹静态检查。** "
                  "迁移收尾按 Owner 要求不启动游戏；本候选组合未验证加载、联网、存档或视觉。"]
    if info.get("_overlay"):
        lines += ["", f"版本放行补丁：`A004/workspace/patches/mods/{row['folder']}/{info['_overlay']}`。"
                  "原件更新后须重新核对指纹；撤除此补丁后运行 check 会恢复原件版本限制。"]
    lines += ["", "```", "cd A004",
              f"python lab.py check --profile {profile}",
              f"grep -a '{info.get('id') or row['folder']}' runs/<trial>/*console.log", "```"]

    desc = (info.get("description") or "").strip()
    lines += ["", "## 作者原话", "", "```", desc[:1000] if desc else "（mod.info 未提供描述）", "```"]
    lines += ["", "## 来源", "",
              f"- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id={row['wid']}`",
              f"- 本地原件：`A004/workspace/mods_library/{row['wid']}/mods/{row['folder']}`",
              f"- 档案生成：`python tools/mod_archive.py --profile {profile}`", ""]
    return "\n".join(lines) + "\n"


def render_index(rows: list[dict], profile: str, total_items: int, total_size: int) -> str:
    lines = [
        f"# B42.22 Mod 档案索引（档案视图 {profile}）",
        "",
        f"共 {len(rows)} 个条目（启用 {sum(1 for r in rows if r['enabled'])}，"
        f"禁用 {sum(1 for r in rows if not r['enabled'])}），"
        f"合计 {human(total_size)}、脚本物品 {total_items:,} 条。",
        "结构见 [_TEMPLATE.md](_TEMPLATE.md)；文件名为 `<steam_id>_<模组原名>_<模组中文介绍>.md`。",
        "",
        "> 体积、文件数、物品数按本地原件**完整目录**统计，不代表当前引擎实际加载数。"
        "“启用”仅指所选档案视图；默认启动仍用 b422-main。候选状态见各档案及 [兼容说明](../COMPATIBILITY.md)。",
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
            f"{len(row['facts']['items'])} | {'日常' if row['baseline'] else '兼容候选'} / {'启用' if row['enabled'] else '禁用'} | "
            f"[查看]({file_name(row)}) |"
        )
    lines += [
        "",
        "## 查物品 id",
        "",
        "- 直接 `grep -r 'Base.某id' mod_archives/`，命中文件就是加它的 mod。",
        f"- 改了 profile 或更新了 mod：`python tools/mod_archive.py --profile {profile}` 重跑。",
        "",
    ]
    return "\n".join(lines) + "\n"


def render_readme(rows: list[dict], total_items: int, total_size: int, profile: str,
                  pack: dict, profiles: list[dict]) -> str:
    grouped: dict[str, list[dict]] = {name: [] for name, _ in README_GROUPS}
    grouped["其他"] = []
    for row in rows:
        grouped.setdefault(readme_group(row["folder"]), []).append(row)
    baseline = [r for r in rows if r["baseline"]]
    candidate_count = len(rows) - len(baseline)
    lines = [
        "# Grsh PZ Modpack · B42.22 开发主线",
        "",
        "这里记录 A004 当前 Mod 原件、依赖、物品 ID 与兼容候选；不包含游戏或 Mod 二进制。",
        "日常入口在 `A004/start-server.bat`、`A004/start-client.bat`，默认 `b422-main`。",
        f"本页是 `{profile}` 的**档案视图**：{len(rows)} 条中 {len(baseline)} 条属于日常组合，"
        f"其余 {candidate_count} 条为兼容候选。生成档案不会切换运行组合。",
        "",
        "## 从这里读",
        "",
        "- [完整索引](mod_archives/INDEX.md)：按 Mod 查依赖、物品/载具 ID 和分发端。",
        "- [兼容与迁移说明](COMPATIBILITY.md)：补丁、回退、未覆盖项与 Owner 验收。",
        "- [档案模板](mod_archives/_TEMPLATE.md)：自动字段、人工简介与统计限制。",
        "- [迁移前清单](archive/pre-b422-promotion-20261112/README.md)：历史资料，不是当前启用列表。",
        "",
        "## 组合与验证边界",
        "",
        "| 组合 | Client / Server | 世界 | 定位 |",
        "| --- | --- | --- | --- |",
    ]
    for item in profiles:
        purpose = "日常默认；迁移后联机/存档重进未验收" if item["profile"] == "b422-main" else "兼容候选；仅静态检查，未启动"
        lines.append(f"| `{item['profile']}` | {item['client']} / {item['server']} | `{item['world']}` | {purpose} |")
    lines += [
        "",
        f"- 档案输入版本：`{pack.get('gameVersion', GAME_VERSION)}`；当前日常底座为 B42.22.2，git `3d39148846`。",
        "- 迁移前 52/48 已有双端加载证据；新路径仅服务端曾到达就绪，不能代替客户端联网与存档重进。",
        "- Owner 要求迁移收尾不启动游戏，因此新增候选只有离线依赖/版本/指纹证据，**不是兼容通过**。",
        "- Viewpoint 固定官方 0.1.6.2，与 R116 0.3.51 指纹绑定；不混用 nightly，也不加已被内置资源替代的旧 GF2 外置包。",
        "- 四条仅客户端项：`PzPerformanceFixes`、`42_VSGirlBodySFW`、`42_VSGirlBody_Fix`、`BB_WhereAmI`。进服后按服务端清单重载，不把它们仍有效当作已验证。",
        "- 三汉化包必须双端，加载末尾依次是 `LaoYuTranslationJava` → `B42ModTrans_CN` → `B42Trans_CN`。",
        f"- 完整包目录统计：{human(total_size)}；脚本物品 {total_items:,} 条。多个版本目录、资源副本会使统计大于实际加载。",
        "",
        "## Mod 索引（按用途）",
        "",
        "“归属”区分日常与候选，不是运行验收结论。加载顺序以对应 profile 的 loadOrder 为准。",
        "",
    ]
    for group_name in [name for name, _ in README_GROUPS] + ["其他"]:
        items = grouped.get(group_name, [])
        if not items:
            continue
        lines += [f"### {group_name}（{len(items)} 个）", "",
                  "| 中文名 | 原名 | 工作坊 ID | 分发 | 归属 | 物品 | 档案 |",
                  "| --- | --- | --- | --- | --- | --- | --- |"]
        for row in sorted(items, key=lambda x: (x["cat"].get("cn") or x["folder"]).casefold()):
            cn = (row["cat"].get("cn") or row["folder"]).replace("|", "/")
            name = (row["info"].get("name") or row["folder"]).replace("|", "/")
            status = "日常" if row["baseline"] else "兼容候选"
            lines.append(
                f"| {cn} | {name} | [`{row['wid']}`](https://steamcommunity.com/sharedfiles/filedetails/?id={row['wid']}) | "
                f"{row['distribution']} | {status} | {len(row['facts']['items'])} | [查看](mod_archives/{file_name(row)}) |"
            )
        lines.append("")
    lines += [
        "## 更新档案（不会启动游戏）", "", "```bash",
        "# 从 Grsh_PZ_Modpack 目录运行；默认扫描同级 A004",
        "python tools/mod_archive.py",
        "python tools/test_mod_archive.py",
        "# 从 A004 根执行静态检查",
        "python lab.py check --profile b422-main", "```", "",
        "生成器读取 `A004/workspace/mods_library`、`workspace/patches/mods` 和所选定义；只写 Markdown，不改 Mod。",
        "修改人工简介用 `tools/mod_catalog.json`；更新日期保存在 `tools/workshop_times.json`。",
        "`--out` 会重建指定档案目录，并把 README 写在其父目录；不要指向未保全的历史资料。", "",
        "## 权属与范围", "",
        "所有 Mod 版权归各自作者。这里是本地开发资料，不是正式发布、独立 Review 或 Owner 玩法验收。", "",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--profile", default="b422-compat",
                    help="archive view only; the lab still defaults to b422-main")
    ap.add_argument("--lab", default=str(LAB_DEFAULT))
    ap.add_argument("--out", default=str(ROOT / "mod_archives"))
    args = ap.parse_args()

    lab = Path(args.lab).resolve()
    profile_path = lab / "workspace" / "defs" / args.profile / "pack.json"
    pack = json.loads(profile_path.read_text(encoding="utf-8"))
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))["mods"]
    times = read_times()
    baseline_path = lab / "workspace" / "defs" / "b422-main" / "pack.json"
    baseline_pack = json.loads(baseline_path.read_text(encoding="utf-8")) if baseline_path.is_file() else {}
    baseline_folders = {m["folder"] for m in baseline_pack.get("mods", []) if m.get("enabled", True)}
    profiles = []
    for name in ("b422-main", "b422-compat-render", "b422-compat-rv", "b422-compat"):
        source = lab / "workspace" / "defs" / name / "pack.json"
        if source.is_file():
            data = json.loads(source.read_text(encoding="utf-8"))
            selected = [m for m in data.get("mods", []) if m.get("enabled", True)]
            profiles.append({"profile": name, "world": data.get("worldName", "-"),
                             "client": sum(m.get("distribution", "both") in {"both", "client"} for m in selected),
                             "server": sum(m.get("distribution", "both") in {"both", "server"} for m in selected)})
    mods = pack.get("mods", [])
    load_order = pack.get("loadOrder") or []
    duplicate_wids = {wid for wid, count in Counter(str(m["workshopId"]) for m in mods).items() if count > 1}

    rows: list[dict] = []
    for idx, mod in enumerate(mods, 1):
        wid = str(mod["workshopId"])
        folder = mod.get("folder") or mod.get("modId")
        root = pick_root(lab / "workspace" / "mods_library", wid, folder)
        if not root.is_dir():
            raise ValueError(f"missing Base directory: {wid}/{folder}")
        info = read_info(root, lab / "workspace" / "patches" / "mods" / folder,
                         pack.get("gameVersion", GAME_VERSION))
        if not info:
            raise ValueError(f"no applicable mod.info: {wid}/{folder}")
        key = catalog_key(wid, folder, duplicate_wids)
        entry = catalog.get(key) or catalog.get(wid) or {}
        rows.append({
            "idx": idx,
            "wid": wid,
            "folder": folder,
            "enabled": mod.get("enabled", True),
            "baseline": folder in baseline_folders,
            "distribution": mod.get("distribution", "both"),
            "info": info,
            "stats": dir_stats(root),
            "facts": script_facts(root),
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

    missing = [r["folder"] for r in rows if not r["cat"]]
    if missing:
        print("catalog 缺条目:", missing)
        return 2
    names = [file_name(row) for row in rows]
    if len(names) != len(set(names)):
        raise ValueError("duplicate archive filename; make brief/name unique before generating")
    out = Path(args.out).resolve()
    out.mkdir(parents=True, exist_ok=True)
    for old in out.glob("*.md"):
        if old.name != "_TEMPLATE.md":
            old.unlink()

    for row in rows:
        (out / file_name(row)).write_text(render_doc(row, args.profile).rstrip() + "\n", encoding="utf-8")

    total_items = sum(len(r["facts"]["items"]) for r in rows)
    total_size = sum(r["stats"]["bytes"] for r in rows)
    (out / "INDEX.md").write_text(
        render_index(rows, args.profile, total_items, total_size).rstrip() + "\n",
        encoding="utf-8",
    )
    (out.parent / "README.md").write_text(
        render_readme(rows, total_items, total_size, args.profile, pack, profiles).rstrip() + "\n",
        encoding="utf-8",
    )

    print(f"wrote {len(rows)} docs + INDEX.md -> {out}")
    print(f"items={total_items} size={human(total_size)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
