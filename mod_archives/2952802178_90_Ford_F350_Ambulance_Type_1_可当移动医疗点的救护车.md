# '90 Ford F350 救护车（'90 Ford F350 Ambulance Type 1）

1990 Ford F350 救护车，带医疗舱与警灯。

归属：**日常组合（玩法待验收）**；档案视图 `b422-compat`。
当前版本定义：**整车 2、本地物品定义 20、配方 16**；另引用共享物品 25。本地定义数含内部保留项，见独立列表；整车定义包括覆盖原版的条目，不等于新增车型数。

## 如何查找

- **生成整车**：在生成车辆菜单搜索下表完整 ID；显示译名时搜索中文列。联机管理命令用 `/addvehicle 完整ID`。
- **添加到背包**：普通物品、维修件、改装件都在添加物品菜单使用完整物品 ID；不要拿配方或内部槽位去刷车。
- **制作配方**：在制作界面查译名；配方 ID 用于排查，不是可放进背包的物品。
- 中文解释说明用途；只有翻译文件中找到的文字才称为游戏中文名。缺译保留脚本显示名，冲突列出各译文。

## 整车

| 完整生成车辆 ID | 当前中文名 / 名称状态 | 英文名或脚本名 | 变体说明 | 来源 |
| --- | --- | --- | --- | --- |
| `Base.90fordF350SWAT` | '90 Ford F350 S.W.A.T.（未找到有效中文译文）[^1] | '90 Ford F350 S.W.A.T.[^1] | 脚本座位数 5；机修类型 2；具体外观与性能待游戏实刷 | [^2] |
| `Base.90fordF350ambulance` | '90 Ford F350 Ambulance（未找到有效中文译文）[^3] | '90 Ford F350 Ambulance[^3] | 脚本座位数 5；机修类型 2；具体外观与性能待游戏实刷 | [^4] |

## 普通物品与书籍

| 完整物品 ID | 游戏显示名 / 名称状态 | 中文用途 / 类别 | 菜单 | 适用车辆与安装位置 | 来源 / 状态 |
| --- | --- | --- | --- | --- | --- |
| `Base.90fordF350Magazine` | 90 Ford F350 Ambulance Auto Manual（未找到有效中文译文） | 阅读资料；脚本声明解锁：制作第八代福特F系列前车门（Base.8thGenFordFseriesMakeFrontDoor）、制作第八代福特F系列引擎盖（Base.8thGenFordFseriesMakeHood）、制作第八代福特F系列前座椅（Base.8thGenFordFseriesMakeFrontSeat）、制作第八代福特F系列挡风玻璃（Base.8thGenFordFseriesMakeFrontWindshield）、制作第八代福特F系列前侧窗（Base.8thGenFordFseriesMakeFrontSideWindow）、Make 90 Ford F350 Ambulance Rear Door（Base.90fordF350MakeRearDoor）、Make 90 Ford F350 Ambulance Back Doors（Base.90fordF350MakeBackDoors）、Make 90 Ford F350 Ambulance Rear Side Window（Base.90fordF350MakeRearSideWindow）、Make 90 Ford F350 Ambulance Back Windows（Base.90fordF350MakeBackWindows）、Make 90 Ford F350 Ambulance Sidesteps（Base.90fordF350MakeSidesteps） / 普通物品 / 书籍 | 添加物品 | 未定位整车安装关系 | 90fordF350ambulance[^5] |

## 维修配件

| 完整物品 ID | 游戏显示名 / 名称状态 | 中文用途 / 类别 | 菜单 | 适用车辆与安装位置 | 来源 / 状态 |
| --- | --- | --- | --- | --- | --- |
| `Base.90fordF350DoubleTires2` | 90 Ford F350 Double Tires（未找到有效中文译文） | 车辆安装件，用于轮胎（TireRearLeft）、轮胎（TireRearRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.90fordF350ambulance → TireRearLeft；Base.90fordF350ambulance → TireRearRight；Base.90fordF350SWAT → TireRearLeft；Base.90fordF350SWAT → TireRearRight | 90fordF350ambulance[^6] |
| `Base.90fordF350Tire2` | 90 Ford F350 Tire（未找到有效中文译文） | 车辆安装件，用于轮胎（TireFrontLeft）、轮胎（TireFrontRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.90fordF350ambulance → TireFrontLeft；Base.90fordF350ambulance → TireFrontRight；Base.90fordF350SWAT → TireFrontLeft；Base.90fordF350SWAT → TireFrontRight | 90fordF350ambulance[^7] |
| `Base.90fordF350ambBackDoors2` | 90 Ford F350 Ambulance Back Doors（未找到有效中文译文） | 车辆安装件，用于车门（DoorRear）；适用车型见右列 / 维修配件 | 添加物品 | Base.90fordF350ambulance → DoorRear；Base.90fordF350SWAT → DoorRear | 90fordF350ambulance[^8] |
| `Base.90fordF350ambCornerStorageLids2` | 90 Ford F350 Ambulance Corner Storage Lids（未找到有效中文译文） | 车辆安装件，用于后备箱（TrunkDoorCorner）；适用车型见右列 / 维修配件 | 添加物品 | Base.90fordF350ambulance → TrunkDoorCorner；Base.90fordF350SWAT → TrunkDoorCorner | 90fordF350ambulance[^9] |
| `Base.90fordF350ambLeftStorageLids2` | 90 Ford F350 Ambulance Left Storage Lids（未找到有效中文译文） | 车辆安装件，用于后备箱（TrunkDoorLeft）；适用车型见右列 / 维修配件 | 添加物品 | Base.90fordF350ambulance → TrunkDoorLeft；Base.90fordF350SWAT → TrunkDoorLeft | 90fordF350ambulance[^10] |
| `Base.90fordF350ambRearDoor2` | 90 Ford F350 Ambulance Rear Door（未找到有效中文译文） | 车辆安装件，用于车门（DoorRearRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.90fordF350ambulance → DoorRearRight；Base.90fordF350SWAT → DoorRearRight | 90fordF350ambulance[^11] |
| `Base.90fordF350ambRightStorageLid2` | 90 Ford F350 Ambulance Right Storage Lid（未找到有效中文译文） | 车辆安装件，用于后备箱（TrunkDoorRightA）；适用车型见右列 / 维修配件 | 添加物品 | Base.90fordF350ambulance → TrunkDoorRightA；Base.90fordF350SWAT → TrunkDoorRightA | 90fordF350ambulance[^12] |
| `Base.90fordF350ambSeatRear2` | Fake seat you should not spawn（未找到有效中文译文） | 车辆安装件，用于座椅（SeatRear*）；适用车型见右列 / 维修配件 | 添加物品 | Base.90fordF350ambulance → SeatRear*；Base.90fordF350SWAT → SeatRear* | 90fordF350ambulance[^13] |
| `Base.90fordF350ambSidesteps2` | 90 Ford F350 Ambulance Side Steps（未找到有效中文译文） | 车辆安装件，用于车辆安装位（DAMNSideSteps）；适用车型见右列 / 维修配件 | 添加物品 | Base.90fordF350ambulance → DAMNSideSteps；Base.90fordF350SWAT → DAMNSideSteps | 90fordF350ambulance[^14] |
| `Base.90fordF350ambWindowRearSide2` | 90 Ford F350 Ambulance Rear Side Window（未找到有效中文译文） | 车辆安装件，用于车窗（WindowRearRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.90fordF350ambulance → WindowRearRight；Base.90fordF350SWAT → WindowRearRight | 90fordF350ambulance[^15] |
| `Base.90fordF350ambWindowsBack2` | 90 Ford F350 Ambulance Back Windows（未找到有效中文译文） | 车辆安装件，用于挡风玻璃（WindshieldRear）；适用车型见右列 / 维修配件 | 添加物品 | Base.90fordF350ambulance → WindshieldRear；Base.90fordF350SWAT → WindshieldRear | 90fordF350ambulance[^16] |

