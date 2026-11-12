# '92 Nissan Skyline GT-R R32（'92 NISSAN Skyline GT-R (R32)）

1992 Nissan Skyline GT-R R32，速度快、适合公路。

归属：**日常组合（玩法待验收）**；档案视图 `b422-compat`。
当前版本定义：**整车 2、本地物品定义 38、配方 23**；另引用共享物品 16。本地定义数含内部保留项，见独立列表；整车定义包括覆盖原版的条目，不等于新增车型数。

## 如何查找

- **生成整车**：在生成车辆菜单搜索下表完整 ID；显示译名时搜索中文列。联机管理命令用 `/addvehicle 完整ID`。
- **添加到背包**：普通物品、维修件、改装件都在添加物品菜单使用完整物品 ID；不要拿配方或内部槽位去刷车。
- **制作配方**：在制作界面查译名；配方 ID 用于排查，不是可放进背包的物品。
- 中文解释说明用途；只有翻译文件中找到的文字才称为游戏中文名。缺译保留脚本显示名，冲突列出各译文。

## 整车

| 完整生成车辆 ID | 当前中文名 / 名称状态 | 英文名或脚本名 | 变体说明 | 来源 |
| --- | --- | --- | --- | --- |
| `Base.92nissanGTR` | 92款日产天际线R32进口版[^1] | '92 NISSAN Skyline GT-R (R32) Imported[^2] | 脚本座位数 4；机修类型 3；具体外观与性能待游戏实刷 | [^3] |
| `Base.92nissanGTRlhd` | 92款日产天际线R32改装版[^4] | '92 NISSAN Skyline GT-R (R32) Converted[^5] | 脚本座位数 4；机修类型 3；具体外观与性能待游戏实刷 | [^6] |

## 普通物品与书籍

| 完整物品 ID | 游戏显示名 / 名称状态 | 中文用途 / 类别 | 菜单 | 适用车辆与安装位置 | 来源 / 状态 |
| --- | --- | --- | --- | --- | --- |
| `Base.R32Magazine` | 92 Nissan Skyline R32 Auto Manual（未找到有效中文译文） | 阅读资料；脚本声明解锁：制作92款日产天际线R32发动机盖（Base.R32MakeHood）、制作92款日产天际线R32前车门（Base.R32MakeFrontDoor）、制作92款日产天际线R32后备箱盖（Base.R32MakeTrunkLid）、制作92款日产天际线R32前座椅（Base.R32MakeFrontSeat）、制作92款日产天际线R32后座椅（Base.R32MakeRearSeat）、制作92款日产天际线R32前挡风玻璃（Base.R32MakeFrontWindshield）、制作92款日产天际线R32前侧窗（Base.R32MakeFrontSideWindow）、制作92款日产天际线R32后侧窗（Base.R32MakeRearSideWindow）、制作92款日产天际线R32后挡风玻璃（Base.R32MakeRearWindshield）、制作92款日产天际线R32原厂消音器（Base.R32MakeMuffler0）、制作92款日产天际线R32高性能消音器（Base.R32MakeMuffler1）、制作小型现代车顶行李架（Base.R32MakeRoofrack） / 普通物品 / 书籍 | 添加物品 | 未定位整车安装关系 | 92nissanGTR[^7] |

## 维修配件

