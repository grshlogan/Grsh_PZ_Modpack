# 游牧网格房车（Nomad Grid RV (Legacy)）

**可建造移动房车** · 分类：载具 / 建造 · 3820158673 · 禁用 · 加载位次 16

## 它做什么

把房车做成可行走的基地：内部网格可建造、可储物，配合 GridRVHost 使用。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3820158673` |
| mod id | `GridRV` |
| 文件夹 | `GridRV` |
| 版本 / 适配 | `42.21` … `42.21` |
| 作者 | Nomad Grid RV team |
| 工作坊更新时间 | 2026-11-04 |
| 分发端 | both |
| 体积 / 文件 | 92.1 MB · 251 文件（lua 18，client 11，server 1；贴图 67；模型 148；翻译 6；Java 源码 0、jar/class 1） |

## 依赖与冲突

- 需要：`ZombieBuddy, Viewpoint, GridRVHost, PZVoxelStudioViewpoint`
- 互斥：`DeadWorksNomadRV, DeadWorksDaleRV`
- 被依赖：`DaleChieftainRV`

## 内容清单

脚本物品 **15** 条：

| 完整 id | 显示名 | 类型 |
| --- | --- | --- |
| `Base.GridRVArmorGrilles` | RV Window Grilles | - |
| `Base.GridRVArmorSkirts` | RV Side Armour | - |
| `Base.GridRVRamV` | RV Spiked Ram (V Wedge) | - |
| `Base.GridRVRamU` | RV Spiked Ram (U Nose) | - |
| `Base.GridRVRamFlat` | RV Spiked Ram (Flat) | - |
| `Base.GridRVArmorDoor` | RV Entry Door Armour | - |
| `Base.GridRVArmourManual` | RV Armour Manual | - |
| `Base.12` | - | - |
| `Base.10` | - | - |
| `Base.1` | - | - |
| `Base.4` | - | - |
| `Base.15` | - | - |
| `Base.6` | - | - |
| `Base.8` | - | - |
| `Base.3` | - | - |

载具脚本 1 条：`GridRV`

配方 4 条：`GridRVMakeArmorDoor`，`GridRVMakeArmorGrilles`，`GridRVMakeArmorSkirts`，`GridRVMakeRamV`

## 双端与联机

双端；房车内部建造需要服务端认可，建议只在联机里用完整三件套。

本机实测文件构成：客户端有 lua；服务端有 lua。

## 实测与排查

刷法：管理员聊天框 `/addvehicle "Base.GridRV" "TEST"`（或只写类名生成在自己身上），也可用 -debug 的「生成车辆」窗口选 `Base.GridRV`。自然刷新权重：campground 2、rvpark 2、trailerpark 0.75、parkingstall 0.35、farm 0.25、四个 trafficjam 0.35；沙盒 `GridRV → SpawnRate` 默认 100，设 0 即完全不刷。15 条脚本物品 + 1 个载具脚本；92 MB。

```
python lab.py check --profile play
grep -a 'GridRV' runs/<trial>/console.log
```

## 作者原话

```
Original 3 x 8 tile RV with movable native-size furniture. Host multiplayer with server-authorized cabin interactions.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3820158673`
- 本地快照：`workspace/mods_library/3820158673/mods/GridRV`
- 档案生成：`python tools/mod_archive.py --profile play`

