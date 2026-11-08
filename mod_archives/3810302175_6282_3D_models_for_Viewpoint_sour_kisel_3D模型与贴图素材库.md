# 6282体素模型包（6282 3D models for Viewpoint [sour_kisel]）

**3D模型与贴图素材库** · 分类：素材 / 模型 · 3810302175 · 启用 · 加载位次 3

## 它做什么

把原版大量物件换成体素/3D 模型，是 Viewpoint 画面观感的主要素材来源。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3810302175` |
| mod id | `PZVoxelStudioViewpoint` |
| 文件夹 | `PZVoxelStudioViewpoint` |
| 版本 / 适配 | `42.21.0` … `42.21.0` |
| 作者 | sour_kisel |
| 工作坊更新时间 | 2026-10-31 |
| 分发端 | both |
| 体积 / 文件 | 272.7 MB · 26,304 文件（lua 1，client 1，server 0；贴图 8487；模型 9312；翻译 0） |

## 依赖与冲突

- 需要：无
- 互斥：无
- 被依赖：`GridRV`、`DaleChieftainRV`、`DeadWorksDaleRV`、`DeadWorksNomadRV`、`DeadWorksVehicleFramework`、`GridVans`

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端都要装，缺一边会出现物件显示不一致。

本机实测文件构成：客户端有 lua；服务端无 lua（只挂载）。

## 实测与排查

272 MB、14 组 pz-voxel-studio 模型包；客户端启动时全部读入。

```
python lab.py check --profile play
grep -a 'PZVoxelStudioViewpoint' runs/<trial>/console.log
```

## 作者原话

```
Voxel Studio 3D models for Project Viewpoint (first-person view). Stairs and corner-laid models re-anchored for Viewpoint.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3810302175`
- 本地快照：`workspace/mods_library/3810302175/mods/PZVoxelStudioViewpoint`
- 档案生成：`python tools/mod_archive.py --profile play`