| 完整物品 ID | 游戏显示名 / 名称状态 | 中文用途 / 类别 | 菜单 | 适用车辆与安装位置 | 来源 / 状态 |
| --- | --- | --- | --- | --- | --- |
| `Base.R32Door3` | 92 Nissan Skyline R32 Door（未找到有效中文译文） | 车辆安装件，用于车门（Door*）；适用车型见右列 / 维修配件 | 添加物品 | Base.92nissanGTR → Door*；Base.92nissanGTRlhd → Door* | 92nissanGTR[^8] |
| `Base.R32EngineDoor0` | 92 Nissan Skyline R32 Hood（未找到有效中文译文） | 车辆安装件，用于引擎盖（EngineDoor）；适用车型见右列 / 维修配件 | 添加物品 | Base.92nissanGTR → EngineDoor；Base.92nissanGTRlhd → EngineDoor | 92nissanGTR[^9] |
| `Base.R32FrontSeat3` | 92 Nissan Skyline R32 Front Seat（未找到有效中文译文） | 车辆安装件，用于座椅（SeatFrontLeft）、座椅（SeatFrontRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.92nissanGTR → SeatFrontLeft；Base.92nissanGTR → SeatFrontRight；Base.92nissanGTRlhd → SeatFrontLeft；Base.92nissanGTRlhd → SeatFrontRight | 92nissanGTR[^10] |
| `Base.R32FrontSideWindow3` | 92 Nissan Skyline R32 Front Side Window（未找到有效中文译文） | 车辆安装件，用于车窗（WindowFrontLeft）、车窗（WindowFrontRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.92nissanGTR → WindowFrontLeft；Base.92nissanGTR → WindowFrontRight；Base.92nissanGTRlhd → WindowFrontLeft；Base.92nissanGTRlhd → WindowFrontRight | 92nissanGTR[^11] |
| `Base.R32RearSeat3` | 92 Nissan Skyline R32 Rear Seat（未找到有效中文译文） | 车辆安装件，用于座椅（SeatRearLeft）、座椅（SeatRearRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.92nissanGTR → SeatRearLeft；Base.92nissanGTR → SeatRearRight；Base.92nissanGTRlhd → SeatRearLeft；Base.92nissanGTRlhd → SeatRearRight | 92nissanGTR[^12] |
| `Base.R32RearSideWindow3` | 92 Nissan Skyline R32 Rear Side Window（未找到有效中文译文） | 车辆安装件，用于车窗（WindowRearLeft）、车窗（WindowRearRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.92nissanGTR → WindowRearLeft；Base.92nissanGTR → WindowRearRight；Base.92nissanGTRlhd → WindowRearLeft；Base.92nissanGTRlhd → WindowRearRight | 92nissanGTR[^13] |
| `Base.R32Sideskirts1` | 92 Nissan Skyline R32 Type1 Sideskirts（未找到有效中文译文） | 车辆安装件，用于车辆安装位（DAMNSideskirts）；适用车型见右列 / 维修配件 | 添加物品 | Base.92nissanGTR → DAMNSideskirts；Base.92nissanGTRlhd → DAMNSideskirts | 92nissanGTR[^14] |
| `Base.R32Sideskirts2` | 92 Nissan Skyline R32 Type2 Sideskirts（未找到有效中文译文） | 车辆安装件，用于车辆安装位（DAMNSideskirts）；适用车型见右列 / 维修配件 | 添加物品 | Base.92nissanGTR → DAMNSideskirts；Base.92nissanGTRlhd → DAMNSideskirts | 92nissanGTR[^15] |
| `Base.R32Sideskirts3` | 92 Nissan Skyline R32 Type3 Sideskirts（未找到有效中文译文） | 车辆安装件，用于车辆安装位（DAMNSideskirts）；适用车型见右列 / 维修配件 | 添加物品 | Base.92nissanGTR → DAMNSideskirts；Base.92nissanGTRlhd → DAMNSideskirts | 92nissanGTR[^16] |
| `Base.R32SideskirtsA` | 92 Nissan Skyline R32 Armored Sideskirts（未找到有效中文译文） | 车辆安装件，用于车辆安装位（DAMNSideskirts）；适用车型见右列 / 维修配件 | 添加物品 | Base.92nissanGTR → DAMNSideskirts；Base.92nissanGTRlhd → DAMNSideskirts | 92nissanGTR[^17] |
| `Base.R32Tire0` | 92 Nissan Skyline R32 Stock Tire（未找到有效中文译文） | 车辆安装件，用于轮胎（DAMNSpareTire）、轮胎（Tire*）；适用车型见右列 / 维修配件 | 添加物品 | Base.92nissanGTR → DAMNSpareTire；Base.92nissanGTR → Tire*；Base.92nissanGTRlhd → DAMNSpareTire；Base.92nissanGTRlhd → Tire* | 92nissanGTR[^18] |
| `Base.R32Tire1` | 92 Nissan Skyline R32 Performance Tire（未找到有效中文译文） | 车辆安装件，用于轮胎（DAMNSpareTire）、轮胎（Tire*）；适用车型见右列 / 维修配件 | 添加物品 | Base.92nissanGTR → DAMNSpareTire；Base.92nissanGTR → Tire*；Base.92nissanGTRlhd → DAMNSpareTire；Base.92nissanGTRlhd → Tire* | 92nissanGTR[^19] |
| `Base.R32Tire2` | 92 Nissan Skyline R32 Slick Tire（未找到有效中文译文） | 车辆安装件，用于轮胎（DAMNSpareTire）、轮胎（Tire*）；适用车型见右列 / 维修配件 | 添加物品 | Base.92nissanGTR → DAMNSpareTire；Base.92nissanGTR → Tire*；Base.92nissanGTRlhd → DAMNSpareTire；Base.92nissanGTRlhd → Tire* | 92nissanGTR[^20] |
| `Base.R32TireA` | 92 Nissan Skyline R32 Armored Tire（未找到有效中文译文） | 车辆安装件，用于轮胎（DAMNSpareTire）、轮胎（Tire*）；适用车型见右列 / 维修配件 | 添加物品 | Base.92nissanGTR → DAMNSpareTire；Base.92nissanGTR → Tire*；Base.92nissanGTRlhd → DAMNSpareTire；Base.92nissanGTRlhd → Tire* | 92nissanGTR[^21] |
| `Base.R32TrunkDoor3` | 92 Nissan Skyline R32 Trunk Lid（未找到有效中文译文） | 车辆安装件，用于后备箱（TrunkDoor）；适用车型见右列 / 维修配件 | 添加物品 | Base.92nissanGTR → TrunkDoor；Base.92nissanGTRlhd → TrunkDoor | 92nissanGTR[^22] |
| `Base.R32Windshield3` | 92 Nissan Skyline R32 Windshield（未找到有效中文译文） | 车辆安装件，用于挡风玻璃（Windshield）；适用车型见右列 / 维修配件 | 添加物品 | Base.92nissanGTR → Windshield；Base.92nissanGTRlhd → Windshield | 92nissanGTR[^23] |
| `Base.R32WindshieldRear3` | 92 Nissan Skyline R32 Rear Windshield（未找到有效中文译文） | 车辆安装件，用于挡风玻璃（WindshieldRear）；适用车型见右列 / 维修配件 | 添加物品 | Base.92nissanGTR → WindshieldRear；Base.92nissanGTRlhd → WindshieldRear | 92nissanGTR[^24] |
| `Base.R32muffler0` | 92 Nissan Skyline R32 Stock Muffler（未找到有效中文译文） | 车辆安装件，用于消声器（R32Muffler）；适用车型见右列 / 维修配件 | 添加物品 | Base.92nissanGTR → R32Muffler；Base.92nissanGTRlhd → R32Muffler | 92nissanGTR[^25] |
| `Base.R32muffler1` | 92 Nissan Skyline R32 Performance Muffler（未找到有效中文译文） | 车辆安装件，用于消声器（R32Muffler）；适用车型见右列 / 维修配件 | 添加物品 | Base.92nissanGTR → R32Muffler；Base.92nissanGTRlhd → R32Muffler | 92nissanGTR[^26] |

## 改装配件

