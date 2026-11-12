# '91 Range Rover Classic（'91 RANGE ROVER Classic）

1991 Range Rover Classic，适合土路与越野。

归属：**日常组合（玩法待验收）**；档案视图 `b422-compat`。
当前版本定义：**整车 2、本地物品定义 26、配方 21**；另引用共享物品 22。本地定义数含内部保留项，见独立列表；整车定义包括覆盖原版的条目，不等于新增车型数。

## 如何查找

- **生成整车**：在生成车辆菜单搜索下表完整 ID；显示译名时搜索中文列。联机管理命令用 `/addvehicle 完整ID`。
- **添加到背包**：普通物品、维修件、改装件都在添加物品菜单使用完整物品 ID；不要拿配方或内部槽位去刷车。
- **制作配方**：在制作界面查译名；配方 ID 用于排查，不是可放进背包的物品。
- 中文解释说明用途；只有翻译文件中找到的文字才称为游戏中文名。缺译保留脚本显示名，冲突列出各译文。

## 整车

| 完整生成车辆 ID | 当前中文名 / 名称状态 | 英文名或脚本名 | 变体说明 | 来源 |
| --- | --- | --- | --- | --- |
| `Base.91range` | 91款路虎揽胜四门版[^1] | '91 RANGE ROVER 4-door[^2] | 脚本座位数 4；机修类型 2；具体外观与性能待游戏实刷 | [^3] |
| `Base.91range2` | 91款路虎揽胜双门版[^4] | '91 RANGE ROVER 2-door[^5] | 脚本座位数 4；机修类型 2；具体外观与性能待游戏实刷 | [^6] |

## 普通物品与书籍

| 完整物品 ID | 游戏显示名 / 名称状态 | 中文用途 / 类别 | 菜单 | 适用车辆与安装位置 | 来源 / 状态 |
| --- | --- | --- | --- | --- | --- |
| `Base.91rangeMagazine` | 91 Range Rover Auto Manual（未找到有效中文译文） | 阅读资料；脚本声明解锁：制作91款路虎揽胜引擎盖（Base.91rangeMakeHood）、制作91款路虎揽胜前车门（Base.91rangeMakeFrontDoor）、制作91款路虎揽胜后车门（Base.91rangeMakeRearDoor）、制作91款路虎揽胜后备箱盖（Base.91rangeMakeTrunkLid）、制作91款路虎揽胜前座椅（Base.91rangeMakeFrontSeat）、制作91款路虎揽胜后座椅（Base.91rangeMakeRearSeat）、制作91款路虎揽胜前挡风玻璃（Base.91rangeMakeFrontWindshield）、制作91款路虎揽胜前侧窗（Base.91rangeMakeFrontSideWindow）、制作91款路虎揽胜后侧窗（Base.91rangeMakeRearSideWindow）、制作91款路虎揽胜天窗（Base.91rangeMakeSunroofWindow）、制作91款路虎揽胜后挡风玻璃（Base.91rangeMakeRearWindshield）、制作91款路虎揽胜车顶行李架（Base.91rangeMakeRoofrack）、制作91款路虎揽胜挡泥板（Base.91rangeMakeMudflaps）、制作91款路虎揽胜侧踏板（Base.91rangeMakeSidesteps） / 普通物品 / 书籍 | 添加物品 | 未定位整车安装关系 | 91range[^7] |

## 维修配件

