# '91 Range Rover Classic（'91 RANGE ROVER Classic）

**经典英式越野 SUV** · 分类：载具 / 越野 · `2409333430` · 启用 · 加载位次 28

## 它做什么

1991 Range Rover Classic，适合土路与越野。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `2409333430` |
| mod id | `91range` |
| 文件夹 | `91range` |
| 版本 / 适配 | `42.20.0` … `-` |
| 作者 | KI5 |
| 工作坊更新时间 | 2026-10-09 |
| 分发端 | both（双端） |
| 体积 / 文件 | 18.1 MB · 430 文件（lua 31，client 12，server 11；贴图 286；模型 6；翻译 7） |

## 依赖与冲突

- 需要：`damnlib`
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有独立脚本物品；载具和配方见下。

载具脚本 2 条：`91range`，`91range2`

配方 25 条：`91range`，`91rangeMakeFrontBullbar`，`91rangeMakeFrontDoor`，`91rangeMakeFrontSeat`，`91rangeMakeFrontSideWindow`，`91rangeMakeFrontWindowArmor`，`91rangeMakeFrontWindshield`，`91rangeMakeFrontWindshieldArmor`，`91rangeMakeHood`，`91rangeMakeMudflaps`，`91rangeMakeRearBullbar`，`91rangeMakeRearDoor`，`91rangeMakeRearSeat`，`91rangeMakeRearSideWindow`，`91rangeMakeRearWindowArmor`，`91rangeMakeRearWindshield`，`91rangeMakeRearWindshieldArmor`，`91rangeMakeRoofrack`，`91rangeMakeSidesteps`，`91rangeMakeSunroofWindow`，`91rangeMakeTire`，`91rangeMakeTrunkLid`，`Dismantle`，`Make`，`Repair`

## 双端与联机

双端都要装。

当前 profile：both（双端）。

本机文件构成：客户端有 lua；服务端有 lua。

## 实测与排查

require damnlib；36 个脚本物品、2 个载具脚本、25 条配方。

```
cd A004/B42.22_TEST
python lab.py check --profile b422-batch2
grep -a '91range' runs/<trial>/console.log
```

## 作者原话

```
This mod adds RANGE ROVER Classic, SUV from 1991
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=2409333430`
- 本地快照（测试台）：`A004/B42.22_TEST/workspace/mods_library/2409333430/mods/91range`
- 档案生成：`python tools/mod_archive.py --profile b422-batch2`