| 完整物品 ID | 游戏显示名 / 名称状态 | 中文用途 / 类别 | 菜单 | 适用车辆与安装位置 | 来源 / 状态 |
| --- | --- | --- | --- | --- | --- |
| `Base.R32Bumper0` | 92 Nissan Skyline R32 Stock Front Bumper（未找到有效中文译文） | 车辆安装件，用于保险杠（DAMNBumperFront）；适用车型见右列 / 改装配件 | 添加物品 | Base.92nissanGTR → DAMNBumperFront；Base.92nissanGTRlhd → DAMNBumperFront | 92nissanGTR[^27] |
| `Base.R32Bumper1` | 92 Nissan Skyline R32 Type1 Front Bumper（未找到有效中文译文） | 车辆安装件，用于保险杠（DAMNBumperFront）；适用车型见右列 / 改装配件 | 添加物品 | Base.92nissanGTR → DAMNBumperFront；Base.92nissanGTRlhd → DAMNBumperFront | 92nissanGTR[^28] |
| `Base.R32Bumper2` | 92 Nissan Skyline R32 Type2 Front Bumper（未找到有效中文译文） | 车辆安装件，用于保险杠（DAMNBumperFront）；适用车型见右列 / 改装配件 | 添加物品 | Base.92nissanGTR → DAMNBumperFront；Base.92nissanGTRlhd → DAMNBumperFront | 92nissanGTR[^29] |
| `Base.R32Bumper3` | 92 Nissan Skyline R32 Type3 Front Bumper（未找到有效中文译文） | 车辆安装件，用于保险杠（DAMNBumperFront）；适用车型见右列 / 改装配件 | 添加物品 | Base.92nissanGTR → DAMNBumperFront；Base.92nissanGTRlhd → DAMNBumperFront | 92nissanGTR[^30] |
| `Base.R32BumperA` | 92 Nissan Skyline R32 Makeshift Front Bullbar（未找到有效中文译文） | 车辆安装件，用于保险杠（DAMNBumperFront）；适用车型见右列 / 改装配件 | 添加物品 | Base.92nissanGTR → DAMNBumperFront；Base.92nissanGTRlhd → DAMNBumperFront | 92nissanGTR[^31] |
| `Base.R32BumperRear0` | 92 Nissan Skyline R32 Stock Rear Bumper（未找到有效中文译文） | 车辆安装件，用于保险杠（DAMNBumperRear）；适用车型见右列 / 改装配件 | 添加物品 | Base.92nissanGTR → DAMNBumperRear；Base.92nissanGTRlhd → DAMNBumperRear | 92nissanGTR[^32] |
| `Base.R32BumperRear1` | 92 Nissan Skyline R32 Type1 Rear Bumper（未找到有效中文译文） | 车辆安装件，用于保险杠（DAMNBumperRear）；适用车型见右列 / 改装配件 | 添加物品 | Base.92nissanGTR → DAMNBumperRear；Base.92nissanGTRlhd → DAMNBumperRear | 92nissanGTR[^33] |
| `Base.R32BumperRear2` | 92 Nissan Skyline R32 Type2 Rear Bumper（未找到有效中文译文） | 车辆安装件，用于保险杠（DAMNBumperRear）；适用车型见右列 / 改装配件 | 添加物品 | Base.92nissanGTR → DAMNBumperRear；Base.92nissanGTRlhd → DAMNBumperRear | 92nissanGTR[^34] |
| `Base.R32BumperRear3` | 92 Nissan Skyline R32 Type3 Rear Bumper（未找到有效中文译文） | 车辆安装件，用于保险杠（DAMNBumperRear）；适用车型见右列 / 改装配件 | 添加物品 | Base.92nissanGTR → DAMNBumperRear；Base.92nissanGTRlhd → DAMNBumperRear | 92nissanGTR[^35] |
| `Base.R32BumperRearA` | 92 Nissan Skyline R32 Makeshift Rear Bullbar（未找到有效中文译文） | 车辆安装件，用于保险杠（DAMNBumperRear）；适用车型见右列 / 改装配件 | 添加物品 | Base.92nissanGTR → DAMNBumperRear；Base.92nissanGTRlhd → DAMNBumperRear | 92nissanGTR[^36] |
| `Base.R32DoorArmor` | 92 Nissan Skyline R32 Makeshift Door Armor（未找到有效中文译文） | 车辆安装件，用于防护件（DAMNFrontLeftArmor）、防护件（DAMNFrontRightArmor）；适用车型见右列 / 改装配件 | 添加物品 | Base.92nissanGTR → DAMNFrontLeftArmor；Base.92nissanGTR → DAMNFrontRightArmor；Base.92nissanGTRlhd → DAMNFrontLeftArmor；Base.92nissanGTRlhd → DAMNFrontRightArmor | 92nissanGTR[^37] |
| `Base.R32RearWindowArmor` | 92 Nissan Skyline R32 Makeshift Rear Window Armor（未找到有效中文译文） | 车辆安装件，用于防护件（DAMNRearLeftArmor）、防护件（DAMNRearRightArmor）；适用车型见右列 / 改装配件 | 添加物品 | Base.92nissanGTR → DAMNRearLeftArmor；Base.92nissanGTR → DAMNRearRightArmor；Base.92nissanGTRlhd → DAMNRearLeftArmor；Base.92nissanGTRlhd → DAMNRearRightArmor | 92nissanGTR[^38] |
| `Base.R32Spoiler0` | 92 Nissan Skyline R32 Stock Spoiler（未找到有效中文译文） | 车辆安装件，用于扰流板（DAMNSpoiler）；适用车型见右列 / 改装配件 | 添加物品 | Base.92nissanGTR → DAMNSpoiler；Base.92nissanGTRlhd → DAMNSpoiler | 92nissanGTR[^39] |
| `Base.R32Spoiler1` | 92 Nissan Skyline R32 Type1 Spoiler（未找到有效中文译文） | 车辆安装件，用于扰流板（DAMNSpoiler）；适用车型见右列 / 改装配件 | 添加物品 | Base.92nissanGTR → DAMNSpoiler；Base.92nissanGTRlhd → DAMNSpoiler | 92nissanGTR[^40] |
| `Base.R32Spoiler2` | 92 Nissan Skyline R32 Type2 Spoiler（未找到有效中文译文） | 车辆安装件，用于扰流板（DAMNSpoiler）；适用车型见右列 / 改装配件 | 添加物品 | Base.92nissanGTR → DAMNSpoiler；Base.92nissanGTRlhd → DAMNSpoiler | 92nissanGTR[^41] |
| `Base.R32Spoiler3` | 92 Nissan Skyline R32 Type3 Spoiler（未找到有效中文译文） | 车辆安装件，用于扰流板（DAMNSpoiler）；适用车型见右列 / 改装配件 | 添加物品 | Base.92nissanGTR → DAMNSpoiler；Base.92nissanGTRlhd → DAMNSpoiler | 92nissanGTR[^42] |
| `Base.R32WindshieldArmor` | 92 Nissan Skyline R32 Makeshift Windshield Armor（未找到有效中文译文） | 车辆安装件，用于挡风玻璃（DAMNWindshieldArmor）；适用车型见右列 / 改装配件 | 添加物品 | Base.92nissanGTR → DAMNWindshieldArmor；Base.92nissanGTRlhd → DAMNWindshieldArmor | 92nissanGTR[^43] |
| `Base.R32WindshieldRearArmor` | 92 Nissan Skyline R32 Makeshift Rear Windshield Armor（未找到有效中文译文） | 车辆安装件，用于挡风玻璃（DAMNWindshieldRearArmor）；适用车型见右列 / 改装配件 | 添加物品 | Base.92nissanGTR → DAMNWindshieldRearArmor；Base.92nissanGTRlhd → DAMNWindshieldRearArmor | 92nissanGTR[^44] |