| 完整物品 ID | 游戏显示名 / 名称状态 | 中文用途 / 类别 | 菜单 | 适用车辆与安装位置 | 来源 / 状态 |
| --- | --- | --- | --- | --- | --- |
| `Base.91rangeEngineDoor2` | 91 Range Rover Hood（未找到有效中文译文） | 车辆安装件，用于引擎盖（EngineDoor）；适用车型见右列 / 维修配件 | 添加物品 | Base.91range → EngineDoor；Base.91range2 → EngineDoor | 91range[^8] |
| `Base.91rangeFrontDoor2` | 91 Range Rover Front Door（未找到有效中文译文） | 车辆安装件，用于车门（DoorFrontLeft）、车门（DoorFrontRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.91range → DoorFrontLeft；Base.91range → DoorFrontRight；Base.91range2 → DoorFrontLeft；Base.91range2 → DoorFrontRight | 91range[^9] |
| `Base.91rangeFrontSideWindow2` | 91 Range Rover Front Side Window（未找到有效中文译文） | 车辆安装件，用于车窗（WindowFrontLeft）、车窗（WindowFrontRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.91range → WindowFrontLeft；Base.91range → WindowFrontRight；Base.91range2 → WindowFrontLeft；Base.91range2 → WindowFrontRight | 91range[^10] |
| `Base.91rangeMudflaps2` | 91 Range Rover Mudflaps（未找到有效中文译文） | 车辆安装件，用于车辆安装位（DAMNMudflaps）；适用车型见右列 / 维修配件 | 添加物品 | Base.91range → DAMNMudflaps；Base.91range2 → DAMNMudflaps | 91range[^11] |
| `Base.91rangeRearDoor2` | 91 Range Rover Rear Door（未找到有效中文译文） | 车辆安装件，用于车门（DoorRearLeft）、车门（DoorRearRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.91range → DoorRearLeft；Base.91range → DoorRearRight | 91range[^12] |
| `Base.91rangeRearSideWindow2` | 91 Range Rover Rear Side Window（未找到有效中文译文） | 车辆安装件，用于车窗（WindowRearLeft）、车窗（WindowRearRight）、车窗（WindowBackLeft）、车窗（WindowBackRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.91range → WindowRearLeft；Base.91range → WindowRearRight；Base.91range → WindowBackLeft；Base.91range → WindowBackRight；Base.91range2 → WindowRearLeft；Base.91range2 → WindowRearRight；Base.91range2 → WindowBackLeft；Base.91range2 → WindowBackRight | 91range[^13] |
| `Base.91rangeRearWindshield2` | 91 Range Rover Rear Windshield（未找到有效中文译文） | 车辆安装件，用于挡风玻璃（WindshieldRear）；适用车型见右列 / 维修配件 | 添加物品 | Base.91range → WindshieldRear；Base.91range2 → WindshieldRear | 91range[^14] |
| `Base.91rangeSeatFront2` | 91 Range Rover Front Seat（未找到有效中文译文） | 车辆安装件，用于座椅（SeatFront*）；适用车型见右列 / 维修配件 | 添加物品 | Base.91range → SeatFront*；Base.91range2 → SeatFront* | 91range[^15] |
| `Base.91rangeSeatRear2` | 91 Range Rover Rear Seat（未找到有效中文译文） | 车辆安装件，用于座椅（SeatRear*）；适用车型见右列 / 维修配件 | 添加物品 | Base.91range → SeatRear*；Base.91range2 → SeatRear* | 91range[^16] |
| `Base.91rangeSideSteps2` | 91 Range Rover Side Steps（未找到有效中文译文） | 车辆安装件，用于车辆安装位（DAMNSideSteps）；适用车型见右列 / 维修配件 | 添加物品 | Base.91range → DAMNSideSteps；Base.91range2 → DAMNSideSteps | 91range[^17] |
| `Base.91rangeSnorkel2` | 91 Range Rover Snorkel（未找到有效中文译文） | 车辆安装件，用于车辆安装位（DAMNSnorkel）；适用车型见右列 / 维修配件 | 添加物品 | Base.91range → DAMNSnorkel；Base.91range2 → DAMNSnorkel | 91range[^18] |
| `Base.91rangeSunRoof2` | 91 Range Rover Sunroof（未找到有效中文译文） | 车辆安装件，用于车顶（DAMNSunRoof）；适用车型见右列 / 维修配件 | 添加物品 | Base.91range → DAMNSunRoof；Base.91range2 → DAMNSunRoof | 91range[^19] |
| `Base.91rangeTire2` | 91 Range Rover Tire（未找到有效中文译文） | 车辆安装件，用于轮胎（Tire*）、后备箱（DAMNSpareTireTrunk）、轮胎（DAMNSpareTireRoof）；适用车型见右列 / 维修配件 | 添加物品 | Base.91range → Tire*；Base.91range → DAMNSpareTireTrunk；Base.91range → DAMNSpareTireRoof；Base.91range2 → Tire*；Base.91range2 → DAMNSpareTireTrunk；Base.91range2 → DAMNSpareTireRoof | 91range[^20] |
| `Base.91rangeTrunkDoor2` | 91 Range Rover Trunk Lid（未找到有效中文译文） | 车辆安装件，用于后备箱（TrunkDoor）；适用车型见右列 / 维修配件 | 添加物品 | Base.91range → TrunkDoor；Base.91range2 → TrunkDoor | 91range[^21] |
| `Base.91rangeWindshield2` | 91 Range Rover Windshield（未找到有效中文译文） | 车辆安装件，用于挡风玻璃（Windshield）；适用车型见右列 / 维修配件 | 添加物品 | Base.91range → Windshield；Base.91range2 → Windshield | 91range[^22] |

## 改装配件

| 完整物品 ID | 游戏显示名 / 名称状态 | 中文用途 / 类别 | 菜单 | 适用车辆与安装位置 | 来源 / 状态 |
| --- | --- | --- | --- | --- | --- |
| `Base.91rangeBullbarFrontA` | 91 Range Rover Front Bullbar（未找到有效中文译文） | 车辆安装件，用于保险杠（DAMNBumperFront）；适用车型见右列 / 改装配件 | 添加物品 | Base.91range → DAMNBumperFront；Base.91range2 → DAMNBumperFront | 91range[^23] |
| `Base.91rangeBullbarRearA` | 91 Range Rover Rear Bullbar（未找到有效中文译文） | 车辆安装件，用于保险杠（DAMNBumperRear）；适用车型见右列 / 改装配件 | 添加物品 | Base.91range → DAMNBumperRear；Base.91range2 → DAMNBumperRear | 91range[^24] |
| `Base.91rangeBumperFront0` | 91 Range Rover Front Bumper Type 1（未找到有效中文译文） | 车辆安装件，用于保险杠（DAMNBumperFront）；适用车型见右列 / 改装配件 | 添加物品 | Base.91range → DAMNBumperFront；Base.91range2 → DAMNBumperFront | 91range[^25] |
| `Base.91rangeBumperFront1` | 91 Range Rover Front Bumper Type 2（未找到有效中文译文） | 车辆安装件，用于保险杠（DAMNBumperFront）；适用车型见右列 / 改装配件 | 添加物品 | Base.91range → DAMNBumperFront；Base.91range2 → DAMNBumperFront | 91range[^26] |
| `Base.91rangeBumperRear0` | 91 Range Rover Rear Bumper（未找到有效中文译文） | 车辆安装件，用于保险杠（DAMNBumperRear）；适用车型见右列 / 改装配件 | 添加物品 | Base.91range → DAMNBumperRear；Base.91range2 → DAMNBumperRear | 91range[^27] |
| `Base.91rangeFrontWindowArmor` | 91 Range Rover Front Window Armor（未找到有效中文译文） | 车辆安装件，用于防护件（DAMNFrontLeftArmor）、防护件（DAMNFrontRightArmor）；适用车型见右列 / 改装配件 | 添加物品 | Base.91range → DAMNFrontLeftArmor；Base.91range → DAMNFrontRightArmor；Base.91range2 → DAMNFrontLeftArmor；Base.91range2 → DAMNFrontRightArmor | 91range[^28] |
| `Base.91rangeRearWindowArmor` | 91 Range Rover Rear Window Armor（未找到有效中文译文） | 车辆安装件，用于防护件（DAMNRearLeftArmor）、防护件（DAMNRearRightArmor）、防护件（DAMNBackLeftArmor）、防护件（DAMNBackRightArmor）；适用车型见右列 / 改装配件 | 添加物品 | Base.91range → DAMNRearLeftArmor；Base.91range → DAMNRearRightArmor；Base.91range → DAMNBackLeftArmor；Base.91range → DAMNBackRightArmor；Base.91range2 → DAMNRearLeftArmor；Base.91range2 → DAMNRearRightArmor；Base.91range2 → DAMNBackLeftArmor；Base.91range2 → DAMNBackRightArmor | 91range[^29] |
| `Base.91rangeRoofrack2` | 91 Range Rover Roofrack（未找到有效中文译文） | 车辆安装件，用于车顶行李架（RR91Roofrack）；适用车型见右列 / 改装配件 | 添加物品 | Base.91range → RR91Roofrack；Base.91range2 → RR91Roofrack | 91range[^30] |
| `Base.91rangeWindshieldArmor` | 91 Range Rover Windshield Armor（未找到有效中文译文） | 车辆安装件，用于挡风玻璃（DAMNWindshieldArmor）；适用车型见右列 / 改装配件 | 添加物品 | Base.91range → DAMNWindshieldArmor；Base.91range2 → DAMNWindshieldArmor | 91range[^31] |
| `Base.91rangeWindshieldRearArmor` | 91 Range Rover Rear Windshield Armor（未找到有效中文译文） | 车辆安装件，用于挡风玻璃（DAMNWindshieldRearArmor）；适用车型见右列 / 改装配件 | 添加物品 | Base.91range → DAMNWindshieldRearArmor；Base.91range2 → DAMNWindshieldRearArmor | 91range[^32] |

