# 视角界面（Viewpoint - Interface）

**视角模式UI** · 分类：UI / 渲染 · 3812616893 · 启用 · 加载位次 13

## 它做什么

给 Viewpoint 补界面：切换视角模式、显示当前焦距与准星状态。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3812616893` |
| mod id | `ViewpointUI` |
| 文件夹 | `ViewpointUI` |
| 版本 / 适配 | `42.21` … `-` |
| 作者 | - |
| 工作坊更新时间 | 2026-10-25 |
| 分发端 | both |
| 体积 / 文件 | 2.1 MB · 113 文件（lua 83，client 67，server 0；贴图 2；模型 0；翻译 1；Java 源码 19、jar/class 1） |

## 依赖与冲突

- 需要：`Viewpoint`
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端挂载。

本机实测文件构成：客户端有 lua；服务端无 lua（只挂载）。

## 实测与排查

require Viewpoint，versionMin=42.21。

```
python lab.py check --profile play
grep -a 'ViewpointUI' runs/<trial>/console.log
```

## 作者原话

```
A complete first and third person interface for Viewpoint: aim-and-use interactions, inventory and looting, crafting, building with placement in first person, health, skills, character, vehicles and admin tools, all on the game's own mechanics. Requires Viewpoint and ZombieBuddy.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3812616893`
- 本地快照：`workspace/mods_library/3812616893/mods/ViewpointUI`
- 档案生成：`python tools/mod_archive.py --profile play`