## 共享配件

下列物品由已启用依赖或游戏原版提供，不计入本 Mod 的本地物品数。

| 完整物品 ID | 游戏显示名 / 名称状态 | 中文用途 / 类别 | 菜单 | 适用车辆与安装位置 | 来源 / 状态 |
| --- | --- | --- | --- | --- | --- |
| `Base.BigGasTank3` | 油箱 (大型)（翻译文件含非标准语法，待游戏核实）[^46] | 车辆安装件，用于油箱（GasTank）；适用车型见右列 / 维修配件 | 添加物品 | Base.92nissanGTR → GasTank；Base.92nissanGTRlhd → GasTank | 游戏原版[^45] |
| `Base.CarBattery3` | 汽车电池（翻译文件含非标准语法，待游戏核实）[^48] | 车辆安装件，用于蓄电池（Battery）；适用车型见右列 / 维修配件 | 添加物品 | Base.92nissanGTR → Battery；Base.92nissanGTRlhd → Battery | 游戏原版[^47] |
| `Base.GloveBox3` | 手套箱（翻译文件含非标准语法，待游戏核实）[^50] | 车辆安装件，用于车辆安装位（GloveBox）；适用车型见右列 / 维修配件 | 添加物品 | Base.92nissanGTR → GloveBox；Base.92nissanGTRlhd → GloveBox | 游戏原版[^49] |
| `Base.LightBulb` | 灯泡-白色 / 灯泡 (白)（译文冲突，待游戏核实）[^52] | 车辆安装件，用于车灯（Headlight*）、车灯（JP82DorothyLights）；适用车型见右列 / 维修配件 | 添加物品 | Base.92nissanGTR → Headlight*；Base.92nissanGTRlhd → Headlight* | 游戏原版[^51] |
| `Base.ModernBrake3` | 制动器 (高级)（翻译文件含非标准语法，待游戏核实）[^54] | 车辆安装件，用于制动器（Brake*）；适用车型见右列 / 维修配件 | 添加物品 | Base.92nissanGTR → Brake*；Base.92nissanGTRlhd → Brake* | 游戏原版[^53] |
| `Base.ModernSmallRoofrack3` | Small Modern Roofrack（未找到有效中文译文） | 车辆安装件，用于车顶行李架（R32Roofrack）；适用车型见右列 / 改装配件 | 添加物品 | Base.92nissanGTR → R32Roofrack；Base.92nissanGTRlhd → R32Roofrack | damnlib[^55] |
| `Base.ModernSuspension3` | 悬挂 (高级)（翻译文件含非标准语法，待游戏核实）[^57] | 车辆安装件，用于悬挂（Suspension*）；适用车型见右列 / 维修配件 | 添加物品 | Base.92nissanGTR → Suspension*；Base.92nissanGTRlhd → Suspension* | 游戏原版[^56] |
| `Base.NormalBrake3` | 制动器 (普通)（翻译文件含非标准语法，待游戏核实）[^59] | 车辆安装件，用于制动器（Brake*）；适用车型见右列 / 维修配件 | 添加物品 | Base.92nissanGTR → Brake*；Base.92nissanGTRlhd → Brake* | 游戏原版[^58] |
| `Base.NormalGasTank3` | 油箱 (标准)（翻译文件含非标准语法，待游戏核实）[^61] | 车辆安装件，用于油箱（GasTank）；适用车型见右列 / 维修配件 | 添加物品 | Base.92nissanGTR → GasTank；Base.92nissanGTRlhd → GasTank | 游戏原版[^60] |
| `Base.NormalSuspension3` | 悬挂 (普通)（翻译文件含非标准语法，待游戏核实）[^63] | 车辆安装件，用于悬挂（Suspension*）；适用车型见右列 / 维修配件 | 添加物品 | Base.92nissanGTR → Suspension*；Base.92nissanGTRlhd → Suspension* | 游戏原版[^62] |
| `Base.OldBrake3` | 制动器 (老式)（翻译文件含非标准语法，待游戏核实）[^65] | 车辆安装件，用于制动器（Brake*）；适用车型见右列 / 维修配件 | 添加物品 | Base.92nissanGTR → Brake*；Base.92nissanGTRlhd → Brake* | 游戏原版[^64] |
| `Base.RadioBlack` | 收音机 (超值科技) / 收音机 (廉科) / 廉科牌收音机（译文冲突，待游戏核实）[^67] | 车辆安装件，用于车辆安装位（Radio）；适用车型见右列 / 维修配件 | 添加物品 | Base.92nissanGTR → Radio；Base.92nissanGTRlhd → Radio | 游戏原版[^66] |
| `Base.RadioMakeShift` | 收音机 (简易) / 自制收音机（译文冲突，待游戏核实）[^69] | 车辆安装件，用于车辆安装位（Radio）；适用车型见右列 / 维修配件 | 添加物品 | Base.92nissanGTR → Radio；Base.92nissanGTRlhd → Radio | 游戏原版[^68] |
| `Base.RadioRed` | 导航仪 / 收音机 (昂科) / 昂科牌收音机（译文冲突，待游戏核实）[^71] | 车辆安装件，用于车辆安装位（Radio）；适用车型见右列 / 维修配件 | 添加物品 | Base.92nissanGTR → Radio；Base.92nissanGTRlhd → Radio | 游戏原版[^70] |
| `Base.SmallGasTank3` | 油箱 (小型)（翻译文件含非标准语法，待游戏核实）[^73] | 车辆安装件，用于油箱（GasTank）；适用车型见右列 / 维修配件 | 添加物品 | Base.92nissanGTR → GasTank；Base.92nissanGTRlhd → GasTank | 游戏原版[^72] |