## 共享配件

下列物品由已启用依赖或游戏原版提供，不计入本 Mod 的本地物品数。

| 完整物品 ID | 游戏显示名 / 名称状态 | 中文用途 / 类别 | 菜单 | 适用车辆与安装位置 | 来源 / 状态 |
| --- | --- | --- | --- | --- | --- |
| `Base.89defenderDakarTire2` | Land Rover Dakar Tire（未找到有效中文译文） | 车辆安装件，用于轮胎（Tire*）、后备箱（DAMNSpareTireTrunk）、轮胎（DAMNSpareTireRoof）；适用车型见右列 / 维修配件 | 添加物品 | Base.91range → Tire*；Base.91range → DAMNSpareTireTrunk；Base.91range → DAMNSpareTireRoof；Base.91range2 → Tire*；Base.91range2 → DAMNSpareTireTrunk；Base.91range2 → DAMNSpareTireRoof | damnlib[^33] |
| `Base.89defenderMilitaryTire2` | Land Rover Wolf Military Tire（未找到有效中文译文） | 车辆安装件，用于轮胎（Tire*）、后备箱（DAMNSpareTireTrunk）、轮胎（DAMNSpareTireRoof）；适用车型见右列 / 维修配件 | 添加物品 | Base.91range → Tire*；Base.91range → DAMNSpareTireTrunk；Base.91range → DAMNSpareTireRoof；Base.91range2 → Tire*；Base.91range2 → DAMNSpareTireTrunk；Base.91range2 → DAMNSpareTireRoof | damnlib[^34] |
| `Base.89defenderTire2` | Land Rover Defender Tire（未找到有效中文译文） | 车辆安装件，用于轮胎（Tire*）、后备箱（DAMNSpareTireTrunk）、轮胎（DAMNSpareTireRoof）；适用车型见右列 / 维修配件 | 添加物品 | Base.91range → Tire*；Base.91range → DAMNSpareTireTrunk；Base.91range → DAMNSpareTireRoof；Base.91range2 → Tire*；Base.91range2 → DAMNSpareTireTrunk；Base.91range2 → DAMNSpareTireRoof | damnlib[^35] |
| `Base.BigGasTank2` | 油箱 (大型)（翻译文件含非标准语法，待游戏核实）[^37] | 车辆安装件，用于油箱（GasTank）；适用车型见右列 / 维修配件 | 添加物品 | Base.91range → GasTank；Base.91range2 → GasTank | 游戏原版[^36] |
| `Base.CarBattery2` | 汽车电池（翻译文件含非标准语法，待游戏核实）[^39] | 车辆安装件，用于蓄电池（Battery）、蓄电池（GRHouseBattery1）、蓄电池（GRHouseBattery2）；适用车型见右列 / 维修配件 | 添加物品 | Base.91range → Battery；Base.91range2 → Battery | 游戏原版[^38] |
| `Base.GloveBox2` | 手套箱（翻译文件含非标准语法，待游戏核实）[^41] | 车辆安装件，用于车辆安装位（GloveBox）；适用车型见右列 / 维修配件 | 添加物品 | Base.91range → GloveBox；Base.91range2 → GloveBox | 游戏原版[^40] |
| `Base.LightBulb` | 灯泡-白色 / 灯泡 (白)（译文冲突，待游戏核实）[^43] | 车辆安装件，用于车灯（Headlight*）、车灯（JP82DorothyLights）；适用车型见右列 / 维修配件 | 添加物品 | Base.91range → Headlight*；Base.91range2 → Headlight* | 游戏原版[^42] |
| `Base.ModernBrake2` | 制动器 (高级)（翻译文件含非标准语法，待游戏核实）[^45] | 车辆安装件，用于制动器（Brake*）；适用车型见右列 / 维修配件 | 添加物品 | Base.91range → Brake*；Base.91range2 → Brake* | 游戏原版[^44] |
| `Base.ModernCarMuffler2` | 消声器 (高级)（翻译文件含非标准语法，待游戏核实）[^47] | 车辆安装件，用于消声器（Muffler）；适用车型见右列 / 维修配件 | 添加物品 | Base.91range → Muffler；Base.91range2 → Muffler | 游戏原版[^46] |
| `Base.ModernSuspension2` | 悬挂 (高级)（翻译文件含非标准语法，待游戏核实）[^49] | 车辆安装件，用于悬挂（Suspension*）；适用车型见右列 / 维修配件 | 添加物品 | Base.91range → Suspension*；Base.91range2 → Suspension* | 游戏原版[^48] |
| `Base.NormalBrake2` | 制动器 (普通)（翻译文件含非标准语法，待游戏核实）[^51] | 车辆安装件，用于制动器（Brake*）；适用车型见右列 / 维修配件 | 添加物品 | Base.91range → Brake*；Base.91range2 → Brake* | 游戏原版[^50] |
| `Base.NormalCarMuffler2` | 消声器 (普通)（翻译文件含非标准语法，待游戏核实）[^53] | 车辆安装件，用于消声器（Muffler）；适用车型见右列 / 维修配件 | 添加物品 | Base.91range → Muffler；Base.91range2 → Muffler | 游戏原版[^52] |
| `Base.NormalGasTank2` | 油箱 (标准)（翻译文件含非标准语法，待游戏核实）[^55] | 车辆安装件，用于油箱（GasTank）；适用车型见右列 / 维修配件 | 添加物品 | Base.91range → GasTank；Base.91range2 → GasTank | 游戏原版[^54] |
| `Base.NormalSuspension2` | 悬挂 (普通)（翻译文件含非标准语法，待游戏核实）[^57] | 车辆安装件，用于悬挂（Suspension*）；适用车型见右列 / 维修配件 | 添加物品 | Base.91range → Suspension*；Base.91range2 → Suspension* | 游戏原版[^56] |
| `Base.OldBrake2` | 制动器 (老式)（翻译文件含非标准语法，待游戏核实）[^59] | 车辆安装件，用于制动器（Brake*）；适用车型见右列 / 维修配件 | 添加物品 | Base.91range → Brake*；Base.91range2 → Brake* | 游戏原版[^58] |
| `Base.OldCarMuffler2` | 消声器 (老式)（翻译文件含非标准语法，待游戏核实）[^61] | 车辆安装件，用于消声器（Muffler）；适用车型见右列 / 维修配件 | 添加物品 | Base.91range → Muffler；Base.91range2 → Muffler | 游戏原版[^60] |
| `Base.RadioBlack` | 收音机 (超值科技) / 收音机 (廉科) / 廉科牌收音机（译文冲突，待游戏核实）[^63] | 车辆安装件，用于车辆安装位（Radio）；适用车型见右列 / 维修配件 | 添加物品 | Base.91range → Radio；Base.91range2 → Radio | 游戏原版[^62] |
| `Base.RadioMakeShift` | 收音机 (简易) / 自制收音机（译文冲突，待游戏核实）[^65] | 车辆安装件，用于车辆安装位（Radio）；适用车型见右列 / 维修配件 | 添加物品 | Base.91range → Radio；Base.91range2 → Radio | 游戏原版[^64] |
| `Base.RadioRed` | 导航仪 / 收音机 (昂科) / 昂科牌收音机（译文冲突，待游戏核实）[^67] | 车辆安装件，用于车辆安装位（Radio）；适用车型见右列 / 维修配件 | 添加物品 | Base.91range → Radio；Base.91range2 → Radio | 游戏原版[^66] |
| `Base.SmallGasTank2` | 油箱 (小型)（翻译文件含非标准语法，待游戏核实）[^69] | 车辆安装件，用于油箱（GasTank）；适用车型见右列 / 维修配件 | 添加物品 | Base.91range → GasTank；Base.91range2 → GasTank | 游戏原版[^68] |
| `damnCraft.SmallTire2` | Small Universal Tire（未找到有效中文译文） | 车辆安装件，用于轮胎（Tire*）、轮胎（KI5TRSpareTire）、后备箱（DAMNSpareTireTrunk）、轮胎（DAMNSpareTireRoof）、轮胎（DAMNSpareTire）、轮胎（DAMNSpareTireFront）、轮胎（DAMNSpareTireBed）；适用车型见右列 / 维修配件 | 添加物品 | Base.91range → Tire*；Base.91range → DAMNSpareTireTrunk；Base.91range → DAMNSpareTireRoof；Base.91range2 → Tire*；Base.91range2 → DAMNSpareTireTrunk；Base.91range2 → DAMNSpareTireRoof | damnlib[^70] |