## 改装配件

| 完整物品 ID | 游戏显示名 / 名称状态 | 中文用途 / 类别 | 菜单 | 适用车辆与安装位置 | 来源 / 状态 |
| --- | --- | --- | --- | --- | --- |
| `Base.90fordF350ambBullbarFront` | 90 Ford F350 Ambulance Front Bullbar（未找到有效中文译文） | 车辆安装件，用于保险杠（DAMNBumperFront）；适用车型见右列 / 改装配件 | 添加物品 | Base.90fordF350ambulance → DAMNBumperFront；Base.90fordF350SWAT → DAMNBumperFront | 90fordF350ambulance[^17] |
| `Base.90fordF350ambBumperFront` | 90 Ford F350 Ambulance Front Bumper（未找到有效中文译文） | 车辆安装件，用于保险杠（DAMNBumperFront）；适用车型见右列 / 改装配件 | 添加物品 | Base.90fordF350ambulance → DAMNBumperFront；Base.90fordF350SWAT → DAMNBumperFront | 90fordF350ambulance[^18] |
| `Base.90fordF350ambBumperRear` | 90 Ford F350 Ambulance Rear Bumper（未找到有效中文译文） | 车辆安装件，用于保险杠（DAMNBumperRear）；适用车型见右列 / 改装配件 | 添加物品 | Base.90fordF350ambulance → DAMNBumperRear；Base.90fordF350SWAT → DAMNBumperRear | 90fordF350ambulance[^19] |
| `Base.90fordF350ambReinforcedBumperFront` | 90 Ford F350 Ambulance Reinforced Front Bumper（未找到有效中文译文） | 车辆安装件，用于保险杠（DAMNBumperFront）；适用车型见右列 / 改装配件 | 添加物品 | Base.90fordF350ambulance → DAMNBumperFront；Base.90fordF350SWAT → DAMNBumperFront | 90fordF350ambulance[^20] |
| `Base.90fordF350ambWindowFrontArmor` | 90 Ford F350 Ambulance Front Window Armor（未找到有效中文译文） | 车辆安装件，用于防护件（DAMNFrontLeftArmor）、防护件（DAMNFrontRightArmor）；适用车型见右列 / 改装配件 | 添加物品 | Base.90fordF350ambulance → DAMNFrontLeftArmor；Base.90fordF350ambulance → DAMNFrontRightArmor；Base.90fordF350SWAT → DAMNFrontLeftArmor；Base.90fordF350SWAT → DAMNFrontRightArmor | 90fordF350ambulance[^21] |
| `Base.90fordF350ambWindowRearArmor` | 90 Ford F350 Ambulance Rear Window Armor（未找到有效中文译文） | 车辆安装件，用于防护件（DAMNRearRightArmor）；适用车型见右列 / 改装配件 | 添加物品 | Base.90fordF350ambulance → DAMNRearRightArmor；Base.90fordF350SWAT → DAMNRearRightArmor | 90fordF350ambulance[^22] |
| `Base.90fordF350ambWindshieldArmor` | 90 Ford F350 Ambulance Windshield Armor（未找到有效中文译文） | 车辆安装件，用于挡风玻璃（DAMNWindshieldArmor）；适用车型见右列 / 改装配件 | 添加物品 | Base.90fordF350ambulance → DAMNWindshieldArmor；Base.90fordF350SWAT → DAMNWindshieldArmor | 90fordF350ambulance[^23] |
| `Base.90fordF350ambWindshieldRearArmor` | 90 Ford F350 Ambulance Rear Windshield Armor（未找到有效中文译文） | 车辆安装件，用于挡风玻璃（DAMNWindshieldRearArmor）；适用车型见右列 / 改装配件 | 添加物品 | Base.90fordF350ambulance → DAMNWindshieldRearArmor；Base.90fordF350SWAT → DAMNWindshieldRearArmor | 90fordF350ambulance[^24] |