## 制作配方

| 配方完整 ID（排查用） | 游戏配方名 / 名称状态 | 中文用途 | 菜单 | 来源 |
| --- | --- | --- | --- | --- |
| `Base.R32MakeArmoredSideskirts` | 制作92款日产天际线R32装甲侧裙[^74] | 制作产出：92 Nissan Skyline R32 Armored Sideskirts（车辆安装件，用于车辆安装位（DAMNSideskirts）；适用车型见右列） | 制作界面 | [^75] |
| `Base.R32MakeFrontBullbar` | 制作92款日产天际线R32前防撞杠[^76] | 制作产出：92 Nissan Skyline R32 Makeshift Front Bullbar（车辆安装件，用于保险杠（DAMNBumperFront）；适用车型见右列） | 制作界面 | [^77] |
| `Base.R32MakeFrontDoor` | 制作92款日产天际线R32前车门[^78] | 制作产出：92 Nissan Skyline R32 Door（车辆安装件，用于车门（Door*）；适用车型见右列） | 制作界面 | [^79] |
| `Base.R32MakeFrontSeat` | 制作92款日产天际线R32前座椅[^80] | 制作产出：92 Nissan Skyline R32 Front Seat（车辆安装件，用于座椅（SeatFrontLeft）、座椅（SeatFrontRight）；适用车型见右列） | 制作界面 | [^81] |
| `Base.R32MakeFrontSideWindow` | 制作92款日产天际线R32前侧窗[^82] | 制作产出：92 Nissan Skyline R32 Front Side Window（车辆安装件，用于车窗（WindowFrontLeft）、车窗（WindowFrontRight）；适用车型见右列） | 制作界面 | [^83] |
| `Base.R32MakeFrontWindowArmor` | 制作92款日产天际线R32前窗装甲[^84] | 制作产出：92 Nissan Skyline R32 Makeshift Door Armor（车辆安装件，用于防护件（DAMNFrontLeftArmor）、防护件（DAMNFrontRightArmor）；适用车型见右列） | 制作界面 | [^85] |
| `Base.R32MakeFrontWindshield` | 制作92款日产天际线R32前挡风玻璃[^86] | 制作产出：92 Nissan Skyline R32 Windshield（车辆安装件，用于挡风玻璃（Windshield）；适用车型见右列） | 制作界面 | [^87] |
| `Base.R32MakeFrontWindshieldArmor` | 制作92款日产天际线R32前挡风玻璃装甲[^88] | 制作产出：92 Nissan Skyline R32 Makeshift Windshield Armor（车辆安装件，用于挡风玻璃（DAMNWindshieldArmor）；适用车型见右列） | 制作界面 | [^89] |
| `Base.R32MakeHood` | 制作92款日产天际线R32发动机盖[^90] | 制作产出：92 Nissan Skyline R32 Hood（车辆安装件，用于引擎盖（EngineDoor）；适用车型见右列） | 制作界面 | [^91] |
| `Base.R32MakeMuffler0` | 制作92款日产天际线R32原厂消音器[^92] | 制作产出：92 Nissan Skyline R32 Stock Muffler（车辆安装件，用于消声器（R32Muffler）；适用车型见右列） | 制作界面 | [^93] |
| `Base.R32MakeMuffler1` | 制作92款日产天际线R32高性能消音器[^94] | 制作产出：92 Nissan Skyline R32 Performance Muffler（车辆安装件，用于消声器（R32Muffler）；适用车型见右列） | 制作界面 | [^95] |
| `Base.R32MakeRearBullbar` | 制作92款日产天际线R32后防撞杠[^96] | 制作产出：92 Nissan Skyline R32 Makeshift Rear Bullbar（车辆安装件，用于保险杠（DAMNBumperRear）；适用车型见右列） | 制作界面 | [^97] |
| `Base.R32MakeRearSeat` | 制作92款日产天际线R32后座椅[^98] | 制作产出：92 Nissan Skyline R32 Rear Seat（车辆安装件，用于座椅（SeatRearLeft）、座椅（SeatRearRight）；适用车型见右列） | 制作界面 | [^99] |
| `Base.R32MakeRearSideWindow` | 制作92款日产天际线R32后侧窗[^100] | 制作产出：92 Nissan Skyline R32 Rear Side Window（车辆安装件，用于车窗（WindowRearLeft）、车窗（WindowRearRight）；适用车型见右列） | 制作界面 | [^101] |
| `Base.R32MakeRearWindowArmor` | 制作92款日产天际线R32后窗装甲[^102] | 制作产出：92 Nissan Skyline R32 Makeshift Rear Window Armor（车辆安装件，用于防护件（DAMNRearLeftArmor）、防护件（DAMNRearRightArmor）；适用车型见右列） | 制作界面 | [^103] |
| `Base.R32MakeRearWindshield` | 制作92款日产天际线R32后挡风玻璃[^104] | 制作产出：92 Nissan Skyline R32 Rear Windshield（车辆安装件，用于挡风玻璃（WindshieldRear）；适用车型见右列） | 制作界面 | [^105] |
| `Base.R32MakeRearWindshieldArmor` | 制作92款日产天际线R32后挡风玻璃装甲[^106] | 制作产出：92 Nissan Skyline R32 Makeshift Rear Windshield Armor（车辆安装件，用于挡风玻璃（DAMNWindshieldRearArmor）；适用车型见右列） | 制作界面 | [^107] |
| `Base.R32MakeRoofrack` | 制作小型现代车顶行李架[^108] | 制作产出：Small Modern Roofrack（车辆安装件，用于车顶行李架（R32Roofrack）；适用车型见右列） | 制作界面 | [^109] |
| `Base.R32MakeTire0` | R32MakeTire0（未找到有效中文译文） | 制作产出：92 Nissan Skyline R32 Stock Tire（车辆安装件，用于轮胎（DAMNSpareTire）、轮胎（Tire*）；适用车型见右列） | 制作界面 | [^110] |
| `Base.R32MakeTire1` | R32MakeTire1（未找到有效中文译文） | 制作产出：92 Nissan Skyline R32 Performance Tire（车辆安装件，用于轮胎（DAMNSpareTire）、轮胎（Tire*）；适用车型见右列） | 制作界面 | [^111] |
| `Base.R32MakeTire2` | R32MakeTire2（未找到有效中文译文） | 制作产出：92 Nissan Skyline R32 Slick Tire（车辆安装件，用于轮胎（DAMNSpareTire）、轮胎（Tire*）；适用车型见右列） | 制作界面 | [^112] |
| `Base.R32MakeTireA` | R32MakeTireA（未找到有效中文译文） | 制作产出：92 Nissan Skyline R32 Armored Tire（车辆安装件，用于轮胎（DAMNSpareTire）、轮胎（Tire*）；适用车型见右列） | 制作界面 | [^113] |
| `Base.R32MakeTrunkLid` | 制作92款日产天际线R32后备箱盖[^114] | 制作产出：92 Nissan Skyline R32 Trunk Lid（车辆安装件，用于后备箱（TrunkDoor）；适用车型见右列） | 制作界面 | [^115] |

