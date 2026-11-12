# '90 Ford F350 救护车（'90 Ford F350 Ambulance Type 1）

**可当移动医疗点的救护车** · 分类：载具 / 公务 · `2952802178` · 启用 · 加载位次 40

## 它做什么

1990 Ford F350 救护车，带医疗舱与警灯。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `2952802178` |
| mod id | `90fordF350ambulance` |
| 文件夹 | `90fordF350ambulance` |
| 版本 / 适配 | `42.20.0` … `-` |
| 作者 | KI5 |
| 工作坊更新时间 | 2026-10-27 |
| 分发端 | both（双端） |
| 体积 / 文件 | 10.0 MB · 279 文件（lua 32，client 12，server 12；贴图 162；模型 6；翻译 9） |

## 依赖与冲突

- 需要：`damnlib`
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有独立脚本物品；载具和配方见下。

载具脚本 2 条：`90fordF350SWAT`，`90fordF350ambulance`

配方 20 条：`90fordF350`，`90fordF350DismantleDoubleTires`，`90fordF350MakeBackDoors`，`90fordF350MakeBackWindows`，`90fordF350MakeDoubleTires`，`90fordF350MakeFrontBullbar`，`90fordF350MakeFrontBumper`，`90fordF350MakeFrontWindowArmor`，`90fordF350MakeFrontWindshieldArmor`，`90fordF350MakeRearBumper`，`90fordF350MakeRearDoor`，`90fordF350MakeRearSideWindow`，`90fordF350MakeRearWindowArmor`，`90fordF350MakeRearWindshieldArmor`，`90fordF350MakeReinforcedBumper`，`90fordF350MakeSidesteps`，`90fordF350MakeTire`，`Dismantle`，`Make`，`Repair`

## 双端与联机

双端都要装。

当前 profile：both（双端）。

本机文件构成：客户端有 lua；服务端有 lua。

## 实测与排查

require damnlib；54 个脚本物品、2 个载具脚本、20 条配方。

```
cd A004/B42.22_TEST
python lab.py check --profile b422-batch2
grep -a '90fordF350ambulance' runs/<trial>/console.log
```

## 作者原话

```
This mod adds Ford F350, Type 1 Ambulance from 1990
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=2952802178`
- 本地快照（测试台）：`A004/B42.22_TEST/workspace/mods_library/2952802178/mods/90fordF350ambulance`
- 档案生成：`python tools/mod_archive.py --profile b422-batch2`
