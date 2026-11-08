# '91 Range Rover Classic（'91 RANGE ROVER Classic）

**经典英式越野 SUV** · 分类：载具 / 越野 · 2409333430 · 启用 · 加载位次 33

## 它做什么

1991 Range Rover Classic，适合土路与越野。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `2409333430` |
| mod id | `91range` |
| 文件夹 | `91range` |
| 版本 / 适配 | `42.0.0` … `-` |
| 作者 | KI5 |
| 工作坊更新时间 | 2026-10-09 |
| 分发端 | both |
| 体积 / 文件 | 18.1 MB · 430 文件（lua 31，client 12，server 11；贴图 286；模型 6；翻译 7） |

## 依赖与冲突

- 需要：`damnlib`
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

脚本物品 **36** 条：

| 完整 id | 显示名 | 类型 |
| --- | --- | --- |
| `Base.1` | - | - |
| `Base.2` | - | - |
| `Base.4` | - | - |
| `Base.9` | - | - |
| `Base.10` | - | - |
| `Base.8` | - | - |
| `Base.3` | - | - |
| `Base.7` | - | - |
| `Base.6` | - | - |
| `Base.91rangeMagazine` | 91 Range Rover Auto Manual | Literature |
| `Base.91rangeTire2` | 91 Range Rover Tire | Normal |
| `Base.91rangeRoofrack2` | 91 Range Rover Roofrack | Normal |
| `Base.91rangeFrontDoor2` | 91 Range Rover Front Door | Normal |
| `Base.91rangeRearDoor2` | 91 Range Rover Rear Door | Normal |
| `Base.91rangeFrontWindowArmor` | 91 Range Rover Front Window Armor | Normal |
| `Base.91rangeRearWindowArmor` | 91 Range Rover Rear Window Armor | Normal |
| `Base.91rangeWindshieldArmor` | 91 Range Rover Windshield Armor | Normal |
| `Base.91rangeWindshieldRearArmor` | 91 Range Rover Rear Windshield Armor | Normal |
| `Base.91rangeEngineDoor2` | 91 Range Rover Hood | Normal |
| `Base.91rangeTrunkDoor2` | 91 Range Rover Trunk Lid | Normal |
| `Base.91rangeSeatFront2` | 91 Range Rover Front Seat | Normal |
| `Base.91rangeSeatRear2` | 91 Range Rover Rear Seat | Normal |
| `Base.91rangeBumperFront0` | 91 Range Rover Front Bumper Type 1 | Normal |
| `Base.91rangeBumperFront1` | 91 Range Rover Front Bumper Type 2 | Normal |
| `Base.91rangeBullbarFrontA` | 91 Range Rover Front Bullbar | Normal |
| `Base.91rangeBumperRear0` | 91 Range Rover Rear Bumper | Normal |
| `Base.91rangeBullbarRearA` | 91 Range Rover Rear Bullbar | Normal |
| `Base.91rangeWindshield2` | 91 Range Rover Windshield | Normal |
| `Base.91rangeFrontSideWindow2` | 91 Range Rover Front Side Window | Normal |
| `Base.91rangeRearSideWindow2` | 91 Range Rover Rear Side Window | Normal |
| `Base.91rangeRearWindshield2` | 91 Range Rover Rear Windshield | Normal |
| `Base.91rangeSunRoof2` | 91 Range Rover Sunroof | Normal |
| `Base.91rangeMudflaps2` | 91 Range Rover Mudflaps | Normal |
| `Base.91rangeSideSteps2` | 91 Range Rover Side Steps | Normal |
| `Base.91rangeSnorkel2` | 91 Range Rover Snorkel | Normal |
| `Base.91rangeTrunk2` | no | Normal |

载具脚本 2 条：`91range`，`91range2`

配方 25 条：`91range`，`91rangeMakeFrontBullbar`，`91rangeMakeFrontDoor`，`91rangeMakeFrontSeat`，`91rangeMakeFrontSideWindow`，`91rangeMakeFrontWindowArmor`，`91rangeMakeFrontWindshield`，`91rangeMakeFrontWindshieldArmor`，`91rangeMakeHood`，`91rangeMakeMudflaps`，`91rangeMakeRearBullbar`，`91rangeMakeRearDoor`，`91rangeMakeRearSeat`，`91rangeMakeRearSideWindow`，`91rangeMakeRearWindowArmor`，`91rangeMakeRearWindshield`，`91rangeMakeRearWindshieldArmor`，`91rangeMakeRoofrack`，`91rangeMakeSidesteps`，`91rangeMakeSunroofWindow`，`91rangeMakeTire`，`91rangeMakeTrunkLid`，`Dismantle`，`Make`，`Repair`

## 双端与联机

双端都要装。

本机实测文件构成：客户端有 lua；服务端有 lua。

## 实测与排查

18.1 MB；require damnlib。

```
python lab.py check --profile play
grep -a '91range' runs/<trial>/console.log
```

## 作者原话

```
This mod adds RANGE ROVER Classic, SUV from 1991
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=2409333430`
- 本地快照：`workspace/mods_library/2409333430/mods/91range`
- 档案生成：`python tools/mod_archive.py --profile play`