## 内部定义、历史分支与未解析引用

有效资源层：42.20, common；仅合并 common 与所选版本，Overlay 按相对路径覆盖。
车辆模板 17 个、内部槽位 59 个，均不算整车或背包物品。旧根目录和未选中版本的定义不列入当前可用表。模板中短物品引用若追加机修类型后缀才匹配定义，属于静态映射，安装仍待实测。

内部或过时的 item 定义单列于此，不在上面的背包刷取建议中；它们仍计入各自来源的定义数量。

| 保留定义 ID（不作正常刷取建议） | 脚本显示名 | 中文说明 / 状态 | 来源 |
| --- | --- | --- | --- |
| `damnCraft.Trunk3` | no | 车辆后备箱的内部容量载体，当前挑战者等模板仍引用；不是背包或独立行李箱；显示名 no、图标 na；不作正常刷取建议 | [^116] |

<details><summary>查看内部槽位（不能直接刷取）</summary>

| 槽位 | 名称或说明 | 来源 |
| --- | --- | --- |
| `Battery` | 电池 / 蓄电池 | [^117] |
| `Brake*` | Brake* / 制动器 | [^118] |
| `BrakeFrontLeft` | 左前制动 / 制动器 | [^119] |
| `BrakeFrontRight` | 右前制动 / 制动器 | [^120] |
| `BrakeRearLeft` | 左后制动 / 制动器 | [^121] |
| `BrakeRearRight` | 右后制动 / 制动器 | [^122] |
| `DAMNBumperFront` | 前保险杠 / 保险杠 | [^123] |
| `DAMNBumperRear` | 后保险杠 / 保险杠 | [^124] |
| `DAMNFrontLeftArmor` | 左前车窗装甲 / 防护件 | [^125] |
| `DAMNFrontRightArmor` | 右前车窗装甲 / 防护件 | [^126] |
| `DAMNRearLeftArmor` | 左后车窗装甲 / 防护件 | [^127] |
| `DAMNRearRightArmor` | 右后车窗装甲 / 防护件 | [^128] |
| `DAMNSideskirts` | 侧裙 / 车辆安装位 | [^129] |
| `DAMNSpareTire` | 备胎 / 轮胎 | [^130] |
| `DAMNSpoiler` | 尾翼 / 扰流板 | [^131] |
| `DAMNWindshieldArmor` | 挡风玻璃装甲 / 挡风玻璃 | [^132] |
| `DAMNWindshieldRearArmor` | 后挡风玻璃装甲 / 挡风玻璃 | [^133] |
| `Door*` | Door* / 车门 | [^134] |
| `DoorFrontLeft` | 左前门 / 车门 | [^135] |
| `DoorFrontRight` | 右前门 / 车门 | [^136] |
| `Engine` | 引擎 / 发动机 | [^137] |
| `EngineDoor` | 引擎盖 / 引擎盖 | [^138] |
| `GasTank` | 油箱 / 油箱 | [^139] |
| `GloveBox` | 手套箱 / 车辆安装位 | [^140] |
| `Headlight*` | Headlight* / 车灯 | [^141] |
| `HeadlightLeft` | 左大灯 / 车灯 | [^142] |
| `HeadlightRearLeft` | 左尾灯 / 车灯 | [^143] |
| `HeadlightRearRight` | 右尾灯 / 车灯 | [^144] |
| `HeadlightRight` | 右大灯 / 车灯 | [^145] |
| `Heater` | 加热器 / 车辆安装位 | [^146] |
| `PassengerCompartment` | 乘员舱 / 车辆安装位 | [^147] |
| `R32Muffler` | 消音器 / 消声器 | [^148] |
| `R32Roofrack` | 车顶行李架 / 车顶行李架 | [^149] |
| `R32Trunk` | 后备箱 / 后备箱 | [^150] |
| `Radio` | 电台 / 车辆安装位 | [^151] |
| `Seat*` | Seat* / 座椅 | [^152] |
| `SeatFrontLeft` | 驾驶座 / 座椅 | [^153] |
| `SeatFrontRight` | 右前座 / 座椅 | [^154] |
| `SeatRearLeft` | 左后座 / 座椅 | [^155] |
| `SeatRearRight` | 右后座 / 座椅 | [^156] |
| `Suspension*` | Suspension* / 悬挂 | [^157] |
| `SuspensionFrontLeft` | 左前悬挂 / 悬挂 | [^158] |
| `SuspensionFrontRight` | 右前悬挂 / 悬挂 | [^159] |
| `SuspensionRearLeft` | 左后悬挂 / 悬挂 | [^160] |
| `SuspensionRearRight` | 右后悬挂 / 悬挂 | [^161] |
| `Tire*` | Tire* / 轮胎 | [^162] |
| `TireFrontLeft` | 左前胎 / 轮胎 | [^163] |
| `TireFrontRight` | 右前胎 / 轮胎 | [^164] |
| `TireRearLeft` | 左后胎 / 轮胎 | [^165] |
| `TireRearRight` | 右后胎 / 轮胎 | [^166] |
| `TruckBed` | 补给箱 / 行李箱 / 车辆安装位 | [^167] |
| `TrunkDoor` | 后车盖 / 后备箱 | [^168] |
| `Window*` | Window* / 车窗 | [^169] |
| `WindowFrontLeft` | 左前窗 / 车窗 | [^170] |
| `WindowFrontRight` | 右前窗 / 车窗 | [^171] |
| `WindowRearLeft` | 左后窗 / 车窗 | [^172] |
| `WindowRearRight` | 右后窗 / 车窗 | [^173] |
| `Windshield` | 挡风玻璃 / 挡风玻璃 | [^174] |
| `WindshieldRear` | 后挡风玻璃 / 挡风玻璃 | [^175] |