## 制作配方

| 配方完整 ID（排查用） | 游戏配方名 / 名称状态 | 中文用途 | 菜单 | 来源 |
| --- | --- | --- | --- | --- |
| `Base.91rangeMakeFrontBullbar` | 制作91款路虎揽胜前防撞杠[^71] | 制作产出：91 Range Rover Front Bullbar（车辆安装件，用于保险杠（DAMNBumperFront）；适用车型见右列） | 制作界面 | [^72] |
| `Base.91rangeMakeFrontDoor` | 制作91款路虎揽胜前车门[^73] | 制作产出：91 Range Rover Front Door（车辆安装件，用于车门（DoorFrontLeft）、车门（DoorFrontRight）；适用车型见右列） | 制作界面 | [^74] |
| `Base.91rangeMakeFrontSeat` | 制作91款路虎揽胜前座椅[^75] | 制作产出：91 Range Rover Front Seat（车辆安装件，用于座椅（SeatFront*）；适用车型见右列） | 制作界面 | [^76] |
| `Base.91rangeMakeFrontSideWindow` | 制作91款路虎揽胜前侧窗[^77] | 制作产出：91 Range Rover Front Side Window（车辆安装件，用于车窗（WindowFrontLeft）、车窗（WindowFrontRight）；适用车型见右列） | 制作界面 | [^78] |
| `Base.91rangeMakeFrontWindowArmor` | 制作91款路虎揽胜前车窗装甲[^79] | 制作产出：91 Range Rover Front Window Armor（车辆安装件，用于防护件（DAMNFrontLeftArmor）、防护件（DAMNFrontRightArmor）；适用车型见右列） | 制作界面 | [^80] |
| `Base.91rangeMakeFrontWindshield` | 制作91款路虎揽胜前挡风玻璃[^81] | 制作产出：91 Range Rover Windshield（车辆安装件，用于挡风玻璃（Windshield）；适用车型见右列） | 制作界面 | [^82] |
| `Base.91rangeMakeFrontWindshieldArmor` | 制作91款路虎揽胜前挡风玻璃装甲[^83] | 制作产出：91 Range Rover Windshield Armor（车辆安装件，用于挡风玻璃（DAMNWindshieldArmor）；适用车型见右列） | 制作界面 | [^84] |
| `Base.91rangeMakeHood` | 制作91款路虎揽胜引擎盖[^85] | 制作产出：91 Range Rover Hood（车辆安装件，用于引擎盖（EngineDoor）；适用车型见右列） | 制作界面 | [^86] |
| `Base.91rangeMakeMudflaps` | 制作91款路虎揽胜挡泥板[^87] | 制作产出：91 Range Rover Mudflaps（车辆安装件，用于车辆安装位（DAMNMudflaps）；适用车型见右列） | 制作界面 | [^88] |
| `Base.91rangeMakeRearBullbar` | 制作91款路虎揽胜后防撞杠[^89] | 制作产出：91 Range Rover Rear Bullbar（车辆安装件，用于保险杠（DAMNBumperRear）；适用车型见右列） | 制作界面 | [^90] |
| `Base.91rangeMakeRearDoor` | 制作91款路虎揽胜后车门[^91] | 制作产出：91 Range Rover Rear Door（车辆安装件，用于车门（DoorRearLeft）、车门（DoorRearRight）；适用车型见右列） | 制作界面 | [^92] |
| `Base.91rangeMakeRearSeat` | 制作91款路虎揽胜后座椅[^93] | 制作产出：91 Range Rover Rear Seat（车辆安装件，用于座椅（SeatRear*）；适用车型见右列） | 制作界面 | [^94] |
| `Base.91rangeMakeRearSideWindow` | 制作91款路虎揽胜后侧窗[^95] | 制作产出：91 Range Rover Rear Side Window（车辆安装件，用于车窗（WindowRearLeft）、车窗（WindowRearRight）、车窗（WindowBackLeft）、车窗（WindowBackRight）；适用车型见右列） | 制作界面 | [^96] |
| `Base.91rangeMakeRearWindowArmor` | 制作91款路虎揽胜后车窗装甲[^97] | 制作产出：91 Range Rover Rear Window Armor（车辆安装件，用于防护件（DAMNRearLeftArmor）、防护件（DAMNRearRightArmor）、防护件（DAMNBackLeftArmor）、防护件（DAMNBackRightArmor）；适用车型见右列） | 制作界面 | [^98] |
| `Base.91rangeMakeRearWindshield` | 制作91款路虎揽胜后挡风玻璃[^99] | 制作产出：91 Range Rover Rear Windshield（车辆安装件，用于挡风玻璃（WindshieldRear）；适用车型见右列） | 制作界面 | [^100] |
| `Base.91rangeMakeRearWindshieldArmor` | 制作91款路虎揽胜后挡风玻璃装甲[^101] | 制作产出：91 Range Rover Rear Windshield Armor（车辆安装件，用于挡风玻璃（DAMNWindshieldRearArmor）；适用车型见右列） | 制作界面 | [^102] |
| `Base.91rangeMakeRoofrack` | 制作91款路虎揽胜车顶行李架[^103] | 制作产出：91 Range Rover Roofrack（车辆安装件，用于车顶行李架（RR91Roofrack）；适用车型见右列） | 制作界面 | [^104] |
| `Base.91rangeMakeSidesteps` | 制作91款路虎揽胜侧踏板[^105] | 制作产出：91 Range Rover Side Steps（车辆安装件，用于车辆安装位（DAMNSideSteps）；适用车型见右列） | 制作界面 | [^106] |
| `Base.91rangeMakeSunroofWindow` | 制作91款路虎揽胜天窗[^107] | 制作产出：91 Range Rover Sunroof（车辆安装件，用于车顶（DAMNSunRoof）；适用车型见右列） | 制作界面 | [^108] |
| `Base.91rangeMakeTire` | 制作91款路虎揽胜轮胎[^109] | 制作产出：91 Range Rover Tire（车辆安装件，用于轮胎（Tire*）、后备箱（DAMNSpareTireTrunk）、轮胎（DAMNSpareTireRoof）；适用车型见右列） | 制作界面 | [^110] |
| `Base.91rangeMakeTrunkLid` | 制作91款路虎揽胜后备箱盖[^111] | 制作产出：91 Range Rover Trunk Lid（车辆安装件，用于后备箱（TrunkDoor）；适用车型见右列） | 制作界面 | [^112] |