## 共享配件

下列物品由已启用依赖或游戏原版提供，不计入本 Mod 的本地物品数。

| 完整物品 ID | 游戏显示名 / 名称状态 | 中文用途 / 类别 | 菜单 | 适用车辆与安装位置 | 来源 / 状态 |
| --- | --- | --- | --- | --- | --- |
| `Base.8thGenFordFseriesEngineDoor2` | 8th Gen Ford F Series Hood（未找到有效中文译文） | 车辆安装件，用于引擎盖（EngineDoor）；适用车型见右列 / 维修配件 | 添加物品 | Base.90fordF350ambulance → EngineDoor；Base.90fordF350SWAT → EngineDoor | damnlib[^25] |
| `Base.8thGenFordFseriesFrontDoor2` | 8th Gen Ford F Series Front Door（未找到有效中文译文） | 车辆安装件，用于车门（DoorFrontLeft）、车门（DoorFrontRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.90fordF350ambulance → DoorFrontLeft；Base.90fordF350ambulance → DoorFrontRight；Base.90fordF350SWAT → DoorFrontLeft；Base.90fordF350SWAT → DoorFrontRight | damnlib[^26] |
| `Base.8thGenFordFseriesSeatFront2` | 8th Gen Ford F Series Front Seat（未找到有效中文译文） | 车辆安装件，用于座椅（SeatFront*）；适用车型见右列 / 维修配件 | 添加物品 | Base.90fordF350ambulance → SeatFront*；Base.90fordF350SWAT → SeatFront* | damnlib[^27] |
| `Base.8thGenFordFseriesWindowFrontSide2` | 8th Gen Ford F Series Front Side Window（未找到有效中文译文） | 车辆安装件，用于车窗（WindowFrontLeft）、车窗（WindowFrontRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.90fordF350ambulance → WindowFrontLeft；Base.90fordF350ambulance → WindowFrontRight；Base.90fordF350SWAT → WindowFrontLeft；Base.90fordF350SWAT → WindowFrontRight | damnlib[^28] |
| `Base.8thGenFordFseriesWindshield2` | 8th Gen Ford F Series Windshield（未找到有效中文译文） | 车辆安装件，用于挡风玻璃（Windshield）；适用车型见右列 / 维修配件 | 添加物品 | Base.90fordF350ambulance → Windshield；Base.90fordF350SWAT → Windshield | damnlib[^29] |
| `Base.BigGasTank2` | 油箱 (大型)（翻译文件含非标准语法，待游戏核实）[^31] | 车辆安装件，用于油箱（GasTank）；适用车型见右列 / 维修配件 | 添加物品 | Base.90fordF350ambulance → GasTank；Base.90fordF350SWAT → GasTank | 游戏原版[^30] |
| `Base.CarBattery2` | 汽车电池（翻译文件含非标准语法，待游戏核实）[^33] | 车辆安装件，用于蓄电池（Battery）、蓄电池（GRHouseBattery1）、蓄电池（GRHouseBattery2）；适用车型见右列 / 维修配件 | 添加物品 | Base.90fordF350ambulance → Battery；Base.90fordF350SWAT → Battery | 游戏原版[^32] |
| `Base.GloveBox2` | 手套箱（翻译文件含非标准语法，待游戏核实）[^35] | 车辆安装件，用于车辆安装位（GloveBox）；适用车型见右列 / 维修配件 | 添加物品 | Base.90fordF350ambulance → GloveBox；Base.90fordF350SWAT → GloveBox | 游戏原版[^34] |
| `Base.HamRadio1` | 微型导航仪 / 收音机 (业余电台) / 民用无线电台 (昂科) / 民用无线电台 - 昂科公司（译文冲突，待游戏核实）[^37] | 车辆安装件，用于车辆安装位（Radio）；适用车型见右列 / 维修配件 | 添加物品 | Base.90fordF350ambulance → Radio；Base.90fordF350SWAT → Radio | 游戏原版[^36] |
| `Base.HamRadio2` | 收音机 (军用) / 军用无线电台（译文冲突，待游戏核实）[^39] | 车辆安装件，用于车辆安装位（Radio）；适用车型见右列 / 维修配件 | 添加物品 | Base.90fordF350ambulance → Radio；Base.90fordF350SWAT → Radio | 游戏原版[^38] |
| `Base.HamRadioMakeShift` | 收音机 (简易业余无线电) / 收音机 (简易业余电台) / 自制无线电台（译文冲突，待游戏核实）[^41] | 车辆安装件，用于车辆安装位（Radio）；适用车型见右列 / 维修配件 | 添加物品 | Base.90fordF350ambulance → Radio；Base.90fordF350SWAT → Radio | 游戏原版[^40] |
| `Base.LightBulb` | 灯泡-白色 / 灯泡 (白)（译文冲突，待游戏核实）[^43] | 车辆安装件，用于车灯（Headlight*）、车灯（JP82DorothyLights）；适用车型见右列 / 维修配件 | 添加物品 | Base.90fordF350ambulance → Headlight*；Base.90fordF350SWAT → Headlight* | 游戏原版[^42] |
| `Base.ModernBrake2` | 制动器 (高级)（翻译文件含非标准语法，待游戏核实）[^45] | 车辆安装件，用于制动器（Brake*）；适用车型见右列 / 维修配件 | 添加物品 | Base.90fordF350ambulance → Brake*；Base.90fordF350SWAT → Brake* | 游戏原版[^44] |
| `Base.ModernCarMuffler2` | 消声器 (高级)（翻译文件含非标准语法，待游戏核实）[^47] | 车辆安装件，用于消声器（Muffler）；适用车型见右列 / 维修配件 | 添加物品 | Base.90fordF350ambulance → Muffler；Base.90fordF350SWAT → Muffler | 游戏原版[^46] |
| `Base.ModernSuspension2` | 悬挂 (高级)（翻译文件含非标准语法，待游戏核实）[^49] | 车辆安装件，用于悬挂（Suspension*）；适用车型见右列 / 维修配件 | 添加物品 | Base.90fordF350ambulance → Suspension*；Base.90fordF350SWAT → Suspension* | 游戏原版[^48] |
| `Base.NormalBrake2` | 制动器 (普通)（翻译文件含非标准语法，待游戏核实）[^51] | 车辆安装件，用于制动器（Brake*）；适用车型见右列 / 维修配件 | 添加物品 | Base.90fordF350ambulance → Brake*；Base.90fordF350SWAT → Brake* | 游戏原版[^50] |
| `Base.NormalCarMuffler2` | 消声器 (普通)（翻译文件含非标准语法，待游戏核实）[^53] | 车辆安装件，用于消声器（Muffler）；适用车型见右列 / 维修配件 | 添加物品 | Base.90fordF350ambulance → Muffler；Base.90fordF350SWAT → Muffler | 游戏原版[^52] |
| `Base.NormalGasTank2` | 油箱 (标准)（翻译文件含非标准语法，待游戏核实）[^55] | 车辆安装件，用于油箱（GasTank）；适用车型见右列 / 维修配件 | 添加物品 | Base.90fordF350ambulance → GasTank；Base.90fordF350SWAT → GasTank | 游戏原版[^54] |
| `Base.NormalSuspension2` | 悬挂 (普通)（翻译文件含非标准语法，待游戏核实）[^57] | 车辆安装件，用于悬挂（Suspension*）；适用车型见右列 / 维修配件 | 添加物品 | Base.90fordF350ambulance → Suspension*；Base.90fordF350SWAT → Suspension* | 游戏原版[^56] |
| `Base.OldBrake2` | 制动器 (老式)（翻译文件含非标准语法，待游戏核实）[^59] | 车辆安装件，用于制动器（Brake*）；适用车型见右列 / 维修配件 | 添加物品 | Base.90fordF350ambulance → Brake*；Base.90fordF350SWAT → Brake* | 游戏原版[^58] |
| `Base.OldCarMuffler2` | 消声器 (老式)（翻译文件含非标准语法，待游戏核实）[^61] | 车辆安装件，用于消声器（Muffler）；适用车型见右列 / 维修配件 | 添加物品 | Base.90fordF350ambulance → Muffler；Base.90fordF350SWAT → Muffler | 游戏原版[^60] |
| `Base.SmallGasTank2` | 油箱 (小型)（翻译文件含非标准语法，待游戏核实）[^63] | 车辆安装件，用于油箱（GasTank）；适用车型见右列 / 维修配件 | 添加物品 | Base.90fordF350ambulance → GasTank；Base.90fordF350SWAT → GasTank | 游戏原版[^62] |
| `USMIL.Stretcher0` | Military Stretcher（未找到有效中文译文） | 车辆安装件，用于车辆安装位（DAMNStretcher）；适用车型见右列 / 维修配件 | 添加物品 | Base.90fordF350ambulance → DAMNStretcher；Base.90fordF350SWAT → DAMNStretcher | damnlib[^64] |
| `USMIL.Stretcher1` | Ambulance Stretcher（未找到有效中文译文） | 车辆安装件，用于车辆安装位（DAMNStretcher）；适用车型见右列 / 维修配件 | 添加物品 | Base.90fordF350ambulance → DAMNStretcher；Base.90fordF350SWAT → DAMNStretcher | damnlib[^65] |

