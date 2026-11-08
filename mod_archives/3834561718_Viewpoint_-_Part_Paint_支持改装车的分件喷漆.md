# 车身分件喷漆（Viewpoint - Part Paint）

**支持改装车的分件喷漆** · 分类：渲染 / 车辆 · 3834561718 · 启用 · 加载位次 28

## 它做什么

让车身各分件单独上色，KI5 等改装车也能按分件换色。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3834561718` |
| mod id | `ViewpointPartPaint` |
| 文件夹 | `ViewpointPartPaint` |
| 版本 / 适配 | `42.21` … `-` |
| 作者 | - |
| 工作坊更新时间 | 2026-11-07 |
| 分发端 | both |
| 体积 / 文件 | 700.4 KB · 33 文件（lua 4，client 2，server 0；贴图 1；模型 1；翻译 6；Java 源码 17、jar/class 1） |

## 依赖与冲突

- 需要：`ZombieBuddy, Viewpoint`
- 互斥：`VehiclePartPaint, VehiclePartPaintNoJava`
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端挂载；Java 模块。

本机实测文件构成：客户端有 lua；服务端无 lua（只挂载）。

## 实测与排查

与 VehiclePartPaint / VehiclePartPaintNoJava 互斥（本包未装）；jar=ViewpointPartPaint.jar。

```
python lab.py check --profile play
grep -a 'ViewpointPartPaint' runs/<trial>/console.log
```

## 作者原话

```
Hoods, trunk lids and doors keep the look of the car they were taken from: put a blue hood on a white car and it stays blue, a police door on a plain car of the same model keeps its livery. In Project Viewpoint's 3D view and in the isometric view. Needs ZombieBuddy and Viewpoint, Java approval required. Not using Viewpoint? Use Vehicle Part Paint instead.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3834561718`
- 本地快照：`workspace/mods_library/3834561718/mods/ViewpointPartPaint`
- 档案生成：`python tools/mod_archive.py --profile play`

