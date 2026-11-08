# Neat界面框架（NeatUI_Framework）

**制作界面框架** · 分类：框架 / UI · 3508537032 · 启用 · 加载位次 25

## 它做什么

Neat 系列的界面框架，提供制作面板的布局、皮肤与交互组件。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3508537032` |
| mod id | `NeatUI_Framework` |
| 文件夹 | `NeatUI_Framework` |
| 版本 / 适配 | `42.0.2` … `-` |
| 作者 | Rocco, Afyrmo |
| 工作坊更新时间 | 2026-10-31 |
| 分发端 | both |
| 体积 / 文件 | 2.2 MB · 98 文件（lua 11，client 11，server 0；贴图 62；模型 0；翻译 0） |

## 依赖与冲突

- 需要：无
- 互斥：无
- 被依赖：`Project_Cook`、`Neat_Crafting`

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端。

本机实测文件构成：客户端有 lua；服务端无 lua（只挂载）。

## 实测与排查

Neat_Crafting 与 Project_Cook 都 require 它。

```
python lab.py check --profile play
grep -a 'NeatUI_Framework' runs/<trial>/console.log
```

## 作者原话

```
Shared UI framework for Neat mods, providing reusable interface components, styling, shared UI assets, and compatibility helpers for Project Zomboid Build 42. <LINE> Build Support: Build 42. <LINE> Includes compatibility helpers for UI API changes across Build 42 versions. <LINE> Linux dedicated server compatibility: Lua file paths and line endings remain normalized to reduce the chance of checksum issues on case-sensitive servers. <LINE> Multiplayer/server compatibility: empty animation/actiongroup media folders are included because this framework does not ship custom animation files.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3508537032`
- 本地快照：`workspace/mods_library/3508537032/mods/NeatUI_Framework`
- 档案生成：`python tools/mod_archive.py --profile play`