## 制作配方

| 配方完整 ID（排查用） | 游戏配方名 / 名称状态 | 中文用途 | 菜单 | 来源 |
| --- | --- | --- | --- | --- |
| `Base.90fordF350DismantleDoubleTires` | Dismantle 90 Ford F350 Double Tires（未找到有效中文译文）[^66] | 制作产出：90 Ford F350 Tire（车辆安装件，用于轮胎（TireFrontLeft）、轮胎（TireFrontRight）；适用车型见右列） | 制作界面 | [^67] |
| `Base.90fordF350MakeBackDoors` | Make 90 Ford F350 Ambulance Back Doors（未找到有效中文译文）[^68] | 制作产出：90 Ford F350 Ambulance Back Doors（车辆安装件，用于车门（DoorRear）；适用车型见右列） | 制作界面 | [^69] |
| `Base.90fordF350MakeBackWindows` | Make 90 Ford F350 Ambulance Back Windows（未找到有效中文译文）[^70] | 制作产出：90 Ford F350 Ambulance Back Windows（车辆安装件，用于挡风玻璃（WindshieldRear）；适用车型见右列） | 制作界面 | [^71] |
| `Base.90fordF350MakeDoubleTires` | Make 90 Ford F350 Double Tires（未找到有效中文译文）[^72] | 制作产出：90 Ford F350 Double Tires（车辆安装件，用于轮胎（TireRearLeft）、轮胎（TireRearRight）；适用车型见右列） | 制作界面 | [^73] |
| `Base.90fordF350MakeFrontBullbar` | Make 90 Ford F350 Ambulance Front Bullbar（未找到有效中文译文）[^74] | 制作产出：90 Ford F350 Ambulance Front Bullbar（车辆安装件，用于保险杠（DAMNBumperFront）；适用车型见右列） | 制作界面 | [^75] |
| `Base.90fordF350MakeFrontBumper` | Make 90 Ford F350 Ambulance Front Bumper（未找到有效中文译文）[^76] | 制作产出：90 Ford F350 Ambulance Front Bumper（车辆安装件，用于保险杠（DAMNBumperFront）；适用车型见右列） | 制作界面 | [^77] |
| `Base.90fordF350MakeFrontWindowArmor` | Make 90 Ford F350 Ambulance Front Window Armor（未找到有效中文译文）[^78] | 制作产出：90 Ford F350 Ambulance Front Window Armor（车辆安装件，用于防护件（DAMNFrontLeftArmor）、防护件（DAMNFrontRightArmor）；适用车型见右列） | 制作界面 | [^79] |
| `Base.90fordF350MakeFrontWindshieldArmor` | Make 90 Ford F350 Ambulance Front Windshield Armor（未找到有效中文译文）[^80] | 制作产出：90 Ford F350 Ambulance Windshield Armor（车辆安装件，用于挡风玻璃（DAMNWindshieldArmor）；适用车型见右列） | 制作界面 | [^81] |
| `Base.90fordF350MakeRearBumper` | Make 90 Ford F350 Ambulance Rear Bumper（未找到有效中文译文）[^82] | 制作产出：90 Ford F350 Ambulance Rear Bumper（车辆安装件，用于保险杠（DAMNBumperRear）；适用车型见右列） | 制作界面 | [^83] |
| `Base.90fordF350MakeRearDoor` | Make 90 Ford F350 Ambulance Rear Door（未找到有效中文译文）[^84] | 制作产出：90 Ford F350 Ambulance Rear Door（车辆安装件，用于车门（DoorRearRight）；适用车型见右列） | 制作界面 | [^85] |
| `Base.90fordF350MakeRearSideWindow` | Make 90 Ford F350 Ambulance Rear Side Window（未找到有效中文译文）[^86] | 制作产出：90 Ford F350 Ambulance Rear Side Window（车辆安装件，用于车窗（WindowRearRight）；适用车型见右列） | 制作界面 | [^87] |
| `Base.90fordF350MakeRearWindowArmor` | Make 90 Ford F350 Ambulance Rear Window Armor（未找到有效中文译文）[^88] | 制作产出：90 Ford F350 Ambulance Rear Window Armor（车辆安装件，用于防护件（DAMNRearRightArmor）；适用车型见右列） | 制作界面 | [^89] |
| `Base.90fordF350MakeRearWindshieldArmor` | Make 90 Ford F350 Ambulance Rear Windshield Armor（未找到有效中文译文）[^90] | 制作产出：90 Ford F350 Ambulance Rear Windshield Armor（车辆安装件，用于挡风玻璃（DAMNWindshieldRearArmor）；适用车型见右列） | 制作界面 | [^91] |
| `Base.90fordF350MakeReinforcedBumper` | Make 90 Ford F350 Ambulance Reinforced Bumper（未找到有效中文译文）[^92] | 制作产出：90 Ford F350 Ambulance Reinforced Front Bumper（车辆安装件，用于保险杠（DAMNBumperFront）；适用车型见右列） | 制作界面 | [^93] |
| `Base.90fordF350MakeSidesteps` | Make 90 Ford F350 Ambulance Sidesteps（未找到有效中文译文）[^94] | 制作产出：90 Ford F350 Ambulance Side Steps（车辆安装件，用于车辆安装位（DAMNSideSteps）；适用车型见右列） | 制作界面 | [^95] |
| `Base.90fordF350MakeTire` | Make 90 Ford F350 Tire（未找到有效中文译文）[^96] | 制作产出：90 Ford F350 Tire（车辆安装件，用于轮胎（TireFrontLeft）、轮胎（TireFrontRight）；适用车型见右列） | 制作界面 | [^97] |

