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
    ("房车", {"GridVansHost", "GridVans", "DeadWorksVehicleFramework",
                       "aparosa_DWVFTweaks", "DeadWorksNomadRV", "DeadWorksDaleRV"}),
    ("汉化", {"LaoYuTranslationJava", "B42ModTrans_CN_As1", "B42Trans_CN_As1"}),
]


def vtuple(text: str) -> tuple[int, int, int]:
    parts = [int(x) for x in re.findall(r"\d+", text or "")[:3]]
    return tuple(parts + [0] * (3 - len(parts)))  # type: ignore[return-value]


def parse_info(path: Path) -> dict:
    out: dict = OrderedDict()
    try:
        text = read_text(path)
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


def read_text(path: Path) -> str:
    """Decode losslessly; replacement characters would corrupt copyable IDs."""
    data = path.read_bytes()
    for encoding in ("utf-8-sig", "gb18030"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            continue
    raise ValueError(f"unsupported text encoding: {path}")


def strip_comments(text: str) -> str:
    # Script packs use nested block comments. Preserve offsets and line numbers.
    result, i, depth, quote = list(text), 0, 0, False
    while i < len(text):
        pair = text[i:i + 2]
        if text[i:i + 3] == "/*/" and not quote:
            depth = depth - 1 if depth else 1
            result[i:i + 3] = "   "
            i += 3
            continue
        if depth:
            if pair == "/*":
                depth += 1
            elif pair == "*/":
                depth -= 1
            else:
                if text[i] not in "\r\n":
                    result[i] = " "
                i += 1
                continue
            result[i:i + 2] = "  "
            i += 2
        elif quote:
            if text[i] == chr(92):
                i += 2
            else:
                quote = text[i] != '"'
                i += 1
        elif pair == "/*":
            depth = 1
            result[i:i + 2] = "  "
            i += 2
        elif pair == "//":
            while i < len(text) and text[i] not in "\r\n":
                result[i] = " "
                i += 1
        else:
            quote = text[i] == '"'
            i += 1
    if depth:
        raise ValueError("unterminated script comment")
    return "".join(result)


def blocks(text: str, offset: int = 0, diagnostics: list | None = None) -> list[dict]:
    """Return only immediate brace children, with offsets into the source file."""
    result = []
    depth, segment, opening, start = 0, 0, 0, 0
    quote, escaped, header = "", False, ""
    for i, char in enumerate(text):
        if quote:
            if escaped:
                escaped = False
            elif char == chr(92):
                escaped = True
            elif char == quote:
                quote = ""
            continue
        if char == '"':
            quote = char
        elif char == "{":
            if depth == 0:
                prefix = text[segment:i].rstrip()
                header = re.split(r"[,;\n\r]", prefix)[-1].strip()
                start = i - len(text[segment:i]) + len(prefix) - len(header)
                opening = i
            depth += 1
        elif char == "}":
            depth -= 1
            if depth < 0:
                if diagnostics is None:
                    raise ValueError("unmatched closing script brace")
                diagnostics.append(text.count(chr(10), 0, i) + 1)
                depth, segment = 0, i + 1
                continue
            if depth == 0:
                result.append({"header": header, "body": text[opening + 1:i],
                               "offset": offset + opening + 1,
                               "start": offset + start, "end": offset + i + 1})
                segment = i + 1
    if depth or quote:
        raise ValueError("unterminated script block or string")
    return result


def field_pairs(body: str) -> list[tuple[str, str]]:
    plain = list(body)
    for child in blocks(body):
        plain[child["start"]:child["end"]] = " " * (child["end"] - child["start"])
    pattern = r'\b([A-Za-z_][\w!]*)\s*=\s*("(?:\\.|[^"\\])*"|[^,\n]+)'
    return [(m[1].lower(), m[2].strip().strip('"'))
            for m in re.finditer(pattern, "".join(plain))]


def effective_files(folder: Path, overlay: Path | None = None,
                    game_version: str = GAME_VERSION) -> dict[str, tuple[Path, str]]:
    """Virtual common + selected-version media tree; Overlay wins by relative path."""
    info = read_info(folder, overlay, game_version)
    selected = Path(info.get("_info_path", "mod.info")).parent
    layers = [Path("common"), selected] if selected != Path("common") else [selected]
    files = {}
    for layer in layers:
        media = folder / layer / "media"
        if media.is_dir():
            for path in sorted(media.rglob("*")):
                if path.is_file():
                    rel = (layer / "media" / path.relative_to(media)).as_posix()
                    patch = overlay / rel if overlay else None
                    files[path.relative_to(media).as_posix()] = (
                        patch if patch and patch.is_file() else path, rel)
        patched_media = overlay / layer / "media" if overlay else None
        if patched_media and patched_media.is_dir():
            for path in sorted(patched_media.rglob("*")):
                if path.is_file():
                    rel = (layer / "media" / path.relative_to(patched_media)).as_posix()
                    files[path.relative_to(patched_media).as_posix()] = (path, rel)
    return files


def qualify(name: str, module: str) -> str:
    return name if "." in name else f"{module}.{name}"


def script_facts(folder: Path, overlay: Path | None = None,
                 game_version: str = GAME_VERSION, media_files: dict | None = None) -> dict:
    files = media_files if media_files is not None else effective_files(folder, overlay, game_version)
    facts = {key: OrderedDict() for key in ("items", "vehicles", "recipes", "templates")}
    facts["warnings"] = []
    facts["branches"] = sorted({rel.split("/media/")[0]
                                for _, rel in files.values() if "/media/" in rel})
    for virtual, (path, relative) in files.items():
        if not virtual.startswith("scripts/") or path.suffix.lower() != ".txt":
            continue
        source_relative = f"Overlay/{relative}" if not path.is_relative_to(folder) else relative
        text = strip_comments(read_text(path))
        extra_braces = []
        try:
            modules = blocks(text, diagnostics=extra_braces)
        except ValueError as exc:
            raise ValueError(f"{relative}: {exc}") from exc
        facts["warnings"] += [f"{relative}:{line}：原件多余的顶层闭合括号，静态提取时跳过"
                              for line in extra_braces]
        for module_block in modules:
            match = re.fullmatch(r"module\s+([\w]+)", module_block["header"])
            if not match:
                continue
            module = match[1]
            for node in blocks(module_block["body"], module_block["offset"]):
                match = re.fullmatch(r"(item|vehicle|template\s+vehicle|craftRecipe|recipe)\s+(.+)", node["header"])
                if not match:
                    continue
                kind, name = match[1], match[2].strip().strip('"')
                pairs = field_pairs(node["body"])
                props = dict(pairs)
                source = f"{source_relative}:{text.count(chr(10), 0, node['start']) + 1}"
                entry = {"name": name, "module": module, "properties": props,
                         "display": props.get("displayname", ""),
                         "type": props.get("type", props.get("itemtype", "")),
                         "source": source, "body": node["body"], "kind": kind,
                         "templates": [qualify(x.strip(), module)
                                       for k, v in pairs if k in {"template", "template!"}
                                       for x in v.split(";") if x.strip()], "parts": {}}
                for part in blocks(node["body"], node["offset"]):
                    if part["header"].startswith("part "):
                        slot = part["header"][5:].strip()
                        entry["parts"][slot] = {
                            "properties": dict(field_pairs(part["body"])),
                            "source": f"{source_relative}:{text.count(chr(10), 0, part['start']) + 1}",
                        }
                bucket = {"item": "items", "vehicle": "vehicles", "craftRecipe": "recipes",
                          "recipe": "recipes"}.get(kind, "templates")
                facts[bucket][qualify(name, module)] = entry
    return facts


def load_translations(files: dict, origin: str = "") -> dict:
    """Keep all translation candidates; load order alone does not prove precedence."""
    names = {}
    for virtual, (path, relative) in files.items():
        match = re.search(r"(?:^|/)Translate/(CN|EN)/([^/]+)\.(json|txt)$", virtual, re.I)
        if not match:
            continue
        language, filename, extension = match[1].upper(), match[2], match[3].lower()
        family = re.sub(r"_(CN|EN)$", "", filename, flags=re.I)
        if family not in {"ItemName", "Recipes", "IG_UI"}:
            continue
        text = read_text(path)
        if extension == "json":
            syntax_warning = False
            try:
                pairs = json.loads(text, object_pairs_hook=list)
            except json.JSONDecodeError:
                cleaned = strip_comments(text)
                cleaned = re.sub(r'"(?:\\.|[^"\\])*"|,(?=\s*[}\]])',
                                 lambda m: " " if m[0] == "," else m[0], cleaned)
                try:
                    pairs = json.loads(cleaned, object_pairs_hook=list)
                except json.JSONDecodeError as exc:
                    raise ValueError(f"{origin}/{relative}: {exc}") from exc
                syntax_warning = True
            locations = {}
            for line_no, line in enumerate(text.splitlines(), 1):
                found = re.search(r'("(?:\\.|[^"\\])*")\s*:', line)
                if found:
                    locations.setdefault(json.loads(found[1]), line_no)
            entries = [(key, value, locations.get(key, 1))
                       for key, value in pairs if isinstance(value, str)]
        else:
            pattern = r'(?:\[\s*"([^"\n]+)"\s*\]|([\w.]+))\s*=\s*("(?:\\.|[^"\\])*")'
            entries = []
            syntax_warning = False
            for found in re.finditer(pattern, re.sub(r"--[^\n]*", "", text)):
                try:
                    value = json.loads(found[3])
                except json.JSONDecodeError:
                    value = found[3][1:-1].replace(chr(92) + '"', '"')
                entries.append((found[1] or found[2], value, text.count(chr(10), 0, found.start()) + 1))
        for key, value, line in entries:
            if family == "ItemName":
                kind, key = "item", key.removeprefix("ItemName_")
            elif family == "Recipes":
                kind, key = "recipe", key.removeprefix("Recipe_")
            elif key.startswith("IGUI_VehicleName"):
                kind, key = "vehicle", key[len("IGUI_VehicleName"):]
            elif key.startswith("IGUI_VehiclePart"):
                kind, key = "slot", key[len("IGUI_VehiclePart"):]
            else:
                continue
            source = f"{origin}/{relative}:{line}".lstrip("/")
            names.setdefault((language, kind, key), []).append({"text": value, "source": source,
                                                               "syntax_warning": syntax_warning})
    return names


def name_for(names: dict, kind: str, full_id: str, fallback: str,
             language: str = "CN") -> dict:
    keys = [full_id]
    if kind in {"recipe", "vehicle"}:
        keys.append(full_id.split(".", 1)[-1])
    entries = [entry for key in dict.fromkeys(keys)
               for entry in names.get((language, kind, key), [])]
    values = list(dict.fromkeys(entry["text"] for entry in entries))
    sources = list(dict.fromkeys(entry["source"] for entry in entries))
    if not values:
        if language == "CN":
            english = name_for(names, kind, full_id, fallback, "EN")
            warning = "；" + english["status"] if english["sources"] and english["status"] != "有效翻译文件" else ""
            return {**english, "status": "未找到有效中文译文" + warning}
        return {"text": fallback or full_id, "status": "脚本名回退", "sources": []}
    status = "译文冲突，待游戏核实" if len(values) > 1 else "有效翻译文件"
    if len(values) == 1 and any(e.get("syntax_warning") for e in entries):
        status = "翻译文件含非标准语法，待游戏核实"
    return {"text": " / ".join(values), "status": status,
            "sources": sources}


def recipe_outputs(entry: dict) -> list[str]:
    result = []
    for block in blocks(entry["body"]):
        if block["header"].lower() == "outputs":
            for found in re.finditer(r"\bitem\s+\d+\s+([\w.]+)", block["body"]):
                result.append(qualify(found[1], entry["module"]))
    legacy = entry["properties"].get("result", "").split("=", 1)[0].strip()
    if legacy:
        result.append(qualify(legacy, entry["module"]))
    return list(dict.fromkeys(result))


def slot_explanation(slot: str) -> str:
    # These are descriptions of script installation slots, not invented item effects.
    kinds = [("engineDoor", "引擎盖"), ("windshield", "挡风玻璃"),
             ("window", "车窗"), ("roofrack", "车顶行李架"), ("trunk", "后备箱"),
             ("door", "车门"), ("seat", "座椅"), ("tire", "轮胎"),
             ("suspension", "悬挂"), ("brake", "制动器"), ("battery", "蓄电池"),
             ("gastank", "油箱"), ("muffler", "消声器"), ("bumper", "保险杠"),
             ("armor", "防护件"), ("spoiler", "扰流板"), ("roof", "车顶"),
             ("gunrack", "枪架"), ("engine", "发动机"), ("light", "车灯")]
    return next((cn for token, cn in kinds if token.lower() in slot.lower()), "车辆安装位")


def enrich_content(rows: list[dict], names: dict, core: dict | None = None) -> None:
    """Resolve template/part/recipe references against selected, enabled definitions."""
    items, templates = {}, {}
    ingredients, products = {}, {}
    providers = {}
    overrides = {key: value for row in rows for key, value in row["cat"].get("content", {}).items()}
    for kind, target in (("items", items), ("templates", templates)):
        for key, entry in (core or {}).get(kind, {}).items():
            target[key] = entry
            providers[key] = "游戏原版"
    active = sorted((r for r in rows if r["enabled"]), key=lambda r: r.get("load") or 10000)
    for row in active:
        for kind, target in (("items", items), ("templates", templates)):
            for key, entry in row["facts"][kind].items():
                target[key] = entry
                providers[key] = row["folder"]
    for entry in items.values():
        entry["fitments"] = []

    def parts_of(entry: dict, seen: frozenset = frozenset()) -> dict:
        parts = {}
        for reference in entry["templates"]:
            key, _, selector = reference.partition("/")
            if key in seen or key not in templates:
                continue
            inherited = parts_of(templates[key], seen | {key})
            if selector.startswith("part/"):
                wanted = selector[5:]
                inherited = {s: p for s, p in inherited.items() if s == wanted}
            for slot, value in inherited.items():
                previous = parts.get(slot, {})
                parts[slot] = {"source": value["source"], "properties": {
                    **previous.get("properties", {}), **value["properties"]}}
        for slot, value in entry["parts"].items():
            previous = parts.get(slot, {})
            parts[slot] = {"source": value["source"], "properties": {
                **previous.get("properties", {}), **value["properties"]}}
        return parts

    for row in rows:
        facts = row["facts"]
        facts["shared_items"], facts["internal"], facts["unresolved"] = {}, {}, []
        for vehicle_id, vehicle in facts["vehicles"].items():
            vehicle["cn"] = name_for(names, "vehicle", vehicle_id, vehicle["name"])
            vehicle["en"] = name_for(names, "vehicle", vehicle_id, vehicle["name"], "EN")
            for ref in vehicle["templates"]:
                if ref.split("/", 1)[0] not in templates:
                    facts["unresolved"].append({"reference": ref, "source": vehicle["source"],
                                                "reason": "模板未在已启用内容中定位"})
            for slot, part in parts_of(vehicle).items():
                facts["internal"].setdefault(slot, {"source": part["source"],
                    "label": name_for(names, "slot", slot, slot)["text"]})
                for raw in part["properties"].get("itemtype", "").split(";"):
                    raw = raw.strip()
                    if not raw or raw.lower() in {"nil", "base.nil", "null", "none"}:
                        continue
                    reference = qualify(raw, vehicle["module"])
                    resolved = reference if reference in items else reference + vehicle["properties"].get("mechanictype", "")
                    if resolved not in items:
                        facts["unresolved"].append({"reference": reference, "source": part["source"],
                                                    "reason": "配件引用缺少有效物品定义"})
                        continue
                    fitment = {"vehicle": vehicle_id, "slot": slot, "source": part["source"],
                               "mapping": "直接引用" if resolved == reference else "按机修类型后缀静态映射"}
                    if fitment not in items[resolved]["fitments"]:
                        items[resolved]["fitments"].append(fitment)
                    if resolved not in facts["items"]:
                        facts["shared_items"][resolved] = items[resolved]
        for recipe_id, entry in facts["recipes"].items():
            entry["cn"] = name_for(names, "recipe", recipe_id, entry["name"])
            entry["outputs"] = recipe_outputs(entry)
            for block in blocks(entry["body"]):
                if block["header"].lower() == "inputs":
                    for reference in set(re.findall(r"\b[A-Za-z_]\w*\.[A-Za-z_0-9]\w*", block["body"])):
                        if reference in items:
                            ingredients.setdefault(reference, []).append(recipe_id)
            for output in recipe_outputs(entry):
                products.setdefault(output, []).append(recipe_id)
            for output in entry["outputs"]:
                if output in items and output not in facts["items"]:
                    facts["shared_items"][output] = items[output]
                elif output not in items:
                    facts["unresolved"].append({"reference": output, "source": entry["source"],
                                                "reason": "配方产出未定位到有效物品定义"})
            entry["purpose"] = "制作产出：" + "、".join(
                name_for(names, "item", x, items[x]["display"] or x)["text"]
                for x in entry["outputs"] if x in items)
            if entry["purpose"] == "制作产出：":
                entry["purpose"] = "制作操作；脚本未声明可静态定位的物品产出，具体作用待核实"

    for row in rows:
        facts = row["facts"]
        # Shared entries use their provider's authored explanation on every page.
        for key, entry in {**facts["shared_items"], **facts["items"]}.items():
            entry["provider"] = providers.get(key, row["folder"])
            entry["cn"] = name_for(names, "item", key, entry["display"] or entry["name"])
            fitments = entry.get("fitments", [])
            learned = [qualify(x.strip(), entry["module"]) for x in
                       entry["properties"].get("learnedrecipes", "").split(";") if x.strip()]
            item_type = entry["type"].lower().rsplit(":", 1)[-1]
            if item_type == "literature" or learned:
                entry["category"] = "普通物品 / 书籍"
                recipe_names = [name_for(names, "recipe", x, x)["text"] + f"（{x}）" for x in learned]
                entry["purpose"] = "阅读资料" + ("；脚本声明解锁：" + "、".join(recipe_names) if learned else "；未声明解锁配方，阅读效果待游戏核实")
            elif fitments:
                slots = list(dict.fromkeys(x["slot"] for x in fitments))
                optional = any(re.search(r"armor|bumper|spoiler|roofrack|gunrack|bullbar|bodykit|cover", x, re.I) for x in slots)
                entry["category"] = "改装配件" if optional else "维修配件"
                positions = list(dict.fromkeys(slot_explanation(s) + f"（{s}）" for s in slots))
                entry["purpose"] = "车辆安装件，用于" + "、".join(positions) + "；适用车型见右列"
            else:
                entry["category"] = "普通物品 / 书籍"
                meanings = {"food": "食物；可食用效果由食物属性决定", "weapon": "武器；伤害等参数以脚本属性为准",
                            "drainable": "可消耗用品；用途由使用回调和配方决定", "container": "容器；用于存放物品",
                            "clothing": "穿戴物品；穿戴位置：" + entry["properties"].get("bodylocation", "脚本未标注"),
                            "moveable": "可移动家具或模型物品；放置与交互效果待游戏核实"}
                entry["purpose"] = meanings.get(item_type, "脚本物品；未找到整车安装关系，具体使用方式待核实")
                tags = entry["properties"].get("tags", "").lower()
                if "tire" in tags or "tyre" in tags:
                    entry["category"] = "维修配件"
                    entry["purpose"] = "轮胎类维修件；机修类别 " + entry["properties"].get("vehicletype", "未标注") + "；当前组合未定位适配整车，不据名称推定车型"
                elif entry["properties"].get("mechanicsitem", "").lower() == "true":
                    entry["category"] = "维修配件"
                    entry["purpose"] = "车辆维修物品；脚本声明 MechanicsItem，但未定位当前整车的安装关系，适配待核实"
                elif entry["properties"].get("displaycategory", "").lower() == "junk":
                    entry["purpose"] = "杂物或装饰条目；未定位安装关系或使用回调，不承诺额外效果"
                if key in ingredients:
                    entry["purpose"] = "制作材料；用于配方：" + "、".join(dict.fromkeys(ingredients[key]))
                elif key in products:
                    entry["purpose"] = "制作产物；来自配方：" + "、".join(dict.fromkeys(products[key])) + "；具体使用方式待核实"
            entry["status"] = ""
            if entry["display"].lower() == "not in use":
                entry["status"] = "作者显示名为 Not in use；" + ("当前模板仍引用，不能据名称判为停用" if fitments else "未找到当前整车引用")
            if entry["display"].lower().startswith("obsolete") and not fitments:
                entry["category"] = "内部定义"
                entry["status"] = "作者显示名标记 Obsolete；当前版本仍有定义，但未找到整车引用，不作为正常刷取建议"
            for field in ("category", "purpose", "status"):
                if field in overrides.get(key, {}):
                    entry[field] = overrides[key][field]
            entry["purpose_sources"] = overrides.get(key, {}).get("sources", [])

    for row in rows:
        for entry in row["facts"]["recipes"].values():
            descriptions = []
            for output in entry["outputs"]:
                if output in items:
                    product = items[output]
                    label = name_for(names, "item", output, product["display"] or output)["text"]
                    meaning = product.get("purpose", "当前组合提供的物品；具体用途待核实")
                    descriptions.append(f"{label}（{meaning}）")
            if descriptions:
                entry["purpose"] = "制作产出：" + "；".join(descriptions)


def manual_sections(text: str) -> str:
    """Keep authored observations, excluding generated inventories and metadata."""
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    if "<!-- retained:start -->" in text:
        inside = text.split("<!-- retained:start -->", 1)[1].split("<!-- retained:end -->", 1)[0].strip()
        tail = text.split("<!-- retained:end -->", 1)[1]
        return "\n\n".join(x for x in (inside, manual_sections(tail)) if x)
    headings = list(re.finditer(r"^## (.+)$", text, re.M))
    excluded = {"它做什么", "概览", "内容清单", "作者原话", "来源", "静态来源", "如何查找", "整车", "普通物品与书籍",
                "维修配件", "改装配件", "制作配方", "共享配件", "内部定义、历史分支与未解析引用", "证据与使用边界"}
    return "\n\n".join(text[h.start():headings[i + 1].start() if i + 1 < len(headings) else len(text)].strip()
                        for i, h in enumerate(headings) if h[1] not in excluded)


def adopt_existing(rows: list[dict], catalog: dict, archive: Path) -> None:
    """One-time import into the catalog makes manual notes survive regeneration."""
    for row in rows:
        matches = []
        for page in archive.glob(f"{row['wid']}_*.md"):
            text = read_text(page).replace("\r\n", "\n").replace("\r", "\n")
            mod_line = re.search(r"^\| mod id[^|]*\|(.+)$", text, re.M | re.I)
            rid = row["info"].get("id", row["folder"])
            if mod_line and f"`{rid}`" in mod_line[1]:
                matches.append((page, text))
        if len(matches) > 1:
            raise ValueError(f"ambiguous existing archive: {row['folder']}")
        if not matches:
            continue
        page, text = matches[0]
        cat = row["cat"]
        title = text.splitlines()[0].removeprefix("# ")
        cat.setdefault("cn", title.split("（", 1)[0])
        cat.setdefault("brief", cat["cn"])
        category = re.search(r"分类：([^·\n]+)", text)
        cat.setdefault("cat", category[1].strip() if category else "其他")
        for heading, key in (("它做什么", "what"), ("双端与联机", "mp"), ("实测与排查", "note")):
            found = re.search(rf"^## {heading}\n+(.*?)(?=^## |\Z)", text, re.M | re.S)
            if found:
                cat[key] = found[1].strip()
        cat["file"] = page.name
        cat["retained"] = manual_sections(text)
        catalog[row["catalog_key"]] = cat


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
    if row["cat"].get("file"):
        filename = row["cat"]["file"]
        if Path(filename).name != filename or not filename.endswith(".md"):
            raise ValueError("unsafe archive filename in catalog")
        return filename
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
    if folder in {"ImmersiveDriving", "ShiftYourGear", "ViewpointVanillaSteering",
                  "ViewpointDriveByShooting", "CarRoofFix", "CarEnterExitFix"}:
        return "驾驶与载具交互"
    for name, folders in README_GROUPS:
        if folder in folders:
            return name
    return "其他"


def cell(value: object) -> str:
    return str(value).replace("|", "&#124;").replace("\n", "<br>").replace("\r", "")


def grouped_pages(rows: list[dict]) -> list[dict]:
    groups = OrderedDict()
    for row in rows:
        groups.setdefault(file_name(row), []).append(row)
    result = []
    for members in groups.values():
        page = dict(members[0])
        page["members"] = members
        page["facts"] = {}
        for key in ("items", "vehicles", "recipes", "templates", "shared_items", "internal"):
            page["facts"][key] = {k: v for r in members for k, v in r["facts"][key].items()}
        for key in ("branches", "warnings", "unresolved"):
            page["facts"][key] = [v for r in members for v in r["facts"][key]]
        result.append(page)
    return result


def render_doc(row: dict, profile: str, retained: str = "") -> str:
    info, facts, cat = row["info"], row["facts"], row["cat"]
    references = OrderedDict()

    def cite(sources: list[str]) -> str:
        if not sources:
            return ""
        key = tuple(dict.fromkeys(sources))
        references.setdefault(key, len(references) + 1)
        return f"[^{references[key]}]"

    def display(entry: dict) -> str:
        name = entry["cn"]
        status = "" if name["status"] == "有效翻译文件" else f"（{name['status']}）"
        return cell(name["text"] + status) + cite(name["sources"])

    counts = {k: len(facts[k]) for k in ("vehicles", "items", "recipes", "shared_items", "templates")}
    name = info.get("name") or row["folder"]
    title = cat.get("cn", name)
    lines = [f"# {title}" + (f"（{name}）" if title != name else ""), "",
             f"{cat.get('what', '')}", "",
             f"归属：**{'日常组合（玩法待验收）' if row['baseline'] else '兼容候选（未运行验收）'}**；档案视图 `{profile}`。",
             f"当前版本定义：**整车 {counts['vehicles']}、本地物品定义 {counts['items']}、配方 {counts['recipes']}**；"
             f"另引用共享物品 {counts['shared_items']}。本地定义数含内部保留项，见独立列表；整车定义包括覆盖原版的条目，不等于新增车型数。", "",
             "## 如何查找", "",
             "- **生成整车**：在生成车辆菜单搜索下表完整 ID；显示译名时搜索中文列。联机管理命令用 `/addvehicle 完整ID`。",
             "- **添加到背包**：普通物品、维修件、改装件都在添加物品菜单使用完整物品 ID；不要拿配方或内部槽位去刷车。",
             "- **制作配方**：在制作界面查译名；配方 ID 用于排查，不是可放进背包的物品。",
             "- 中文解释说明用途；只有翻译文件中找到的文字才称为游戏中文名。缺译保留脚本显示名，冲突列出各译文。", "",
             "## 整车", ""]
    if facts["vehicles"]:
        lines += ["| 完整生成车辆 ID | 当前中文名 / 名称状态 | 英文名或脚本名 | 变体说明 | 来源 |",
                  "| --- | --- | --- | --- | --- |"]
        for key, entry in sorted(facts["vehicles"].items()):
            p = entry["properties"]
            detail = "；".join(x for x in (
                f"脚本座位数 {p['seats']}" if p.get("seats") else "",
                f"机修类型 {p['mechanictype']}" if p.get("mechanictype") else "",
                "具体外观与性能待游戏实刷"))
            override = cat.get("content", {}).get(key, {}).get("purpose")
            lines.append(f"| `{key}` | {display(entry)} | {cell(entry['en']['text'])}{cite(entry['en']['sources'])} | "
                         f"{cell(override or detail)} | {cite([entry['source']])} |")
    else:
        lines.append("本 Mod 没有当前版本的独立整车定义。")

    categories = [("普通物品与书籍", "普通物品 / 书籍"), ("维修配件", "维修配件"), ("改装配件", "改装配件")]
    for heading, category in categories + [("共享配件", None)]:
        selected = {key: e for key, e in (facts["shared_items"] if category is None else facts["items"]).items()
                    if (e["category"] != "内部定义" if category is None else e["category"] == category)}
        lines += ["", f"## {heading}", ""]
        if not selected:
            lines.append("无当前有效条目。")
            continue
        if category is None:
            lines += ["下列物品由已启用依赖或游戏原版提供，不计入本 Mod 的本地物品数。", ""]
        lines += ["| 完整物品 ID | 游戏显示名 / 名称状态 | 中文用途 / 类别 | 菜单 | 适用车辆与安装位置 | 来源 / 状态 |",
                  "| --- | --- | --- | --- | --- | --- |"]
        for key, entry in sorted(selected.items()):
            fits = entry.get("fitments", [])
            local_fits = [f for f in fits if f["vehicle"] in facts["vehicles"]] or fits
            fit_text = "；".join(dict.fromkeys(f"{f['vehicle']} → {f['slot']}" for f in local_fits)) or "未定位整车安装关系"
            source = entry["provider"] + cite([entry["source"]] + entry.get("purpose_sources", []) + [f["source"] for f in local_fits])
            if entry.get("status"):
                source += "；" + entry["status"]
            lines.append(f"| `{key}` | {display(entry)} | {cell(entry['purpose'])} / {cell(entry['category'])} | "
                         f"添加物品 | {cell(fit_text)} | {cell(source)} |")

    lines += ["", "## 制作配方", ""]
    if facts["recipes"]:
        lines += ["| 配方完整 ID（排查用） | 游戏配方名 / 名称状态 | 中文用途 | 菜单 | 来源 |", "| --- | --- | --- | --- | --- |"]
        for key, entry in sorted(facts["recipes"].items()):
            lines.append(f"| `{key}` | {display(entry)} | {cell(entry['purpose'])} | 制作界面 | {cite([entry['source']])} |")
    else:
        lines.append("无当前有效的脚本制作配方。Lua 动态添加的内容不在本次静态统计内。")

    lines += ["", "## 内部定义、历史分支与未解析引用", "",
              f"有效资源层：{', '.join(sorted(set(facts['branches']))) or '根目录'}；仅合并 common 与所选版本，Overlay 按相对路径覆盖。",
              f"车辆模板 {counts['templates']} 个、内部槽位 {len(facts['internal'])} 个，均不算整车或背包物品。"
              "旧根目录和未选中版本的定义不列入当前可用表。模板中短物品引用若追加机修类型后缀才匹配定义，属于静态映射，安装仍待实测。", ""]
    internal_items = {k: e for k, e in {**facts["shared_items"], **facts["items"]}.items() if e["category"] == "内部定义"}
    if internal_items:
        lines += ["内部或过时的 item 定义单列于此，不在上面的背包刷取建议中；它们仍计入各自来源的定义数量。", "",
                  "| 保留定义 ID（不作正常刷取建议） | 脚本显示名 | 中文说明 / 状态 | 来源 |", "| --- | --- | --- | --- |"]
        lines += [f"| `{key}` | {cell(e['display'])} | {cell(e['purpose'])}；{cell(e['status'])} | {cite([e['source']])} |" for key, e in sorted(internal_items.items())]
        lines.append("")
    if facts["internal"]:
        lines += ["<details><summary>查看内部槽位（不能直接刷取）</summary>", "", "| 槽位 | 名称或说明 | 来源 |", "| --- | --- | --- |"]
        lines += [f"| `{s}` | {cell(p['label'])} / {slot_explanation(s)} | {cite([p['source']])} |"
                  for s, p in sorted(facts["internal"].items())]
        lines += ["", "</details>", ""]
    unique = {(x["reference"], x["source"], x["reason"]) for x in facts["unresolved"]}
    if unique:
        lines += ["<details><summary>未定位引用：保留排查线索，不作为可刷 ID</summary>", "", "| 引用（不可直接刷取） | 原因 | 来源 |", "| --- | --- | --- |"]
        lines += [f"| {cell(ref)} | {reason} | {cite([source])} |" for ref, source, reason in sorted(unique)]
        lines += ["", "</details>", ""]
    for warning in dict.fromkeys(facts["warnings"]):
        lines.append("- 静态语法警告：" + warning)
    if cat.get("historical"):
        lines += ["", cat["historical"]]
    lines += ["", "## 概览", "", "| Mod ID / 文件夹 | 分发端 | 版本 | 选择的 mod.info | 原件范围 → 当前范围 |", "| --- | --- | --- | --- | --- |"]
    for member in row.get("members", [row]):
        mi = member["info"]
        bounds = f"{mi.get('_base_versionmin') or '-'} … {mi.get('_base_versionmax') or '-'} → {mi.get('versionmin', '-')} … {mi.get('versionmax', '-')}"
        lines.append(f"| `{mi.get('id', member['folder'])}` / `{member['folder']}` | {dist_label(member['distribution'])} | "
                     f"{cell(mi.get('modversion', '未标注'))} | `{mi['_info_path']}` | {bounds}{'（Overlay）' if mi.get('_overlay') else ''} |")
    lines += ["", f"原件体积 {human(sum(m['stats']['bytes'] for m in row.get('members', [row])))}；体积按完整目录统计，与当前内容定义数分开。",
              f"工作坊：[查看作者页面](https://steamcommunity.com/sharedfiles/filedetails/?id={row['wid']})。", "",
              "## 证据与使用边界", "",
              "**verified：有效源码静态确认。** 每个当前可复制 ID 均来自所选版本的定义；这不保证游戏已成功注册、生成、安装或联机同步。",
              "挑战者 5 个车辆中文名另有 Owner 截图确认；本轮没有启动游戏。译文冲突、动态 Lua 内容和玩法效果仍需 Owner 游戏内核实。",
              "以下人工记录保留原始语境；其中旧组合、旧数量和旧候选状态仅供追溯，当前统计与归属以上表和 profile 为准。", "",
              "<!-- retained:start -->", retained or cat.get("retained") or ("## 实测与排查\n\n" + cat.get("note", "暂无专项运行记录。")), "<!-- retained:end -->", "",
              "## 静态来源", "",
              "路径相对 `A004/workspace/mods_library/`；`Overlay/<文件夹>/` 指 `A004/workspace/patches/mods/<文件夹>/`，`游戏原版/` 指当前 B42.22 客户端 Game 目录。翻译来源列出所有候选，未按加载顺序擅自消解异文。", ""]
    for sources, number in references.items():
        lines.append(f"[^{number}]: " + "；".join(f"`{s}`" for s in sources))
    return "\n".join(lines).rstrip() + "\n"


def render_index(pages: list[dict], profile: str, extras: dict[str, str]) -> str:
    vehicles = {k for p in pages for k in p["facts"]["vehicles"]}
    items = {k for p in pages for k in p["facts"]["items"]}
    lines = [f"# B42.22 中文 Mod 手册（{profile}）", "",
             f"当前 {len(pages)} 份档案；整车定义 **{len(vehicles)}** 个、物品定义 **{len(items)}** 个（按完整 ID 去重，含覆盖原版）。共享引用不重复计数。", "",
             "查车先看各页的“整车”表，用完整 ID 或游戏译名搜索；查背包内容看普通物品、维修件、改装件。配方和内部槽位有独立列表。",
             "物品定义数包含当前脚本保留的内部、占位或过时项；这些项目在各页内部定义区单列，不作为背包刷取建议。",
             "结构与统计规则见 [_TEMPLATE.md](_TEMPLATE.md)，运行边界见 [COMPATIBILITY](../COMPATIBILITY.md)。", "",
             "| # | 中文名 | 工作坊 ID | 归属 | 整车 | 本地物品 | 配方 | 共享物品 | 档案 |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for idx, page in enumerate(pages, 1):
        f = page["facts"]
        lines.append(f"| {idx} | {cell(page['cat'].get('cn', page['folder']))} | `{page['wid']}` | "
                     f"{'日常（玩法待验收）' if page['baseline'] else '兼容候选'} | {len(f['vehicles'])} | {len(f['items'])} | {len(f['recipes'])} | {len(f['shared_items'])} | [查看]({file_name(page)}) |")
    if extras:
        lines += ["", "## 保留的档案", "", "这些页面不在本次 profile 中，保留原状态与链接。", ""]
        lines += [f"- [{text.splitlines()[0].removeprefix('# ')}]({name})" for name, text in sorted(extras.items())]
    return "\n".join(lines).rstrip() + "\n"


def render_readme(rows: list[dict], pages: list[dict], profile: str, profiles: list[dict], notes: str = "") -> str:
    baseline = [r for r in rows if r["baseline"]]
    lines = ["# Grsh PZ Modpack · B42.22 中文查询手册", "",
             f"档案视图 `{profile}`：{len(rows)} 个 Mod 中 {len(baseline)} 条属于日常组合；合并附属项后 {len(pages)} 份当前档案。", "",
             "从[完整索引](mod_archives/INDEX.md)找 Mod，再复制该页整车表或物品表的完整 ID。中文解释与实际游戏显示名分列，缺译和冲突均有标记。",
             "日常入口为 `A004/start-server.bat`、`A004/start-client.bat`，默认 `b422-main`。", "",
             "- [兼容与迁移说明](COMPATIBILITY.md)：补丁证据与待验收项。",
             "- [档案格式与统计规则](mod_archives/_TEMPLATE.md)。",
             "- [迁移前历史清单](archive/pre-b422-promotion-20261112/README.md)。", "",
             "## 组合与验证边界", "", "| 组合 | Client / Server | 世界 |", "| --- | --- | --- |"]
    lines += [f"| `{p['profile']}` | {p['client']} / {p['server']} | `{p['world']}` |" for p in profiles]
    client_only = [r["info"].get("id", r["folder"]) for r in baseline if r["distribution"] == "client"]
    lines += ["", f"仅客户端项 {len(client_only)} 条：" + "、".join(f"`{x}`" for x in client_only) + "。",
              "当前数值来自有效 common / 版本层和 Overlay 的静态定义；整车包括覆盖原版的定义，物品不混入旧分支、模板或配方产出引用。",
              "完整原件目录体积单独统计。源码、Owner 截图、游戏实刷是不同证据层；本轮没有游戏运行验证。", "",
              "## 按 Mod 查询", "",
              "“实际文件夹名”对应 `./Zomboid/mods/` 下的目录原名；合并档案会列出全部子 Mod 文件夹。点击 Steam ID 直达工坊页面，点击“详细文档”查看内容与使用方法。",
              "载具数按当前有效整车定义统计（含覆盖原版）；物品数按本 Mod 定义统计（含在详情中单列的内部保留项），共享物品不重复计入。", ""]
    groups = OrderedDict()
    for page in pages:
        group = readme_group(page["folder"])
        if group == "其他" and "载具" in page["cat"].get("cat", ""):
            group = "KI5 载具与载具功能件"
        groups.setdefault(group, []).append(page)
    for group, members in groups.items():
        lines += [f"### {group}", "",
                  "| 中文名 | 实际文件夹名 | Steam ID | 载具数 | 物品数 | 分发端 | 归属 | 详细文档 |",
                  "| --- | --- | --- | --- | --- | --- | --- | --- |"]
        for page in members:
            components = page.get("members", [page])
            folders = "<br>".join(f"`{cell(m['folder'])}`" for m in components)
            labels = {"both": "双端", "client": "仅客户端", "server": "仅服务端"}
            distributions = list(dict.fromkeys(labels.get(m["distribution"], m["distribution"]) for m in components))
            distribution = distributions[0] if len(distributions) == 1 else "<br>".join(
                f"`{cell(m['folder'])}`：{labels.get(m['distribution'], m['distribution'])}" for m in components)
            steam = f"[{page['wid']}](https://steamcommunity.com/sharedfiles/filedetails/?id={page['wid']})"
            lines.append(f"| {cell(page['cat'].get('cn', page['folder']))} | {folders} | {steam} | "
                         f"{len(page['facts']['vehicles'])} | {len(page['facts']['items'])} | {distribution} | "
                         f"{'日常' if page['baseline'] else '兼容候选'} | [详细文档](mod_archives/{file_name(page)}) |")
        lines.append("")
    lines += ["## 更新档案", "", "```bash", "python -B tools/mod_archive.py --profile b422-compat",
              "python -B tools/test_mod_archive.py", "```", "",
              "人工用途、稳定文件名和保留记录存于 `tools/mod_catalog.json`；再次生成保留视图外页面及人工记录。",
              "`--out` 可先写预览目录；README 位于其父目录。新原件需要先补人工目录。生成过程不修改游戏、原件、运行树或存档。", ""]
    if notes:
        lines += ["<details><summary>保留的部署与验证说明（旧语境）</summary>", "", notes, "", "</details>", ""]
    lines += ["所有 Mod 版权归各自作者。本手册不是独立 Review 或 Owner 玩法验收。", ""]
    return "\n".join(lines)


def stamp_facts(facts: dict, origin: str) -> None:
    def stamp(source: str) -> str:
        if source.startswith("Overlay/"):
            return "Overlay/" + origin.rsplit("/", 1)[-1] + "/" + source.removeprefix("Overlay/")
        return f"{origin}/{source}"

    for kind in ("items", "vehicles", "recipes", "templates"):
        for entry in facts[kind].values():
            entry["source"] = stamp(entry["source"])
            for part in entry["parts"].values():
                part["source"] = stamp(part["source"])


def write_changed(path: Path, text: str) -> None:
    data = (text.rstrip() + "\n").encode("utf-8")
    if not path.is_file() or path.read_bytes() != data:
        path.write_bytes(data)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--profile", default="b422-compat")
    ap.add_argument("--lab", default=str(LAB_DEFAULT))
    ap.add_argument("--out", default=str(ROOT / "mod_archives"))
    ap.add_argument("--import-notes", action="store_true", help="import existing authored pages into catalog once")
    ap.add_argument("--report", type=Path, help="optional machine-readable static evidence")
    args = ap.parse_args()
    lab, out = Path(args.lab).resolve(), Path(args.out).resolve()
    pack = json.loads((lab / "workspace/defs" / args.profile / "pack.json").read_text("utf-8"))
    catalog_data = json.loads(CATALOG.read_text("utf-8"))
    catalog, times = catalog_data["mods"], read_times()
    main_path = lab / "workspace/defs/b422-main/pack.json"
    main_pack = json.loads(main_path.read_text("utf-8")) if main_path.is_file() else {}
    baseline = {m["folder"] for m in main_pack.get("mods", []) if m.get("enabled", True)}
    mods, order = pack.get("mods", []), pack.get("loadOrder", [])
    duplicate = {w for w, n in Counter(str(m["workshopId"]) for m in mods).items() if n > 1}
    rows, names = [], {}
    for idx, mod in enumerate(mods, 1):
        wid, folder = str(mod["workshopId"]), mod["folder"]
        root = pick_root(lab / "workspace/mods_library", wid, folder)
        overlay = lab / "workspace/patches/mods" / folder
        info = read_info(root, overlay, pack.get("gameVersion", GAME_VERSION))
        if not info:
            raise ValueError(f"no applicable mod.info: {wid}/{folder}")
        key = catalog_key(wid, folder, duplicate)
        rid = info.get("id", folder)
        rows.append({"idx": idx, "wid": wid, "folder": folder, "enabled": mod.get("enabled", True),
                     "baseline": folder in baseline, "distribution": mod.get("distribution", "both"),
                     "info": info, "load": order.index(rid) + 1 if rid in order else None,
                     "cat": dict(catalog.get(key) or catalog.get(wid) or {}), "catalog_key": key,
                     "updated": times.get(wid, "-"), "root": root, "overlay": overlay})
    source_archive = ROOT / "mod_archives"
    if args.import_notes:
        adopt_existing(rows, catalog, source_archive)
        source_readme = ROOT / "README.md"
        if source_readme.is_file():
            text = read_text(source_readme).replace("\r\n", "\n").replace("\r", "\n")
            found = re.search(r"^## 组合与验证边界\n(.*?)(?=^## )", text, re.M | re.S)
            if found:
                catalog_data.setdefault("readme_notes", found[1].strip())
                catalog_data["readme_notes"] = "\n".join(line for line in catalog_data["readme_notes"].splitlines() if not line.startswith("- 完整包目录统计："))
        catalog_data["_note"] = "当前中文手册的人工目录；file 固定旧链接，content 按完整 ID 记录用途，retained 保留人工证据。统计以有效版本解析为准。"
    missing = [r["folder"] for r in rows if not r["cat"]]
    if missing:
        print("catalog 缺条目:", missing)
        return 2
    for row in rows:
        files = effective_files(row["root"], row["overlay"], pack.get("gameVersion", GAME_VERSION))
        origin = f"{row['wid']}/mods/{row['folder']}"
        row["facts"] = script_facts(row["root"], media_files=files)
        stamp_facts(row["facts"], origin)
        row["stats"] = dir_stats(row["root"])
        if row["enabled"] and row["distribution"] in {"both", "client"}:
            for key, values in load_translations(files, origin).items():
                names.setdefault(key, []).extend(values)
    game = lab / "B42.22_runtime/client/Game"
    scripts = game / "media/scripts"
    core_files = {f"scripts/{p.relative_to(scripts).as_posix()}": (p, f"media/scripts/{p.relative_to(scripts).as_posix()}")
                  for p in sorted(scripts.rglob("*.txt"))} if scripts.is_dir() else {}
    core = script_facts(game, media_files=core_files)
    stamp_facts(core, "游戏原版")
    translations = game / "media/lua/shared/Translate"
    core_names = {f"lua/shared/Translate/{p.relative_to(translations).as_posix()}":
                  (p, f"media/lua/shared/Translate/{p.relative_to(translations).as_posix()}")
                  for language in ("CN", "EN") for p in (translations / language).glob("*")
                  if p.suffix.lower() in {".json", ".txt"}}
    for key, values in load_translations(core_names, "游戏原版").items():
        names.setdefault(key, []).extend(values)
    enrich_content(rows, names, core)
    pages = grouped_pages(rows)
    page_names = {file_name(p) for p in pages}
    extras, extra_bytes = {}, {}
    for source in (source_archive, out):
        for page in source.glob("*.md"):
            if page.name not in page_names | {"INDEX.md", "_TEMPLATE.md"}:
                extras[page.name] = read_text(page)
                extra_bytes[page.name] = page.read_bytes()
    profiles = []
    for name in ("b422-main", "b422-compat-render", "b422-compat-rv", "b422-compat"):
        source = lab / "workspace/defs" / name / "pack.json"
        if source.is_file():
            data = json.loads(source.read_text("utf-8"))
            selected = [m for m in data.get("mods", []) if m.get("enabled", True)]
            profiles.append({"profile": name, "world": data.get("worldName", "-"),
                             "client": sum(m.get("distribution", "both") in {"both", "client"} for m in selected),
                             "server": sum(m.get("distribution", "both") in {"both", "server"} for m in selected)})
    rendered = {}
    for page in pages:
        destination = out / file_name(page)
        retained = manual_sections(read_text(destination)) if destination.is_file() else page["cat"].get("retained", "")
        rendered[file_name(page)] = render_doc(page, args.profile, retained)
    rendered["INDEX.md"] = render_index(pages, args.profile, extras)
    readme = render_readme(rows, pages, args.profile, profiles, catalog_data.get("readme_notes", ""))
    if args.import_notes:
        write_changed(CATALOG, json.dumps(catalog_data, ensure_ascii=False, indent=2))
    out.mkdir(parents=True, exist_ok=True)
    for filename, data in extra_bytes.items():
        destination = out / filename
        if not destination.is_file() or destination.read_bytes() != data:
            destination.write_bytes(data)
    for filename, text in rendered.items():
        write_changed(out / filename, text)
    write_changed(out.parent / "README.md", readme)
    if args.report:
        report = {"profile": args.profile, "game_version": pack.get("gameVersion", GAME_VERSION),
                  "pages": [{"file": file_name(p), "folders": [m["folder"] for m in p["members"]], "facts": p["facts"]} for p in pages],
                  "preserved_files": sorted(extras)}
        write_changed(args.report, json.dumps(report, ensure_ascii=False, indent=2))
    print(f"wrote {len(pages)} current docs, kept {len(extras)} other docs + INDEX.md -> {out}")
    print(f"mods={len(rows)} vehicles={len({k for r in rows for k in r['facts']['vehicles']})} "
          f"items={len({k for r in rows for k in r['facts']['items']})}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
