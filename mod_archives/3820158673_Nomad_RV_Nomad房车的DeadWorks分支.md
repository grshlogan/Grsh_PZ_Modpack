# DeadWorks Nomad 房车（Nomad RV）

**Nomad房车的DeadWorks分支** · 分类：载具 / 房车 · `3820158673` · 启用 · 加载位次 58
归属：**兼容候选（未运行验收）**；档案视图 `b422-compat`。

## 它做什么

提供依赖 DeadWorks 新框架的 Nomad 房车分支及配套物品；不与同一工坊包内的旧 GridRV/Legacy 分支混装。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3820158673` |
| mod id | `DeadWorksNomadRV` |
| 文件夹 | `DeadWorksNomadRV` |
| Mod 版本 | `0.9.2` |
| 原件适配 | `42.21` … `42.21` |
| 当前生效适配 | `42.21` … `42.22`（Overlay 放行，非上游正式支持） |
| 元数据来源 | `42/mod.info` |
| 作者 | DeadWorks Collective |
| 工作坊更新时间 | 2026-11-04 |
| 分发端 | both（双端） |
| 体积 / 文件 | 56.6 MB · 263 文件（lua 6，client 2，server 2；贴图 63；模型 176；翻译 6） |

## 依赖与冲突

- 需要：`DeadWorksVehicleFramework, PZVoxelStudioViewpoint`
- 互斥：`GridRV, GridRVHost, DaleChieftainRV`
- 被依赖：`DeadWorksDaleRV`

## 内容清单

脚本物品 **14** 条：

| 完整 id | 显示名 | 类型 |
| --- | --- | --- |
| `Base.GridRVArmorGrilles` | RV Window Grilles | base:normal |
| `Base.GridRVArmorSkirts` | RV Side Armour | base:normal |
| `Base.GridRVRamV` | RV Spiked Ram (V Wedge) | base:normal |
| `Base.GridRVCowCatcher` | RV Cow Catcher | base:normal |
| `Base.GridRVRamU` | RV Spiked Ram (U Nose) | base:normal |
| `Base.GridRVRamFlat` | RV Spiked Ram (Flat) | base:normal |
| `Base.GridRVArmorDoor` | RV Entry Door Armour | base:normal |
| `Base.GridRVArmourManual` | RV Armour Manual | base:literature |
| `Base.GridRVBikeCarrier` | RV Bike Carrier | base:normal |
| `Base.GridRVCowCatcherXmas` | RV Christmas Cow Catcher | base:normal |
| `Base.GridRVArmorSkirtsXmas` | RV Christmas Side Armour | base:normal |
| `Base.GridRVArmorGrillesXmas` | RV Christmas Window Grilles | base:normal |
| `Base.GridRVArmorDoorXmas` | RV Christmas Entry Door Armour | base:normal |
| `Base.GridRVRamVXmas` | RV Christmas Spiked Ram | base:normal |

载具脚本 1 条：`GridRV`

配方 16 条：`GridRVDecorateArmorDoor`，`GridRVDecorateArmorGrilles`，`GridRVDecorateArmorSkirts`，`GridRVDecorateCowCatcher`，`GridRVDecorateRamV`，`GridRVMakeArmorDoor`，`GridRVMakeArmorGrilles`，`GridRVMakeArmorSkirts`，`GridRVMakeBikeCarrier`，`GridRVMakeCowCatcher`，`GridRVMakeRamV`，`GridRVStripArmorDoor`，`GridRVStripArmorGrilles`，`GridRVStripArmorSkirts`，`GridRVStripCowCatcher`，`GridRVStripRamV`

## 双端与联机

双端候选；依赖 DeadWorksVehicleFramework 与 6282，车内状态和保存读取仍待测试。

当前 profile：both（双端）。

本机文件构成：客户端有 lua；服务端有 lua。

## 实测与排查

原件 0.9.2，42.21 上限；仅元数据 Overlay。未因静态依赖齐全而宣称房车运行正常。

**planned：仅完成依赖、版本与补丁指纹静态检查。** 迁移收尾按 Owner 要求不启动游戏；本候选组合未验证加载、联网、存档或视觉。

版本放行补丁：`A004/workspace/patches/mods/DeadWorksNomadRV/42/mod.info`。原件更新后须重新核对指纹；撤除此补丁后运行 check 会恢复原件版本限制。

```
cd A004
python lab.py check --profile b422-compat
grep -a 'DeadWorksNomadRV' runs/<trial>/*console.log
```

## 作者原话

```
Walkable 3 x 8 tile Nomad RV, model and profile for the DeadWorks Vehicle Framework.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3820158673`
- 本地原件：`A004/workspace/mods_library/3820158673/mods/DeadWorksNomadRV`
- 档案生成：`python tools/mod_archive.py --profile b422-compat`