## 内部定义、历史分支与未解析引用

有效资源层：42.20, common；仅合并 common 与所选版本，Overlay 按相对路径覆盖。
车辆模板 11 个、内部槽位 69 个，均不算整车或背包物品。旧根目录和未选中版本的定义不列入当前可用表。模板中短物品引用若追加机修类型后缀才匹配定义，属于静态映射，安装仍待实测。

内部或过时的 item 定义单列于此，不在上面的背包刷取建议中；它们仍计入各自来源的定义数量。

| 保留定义 ID（不作正常刷取建议） | 脚本显示名 | 中文说明 / 状态 | 来源 |
| --- | --- | --- | --- |
| `damnCraft.Trunk2` | no | 车辆后备箱的内部容量载体，关联车辆槽位与容积状态；不是可携带的旅行箱；显示名 no、图标 na；不作正常刷取建议 | [^98] |

<details><summary>查看内部槽位（不能直接刷取）</summary>

| 槽位 | 名称或说明 | 来源 |
| --- | --- | --- |
| `Battery` | 电池 / 蓄电池 | [^99] |
| `Brake*` | Brake* / 制动器 | [^100] |
| `BrakeFrontLeft` | 左前制动 / 制动器 | [^101] |
| `BrakeFrontRight` | 右前制动 / 制动器 | [^102] |
| `BrakeRearLeft` | 左后制动 / 制动器 | [^103] |
| `BrakeRearRight` | 右后制动 / 制动器 | [^104] |
| `DAMNBumperFront` | 前保险杠 / 保险杠 | [^105] |
| `DAMNBumperRear` | 后保险杠 / 保险杠 | [^106] |
| `DAMNFrontLeftArmor` | 左前车窗装甲 / 防护件 | [^107] |
| `DAMNFrontRightArmor` | 右前车窗装甲 / 防护件 | [^108] |
| `DAMNRearRightArmor` | 右后车窗装甲 / 防护件 | [^109] |
| `DAMNSideSteps` | 侧踏板 / 车辆安装位 | [^110] |
| `DAMNStretcher` | 担架 / 车辆安装位 | [^111] |
| `DAMNWindshieldArmor` | 挡风玻璃装甲 / 挡风玻璃 | [^112] |
| `DAMNWindshieldRearArmor` | 后挡风玻璃装甲 / 挡风玻璃 | [^113] |
| `Door*` | Door* / 车门 | [^114] |
| `DoorFrontLeft` | 左前门 / 车门 | [^115] |
| `DoorFrontRight` | 右前门 / 车门 | [^116] |
| `DoorRear` | 后门 / 车门 | [^117] |
| `DoorRearRight` | 右后门 / 车门 | [^118] |
| `Engine` | 引擎 / 发动机 | [^119] |
| `EngineDoor` | 引擎盖 / 引擎盖 | [^120] |
| `F350InsideFrontStorage` | Interior Front Storage / 车辆安装位 | [^121] |
| `F350InsideLeftStorage` | Interior Left Storage / 车辆安装位 | [^122] |
| `F350InsideRightBottomStorage` | Interior Right Bottom Storage / 车辆安装位 | [^123] |
| `F350InsideRightTopStorage` | Interior Right Top Storage / 车辆安装位 | [^124] |
| `F350LowCornerStorage` | Corner Low Storage / 车辆安装位 | [^125] |
| `F350LowStorage` | Left Low Storage / 车辆安装位 | [^126] |
| `F350RearStorage` | Corner Top Storage / 车辆安装位 | [^127] |
| `F350RightStorage` | Right Storage / 车辆安装位 | [^128] |
| `F350TallStorage` | Left Tall Storage / 车辆安装位 | [^129] |
| `GasTank` | 油箱 / 油箱 | [^130] |
| `GloveBox` | 手套箱 / 车辆安装位 | [^131] |
| `Headlight*` | Headlight* / 车灯 | [^132] |
| `HeadlightLeft` | 左大灯 / 车灯 | [^133] |
| `HeadlightRearLeft` | 左尾灯 / 车灯 | [^134] |
| `HeadlightRearRight` | 右尾灯 / 车灯 | [^135] |
| `HeadlightRight` | 右大灯 / 车灯 | [^136] |
| `Heater` | 加热器 / 车辆安装位 | [^137] |
| `Muffler` | 排气消声器 / 消声器 | [^138] |
| `PassengerCompartment` | 乘员舱 / 车辆安装位 | [^139] |
| `Radio` | 电台 / 车辆安装位 | [^140] |
| `SeatFront*` | SeatFront* / 座椅 | [^141] |
| `SeatFrontLeft` | 驾驶座 / 座椅 | [^142] |
| `SeatFrontRight` | 右前座 / 座椅 | [^143] |
| `SeatRear*` | SeatRear* / 座椅 | [^144] |
| `SeatRearLeft` | 左后座 / 座椅 | [^145] |
| `SeatRearRight` | 右后座 / 座椅 | [^146] |
| `Suspension*` | Suspension* / 悬挂 | [^147] |
| `SuspensionFrontLeft` | 左前悬挂 / 悬挂 | [^148] |
| `SuspensionFrontRight` | 右前悬挂 / 悬挂 | [^149] |
| `SuspensionRearLeft` | 左后悬挂 / 悬挂 | [^150] |
| `SuspensionRearRight` | 右后悬挂 / 悬挂 | [^151] |
| `Tire*` | Tire* / 轮胎 | [^152] |
| `TireFrontLeft` | 左前胎 / 轮胎 | [^153] |
| `TireFrontRight` | 右前胎 / 轮胎 | [^154] |
| `TireRearLeft` | 左后胎 / 轮胎 | [^155] |
| `TireRearRight` | 右后胎 / 轮胎 | [^156] |
| `TruckBed` | 补给箱 / 行李箱 / 车辆安装位 | [^157] |
| `TrunkDoorCorner` | Corner Storage Lids / 后备箱 | [^158] |
| `TrunkDoorLeft` | 左侧储物箱盖 / 后备箱 | [^159] |
| `TrunkDoorRightA` | Right Storage Lid / 后备箱 | [^160] |
| `WindowFront*` | WindowFront* / 车窗 | [^161] |
| `WindowFrontLeft` | 左前窗 / 车窗 | [^162] |
| `WindowFrontRight` | 右前窗 / 车窗 | [^163] |
| `WindowRear*` | WindowRear* / 车窗 | [^164] |
| `WindowRearRight` | 右后窗 / 车窗 | [^165] |
| `Windshield` | 挡风玻璃 / 挡风玻璃 | [^166] |
| `WindshieldRear` | 后挡风玻璃 / 挡风玻璃 | [^167] |