## 内部定义、历史分支与未解析引用

有效资源层：42.20, common；仅合并 common 与所选版本，Overlay 按相对路径覆盖。
车辆模板 19 个、内部槽位 72 个，均不算整车或背包物品。旧根目录和未选中版本的定义不列入当前可用表。模板中短物品引用若追加机修类型后缀才匹配定义，属于静态映射，安装仍待实测。

内部或过时的 item 定义单列于此，不在上面的背包刷取建议中；它们仍计入各自来源的定义数量。

| 保留定义 ID（不作正常刷取建议） | 脚本显示名 | 中文说明 / 状态 | 来源 |
| --- | --- | --- | --- |
| `damnCraft.Trunk2` | no | 车辆后备箱的内部容量载体，关联车辆槽位与容积状态；不是可携带的旅行箱；显示名 no、图标 na；不作正常刷取建议 | [^113] |

<details><summary>查看内部槽位（不能直接刷取）</summary>

| 槽位 | 名称或说明 | 来源 |
| --- | --- | --- |
| `Battery` | 电池 / 蓄电池 | [^114] |
| `Brake*` | Brake* / 制动器 | [^115] |
| `BrakeFrontLeft` | 左前制动 / 制动器 | [^116] |
| `BrakeFrontRight` | 右前制动 / 制动器 | [^117] |
| `BrakeRearLeft` | 左后制动 / 制动器 | [^118] |
| `BrakeRearRight` | 右后制动 / 制动器 | [^119] |
| `DAMNBackLeftArmor` | 左后部车窗装甲 / 防护件 | [^120] |
| `DAMNBackRightArmor` | 右后部车窗装甲 / 防护件 | [^121] |
| `DAMNBumperFront` | 前保险杠 / 保险杠 | [^122] |
| `DAMNBumperRear` | 后保险杠 / 保险杠 | [^123] |
| `DAMNFrontLeftArmor` | 左前车窗装甲 / 防护件 | [^124] |
| `DAMNFrontRightArmor` | 右前车窗装甲 / 防护件 | [^125] |
| `DAMNMudflaps` | 挡泥板 / 车辆安装位 | [^126] |
| `DAMNRearLeftArmor` | 左后车窗装甲 / 防护件 | [^127] |
| `DAMNRearRightArmor` | 右后车窗装甲 / 防护件 | [^128] |
| `DAMNSideSteps` | 侧踏板 / 车辆安装位 | [^129] |
| `DAMNSnorkel` | 涉水喉 / 车辆安装位 | [^130] |
| `DAMNSpareTireRoof` | 车顶备胎 / 轮胎 | [^131] |
| `DAMNSpareTireTrunk` | 后备箱备胎 / 后备箱 | [^132] |
| `DAMNSunRoof` | 天窗 / 车顶 | [^133] |
| `DAMNWindshieldArmor` | 挡风玻璃装甲 / 挡风玻璃 | [^134] |
| `DAMNWindshieldRearArmor` | 后挡风玻璃装甲 / 挡风玻璃 | [^135] |
| `Door*` | Door* / 车门 | [^136] |
| `DoorFrontLeft` | 左前门 / 车门 | [^137] |
| `DoorFrontRight` | 右前门 / 车门 | [^138] |
| `DoorRearLeft` | 左后门 / 车门 | [^139] |
| `DoorRearRight` | 右后门 / 车门 | [^140] |
| `Engine` | 引擎 / 发动机 | [^141] |
| `EngineDoor` | 引擎盖 / 引擎盖 | [^142] |
| `GasTank` | 油箱 / 油箱 | [^143] |
| `GloveBox` | 手套箱 / 车辆安装位 | [^144] |
| `Headlight*` | Headlight* / 车灯 | [^145] |
| `HeadlightLeft` | 左大灯 / 车灯 | [^146] |
| `HeadlightRearLeft` | 左尾灯 / 车灯 | [^147] |
| `HeadlightRearRight` | 右尾灯 / 车灯 | [^148] |
| `HeadlightRight` | 右大灯 / 车灯 | [^149] |
| `Heater` | 加热器 / 车辆安装位 | [^150] |
| `Muffler` | 排气消声器 / 消声器 | [^151] |
| `PassengerCompartment` | 乘员舱 / 车辆安装位 | [^152] |
| `RR91Roofrack` | 车顶行李架储物 / 车顶行李架 | [^153] |
| `RR91Trunk` | 后备箱储物 / 后备箱 | [^154] |
| `Radio` | 电台 / 车辆安装位 | [^155] |
| `SeatFront*` | SeatFront* / 座椅 | [^156] |
| `SeatFrontLeft` | 驾驶座 / 座椅 | [^157] |
| `SeatFrontRight` | 右前座 / 座椅 | [^158] |
| `SeatRear*` | SeatRear* / 座椅 | [^159] |
| `SeatRearLeft` | 左后座 / 座椅 | [^160] |
| `SeatRearRight` | 右后座 / 座椅 | [^161] |
| `Suspension*` | Suspension* / 悬挂 | [^162] |
| `SuspensionFrontLeft` | 左前悬挂 / 悬挂 | [^163] |
| `SuspensionFrontRight` | 右前悬挂 / 悬挂 | [^164] |
| `SuspensionRearLeft` | 左后悬挂 / 悬挂 | [^165] |
| `SuspensionRearRight` | 右后悬挂 / 悬挂 | [^166] |
| `Tire*` | Tire* / 轮胎 | [^167] |
| `TireFrontLeft` | 左前胎 / 轮胎 | [^168] |
| `TireFrontRight` | 右前胎 / 轮胎 | [^169] |
| `TireRearLeft` | 左后胎 / 轮胎 | [^170] |
| `TireRearRight` | 右后胎 / 轮胎 | [^171] |
| `TruckBed` | 补给箱 / 行李箱 / 车辆安装位 | [^172] |
| `TrunkDoor` | 后车盖 / 后备箱 | [^173] |
| `Window*` | Window* / 车窗 | [^174] |
| `WindowBack*` | WindowBack* / 车窗 | [^175] |
| `WindowBackLeft` | 左后部车窗 / 车窗 | [^176] |
| `WindowBackRight` | 右后部车窗 / 车窗 | [^177] |
| `WindowFront*` | WindowFront* / 车窗 | [^178] |
| `WindowFrontLeft` | 左前窗 / 车窗 | [^179] |
| `WindowFrontRight` | 右前窗 / 车窗 | [^180] |
| `WindowRear*` | WindowRear* / 车窗 | [^181] |
| `WindowRearLeft` | 左后窗 / 车窗 | [^182] |
| `WindowRearRight` | 右后窗 / 车窗 | [^183] |
| `Windshield` | 挡风玻璃 / 挡风玻璃 | [^184] |
| `WindshieldRear` | 后挡风玻璃 / 挡风玻璃 | [^185] |

