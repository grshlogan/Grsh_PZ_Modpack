# CleanHotBar 清爽快捷栏（CleanHotBar）

**更清晰的可配置快捷栏** · 分类：界面 / HUD · `3461263912` · 启用 · 加载位次 15

## 它做什么

更干净、信息更丰富的 B42 快捷栏：显示物品状态、弹药和液体，改进手持槽，内置重排、透明度与兼容槽拖拽高亮。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3461263912` |
| mod id | `CleanHotBar` |
| 文件夹 | `CleanHotBar` |
| 版本 / 适配 | `42.15` … `-` |
| 作者 | Rocco, Afyrmo |
| 工作坊更新时间 | 2026-10-29 |
| 分发端 | both（双端） |
| 体积 / 文件 | 810.9 KB · 202 文件（lua 18，client 18，server 0；贴图 119；模型 0；翻译 56） |

## 依赖与冲突

- 需要：无
- 互斥：`qdx_item_condition,TheStar`
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端挂载；HUD 逻辑在客户端。

当前 profile：both（双端）。

本机文件构成：客户端有 lua；服务端无 lua（只挂载）。

## 实测与排查

本地 42.15 适配；versionMin=42.15；与 qdx_item_condition、TheStar 互斥。

```
cd A004/B42.22_TEST
python lab.py check --profile b422-batch2
grep -a 'CleanHotBar' runs/<trial>/console.log
```

## 作者原话

```
A cleaner, more informative hotbar for Build 42, with item condition, ammo and liquid indicators, improved hand-equipped slots, built-in reordering, configurable opacity, and compatible-slot drag highlighting.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3461263912`
- 本地快照（测试台）：`A004/B42.22_TEST/workspace/mods_library/3461263912/mods/CleanHotBar`
- 档案生成：`python tools/mod_archive.py --profile b422-batch2`