</details>


## 概览

| Mod ID / 文件夹 | 分发端 | 版本 | 选择的 mod.info | 原件范围 → 当前范围 |
| --- | --- | --- | --- | --- |
| `90fordF350ambulance` / `90fordF350ambulance` | both（双端） | 未标注 | `42.20/mod.info` | 42.20.0 … - → 42.20.0 … - |

原件体积 10.0 MB；体积按完整目录统计，与当前内容定义数分开。
工作坊：[查看作者页面](https://steamcommunity.com/sharedfiles/filedetails/?id=2952802178)。

## 证据与使用边界

**verified：有效源码静态确认。** 每个当前可复制 ID 均来自所选版本的定义；这不保证游戏已成功注册、生成、安装或联机同步。
挑战者 5 个车辆中文名另有 Owner 截图确认；本轮没有启动游戏。译文冲突、动态 Lua 内容和玩法效果仍需 Owner 游戏内核实。
以下人工记录保留原始语境；其中旧组合、旧数量和旧候选状态仅供追溯，当前统计与归属以上表和 profile 为准。

<!-- retained:start -->
## 依赖与冲突

- 需要：`damnlib`
- 互斥：无
- 被依赖：无（叶子节点）

## 双端与联机

双端都要装。

当前 profile：both（双端）。

本机文件构成：客户端有 lua；服务端有 lua。

## 实测与排查

require damnlib；54 个脚本物品、2 个载具脚本、20 条配方。

```
cd A004
python lab.py check --profile b422-compat
grep -a '90fordF350ambulance' runs/<trial>/*console.log
```
<!-- retained:end -->

## 静态来源

路径相对 `A004/workspace/mods_library/`；`Overlay/<文件夹>/` 指 `A004/workspace/patches/mods/<文件夹>/`，`游戏原版/` 指当前 B42.22 客户端 Game 目录。翻译来源列出所有候选，未按加载顺序擅自消解异文。

[^1]: `2952802178/mods/90fordF350ambulance/common/media/lua/shared/Translate/EN/IG_UI.json:4`
[^2]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350SWAT.txt:3`
[^3]: `2952802178/mods/90fordF350ambulance/common/media/lua/shared/Translate/EN/IG_UI.json:3`
[^4]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance.txt:24`
[^5]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance_vehiclesitems.txt:5`
[^6]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance_vehiclesitems.txt:43`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_tire.txt:56`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_tire.txt:72`
[^7]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance_vehiclesitems.txt:23`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_tire.txt:23`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_tire.txt:40`
[^8]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance_vehiclesitems.txt:80`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_doors.txt:203`
[^9]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance_vehiclesitems.txt:112`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_trunkdoors.txt:153`
[^10]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance_vehiclesitems.txt:97`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_trunkdoors.txt:30`
[^11]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance_vehiclesitems.txt:65`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_doors.txt:149`
[^12]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance_vehiclesitems.txt:127`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_trunkdoors.txt:276`
[^13]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance_vehiclesitems.txt:272`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_seats.txt:145`
[^14]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance_vehiclesitems.txt:320`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_sidesteps.txt:15`
[^15]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance_vehiclesitems.txt:288`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_windows.txt:84`
[^16]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance_vehiclesitems.txt:303`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_windshield.txt:80`
[^17]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance_vehiclesitems.txt:159`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_bumpers.txt:35`
[^18]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance_vehiclesitems.txt:144`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_bumpers.txt:35`
[^19]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance_vehiclesitems.txt:189`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_bumpers.txt:107`
[^20]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance_vehiclesitems.txt:174`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_bumpers.txt:35`
[^21]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance_vehiclesitems.txt:222`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_armor.txt:109`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_armor.txt:173`
[^22]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance_vehiclesitems.txt:238`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_armor.txt:237`
[^23]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance_vehiclesitems.txt:206`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_armor.txt:46`
[^24]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance_vehiclesitems.txt:254`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_armor.txt:301`
[^25]: `3171167894/mods/damnlib/42.20/media/scripts/commonItems/8thGenFordFseries_vehicleitems.txt:22`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_hood.txt:14`
[^26]: `3171167894/mods/damnlib/42.20/media/scripts/commonItems/8thGenFordFseries_vehicleitems.txt:5`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_doors.txt:41`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_doors.txt:95`
[^27]: `3171167894/mods/damnlib/42.20/media/scripts/commonItems/8thGenFordFseries_vehicleitems.txt:39`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_seats.txt:94`
[^28]: `3171167894/mods/damnlib/42.20/media/scripts/commonItems/8thGenFordFseries_vehicleitems.txt:72`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_windows.txt:32`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_windows.txt:58`
[^29]: `3171167894/mods/damnlib/42.20/media/scripts/commonItems/8thGenFordFseries_vehicleitems.txt:57`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_windshield.txt:22`
[^30]: `游戏原版/media/scripts/generated/items/normal.txt:12408`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance.txt:413`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350SWAT.txt:365`
[^31]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:448`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:163`
[^32]: `游戏原版/media/scripts/generated/items/drainable.txt:2368`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance.txt:428`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350SWAT.txt:380`
[^33]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:970`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:380`
[^34]: `游戏原版/media/scripts/generated/items/normal.txt:13025`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance.txt:386`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350SWAT.txt:340`
[^35]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1776`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:687`
[^36]: `游戏原版/media/scripts/generated/items/radio.txt:203`；`游戏原版/media/scripts/generated/vehicles/template_radio_HAM.txt:5`
[^37]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:3000`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25094`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1908`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:3486`
[^38]: `游戏原版/media/scripts/generated/items/radio.txt:229`；`游戏原版/media/scripts/generated/vehicles/template_radio_HAM.txt:5`
[^39]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:7376`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25095`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1909`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:3487`
[^40]: `游戏原版/media/scripts/generated/items/radio.txt:255`；`游戏原版/media/scripts/generated/vehicles/template_radio_HAM.txt:5`
[^41]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:7377`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25096`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1910`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:3488`
[^42]: `游戏原版/media/scripts/generated/items/normal.txt:4661`；`游戏原版/media/scripts/generated/vehicles/template_headlight.txt:25`
[^43]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:6727`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25103`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2563`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:965`
[^44]: `游戏原版/media/scripts/generated/items/normal.txt:12163`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance.txt:476`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350SWAT.txt:426`
[^45]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2780`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1050`
[^46]: `游戏原版/media/scripts/generated/items/normal.txt:13166`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance.txt:441`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350SWAT.txt:391`
[^47]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2783`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1053`
[^48]: `游戏原版/media/scripts/generated/items/normal.txt:12282`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance.txt:493`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350SWAT.txt:443`
[^49]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2786`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1056`
[^50]: `游戏原版/media/scripts/generated/items/normal.txt:12146`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance.txt:476`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350SWAT.txt:426`
[^51]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3219`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1135`
[^52]: `游戏原版/media/scripts/generated/items/normal.txt:13151`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance.txt:441`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350SWAT.txt:391`
[^53]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3222`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1138`
[^54]: `游戏原版/media/scripts/generated/items/normal.txt:12393`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance.txt:413`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350SWAT.txt:365`
[^55]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3228`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1144`
[^56]: `游戏原版/media/scripts/generated/items/normal.txt:12265`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance.txt:493`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350SWAT.txt:443`
[^57]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3231`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1147`
[^58]: `游戏原版/media/scripts/generated/items/normal.txt:12129`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance.txt:476`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350SWAT.txt:426`
[^59]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3255`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1165`
[^60]: `游戏原版/media/scripts/generated/items/normal.txt:13136`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance.txt:441`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350SWAT.txt:391`
[^61]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3258`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1168`
[^62]: `游戏原版/media/scripts/generated/items/normal.txt:12378`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance.txt:413`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350SWAT.txt:365`
[^63]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:4152`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1543`
[^64]: `3171167894/mods/damnlib/42.20/media/scripts/USMIL/items_USMIL.txt:72`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_seats.txt:162`
[^65]: `3171167894/mods/damnlib/42.20/media/scripts/USMIL/items_USMIL.txt:87`；`2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_seats.txt:162`
[^66]: `2952802178/mods/90fordF350ambulance/common/media/lua/shared/Translate/EN/Recipes.json:5`
[^67]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance_recipes.txt:47`
[^68]: `2952802178/mods/90fordF350ambulance/common/media/lua/shared/Translate/EN/Recipes.json:7`
[^69]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance_recipes.txt:95`
[^70]: `2952802178/mods/90fordF350ambulance/common/media/lua/shared/Translate/EN/Recipes.json:9`
[^71]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance_recipes.txt:143`
[^72]: `2952802178/mods/90fordF350ambulance/common/media/lua/shared/Translate/EN/Recipes.json:4`
[^73]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance_recipes.txt:25`
[^74]: `2952802178/mods/90fordF350ambulance/common/media/lua/shared/Translate/EN/Recipes.json:15`
[^75]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance_recipes.txt:278`
[^76]: `2952802178/mods/90fordF350ambulance/common/media/lua/shared/Translate/EN/Recipes.json:14`
[^77]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance_recipes.txt:256`
[^78]: `2952802178/mods/90fordF350ambulance/common/media/lua/shared/Translate/EN/Recipes.json:11`
[^79]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance_recipes.txt:188`
[^80]: `2952802178/mods/90fordF350ambulance/common/media/lua/shared/Translate/EN/Recipes.json:10`
[^81]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance_recipes.txt:165`
[^82]: `2952802178/mods/90fordF350ambulance/common/media/lua/shared/Translate/EN/Recipes.json:17`
[^83]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance_recipes.txt:323`
[^84]: `2952802178/mods/90fordF350ambulance/common/media/lua/shared/Translate/EN/Recipes.json:6`
[^85]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance_recipes.txt:68`
[^86]: `2952802178/mods/90fordF350ambulance/common/media/lua/shared/Translate/EN/Recipes.json:8`
[^87]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance_recipes.txt:121`
[^88]: `2952802178/mods/90fordF350ambulance/common/media/lua/shared/Translate/EN/Recipes.json:12`
[^89]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance_recipes.txt:211`
[^90]: `2952802178/mods/90fordF350ambulance/common/media/lua/shared/Translate/EN/Recipes.json:13`
[^91]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance_recipes.txt:234`
[^92]: `2952802178/mods/90fordF350ambulance/common/media/lua/shared/Translate/EN/Recipes.json:16`
[^93]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance_recipes.txt:301`
[^94]: `2952802178/mods/90fordF350ambulance/common/media/lua/shared/Translate/EN/Recipes.json:18`
[^95]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance_recipes.txt:345`
[^96]: `2952802178/mods/90fordF350ambulance/common/media/lua/shared/Translate/EN/Recipes.json:3`
[^97]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance_recipes.txt:3`
[^98]: `3171167894/mods/damnlib/42.20/media/scripts/damnCraft/items_damnCraft.txt:572`
[^99]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance.txt:428`
[^100]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance.txt:476`
[^101]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:5`
[^102]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:18`
[^103]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:31`
[^104]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:44`
[^105]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_bumpers.txt:35`
[^106]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_bumpers.txt:107`
[^107]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_armor.txt:109`
[^108]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_armor.txt:173`
[^109]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_armor.txt:237`
[^110]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_sidesteps.txt:15`
[^111]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_seats.txt:162`
[^112]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_armor.txt:46`
[^113]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_armor.txt:301`
[^114]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_doors.txt:257`
[^115]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_doors.txt:41`
[^116]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_doors.txt:95`
[^117]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_doors.txt:203`
[^118]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_doors.txt:149`
[^119]: `游戏原版/media/scripts/generated/vehicles/template_engine.txt:5`
[^120]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_hood.txt:14`
[^121]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_storage.txt:160`
[^122]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_storage.txt:100`
[^123]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_storage.txt:140`
[^124]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_storage.txt:120`
[^125]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_storage.txt:62`
[^126]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_storage.txt:24`
[^127]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_storage.txt:43`
[^128]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_storage.txt:81`
[^129]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_storage.txt:5`
[^130]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance.txt:413`
[^131]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance.txt:386`
[^132]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:25`
[^133]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:5`
[^134]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:15`
[^135]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:20`
[^136]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:10`
[^137]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance.txt:454`
[^138]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance.txt:441`
[^139]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance.txt:464`
[^140]: `游戏原版/media/scripts/generated/vehicles/template_radio_HAM.txt:5`
[^141]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_seats.txt:94`
[^142]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_seats.txt:38`
[^143]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_seats.txt:56`
[^144]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_seats.txt:145`
[^145]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_seats.txt:74`
[^146]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_seats.txt:84`
[^147]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/90fordF350ambulance.txt:493`
[^148]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:5`
[^149]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:18`
[^150]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:31`
[^151]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:44`
[^152]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_tire.txt:88`
[^153]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_tire.txt:23`
[^154]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_tire.txt:40`
[^155]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_tire.txt:56`
[^156]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_tire.txt:72`
[^157]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_storage.txt:180`
[^158]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_trunkdoors.txt:153`
[^159]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_trunkdoors.txt:30`
[^160]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_trunkdoors.txt:276`
[^161]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_windows.txt:104`
[^162]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_windows.txt:32`
[^163]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_windows.txt:58`
[^164]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_windows.txt:156`
[^165]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_windows.txt:84`
[^166]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_windshield.txt:22`
[^167]: `2952802178/mods/90fordF350ambulance/42.20/media/scripts/vehicles/template_F350_windshield.txt:80`