</details>

- 静态语法警告：42.20/media/scripts/vehicles/template_R32_doors.txt:208：原件多余的顶层闭合括号，静态提取时跳过

## 概览

| Mod ID / 文件夹 | 分发端 | 版本 | 选择的 mod.info | 原件范围 → 当前范围 |
| --- | --- | --- | --- | --- |
| `92nissanGTR` / `92nissanGTR` | both（双端） | 未标注 | `42.20/mod.info` | 42.20.0 … - → 42.20.0 … - |

原件体积 18.1 MB；体积按完整目录统计，与当前内容定义数分开。
工作坊：[查看作者页面](https://steamcommunity.com/sharedfiles/filedetails/?id=2846036306)。

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

require damnlib；47 个脚本物品、2 个载具脚本、27 条配方。

```
cd A004
python lab.py check --profile b422-compat
grep -a '92nissanGTR' runs/<trial>/*console.log
```
<!-- retained:end -->

## 静态来源

路径相对 `A004/workspace/mods_library/`；`Overlay/<文件夹>/` 指 `A004/workspace/patches/mods/<文件夹>/`，`游戏原版/` 指当前 B42.22 客户端 Game 目录。翻译来源列出所有候选，未按加载顺序擅自消解异文。

[^1]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/IG_UI.json:15046`
[^2]: `2846036306/mods/92nissanGTR/common/media/lua/shared/Translate/EN/IG_UI.json:3`
[^3]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR.txt:38`
[^4]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/IG_UI.json:15047`
[^5]: `2846036306/mods/92nissanGTR/common/media/lua/shared/Translate/EN/IG_UI.json:4`
[^6]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTRlhd.txt:11`
[^7]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_vehiclesitems.txt:5`
[^8]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_vehiclesitems.txt:105`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_doors.txt:131`
[^9]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_vehiclesitems.txt:410`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_hood.txt:14`
[^10]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_vehiclesitems.txt:444`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_seats.txt:37`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_seats.txt:56`
[^11]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_vehiclesitems.txt:546`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_windows.txt:38`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_windows.txt:64`
[^12]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_vehiclesitems.txt:460`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_seats.txt:75`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_seats.txt:94`
[^13]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_vehiclesitems.txt:561`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_windows.txt:90`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_windows.txt:105`
[^14]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_vehiclesitems.txt:286`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_sideskirts.txt:34`
[^15]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_vehiclesitems.txt:301`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_sideskirts.txt:34`
[^16]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_vehiclesitems.txt:316`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_sideskirts.txt:34`
[^17]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_vehiclesitems.txt:331`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_sideskirts.txt:34`
[^18]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_vehiclesitems.txt:23`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_spareTire.txt:6`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_tires.txt:128`
[^19]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_vehiclesitems.txt:43`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_spareTire.txt:6`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_tires.txt:128`
[^20]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_vehiclesitems.txt:63`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_spareTire.txt:6`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_tires.txt:128`
[^21]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_vehiclesitems.txt:83`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_spareTire.txt:6`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_tires.txt:128`
[^22]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_vehiclesitems.txt:427`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_trunkdoor.txt:14`
[^23]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_vehiclesitems.txt:516`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_windshield.txt:37`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_windshield.txt:159`
[^24]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_vehiclesitems.txt:531`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_windshield.txt:95`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_windshield.txt:167`
[^25]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_vehiclesitems.txt:478`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_mufflers.txt:22`
[^26]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_vehiclesitems.txt:496`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_mufflers.txt:22`
[^27]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_vehiclesitems.txt:122`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_bumpers_front.txt:41`
[^28]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_vehiclesitems.txt:138`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_bumpers_front.txt:41`
[^29]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_vehiclesitems.txt:154`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_bumpers_front.txt:41`
[^30]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_vehiclesitems.txt:170`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_bumpers_front.txt:41`
[^31]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_vehiclesitems.txt:186`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_bumpers_front.txt:41`
[^32]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_vehiclesitems.txt:204`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_bumpers_rear.txt:41`
[^33]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_vehiclesitems.txt:220`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_bumpers_rear.txt:41`
[^34]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_vehiclesitems.txt:236`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_bumpers_rear.txt:41`
[^35]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_vehiclesitems.txt:252`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_bumpers_rear.txt:41`
[^36]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_vehiclesitems.txt:268`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_bumpers_rear.txt:41`
[^37]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_vehiclesitems.txt:578`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_armor.txt:114`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_armor.txt:176`
[^38]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_vehiclesitems.txt:594`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_armor.txt:238`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_armor.txt:299`
[^39]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_vehiclesitems.txt:348`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_spoiler.txt:42`
[^40]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_vehiclesitems.txt:363`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_spoiler.txt:42`
[^41]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_vehiclesitems.txt:378`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_spoiler.txt:42`
[^42]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_vehiclesitems.txt:393`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_spoiler.txt:42`
[^43]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_vehiclesitems.txt:610`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_armor.txt:51`
[^44]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_vehiclesitems.txt:626`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_armor.txt:360`
[^45]: `游戏原版/media/scripts/generated/items/normal.txt:12453`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR.txt:375`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTRlhd.txt:348`
[^46]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:449`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:164`
[^47]: `游戏原版/media/scripts/generated/items/drainable.txt:2387`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR.txt:392`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTRlhd.txt:365`
[^48]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:971`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:381`
[^49]: `游戏原版/media/scripts/generated/items/normal.txt:13037`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR.txt:341`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTRlhd.txt:314`
[^50]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1777`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:688`
[^51]: `游戏原版/media/scripts/generated/items/normal.txt:4661`；`游戏原版/media/scripts/generated/vehicles/template_headlight.txt:25`
[^52]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:6727`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25103`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2563`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:965`
[^53]: `游戏原版/media/scripts/generated/items/normal.txt:12214`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR.txt:429`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTRlhd.txt:402`
[^54]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2781`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1051`
[^55]: `3171167894/mods/damnlib/42.20/media/scripts/commonItems/damnCommonRoofracks_vehiclesitems.txt:27`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_roofrack.txt:14`
[^56]: `游戏原版/media/scripts/generated/items/normal.txt:12316`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR.txt:446`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTRlhd.txt:419`
[^57]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2787`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1057`
[^58]: `游戏原版/media/scripts/generated/items/normal.txt:12197`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR.txt:429`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTRlhd.txt:402`
[^59]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3220`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1136`
[^60]: `游戏原版/media/scripts/generated/items/normal.txt:12438`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR.txt:375`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTRlhd.txt:348`
[^61]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3229`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1145`
[^62]: `游戏原版/media/scripts/generated/items/normal.txt:12299`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR.txt:446`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTRlhd.txt:419`
[^63]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3232`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1148`
[^64]: `游戏原版/media/scripts/generated/items/normal.txt:12180`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR.txt:429`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTRlhd.txt:402`
[^65]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3256`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1166`
[^66]: `游戏原版/media/scripts/generated/items/radio.txt:308`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR.txt:463`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTRlhd.txt:436`
[^67]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:7374`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25092`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3645`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:5128`
[^68]: `游戏原版/media/scripts/generated/items/radio.txt:335`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR.txt:463`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTRlhd.txt:436`
[^69]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:7375`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25093`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3649`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:5132`
[^70]: `游戏原版/media/scripts/generated/items/radio.txt:361`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR.txt:463`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTRlhd.txt:436`
[^71]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:3001`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25091`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3651`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:5134`
[^72]: `游戏原版/media/scripts/generated/items/normal.txt:12423`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR.txt:375`；`2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTRlhd.txt:348`
[^73]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:4153`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1544`
[^74]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6236`
[^75]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_recipes.txt:491`
[^76]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6234`
[^77]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_recipes.txt:443`
[^78]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6220`
[^79]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_recipes.txt:115`
[^80]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6222`
[^81]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_recipes.txt:166`
[^82]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6225`
[^83]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_recipes.txt:236`
[^84]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6230`
[^85]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_recipes.txt:348`
[^86]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6224`
[^87]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_recipes.txt:214`
[^88]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6232`
[^89]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_recipes.txt:395`
[^90]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6219`
[^91]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_recipes.txt:91`
[^92]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6228`
[^93]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_recipes.txt:302`
[^94]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6229`
[^95]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_recipes.txt:325`
[^96]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6235`
[^97]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_recipes.txt:467`
[^98]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6223`
[^99]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_recipes.txt:190`
[^100]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6226`
[^101]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_recipes.txt:258`
[^102]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6231`
[^103]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_recipes.txt:372`
[^104]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6227`
[^105]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_recipes.txt:280`
[^106]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6233`
[^107]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_recipes.txt:419`
[^108]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6237`
[^109]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_recipes.txt:515`
[^110]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_recipes.txt:3`
[^111]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_recipes.txt:25`
[^112]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_recipes.txt:47`
[^113]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_recipes.txt:69`
[^114]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6221`
[^115]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR_recipes.txt:141`
[^116]: `3171167894/mods/damnlib/42.20/media/scripts/damnCraft/items_damnCraft.txt:586`
[^117]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR.txt:392`
[^118]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR.txt:429`
[^119]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:5`
[^120]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:18`
[^121]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:31`
[^122]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:44`
[^123]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_bumpers_front.txt:41`
[^124]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_bumpers_rear.txt:41`
[^125]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_armor.txt:114`
[^126]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_armor.txt:176`
[^127]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_armor.txt:238`
[^128]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_armor.txt:299`
[^129]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_sideskirts.txt:34`
[^130]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_spareTire.txt:6`
[^131]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_spoiler.txt:42`
[^132]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_armor.txt:51`
[^133]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_armor.txt:360`
[^134]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_doors.txt:131`
[^135]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_doors.txt:25`
[^136]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_doors.txt:78`
[^137]: `游戏原版/media/scripts/generated/vehicles/template_engine.txt:5`
[^138]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_hood.txt:14`
[^139]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR.txt:375`
[^140]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR.txt:341`
[^141]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:25`
[^142]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:5`
[^143]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:15`
[^144]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:20`
[^145]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:10`
[^146]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR.txt:406`
[^147]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR.txt:416`
[^148]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_mufflers.txt:22`
[^149]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_roofrack.txt:14`
[^150]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_trunk.txt:5`
[^151]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR.txt:463`
[^152]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_seats.txt:113`
[^153]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_seats.txt:37`
[^154]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_seats.txt:56`
[^155]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_seats.txt:75`
[^156]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_seats.txt:94`
[^157]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/92nissanGTR.txt:446`
[^158]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:5`
[^159]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:18`
[^160]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:31`
[^161]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:44`
[^162]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_tires.txt:128`
[^163]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_tires.txt:35`
[^164]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_tires.txt:59`
[^165]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_tires.txt:82`
[^166]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_tires.txt:105`
[^167]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_trunk.txt:24`
[^168]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_trunkdoor.txt:14`
[^169]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_windows.txt:120`
[^170]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_windows.txt:38`
[^171]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_windows.txt:64`
[^172]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_windows.txt:90`
[^173]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_windows.txt:105`
[^174]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_windshield.txt:37`
[^175]: `2846036306/mods/92nissanGTR/42.20/media/scripts/vehicles/template_R32_windshield.txt:95`
