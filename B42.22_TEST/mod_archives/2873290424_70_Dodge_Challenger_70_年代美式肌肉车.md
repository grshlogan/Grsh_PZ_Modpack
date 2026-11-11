# '70 Dodge Challenger

**70 年代美式肌肉车** · 分类：载具 / 轿车 · `2873290424` · 启用 · 加载位次 27

## 它做什么

1970 Dodge Challenger，多种涂装与改装件。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `2873290424` |
| mod id | `70dodge` |
| 文件夹 | `70dodge` |
| 版本 / 适配 | `42.13.0` … `-` |
| 作者 | KI5 |
| 工作坊更新时间 | 2026-03-21 |
| 分发端 | both（双端） |
| 体积 / 文件 | 18.2 MB · 313 文件（lua 24，client 9，server 9；贴图 199；模型 6；翻译 10） |

## 依赖与冲突

- 需要：`damnlib`
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

脚本物品 **30** 条：

| 完整 id | 显示名 | 类型 |
| --- | --- | --- |
| `Base.DodgeMagazine` | 70 Dodge Challenger Auto Manual | Literature |
| `Base.DodgeFrontSeat3` | 70 Dodge Challenger Front Seat | Normal |
| `Base.DodgeRearSeat3` | 70 Dodge Challenger Rear Seat | Normal |
| `Base.DG70RTEngineDoor` | 70 Dodge Challenger RT Hood | Normal |
| `Base.DG70PDEngineDoor` | 70 Dodge Challenger PD Hood | Normal |
| `Base.DG70TAEngineDoor0` | Not in use | Normal |
| `Base.DG70TAEngineDoor1` | 70 Dodge Challenger TA Black Hood | Normal |
| `Base.DG70TrunkDoor3` | 70 Dodge Challenger Trunk Lid | Normal |
| `Base.DG70Door3` | 70 Dodge Challenger Door | Normal |
| `Base.DG70FrontSideWindow3` | 70 Dodge Challenger Front Side Window | Normal |
| `Base.DG70RearSideWindow3` | 70 Dodge Challenger Rear Side Window | Normal |
| `Base.DG70Windshield3` | 70 Dodge Challenger Windshield | Normal |
| `Base.DG70WindshieldRear3` | 70 Dodge Challenger Rear Windshield | Normal |
| `Base.DG70FrontBumper0` | 70 Dodge Challenger Front Bumper | Normal |
| `Base.DG70RearBumper0` | 70 Dodge Challenger Rear Bumper | Normal |
| `Base.DG70FrontBumperA` | 70 Dodge Challenger Front Bullbar Type 1 | Normal |
| `Base.DG70FrontBumperB` | 70 Dodge Challenger Front Bullbar Type 2 | Normal |
| `Base.DG70FrontBumperC` | 70 Dodge Challenger Front Bullbar Type 3 | Normal |
| `Base.DG70RearBumperA` | 70 Dodge Challenger Rear Bullbar Type 1 | Normal |
| `Base.DG70RearBumperB` | 70 Dodge Challenger Rear Bullbar Type 2 | Normal |
| `Base.DG70RearBumperC` | 70 Dodge Challenger Rear Bullbar Type 3 | Normal |
| `Base.DG70WindshieldArmor` | 70 Dodge Challenger Windshield Armor Type 1 | Normal |
| `Base.DG70WindshieldArmorB` | 70 Dodge Challenger Windshield Armor Type 2 | Normal |
| `Base.DG70WindshieldRearArmor` | 70 Dodge Challenger Rear Windshield Armor | Normal |
| `Base.DG70DoorArmor` | 70 Dodge Challenger Door Armor | Normal |
| `Base.DG70Spoiler0` | 70 Dodge Challenger Spoiler Type 1 | Normal |
| `Base.DG70Spoiler1` | 70 Dodge Challenger Spoiler Type 2 | Normal |
| `Base.DG70RTRoof0` | 70 Dodge Challenger RT Roof | Normal |
| `Base.DG70Trunk3` | Trunk | Normal |
| `Base.OldSmallRoofrack3` | Small Vintage Roofrack | Normal |

载具脚本 5 条：`70dodgeBG`，`70dodgeOP`，`70dodgePD`，`70dodgeRT`，`70dodgeTA`

配方 33 条：`70dodge`，`70dodgeB`，`70dodgeBMakeFrontWindshieldArmor`，`70dodgeMakeFrontBullbarA`，`70dodgeMakeFrontBullbarB`，`70dodgeMakeFrontBullbarC`，`70dodgeMakeFrontBumper`，`70dodgeMakeFrontDoor`，`70dodgeMakeFrontSeat`，`70dodgeMakeFrontSideWindow`，`70dodgeMakeFrontWindowArmor`，`70dodgeMakeFrontWindshield`，`70dodgeMakeFrontWindshieldArmor`，`70dodgeMakeRearBullbarA`，`70dodgeMakeRearBullbarB`，`70dodgeMakeRearBullbarC`，`70dodgeMakeRearBumper`，`70dodgeMakeRearSeat`，`70dodgeMakeRearSideWindow`，`70dodgeMakeRearWindshield`，`70dodgeMakeRearWindshieldArmor`，`70dodgeMakeRoofrack`，`70dodgeMakeTire`，`70dodgeMakeTrunkLid`，`70dodgePD`，`70dodgePDMakeHood`，`70dodgeRT`，`70dodgeRTMakeHood`，`70dodgeTA`，`70dodgeTAMakeHood` … 其余 3 条

## 双端与联机

双端都要装。

当前 profile：both（双端）。

本机文件构成：客户端有 lua；服务端有 lua。

## 实测与排查

require damnlib；39 个脚本物品、5 个载具脚本、33 条配方。

```
cd A004/B42.22_TEST
python lab.py check --profile b422-batch2
grep -a '70dodge' runs/<trial>/console.log
```

## 作者原话

```
This mod adds Dodge Challenger, a muscle car from 1970
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=2873290424`
- 本地快照（测试台）：`A004/B42.22_TEST/workspace/mods_library/2873290424/mods/70dodge`
- 档案生成：`python tools/mod_archive.py --profile b422-batch2`
