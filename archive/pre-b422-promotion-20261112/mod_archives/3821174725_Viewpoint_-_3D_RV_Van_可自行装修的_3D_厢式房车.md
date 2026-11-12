# 3D RV Van 厢货（Viewpoint - 3D RV Van）

**可自行装修的 3D 厢式房车** · 分类：载具 / 房车 · 3821174725 · 启用 · 加载位次 21

## 它做什么

Courier Duo 厢式房车，2×5 空货舱可自己摆家具、接水电；内饰画在车模型内，需要 Viewpoint 3D 视角。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3821174725` |
| mod id | `GridVans` |
| 文件夹 | `GridVans` |
| 版本 / 适配 | `42.21` … `42.21` |
| 作者 | Deadworks Collective |
| 工作坊更新时间 | 2026-10-19 |
| 分发端 | both |
| 体积 / 文件 | 54.4 MB · 34 文件（lua 12，client 7，server 0；贴图 2；模型 10；翻译 2；Java 源码 0、jar/class 1） |

## 依赖与冲突

- 需要：`ZombieBuddy, Viewpoint, GridVansHost, PZVoxelStudioViewpoint`
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

载具脚本 1 条：`VansCourierDuo`

## 双端与联机

双端都要装；服务端靠 GridVansHost。

本机实测文件构成：客户端有 lua；服务端无 lua（只挂载）。

## 实测与排查

0.1.8；摆家具需 `Construction 1P Viewpoint` 或 `Project Viewpoint: Visible Construction`。

```
python lab.py check --profile play
grep -a 'GridVans' runs/<trial>/console.log
```

## 作者原话

```
Independent walkable 3D vans with furniture, battery-powered devices and multiplayer interiors.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3821174725`
- 本地快照：`workspace/mods_library/3821174725/mods/GridVans`
- 档案生成：`python tools/mod_archive.py --profile play`