</details>


## 概览

| Mod ID / 文件夹 | 分发端 | 版本 | 选择的 mod.info | 原件范围 → 当前范围 |
| --- | --- | --- | --- | --- |
| `91range` / `91range` | both（双端） | 未标注 | `42.20/mod.info` | 42.20.0 … - → 42.20.0 … - |

原件体积 18.1 MB；体积按完整目录统计，与当前内容定义数分开。
工作坊：[查看作者页面](https://steamcommunity.com/sharedfiles/filedetails/?id=2409333430)。

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

require damnlib；36 个脚本物品、2 个载具脚本、25 条配方。

```
cd A004
python lab.py check --profile b422-compat
grep -a '91range' runs/<trial>/*console.log
```
<!-- retained:end -->

## 静态来源

路径相对 `A004/workspace/mods_library/`；`Overlay/<文件夹>/` 指 `A004/workspace/patches/mods/<文件夹>/`，`游戏原版/` 指当前 B42.22 客户端 Game 目录。翻译来源列出所有候选，未按加载顺序擅自消解异文。

[^1]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/IG_UI.json:12484`
[^2]: `2409333430/mods/91range/common/media/lua/shared/Translate/EN/IG_UI.json:3`
[^3]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range.txt:31`
[^4]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/IG_UI.json:12485`
[^5]: `2409333430/mods/91range/common/media/lua/shared/Translate/EN/IG_UI.json:4`
[^6]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range2.txt:24`
[^7]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_vehiclesitems.txt:6`
[^8]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_vehiclesitems.txt:164`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_hood.txt:14`
[^9]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_vehiclesitems.txt:66`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_doors.txt:42`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_doors.txt:96`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_doors2.txt:24`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_doors2.txt:79`
[^10]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_vehiclesitems.txt:325`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_windows.txt:65`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_windows.txt:91`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_windows2.txt:38`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_windows2.txt:64`
[^11]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_vehiclesitems.txt:387`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_mudflaps.txt:13`
[^12]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_vehiclesitems.txt:81`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_doors.txt:150`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_doors.txt:204`
[^13]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_vehiclesitems.txt:340`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_windows.txt:117`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_windows.txt:143`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_windows.txt:169`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_windows.txt:184`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_windows2.txt:90`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_windows2.txt:106`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_windows2.txt:122`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_windows2.txt:137`
[^14]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_vehiclesitems.txt:355`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_windshields.txt:80`
[^15]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_vehiclesitems.txt:198`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_seats.txt:108`
[^16]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_vehiclesitems.txt:214`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_seats.txt:159`
[^17]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_vehiclesitems.txt:404`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_sidesteps.txt:14`
[^18]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_vehiclesitems.txt:421`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_snorkel.txt:13`
[^19]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_vehiclesitems.txt:370`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_windows.txt:252`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_windows2.txt:308`
[^20]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_vehiclesitems.txt:24`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_tire.txt:238`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_spareTires.txt:13`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_spareTires.txt:79`
[^21]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_vehiclesitems.txt:181`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_trunkdoor.txt:14`
[^22]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_vehiclesitems.txt:310`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_windshields.txt:22`
[^23]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_vehiclesitems.txt:263`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_bumpers.txt:40`
[^24]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_vehiclesitems.txt:293`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_bumpers.txt:112`
[^25]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_vehiclesitems.txt:233`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_bumpers.txt:40`
[^26]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_vehiclesitems.txt:248`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_bumpers.txt:40`
[^27]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_vehiclesitems.txt:278`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_bumpers.txt:112`
[^28]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_vehiclesitems.txt:98`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_armor.txt:129`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_armor.txt:193`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_armor2.txt:98`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_armor2.txt:162`
[^29]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_vehiclesitems.txt:114`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_armor.txt:257`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_armor.txt:321`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_armor.txt:385`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_armor.txt:448`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_armor2.txt:226`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_armor2.txt:290`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_armor2.txt:354`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_armor2.txt:417`
[^30]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_vehiclesitems.txt:46`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_roofrack.txt:14`
[^31]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_vehiclesitems.txt:130`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_armor.txt:66`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_armor2.txt:35`
[^32]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_vehiclesitems.txt:146`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_armor.txt:511`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_armor2.txt:480`
[^33]: `3171167894/mods/damnlib/42.20/media/scripts/commonItems/damnCommonTires_vehiclesitems.txt:563`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_tire.txt:238`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_spareTires.txt:13`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_spareTires.txt:79`
[^34]: `3171167894/mods/damnlib/42.20/media/scripts/commonItems/damnCommonTires_vehiclesitems.txt:583`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_tire.txt:238`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_spareTires.txt:13`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_spareTires.txt:79`
[^35]: `3171167894/mods/damnlib/42.20/media/scripts/commonItems/damnCommonTires_vehiclesitems.txt:543`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_tire.txt:238`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_spareTires.txt:13`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_spareTires.txt:79`
[^36]: `游戏原版/media/scripts/generated/items/normal.txt:12408`；`2409333430/mods/91range/42.20/media/scripts/vehicles/91range.txt:357`；`2409333430/mods/91range/42.20/media/scripts/vehicles/91range2.txt:348`
[^37]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:448`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:163`
[^38]: `游戏原版/media/scripts/generated/items/drainable.txt:2368`；`2409333430/mods/91range/42.20/media/scripts/vehicles/91range.txt:374`；`2409333430/mods/91range/42.20/media/scripts/vehicles/91range2.txt:365`
[^39]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:970`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:380`
[^40]: `游戏原版/media/scripts/generated/items/normal.txt:13025`；`2409333430/mods/91range/42.20/media/scripts/vehicles/91range.txt:325`；`2409333430/mods/91range/42.20/media/scripts/vehicles/91range2.txt:316`
[^41]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1776`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:687`
[^42]: `游戏原版/media/scripts/generated/items/normal.txt:4661`；`游戏原版/media/scripts/generated/vehicles/template_headlight.txt:25`
[^43]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:6727`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25103`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2563`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:965`
[^44]: `游戏原版/media/scripts/generated/items/normal.txt:12163`；`2409333430/mods/91range/42.20/media/scripts/vehicles/91range.txt:441`；`2409333430/mods/91range/42.20/media/scripts/vehicles/91range2.txt:431`
[^45]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2780`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1050`
[^46]: `游戏原版/media/scripts/generated/items/normal.txt:13166`；`2409333430/mods/91range/42.20/media/scripts/vehicles/91range.txt:387`；`2409333430/mods/91range/42.20/media/scripts/vehicles/91range2.txt:378`
[^47]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2783`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1053`
[^48]: `游戏原版/media/scripts/generated/items/normal.txt:12282`；`2409333430/mods/91range/42.20/media/scripts/vehicles/91range.txt:458`；`2409333430/mods/91range/42.20/media/scripts/vehicles/91range2.txt:448`
[^49]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2786`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1056`
[^50]: `游戏原版/media/scripts/generated/items/normal.txt:12146`；`2409333430/mods/91range/42.20/media/scripts/vehicles/91range.txt:441`；`2409333430/mods/91range/42.20/media/scripts/vehicles/91range2.txt:431`
[^51]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3219`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1135`
[^52]: `游戏原版/media/scripts/generated/items/normal.txt:13151`；`2409333430/mods/91range/42.20/media/scripts/vehicles/91range.txt:387`；`2409333430/mods/91range/42.20/media/scripts/vehicles/91range2.txt:378`
[^53]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3222`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1138`
[^54]: `游戏原版/media/scripts/generated/items/normal.txt:12393`；`2409333430/mods/91range/42.20/media/scripts/vehicles/91range.txt:357`；`2409333430/mods/91range/42.20/media/scripts/vehicles/91range2.txt:348`
[^55]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3228`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1144`
[^56]: `游戏原版/media/scripts/generated/items/normal.txt:12265`；`2409333430/mods/91range/42.20/media/scripts/vehicles/91range.txt:458`；`2409333430/mods/91range/42.20/media/scripts/vehicles/91range2.txt:448`
[^57]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3231`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1147`
[^58]: `游戏原版/media/scripts/generated/items/normal.txt:12129`；`2409333430/mods/91range/42.20/media/scripts/vehicles/91range.txt:441`；`2409333430/mods/91range/42.20/media/scripts/vehicles/91range2.txt:431`
[^59]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3255`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1165`
[^60]: `游戏原版/media/scripts/generated/items/normal.txt:13136`；`2409333430/mods/91range/42.20/media/scripts/vehicles/91range.txt:387`；`2409333430/mods/91range/42.20/media/scripts/vehicles/91range2.txt:378`
[^61]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3258`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1168`
[^62]: `游戏原版/media/scripts/generated/items/radio.txt:308`；`游戏原版/media/scripts/generated/vehicles/template_radio.txt:5`
[^63]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:7374`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25092`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3645`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:5128`
[^64]: `游戏原版/media/scripts/generated/items/radio.txt:335`；`游戏原版/media/scripts/generated/vehicles/template_radio.txt:5`
[^65]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:7375`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25093`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3649`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:5132`
[^66]: `游戏原版/media/scripts/generated/items/radio.txt:361`；`游戏原版/media/scripts/generated/vehicles/template_radio.txt:5`
[^67]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:3001`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25091`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3651`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:5134`
[^68]: `游戏原版/media/scripts/generated/items/normal.txt:12378`；`2409333430/mods/91range/42.20/media/scripts/vehicles/91range.txt:357`；`2409333430/mods/91range/42.20/media/scripts/vehicles/91range2.txt:348`
[^69]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:4152`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1543`
[^70]: `3171167894/mods/damnlib/42.20/media/scripts/damnCraft/items_damnCraft.txt:493`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_tire.txt:238`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_spareTires.txt:13`；`2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_spareTires.txt:79`
[^71]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:3760`
[^72]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_recipes.txt:378`
[^73]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:3746`
[^74]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_recipes.txt:49`
[^75]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:3749`
[^76]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_recipes.txt:126`
[^77]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:3752`
[^78]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_recipes.txt:196`
[^79]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:3757`
[^80]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_recipes.txt:308`
[^81]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:3751`
[^82]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_recipes.txt:174`
[^83]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:3756`
[^84]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_recipes.txt:284`
[^85]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:3745`
[^86]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_recipes.txt:25`
[^87]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:3763`
[^88]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_recipes.txt:448`
[^89]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:3761`
[^90]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_recipes.txt:401`
[^91]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:3747`
[^92]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_recipes.txt:75`
[^93]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:3750`
[^94]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_recipes.txt:150`
[^95]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:3753`
[^96]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_recipes.txt:218`
[^97]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:3758`
[^98]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_recipes.txt:331`
[^99]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:3755`
[^100]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_recipes.txt:262`
[^101]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:3759`
[^102]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_recipes.txt:354`
[^103]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:3762`
[^104]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_recipes.txt:423`
[^105]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:3764`
[^106]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_recipes.txt:469`
[^107]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:3754`
[^108]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_recipes.txt:240`
[^109]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:3744`
[^110]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_recipes.txt:3`
[^111]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:3748`
[^112]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range_recipes.txt:101`
[^113]: `3171167894/mods/damnlib/42.20/media/scripts/damnCraft/items_damnCraft.txt:572`
[^114]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range.txt:374`
[^115]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range.txt:441`
[^116]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:5`
[^117]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:18`
[^118]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:31`
[^119]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:44`
[^120]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_armor.txt:385`
[^121]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_armor.txt:448`
[^122]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_bumpers.txt:40`
[^123]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_bumpers.txt:112`
[^124]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_armor.txt:129`
[^125]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_armor.txt:193`
[^126]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_mudflaps.txt:13`
[^127]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_armor.txt:257`
[^128]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_armor.txt:321`
[^129]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_sidesteps.txt:14`
[^130]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_snorkel.txt:13`
[^131]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_spareTires.txt:79`
[^132]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_spareTires.txt:13`
[^133]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_windows.txt:252`
[^134]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_armor.txt:66`
[^135]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_armor.txt:511`
[^136]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_doors.txt:258`
[^137]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_doors.txt:42`
[^138]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_doors.txt:96`
[^139]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_doors.txt:150`
[^140]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_doors.txt:204`
[^141]: `游戏原版/media/scripts/generated/vehicles/template_engine.txt:5`
[^142]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_hood.txt:14`
[^143]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range.txt:357`
[^144]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range.txt:325`
[^145]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:25`
[^146]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:5`
[^147]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:15`
[^148]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:20`
[^149]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:10`
[^150]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range.txt:409`
[^151]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range.txt:387`
[^152]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range.txt:419`
[^153]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_roofrack.txt:14`
[^154]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_trunk.txt:5`
[^155]: `游戏原版/media/scripts/generated/vehicles/template_radio.txt:5`
[^156]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_seats.txt:108`
[^157]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_seats.txt:36`
[^158]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_seats.txt:54`
[^159]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_seats.txt:159`
[^160]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_seats.txt:72`
[^161]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_seats.txt:90`
[^162]: `2409333430/mods/91range/42.20/media/scripts/vehicles/91range.txt:458`
[^163]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:5`
[^164]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:18`
[^165]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:31`
[^166]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:44`
[^167]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_tire.txt:238`
[^168]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_tire.txt:61`
[^169]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_tire.txt:106`
[^170]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_tire.txt:150`
[^171]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_tire.txt:194`
[^172]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_trunk.txt:24`
[^173]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_trunkdoor.txt:14`
[^174]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_windows.txt:200`
[^175]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_windows2.txt:256`
[^176]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_windows.txt:169`
[^177]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_windows.txt:184`
[^178]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_windows2.txt:153`
[^179]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_windows.txt:65`
[^180]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_windows.txt:91`
[^181]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_windows2.txt:205`
[^182]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_windows.txt:117`
[^183]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_windows.txt:143`
[^184]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_windshields.txt:22`
[^185]: `2409333430/mods/91range/42.20/media/scripts/vehicles/template_RR91_windshields.txt:80`
