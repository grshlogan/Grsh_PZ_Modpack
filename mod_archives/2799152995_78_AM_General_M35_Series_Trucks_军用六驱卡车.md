# '78 AM General M35 军卡（'78 AM General M35 Series Trucks）

1978 AM General M35 系列，含加油车、水罐车、救援车等变体子 mod（未启用）。

归属：**日常组合（玩法待验收）**；档案视图 `b422-compat`。
当前版本定义：**整车 4、本地物品定义 19、配方 17**；另引用共享物品 18。本地定义数含内部保留项，见独立列表；整车定义包括覆盖原版的条目，不等于新增车型数。

## 如何查找

- **生成整车**：在生成车辆菜单搜索下表完整 ID；显示译名时搜索中文列。联机管理命令用 `/addvehicle 完整ID`。
- **添加到背包**：普通物品、维修件、改装件都在添加物品菜单使用完整物品 ID；不要拿配方或内部槽位去刷车。
- **制作配方**：在制作界面查译名；配方 ID 用于排查，不是可放进背包的物品。
- 中文解释说明用途；只有翻译文件中找到的文字才称为游戏中文名。缺译保留脚本显示名，冲突列出各译文。

## 整车

| 完整生成车辆 ID | 当前中文名 / 名称状态 | 英文名或脚本名 | 变体说明 | 来源 |
| --- | --- | --- | --- | --- |
| `Base.78amgeneralM35A2` | '78 AM General M35A2（未找到有效中文译文）[^1] | '78 AM General M35A2[^1] | 脚本座位数 2；机修类型 2；具体外观与性能待游戏实刷 | [^2] |
| `Base.78amgeneralM49A2C` | '78 AM General M49A2C Fuel Tanker（未找到有效中文译文）[^3] | '78 AM General M49A2C Fuel Tanker[^3] | 脚本座位数 2；机修类型 2；具体外观与性能待游戏实刷 | [^4] |
| `Base.78amgeneralM50A3` | 78款通用M50A3供水车[^5] | '78 AM General M50A3 Water Tanker[^6] | 脚本座位数 2；机修类型 2；具体外观与性能待游戏实刷 | [^7] |
| `Base.78amgeneralM62` | '78 AM General M62 Wrecker（未找到有效中文译文）[^8] | '78 AM General M62 Wrecker[^8] | 脚本座位数 2；机修类型 2；具体外观与性能待游戏实刷 | [^9] |

## 普通物品与书籍

| 完整物品 ID | 游戏显示名 / 名称状态 | 中文用途 / 类别 | 菜单 | 适用车辆与安装位置 | 来源 / 状态 |
| --- | --- | --- | --- | --- | --- |
| `Base.M35A2Magazine` | 78 AM General M35A2 Auto Manual（未找到有效中文译文） | 阅读资料；脚本声明解锁：Make 78 AM General M35A2 Hood（Base.78amgeneralM35A2MakeHood）、Make 78 AM General M35A2 Front Door（Base.78amgeneralM35A2MakeFrontDoor）、Make 78 AM General M35A2 Tailgate（Base.78amgeneralM35A2MakeTailgate）、Make 78 AM General M49/M50 Pump Doors（Base.78amgeneralM35A2MakeTrunkLid）、Make 78 AM General M35A2 Front Windshield（Base.78amgeneralM35A2MakeFrontWindshield）、Make 78 AM General M35A2 Front Side Window（Base.78amgeneralM35A2MakeFrontSideWindow）、Make 78 AM General M35A2 Front Bumper（Base.78amgeneralM35A2MakeFrontBumper）、Make 78 AM General M35A2 Front Grille（Base.78amgeneralM35A2MakeFrontGrille）、Make 78 AM General M35A2 Mudflaps（Base.78amgeneralM35A2MakeMudflaps）、Make 78 AM General M35A2 Bed Cover（Base.78amgeneralM35A2MakeSoftBedCover）、Make 78 AM General M35A2 Muffler（Base.78amgeneralM35A2MakeMuffler）、Make 78 AM General M35A2 Hard Cab Cover（Base.78amgeneralM35A2MakeHardCabCover）、Make 78 AM General M35A2 Soft Cab Cover（Base.78amgeneralM35A2MakeSoftCabCover） / 普通物品 / 书籍 | 添加物品 | 未定位整车安装关系 | 78amgeneralM35A2[^10] |

## 维修配件

| 完整物品 ID | 游戏显示名 / 名称状态 | 中文用途 / 类别 | 菜单 | 适用车辆与安装位置 | 来源 / 状态 |
| --- | --- | --- | --- | --- | --- |
| `Base.M35A2Door2` | 78 AM General M35A2 Door（未找到有效中文译文） | 车辆安装件，用于车门（DoorFrontLeft）、车门（DoorFrontRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.78amgeneralM35A2 → DoorFrontLeft；Base.78amgeneralM35A2 → DoorFrontRight；Base.78amgeneralM49A2C → DoorFrontLeft；Base.78amgeneralM49A2C → DoorFrontRight；Base.78amgeneralM50A3 → DoorFrontLeft；Base.78amgeneralM50A3 → DoorFrontRight；Base.78amgeneralM62 → DoorFrontLeft；Base.78amgeneralM62 → DoorFrontRight | 78amgeneralM35A2[^11] |
| `Base.M35A2EngineDoor2` | 78 AM General M35A2 Hood（未找到有效中文译文） | 车辆安装件，用于引擎盖（EngineDoor）；适用车型见右列 / 维修配件 | 添加物品 | Base.78amgeneralM35A2 → EngineDoor；Base.78amgeneralM49A2C → EngineDoor；Base.78amgeneralM50A3 → EngineDoor；Base.78amgeneralM62 → EngineDoor | 78amgeneralM35A2[^12] |
| `Base.M35A2Grille1` | 78 AM General M35A2 Grille（未找到有效中文译文） | 车辆安装件，用于车辆安装位（M35A2Grille）；适用车型见右列 / 维修配件 | 添加物品 | Base.78amgeneralM35A2 → M35A2Grille；Base.78amgeneralM49A2C → M35A2Grille；Base.78amgeneralM50A3 → M35A2Grille；Base.78amgeneralM62 → M35A2Grille | 78amgeneralM35A2[^13] |
| `Base.M35A2Mudflaps1` | 78 AM General M35A2 Mudflaps（未找到有效中文译文） | 车辆安装件，用于车辆安装位（DAMNMudflaps）；适用车型见右列 / 维修配件 | 添加物品 | Base.78amgeneralM35A2 → DAMNMudflaps；Base.78amgeneralM49A2C → DAMNMudflaps；Base.78amgeneralM50A3 → DAMNMudflaps；Base.78amgeneralM62 → DAMNMudflaps | 78amgeneralM35A2[^14] |
| `Base.M35A2Muffler1` | 78 AM General M35A2 Muffler（未找到有效中文译文） | 车辆安装件，用于消声器（Muffler）；适用车型见右列 / 维修配件 | 添加物品 | Base.78amgeneralM35A2 → Muffler；Base.78amgeneralM49A2C → Muffler；Base.78amgeneralM50A3 → Muffler；Base.78amgeneralM62 → Muffler | 78amgeneralM35A2[^15] |
| `Base.M35A2SideWindow2` | 78 AM General M35A2 Side Window（未找到有效中文译文） | 车辆安装件，用于车窗（WindowFrontLeft）、车窗（WindowFrontRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.78amgeneralM35A2 → WindowFrontLeft；Base.78amgeneralM35A2 → WindowFrontRight；Base.78amgeneralM49A2C → WindowFrontLeft；Base.78amgeneralM49A2C → WindowFrontRight；Base.78amgeneralM50A3 → WindowFrontLeft；Base.78amgeneralM50A3 → WindowFrontRight；Base.78amgeneralM62 → WindowFrontLeft；Base.78amgeneralM62 → WindowFrontRight | 78amgeneralM35A2[^16] |
| `Base.M35A2Stakes1` | 78 AM General M35A2 Stake Construction（未找到有效中文译文） | 车辆安装件，用于车辆安装位（M35A2Tarp）；适用车型见右列 / 维修配件 | 添加物品 | Base.78amgeneralM35A2 → M35A2Tarp | 78amgeneralM35A2[^17] |
| `Base.M35A2Stakes3` | 78 AM General M35A2 Stake Sidewalls（未找到有效中文译文） | 车辆安装件，用于车辆安装位（M35A2Tarp）；适用车型见右列 / 维修配件 | 添加物品 | Base.78amgeneralM35A2 → M35A2Tarp | 78amgeneralM35A2[^18] |
| `Base.M35A2Tarp2` | 78 AM General M35A2 Tarp Cover（未找到有效中文译文） | 车辆安装件，用于车辆安装位（M35A2Tarp）；适用车型见右列 / 维修配件 | 添加物品 | Base.78amgeneralM35A2 → M35A2Tarp | 78amgeneralM35A2[^19] |
| `Base.M35A2Windshield2` | 78 AM General M35A2 Windshield（未找到有效中文译文） | 车辆安装件，用于挡风玻璃（Windshield）；适用车型见右列 / 维修配件 | 添加物品 | Base.78amgeneralM35A2 → Windshield；Base.78amgeneralM49A2C → Windshield；Base.78amgeneralM50A3 → Windshield；Base.78amgeneralM62 → Windshield | 78amgeneralM35A2[^20] |
| `Base.M35A2tailgate2` | 78 AM General M35A2 Tailgate（未找到有效中文译文） | 车辆安装件，用于后备箱（TrunkDoor）；适用车型见右列 / 维修配件 | 添加物品 | Base.78amgeneralM35A2 → TrunkDoor | 78amgeneralM35A2[^21] |
| `Base.M49PumpDoor2` | 78 AM General M49/M50 Pump Doors（未找到有效中文译文） | 车辆安装件，用于后备箱（TrunkDoor）；适用车型见右列 / 维修配件 | 添加物品 | Base.78amgeneralM49A2C → TrunkDoor；Base.78amgeneralM50A3 → TrunkDoor | 78amgeneralM35A2[^22] |

## 改装配件

| 完整物品 ID | 游戏显示名 / 名称状态 | 中文用途 / 类别 | 菜单 | 适用车辆与安装位置 | 来源 / 状态 |
| --- | --- | --- | --- | --- | --- |
| `Base.M35A2Bumper1` | 78 AM General M35A2 Bumper（未找到有效中文译文） | 车辆安装件，用于保险杠（DAMNBumperFront）；适用车型见右列 / 改装配件 | 添加物品 | Base.78amgeneralM35A2 → DAMNBumperFront；Base.78amgeneralM49A2C → DAMNBumperFront；Base.78amgeneralM50A3 → DAMNBumperFront；Base.78amgeneralM62 → DAMNBumperFront | 78amgeneralM35A2[^23] |
| `Base.M35A2BumperRear1` | no（未找到有效中文译文） | 车辆安装件，用于保险杠（DAMNBumperRear）；适用车型见右列 / 改装配件 | 添加物品 | Base.78amgeneralM35A2 → DAMNBumperRear；Base.78amgeneralM49A2C → DAMNBumperRear；Base.78amgeneralM50A3 → DAMNBumperRear；Base.78amgeneralM62 → DAMNBumperRear | 78amgeneralM35A2[^24] |
| `Base.M35A2DoorArmor1` | 78 AM General M35A2 Door Armor（未找到有效中文译文） | 车辆安装件，用于防护件（DAMNFrontLeftArmor）、防护件（DAMNFrontRightArmor）；适用车型见右列 / 改装配件 | 添加物品 | Base.78amgeneralM35A2 → DAMNFrontLeftArmor；Base.78amgeneralM35A2 → DAMNFrontRightArmor；Base.78amgeneralM49A2C → DAMNFrontLeftArmor；Base.78amgeneralM49A2C → DAMNFrontRightArmor；Base.78amgeneralM50A3 → DAMNFrontLeftArmor；Base.78amgeneralM50A3 → DAMNFrontRightArmor；Base.78amgeneralM62 → DAMNFrontLeftArmor；Base.78amgeneralM62 → DAMNFrontRightArmor | 78amgeneralM35A2[^25] |
| `Base.M35A2HardCover1` | 78 AM General M35A2 Cab Hard Cover（未找到有效中文译文） | 车辆安装件，用于车辆安装位（M35A2CabCovers）；适用车型见右列 / 改装配件 | 添加物品 | Base.78amgeneralM35A2 → M35A2CabCovers；Base.78amgeneralM49A2C → M35A2CabCovers；Base.78amgeneralM50A3 → M35A2CabCovers；Base.78amgeneralM62 → M35A2CabCovers | 78amgeneralM35A2[^26] |
| `Base.M35A2SoftCover2` | 78 AM General M35A2 Cab Soft Cover（未找到有效中文译文） | 车辆安装件，用于车辆安装位（M35A2CabCovers）；适用车型见右列 / 改装配件 | 添加物品 | Base.78amgeneralM35A2 → M35A2CabCovers；Base.78amgeneralM49A2C → M35A2CabCovers；Base.78amgeneralM50A3 → M35A2CabCovers；Base.78amgeneralM62 → M35A2CabCovers | 78amgeneralM35A2[^27] |
| `Base.M35A2WindshieldArmor1` | 78 AM General M35A2 Windshield Armor（未找到有效中文译文） | 车辆安装件，用于挡风玻璃（DAMNWindshieldArmor）；适用车型见右列 / 改装配件 | 添加物品 | Base.78amgeneralM35A2 → DAMNWindshieldArmor；Base.78amgeneralM49A2C → DAMNWindshieldArmor；Base.78amgeneralM50A3 → DAMNWindshieldArmor；Base.78amgeneralM62 → DAMNWindshieldArmor | 78amgeneralM35A2[^28] |

## 共享配件

下列物品由已启用依赖或游戏原版提供，不计入本 Mod 的本地物品数。

| 完整物品 ID | 游戏显示名 / 名称状态 | 中文用途 / 类别 | 菜单 | 适用车辆与安装位置 | 来源 / 状态 |
| --- | --- | --- | --- | --- | --- |
| `Base.BigGasTank2` | 油箱 (大型)（翻译文件含非标准语法，待游戏核实）[^30] | 车辆安装件，用于油箱（GasTank）；适用车型见右列 / 维修配件 | 添加物品 | Base.78amgeneralM35A2 → GasTank；Base.78amgeneralM49A2C → GasTank；Base.78amgeneralM50A3 → GasTank；Base.78amgeneralM62 → GasTank | 游戏原版[^29] |
| `Base.CarBattery2` | 汽车电池（翻译文件含非标准语法，待游戏核实）[^32] | 车辆安装件，用于蓄电池（Battery）、蓄电池（GRHouseBattery1）、蓄电池（GRHouseBattery2）；适用车型见右列 / 维修配件 | 添加物品 | Base.78amgeneralM35A2 → Battery；Base.78amgeneralM49A2C → Battery；Base.78amgeneralM50A3 → Battery；Base.78amgeneralM62 → Battery | 游戏原版[^31] |
| `Base.GloveBox2` | 手套箱（翻译文件含非标准语法，待游戏核实）[^34] | 车辆安装件，用于车辆安装位（GloveBox）；适用车型见右列 / 维修配件 | 添加物品 | Base.78amgeneralM35A2 → GloveBox；Base.78amgeneralM49A2C → GloveBox；Base.78amgeneralM50A3 → GloveBox；Base.78amgeneralM62 → GloveBox | 游戏原版[^33] |
| `Base.HamRadio1` | 微型导航仪 / 收音机 (业余电台) / 民用无线电台 (昂科) / 民用无线电台 - 昂科公司（译文冲突，待游戏核实）[^36] | 车辆安装件，用于车辆安装位（Radio）；适用车型见右列 / 维修配件 | 添加物品 | Base.78amgeneralM35A2 → Radio；Base.78amgeneralM49A2C → Radio；Base.78amgeneralM50A3 → Radio；Base.78amgeneralM62 → Radio | 游戏原版[^35] |
| `Base.HamRadio2` | 收音机 (军用) / 军用无线电台（译文冲突，待游戏核实）[^38] | 车辆安装件，用于车辆安装位（Radio）；适用车型见右列 / 维修配件 | 添加物品 | Base.78amgeneralM35A2 → Radio；Base.78amgeneralM49A2C → Radio；Base.78amgeneralM50A3 → Radio；Base.78amgeneralM62 → Radio | 游戏原版[^37] |
| `Base.HamRadioMakeShift` | 收音机 (简易业余无线电) / 收音机 (简易业余电台) / 自制无线电台（译文冲突，待游戏核实）[^40] | 车辆安装件，用于车辆安装位（Radio）；适用车型见右列 / 维修配件 | 添加物品 | Base.78amgeneralM35A2 → Radio；Base.78amgeneralM49A2C → Radio；Base.78amgeneralM50A3 → Radio；Base.78amgeneralM62 → Radio | 游戏原版[^39] |
| `Base.LightBulb` | 灯泡-白色 / 灯泡 (白)（译文冲突，待游戏核实）[^42] | 车辆安装件，用于车灯（Headlight*）、车灯（JP82DorothyLights）；适用车型见右列 / 维修配件 | 添加物品 | Base.78amgeneralM35A2 → Headlight*；Base.78amgeneralM49A2C → Headlight*；Base.78amgeneralM50A3 → Headlight*；Base.78amgeneralM62 → Headlight* | 游戏原版[^41] |
| `Base.ModernBrake2` | 制动器 (高级)（翻译文件含非标准语法，待游戏核实）[^44] | 车辆安装件，用于制动器（Brake*）；适用车型见右列 / 维修配件 | 添加物品 | Base.78amgeneralM35A2 → Brake*；Base.78amgeneralM49A2C → Brake*；Base.78amgeneralM50A3 → Brake*；Base.78amgeneralM62 → Brake* | 游戏原版[^43] |
| `Base.ModernSuspension2` | 悬挂 (高级)（翻译文件含非标准语法，待游戏核实）[^46] | 车辆安装件，用于悬挂（Suspension*）；适用车型见右列 / 维修配件 | 添加物品 | Base.78amgeneralM35A2 → Suspension*；Base.78amgeneralM49A2C → Suspension*；Base.78amgeneralM50A3 → Suspension*；Base.78amgeneralM62 → Suspension* | 游戏原版[^45] |
| `Base.NormalBrake2` | 制动器 (普通)（翻译文件含非标准语法，待游戏核实）[^48] | 车辆安装件，用于制动器（Brake*）；适用车型见右列 / 维修配件 | 添加物品 | Base.78amgeneralM35A2 → Brake*；Base.78amgeneralM49A2C → Brake*；Base.78amgeneralM50A3 → Brake*；Base.78amgeneralM62 → Brake* | 游戏原版[^47] |
| `Base.NormalGasTank2` | 油箱 (标准)（翻译文件含非标准语法，待游戏核实）[^50] | 车辆安装件，用于油箱（GasTank）；适用车型见右列 / 维修配件 | 添加物品 | Base.78amgeneralM35A2 → GasTank；Base.78amgeneralM49A2C → GasTank；Base.78amgeneralM50A3 → GasTank；Base.78amgeneralM62 → GasTank | 游戏原版[^49] |
| `Base.NormalSuspension2` | 悬挂 (普通)（翻译文件含非标准语法，待游戏核实）[^52] | 车辆安装件，用于悬挂（Suspension*）；适用车型见右列 / 维修配件 | 添加物品 | Base.78amgeneralM35A2 → Suspension*；Base.78amgeneralM49A2C → Suspension*；Base.78amgeneralM50A3 → Suspension*；Base.78amgeneralM62 → Suspension* | 游戏原版[^51] |
| `Base.OldBrake2` | 制动器 (老式)（翻译文件含非标准语法，待游戏核实）[^54] | 车辆安装件，用于制动器（Brake*）；适用车型见右列 / 维修配件 | 添加物品 | Base.78amgeneralM35A2 → Brake*；Base.78amgeneralM49A2C → Brake*；Base.78amgeneralM50A3 → Brake*；Base.78amgeneralM62 → Brake* | 游戏原版[^53] |
| `Base.SmallGasTank2` | 油箱 (小型)（翻译文件含非标准语法，待游戏核实）[^56] | 车辆安装件，用于油箱（GasTank）；适用车型见右列 / 维修配件 | 添加物品 | Base.78amgeneralM35A2 → GasTank；Base.78amgeneralM49A2C → GasTank；Base.78amgeneralM50A3 → GasTank；Base.78amgeneralM62 → GasTank | 游戏原版[^55] |
| `USMIL.Seat0` | Military Vehicle Seat ST1（未找到有效中文译文） | 车辆安装件，用于座椅（Seat*）、座椅（SeatFrontLeft）、座椅（SeatFrontRight）、座椅（SeatFront*）、座椅（SeatMiddleLeft）；适用车型见右列 / 维修配件 | 添加物品 | Base.78amgeneralM35A2 → SeatFront*；Base.78amgeneralM49A2C → SeatFront*；Base.78amgeneralM50A3 → SeatFront*；Base.78amgeneralM62 → SeatFront* | damnlib[^57] |
| `runFlat.Medium4TireAxle` | RunFlat Medium 4 Tire Axle（未找到有效中文译文） | 车辆安装件，用于轮胎（TireRear*）；适用车型见右列 / 维修配件 | 添加物品 | Base.78amgeneralM35A2 → TireRear*；Base.78amgeneralM49A2C → TireRear*；Base.78amgeneralM50A3 → TireRear*；Base.78amgeneralM62 → TireRear* | damnlib[^58] |
| `runFlat.MediumTire` | RunFlat Medium Tire（未找到有效中文译文） | 车辆安装件，用于轮胎（TireFront*）、轮胎（DAMNSpareTire）；适用车型见右列 / 维修配件 | 添加物品 | Base.78amgeneralM35A2 → TireFront*；Base.78amgeneralM35A2 → DAMNSpareTire；Base.78amgeneralM49A2C → TireFront*；Base.78amgeneralM49A2C → DAMNSpareTire；Base.78amgeneralM50A3 → TireFront*；Base.78amgeneralM50A3 → DAMNSpareTire；Base.78amgeneralM62 → TireFront*；Base.78amgeneralM62 → DAMNSpareTire | damnlib[^59] |

## 制作配方

| 配方完整 ID（排查用） | 游戏配方名 / 名称状态 | 中文用途 | 菜单 | 来源 |
| --- | --- | --- | --- | --- |
| `Base.78amgeneralM35A2MakeBedStakes` | Make 78 AM General M35A2 Bed Stakes（未找到有效中文译文）[^60] | 制作产出：78 AM General M35A2 Stake Sidewalls（车辆安装件，用于车辆安装位（M35A2Tarp）；适用车型见右列） | 制作界面 | [^61] |
| `Base.78amgeneralM35A2MakeBedStakesConstruction` | Make 78 AM General M35A2 Bed Stakes Construction（未找到有效中文译文）[^62] | 制作产出：78 AM General M35A2 Stake Construction（车辆安装件，用于车辆安装位（M35A2Tarp）；适用车型见右列） | 制作界面 | [^63] |
| `Base.78amgeneralM35A2MakeFrontBumper` | Make 78 AM General M35A2 Front Bumper（未找到有效中文译文）[^64] | 制作产出：78 AM General M35A2 Bumper（车辆安装件，用于保险杠（DAMNBumperFront）；适用车型见右列） | 制作界面 | [^65] |
| `Base.78amgeneralM35A2MakeFrontDoor` | Make 78 AM General M35A2 Front Door（未找到有效中文译文）[^66] | 制作产出：78 AM General M35A2 Door（车辆安装件，用于车门（DoorFrontLeft）、车门（DoorFrontRight）；适用车型见右列） | 制作界面 | [^67] |
| `Base.78amgeneralM35A2MakeFrontGrille` | Make 78 AM General M35A2 Front Grille（未找到有效中文译文）[^68] | 制作产出：78 AM General M35A2 Grille（车辆安装件，用于车辆安装位（M35A2Grille）；适用车型见右列） | 制作界面 | [^69] |
| `Base.78amgeneralM35A2MakeFrontSideWindow` | Make 78 AM General M35A2 Front Side Window（未找到有效中文译文）[^70] | 制作产出：78 AM General M35A2 Side Window（车辆安装件，用于车窗（WindowFrontLeft）、车窗（WindowFrontRight）；适用车型见右列） | 制作界面 | [^71] |
| `Base.78amgeneralM35A2MakeFrontWindowArmor` | Make 78 AM General M35A2 Front Window Armor（未找到有效中文译文）[^72] | 制作产出：78 AM General M35A2 Door Armor（车辆安装件，用于防护件（DAMNFrontLeftArmor）、防护件（DAMNFrontRightArmor）；适用车型见右列） | 制作界面 | [^73] |
| `Base.78amgeneralM35A2MakeFrontWindshield` | Make 78 AM General M35A2 Front Windshield（未找到有效中文译文）[^74] | 制作产出：78 AM General M35A2 Windshield（车辆安装件，用于挡风玻璃（Windshield）；适用车型见右列） | 制作界面 | [^75] |
| `Base.78amgeneralM35A2MakeFrontWindshieldArmor` | Make 78 AM General M35A2 Front Windshield Armor（未找到有效中文译文）[^76] | 制作产出：78 AM General M35A2 Windshield Armor（车辆安装件，用于挡风玻璃（DAMNWindshieldArmor）；适用车型见右列） | 制作界面 | [^77] |
| `Base.78amgeneralM35A2MakeHardCabCover` | Make 78 AM General M35A2 Hard Cab Cover（未找到有效中文译文）[^78] | 制作产出：78 AM General M35A2 Cab Hard Cover（车辆安装件，用于车辆安装位（M35A2CabCovers）；适用车型见右列） | 制作界面 | [^79] |
| `Base.78amgeneralM35A2MakeHood` | Make 78 AM General M35A2 Hood（未找到有效中文译文）[^80] | 制作产出：78 AM General M35A2 Hood（车辆安装件，用于引擎盖（EngineDoor）；适用车型见右列） | 制作界面 | [^81] |
| `Base.78amgeneralM35A2MakeMudflaps` | Make 78 AM General M35A2 Mudflaps（未找到有效中文译文）[^82] | 制作产出：78 AM General M35A2 Mudflaps（车辆安装件，用于车辆安装位（DAMNMudflaps）；适用车型见右列） | 制作界面 | [^83] |
| `Base.78amgeneralM35A2MakeMuffler` | Make 78 AM General M35A2 Muffler（未找到有效中文译文）[^84] | 制作产出：78 AM General M35A2 Muffler（车辆安装件，用于消声器（Muffler）；适用车型见右列） | 制作界面 | [^85] |
| `Base.78amgeneralM35A2MakeSoftBedCover` | Make 78 AM General M35A2 Bed Cover（未找到有效中文译文）[^86] | 制作产出：78 AM General M35A2 Tarp Cover（车辆安装件，用于车辆安装位（M35A2Tarp）；适用车型见右列） | 制作界面 | [^87] |
| `Base.78amgeneralM35A2MakeSoftCabCover` | Make 78 AM General M35A2 Soft Cab Cover（未找到有效中文译文）[^88] | 制作产出：78 AM General M35A2 Cab Soft Cover（车辆安装件，用于车辆安装位（M35A2CabCovers）；适用车型见右列） | 制作界面 | [^89] |
| `Base.78amgeneralM35A2MakeTailgate` | Make 78 AM General M35A2 Tailgate（未找到有效中文译文）[^90] | 制作产出：78 AM General M35A2 Tailgate（车辆安装件，用于后备箱（TrunkDoor）；适用车型见右列） | 制作界面 | [^91] |
| `Base.78amgeneralM35A2MakeTrunkLid` | Make 78 AM General M49/M50 Pump Doors（未找到有效中文译文）[^92] | 制作产出：78 AM General M49/M50 Pump Doors（车辆安装件，用于后备箱（TrunkDoor）；适用车型见右列） | 制作界面 | [^93] |

## 内部定义、历史分支与未解析引用

有效资源层：42.13, common；仅合并 common 与所选版本，Overlay 按相对路径覆盖。
车辆模板 20 个、内部槽位 59 个，均不算整车或背包物品。旧根目录和未选中版本的定义不列入当前可用表。模板中短物品引用若追加机修类型后缀才匹配定义，属于静态映射，安装仍待实测。

内部或过时的 item 定义单列于此，不在上面的背包刷取建议中；它们仍计入各自来源的定义数量。

| 保留定义 ID（不作正常刷取建议） | 脚本显示名 | 中文说明 / 状态 | 来源 |
| --- | --- | --- | --- |
| `damnCraft.Trunk2` | no | 车辆后备箱的内部容量载体，关联车辆槽位与容积状态；不是可携带的旅行箱；显示名 no、图标 na；不作正常刷取建议 | [^94] |

<details><summary>查看内部槽位（不能直接刷取）</summary>

| 槽位 | 名称或说明 | 来源 |
| --- | --- | --- |
| `Battery` | 电池 / 蓄电池 | [^95] |
| `Brake*` | Brake* / 制动器 | [^96] |
| `BrakeFrontLeft` | 左前制动 / 制动器 | [^97] |
| `BrakeFrontRight` | 右前制动 / 制动器 | [^98] |
| `BrakeRearLeft` | 左后制动 / 制动器 | [^99] |
| `BrakeRearRight` | 右后制动 / 制动器 | [^100] |
| `CTIsystem` | CTIsystem / 车辆安装位 | [^101] |
| `DAMNBumperFront` | 前保险杠 / 保险杠 | [^102] |
| `DAMNBumperRear` | 后保险杠 / 保险杠 | [^103] |
| `DAMNFront*` | DAMNFront* / 车辆安装位 | [^104] |
| `DAMNFrontLeftArmor` | 左前车窗装甲 / 防护件 | [^105] |
| `DAMNFrontRightArmor` | 右前车窗装甲 / 防护件 | [^106] |
| `DAMNGunrack` | 枪架 / 枪架 | [^107] |
| `DAMNMudflaps` | 挡泥板 / 车辆安装位 | [^108] |
| `DAMNSpareTire` | 备胎 / 轮胎 | [^109] |
| `DAMNWindshieldArmor` | 挡风玻璃装甲 / 挡风玻璃 | [^110] |
| `Door*` | Door* / 车门 | [^111] |
| `DoorFrontLeft` | 左前门 / 车门 | [^112] |
| `DoorFrontRight` | 右前门 / 车门 | [^113] |
| `Engine` | 引擎 / 发动机 | [^114] |
| `EngineDoor` | 引擎盖 / 引擎盖 | [^115] |
| `GasTank` | 油箱 / 油箱 | [^116] |
| `GloveBox` | 手套箱 / 车辆安装位 | [^117] |
| `Headlight*` | Headlight* / 车灯 | [^118] |
| `HeadlightLeft` | 左大灯 / 车灯 | [^119] |
| `HeadlightRearLeft` | 左尾灯 / 车灯 | [^120] |
| `HeadlightRearRight` | 右尾灯 / 车灯 | [^121] |
| `HeadlightRight` | 右大灯 / 车灯 | [^122] |
| `Heater` | 加热器 / 车辆安装位 | [^123] |
| `M35A2CabCovers` | Cab Cover / 车辆安装位 | [^124] |
| `M35A2Grille` | Front Grille / 车辆安装位 | [^125] |
| `M35A2Tarp` | Flatbed Cover / 车辆安装位 | [^126] |
| `M35A2Trunk` | Flatbed Storage / 后备箱 | [^127] |
| `M49A2CTrunk` | Pump Compartment Storage / 后备箱 | [^128] |
| `Muffler` | 排气消声器 / 消声器 | [^129] |
| `PassengerCompartment` | 乘员舱 / 车辆安装位 | [^130] |
| `RFsystem` | RFsystem / 车辆安装位 | [^131] |
| `Radio` | 电台 / 车辆安装位 | [^132] |
| `SeatFront*` | SeatFront* / 座椅 | [^133] |
| `SeatFrontLeft` | 驾驶座 / 座椅 | [^134] |
| `SeatFrontRight` | 右前座 / 座椅 | [^135] |
| `Suspension*` | Suspension* / 悬挂 | [^136] |
| `SuspensionFrontLeft` | 左前悬挂 / 悬挂 | [^137] |
| `SuspensionFrontRight` | 右前悬挂 / 悬挂 | [^138] |
| `SuspensionRearLeft` | 左后悬挂 / 悬挂 | [^139] |
| `SuspensionRearRight` | 右后悬挂 / 悬挂 | [^140] |
| `TireFront*` | TireFront* / 轮胎 | [^141] |
| `TireFrontLeft` | 左前胎 / 轮胎 | [^142] |
| `TireFrontRight` | 右前胎 / 轮胎 | [^143] |
| `TireRear*` | TireRear* / 轮胎 | [^144] |
| `TireRearLeft` | 左后胎 / 轮胎 | [^145] |
| `TireRearRight` | 右后胎 / 轮胎 | [^146] |
| `TruckBed` | 补给箱 / 行李箱 / 车辆安装位 | [^147] |
| `TrunkDoor` | 后车盖 / 后备箱 | [^148] |
| `Window*` | Window* / 车窗 | [^149] |
| `WindowFrontLeft` | 左前窗 / 车窗 | [^150] |
| `WindowFrontRight` | 右前窗 / 车窗 | [^151] |
| `Windshield` | 挡风玻璃 / 挡风玻璃 | [^152] |
| `airBrake` | airBrake / 制动器 | [^153] |

</details>


## 概览

| Mod ID / 文件夹 | 分发端 | 版本 | 选择的 mod.info | 原件范围 → 当前范围 |
| --- | --- | --- | --- | --- |
| `78amgeneralM35A2` / `78amgeneralM35A2` | both（双端） | 未标注 | `42.13/mod.info` | 42.13.0 … - → 42.13.0 … - |

原件体积 28.6 MB；体积按完整目录统计，与当前内容定义数分开。
工作坊：[查看作者页面](https://steamcommunity.com/sharedfiles/filedetails/?id=2799152995)。

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

require damnlib；45 个脚本物品、5 个载具脚本、20 条配方；当前包 30.0 MB，变体子 mod 未启用。

```
cd A004
python lab.py check --profile b422-compat
grep -a '78amgeneralM35A2' runs/<trial>/*console.log
```
<!-- retained:end -->

## 静态来源

路径相对 `A004/workspace/mods_library/`；`Overlay/<文件夹>/` 指 `A004/workspace/patches/mods/<文件夹>/`，`游戏原版/` 指当前 B42.22 客户端 Game 目录。翻译来源列出所有候选，未按加载顺序擅自消解异文。

[^1]: `2799152995/mods/78amgeneralM35A2/common/media/lua/shared/Translate/EN/IG_UI.json:3`；`2799152995/mods/78amgeneralM35A2/42.13/media/lua/shared/Translate/EN/IG_UI_EN.txt:2`
[^2]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2.txt:61`
[^3]: `2799152995/mods/78amgeneralM35A2/common/media/lua/shared/Translate/EN/IG_UI.json:4`；`2799152995/mods/78amgeneralM35A2/42.13/media/lua/shared/Translate/EN/IG_UI_EN.txt:3`
[^4]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM49A2C.txt:17`
[^5]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/IG_UI.json:20063`
[^6]: `2799152995/mods/78amgeneralM35A2/common/media/lua/shared/Translate/EN/IG_UI.json:5`；`2799152995/mods/78amgeneralM35A2/42.13/media/lua/shared/Translate/EN/IG_UI_EN.txt:4`
[^7]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM50A3.txt:17`
[^8]: `2799152995/mods/78amgeneralM35A2/common/media/lua/shared/Translate/EN/IG_UI.json:6`；`2799152995/mods/78amgeneralM35A2/42.13/media/lua/shared/Translate/EN/IG_UI_EN.txt:5`
[^9]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM62.txt:17`
[^10]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2_vehiclesitems.txt:5`
[^11]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2_vehiclesitems.txt:225`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_doors.txt:25`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_doors.txt:82`
[^12]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2_vehiclesitems.txt:42`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_hood.txt:14`
[^13]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2_vehiclesitems.txt:135`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_grille.txt:12`
[^14]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2_vehiclesitems.txt:273`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_mudflaps.txt:12`
[^15]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2_vehiclesitems.txt:22`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_mufflers.txt:14`
[^16]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2_vehiclesitems.txt:208`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_windows.txt:24`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_windows.txt:51`
[^17]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2_vehiclesitems.txt:59`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_tarps.txt:27`
[^18]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2_vehiclesitems.txt:87`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_tarps.txt:27`
[^19]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2_vehiclesitems.txt:73`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_tarps.txt:27`
[^20]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2_vehiclesitems.txt:193`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_windshield.txt:14`
[^21]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2_vehiclesitems.txt:103`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_trunkdoor.txt:22`
[^22]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2_vehiclesitems.txt:290`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_trunkdoor.txt:148`
[^23]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2_vehiclesitems.txt:120`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_bumpers.txt:12`
[^24]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2_vehiclesitems.txt:149`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_bumpers.txt:74`
[^25]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2_vehiclesitems.txt:256`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_armor.txt:97`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_armor.txt:118`
[^26]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2_vehiclesitems.txt:162`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_cab_covers.txt:19`
[^27]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2_vehiclesitems.txt:176`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_cab_covers.txt:19`
[^28]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2_vehiclesitems.txt:241`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_armor.txt:31`
[^29]: `游戏原版/media/scripts/generated/items/normal.txt:12408`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2.txt:311`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM49A2C.txt:267`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM50A3.txt:272`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM62.txt:277`
[^30]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:448`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:163`
[^31]: `游戏原版/media/scripts/generated/items/drainable.txt:2368`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2.txt:342`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM49A2C.txt:298`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM50A3.txt:303`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM62.txt:308`
[^32]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:970`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:380`
[^33]: `游戏原版/media/scripts/generated/items/normal.txt:13025`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2.txt:275`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM49A2C.txt:231`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM50A3.txt:236`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM62.txt:241`
[^34]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1776`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:687`
[^35]: `游戏原版/media/scripts/generated/items/radio.txt:203`；`游戏原版/media/scripts/generated/vehicles/template_radio_HAM.txt:5`
[^36]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:3000`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25094`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1908`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:3486`
[^37]: `游戏原版/media/scripts/generated/items/radio.txt:229`；`游戏原版/media/scripts/generated/vehicles/template_radio_HAM.txt:5`
[^38]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:7376`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25095`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1909`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:3487`
[^39]: `游戏原版/media/scripts/generated/items/radio.txt:255`；`游戏原版/media/scripts/generated/vehicles/template_radio_HAM.txt:5`
[^40]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:7377`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25096`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1910`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:3488`
[^41]: `游戏原版/media/scripts/generated/items/normal.txt:4661`；`游戏原版/media/scripts/generated/vehicles/template_headlight.txt:25`
[^42]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:6727`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25103`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2563`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:965`
[^43]: `游戏原版/media/scripts/generated/items/normal.txt:12163`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2.txt:405`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM49A2C.txt:360`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM50A3.txt:365`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM62.txt:369`
[^44]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2780`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1050`
[^45]: `游戏原版/media/scripts/generated/items/normal.txt:12282`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2.txt:422`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM49A2C.txt:377`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM50A3.txt:382`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM62.txt:386`
[^46]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2786`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1056`
[^47]: `游戏原版/media/scripts/generated/items/normal.txt:12146`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2.txt:405`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM49A2C.txt:360`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM50A3.txt:365`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM62.txt:369`
[^48]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3219`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1135`
[^49]: `游戏原版/media/scripts/generated/items/normal.txt:12393`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2.txt:311`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM49A2C.txt:267`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM50A3.txt:272`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM62.txt:277`
[^50]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3228`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1144`
[^51]: `游戏原版/media/scripts/generated/items/normal.txt:12265`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2.txt:422`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM49A2C.txt:377`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM50A3.txt:382`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM62.txt:386`
[^52]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3231`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1147`
[^53]: `游戏原版/media/scripts/generated/items/normal.txt:12129`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2.txt:405`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM49A2C.txt:360`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM50A3.txt:365`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM62.txt:369`
[^54]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3255`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1165`
[^55]: `游戏原版/media/scripts/generated/items/normal.txt:12378`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2.txt:311`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM49A2C.txt:267`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM50A3.txt:272`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM62.txt:277`
[^56]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:4152`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1543`
[^57]: `3171167894/mods/damnlib/42.20/media/scripts/USMIL/items_USMIL.txt:6`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_seats.txt:57`
[^58]: `3171167894/mods/damnlib/42.20/media/scripts/runFlat/items_runFlat.txt:121`；`3171167894/mods/damnlib/42.20/media/scripts/runFlat/template_runFlatsMedium4AxleRear.txt:28`
[^59]: `3171167894/mods/damnlib/42.20/media/scripts/runFlat/items_runFlat.txt:98`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_armored_tire.txt:7`；`2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_sparetire.txt:5`
[^60]: `2799152995/mods/78amgeneralM35A2/common/media/lua/shared/Translate/EN/Recipes.json:16`；`2799152995/mods/78amgeneralM35A2/42.13/media/lua/shared/Translate/EN/Recipes_EN.txt:15`
[^61]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2_recipes.txt:304`
[^62]: `2799152995/mods/78amgeneralM35A2/common/media/lua/shared/Translate/EN/Recipes.json:14`；`2799152995/mods/78amgeneralM35A2/42.13/media/lua/shared/Translate/EN/Recipes_EN.txt:13`
[^63]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2_recipes.txt:259`
[^64]: `2799152995/mods/78amgeneralM35A2/common/media/lua/shared/Translate/EN/Recipes.json:11`；`2799152995/mods/78amgeneralM35A2/42.13/media/lua/shared/Translate/EN/Recipes_EN.txt:10`
[^65]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2_recipes.txt:192`
[^66]: `2799152995/mods/78amgeneralM35A2/common/media/lua/shared/Translate/EN/Recipes.json:4`；`2799152995/mods/78amgeneralM35A2/42.13/media/lua/shared/Translate/EN/Recipes_EN.txt:3`
[^67]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2_recipes.txt:27`
[^68]: `2799152995/mods/78amgeneralM35A2/common/media/lua/shared/Translate/EN/Recipes.json:12`；`2799152995/mods/78amgeneralM35A2/42.13/media/lua/shared/Translate/EN/Recipes_EN.txt:11`
[^69]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2_recipes.txt:215`
[^70]: `2799152995/mods/78amgeneralM35A2/common/media/lua/shared/Translate/EN/Recipes.json:8`；`2799152995/mods/78amgeneralM35A2/42.13/media/lua/shared/Translate/EN/Recipes_EN.txt:7`
[^71]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2_recipes.txt:125`
[^72]: `2799152995/mods/78amgeneralM35A2/common/media/lua/shared/Translate/EN/Recipes.json:10`；`2799152995/mods/78amgeneralM35A2/42.13/media/lua/shared/Translate/EN/Recipes_EN.txt:9`
[^73]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2_recipes.txt:170`
[^74]: `2799152995/mods/78amgeneralM35A2/common/media/lua/shared/Translate/EN/Recipes.json:7`；`2799152995/mods/78amgeneralM35A2/42.13/media/lua/shared/Translate/EN/Recipes_EN.txt:6`
[^75]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2_recipes.txt:103`
[^76]: `2799152995/mods/78amgeneralM35A2/common/media/lua/shared/Translate/EN/Recipes.json:9`；`2799152995/mods/78amgeneralM35A2/42.13/media/lua/shared/Translate/EN/Recipes_EN.txt:8`
[^77]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2_recipes.txt:147`
[^78]: `2799152995/mods/78amgeneralM35A2/common/media/lua/shared/Translate/EN/Recipes.json:18`；`2799152995/mods/78amgeneralM35A2/42.13/media/lua/shared/Translate/EN/Recipes_EN.txt:17`
[^79]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2_recipes.txt:350`
[^80]: `2799152995/mods/78amgeneralM35A2/common/media/lua/shared/Translate/EN/Recipes.json:3`；`2799152995/mods/78amgeneralM35A2/42.13/media/lua/shared/Translate/EN/Recipes_EN.txt:2`
[^81]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2_recipes.txt:3`
[^82]: `2799152995/mods/78amgeneralM35A2/common/media/lua/shared/Translate/EN/Recipes.json:13`；`2799152995/mods/78amgeneralM35A2/42.13/media/lua/shared/Translate/EN/Recipes_EN.txt:12`
[^83]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2_recipes.txt:237`
[^84]: `2799152995/mods/78amgeneralM35A2/common/media/lua/shared/Translate/EN/Recipes.json:17`；`2799152995/mods/78amgeneralM35A2/42.13/media/lua/shared/Translate/EN/Recipes_EN.txt:16`
[^85]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2_recipes.txt:327`
[^86]: `2799152995/mods/78amgeneralM35A2/common/media/lua/shared/Translate/EN/Recipes.json:15`；`2799152995/mods/78amgeneralM35A2/42.13/media/lua/shared/Translate/EN/Recipes_EN.txt:14`
[^87]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2_recipes.txt:282`
[^88]: `2799152995/mods/78amgeneralM35A2/common/media/lua/shared/Translate/EN/Recipes.json:19`；`2799152995/mods/78amgeneralM35A2/42.13/media/lua/shared/Translate/EN/Recipes_EN.txt:18`
[^89]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2_recipes.txt:373`
[^90]: `2799152995/mods/78amgeneralM35A2/common/media/lua/shared/Translate/EN/Recipes.json:5`；`2799152995/mods/78amgeneralM35A2/42.13/media/lua/shared/Translate/EN/Recipes_EN.txt:4`
[^91]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2_recipes.txt:53`
[^92]: `2799152995/mods/78amgeneralM35A2/common/media/lua/shared/Translate/EN/Recipes.json:6`；`2799152995/mods/78amgeneralM35A2/42.13/media/lua/shared/Translate/EN/Recipes_EN.txt:5`
[^93]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2_recipes.txt:78`
[^94]: `3171167894/mods/damnlib/42.20/media/scripts/damnCraft/items_damnCraft.txt:572`
[^95]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2.txt:342`
[^96]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2.txt:405`
[^97]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:5`
[^98]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:18`
[^99]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:31`
[^100]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:44`
[^101]: `3171167894/mods/damnlib/42.20/media/scripts/CTIsystem/template_centralTireInflation.txt:5`
[^102]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_bumpers.txt:12`
[^103]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_bumpers.txt:74`
[^104]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_armor.txt:139`
[^105]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_armor.txt:97`
[^106]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_armor.txt:118`
[^107]: `3171167894/mods/damnlib/42.20/media/scripts/commonItems/template_DAMN_gunrack.txt:5`
[^108]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_mudflaps.txt:12`
[^109]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_sparetire.txt:5`
[^110]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_armor.txt:31`
[^111]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_doors.txt:139`
[^112]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_doors.txt:25`
[^113]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_doors.txt:82`
[^114]: `游戏原版/media/scripts/generated/vehicles/template_engine.txt:5`
[^115]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_hood.txt:14`
[^116]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2.txt:311`
[^117]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2.txt:275`
[^118]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:25`
[^119]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:5`
[^120]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:15`
[^121]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:20`
[^122]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:10`
[^123]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2.txt:355`
[^124]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_cab_covers.txt:19`
[^125]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_grille.txt:12`
[^126]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_tarps.txt:27`
[^127]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2.txt:386`
[^128]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM49A2C.txt:348`
[^129]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_mufflers.txt:14`
[^130]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2.txt:365`
[^131]: `3171167894/mods/damnlib/42.20/media/scripts/runFlat/template_runFlatTires.txt:5`
[^132]: `游戏原版/media/scripts/generated/vehicles/template_radio_HAM.txt:5`
[^133]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_seats.txt:57`
[^134]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_seats.txt:21`
[^135]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_seats.txt:39`
[^136]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/78amgeneralM35A2.txt:422`
[^137]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:5`
[^138]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:18`
[^139]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:31`
[^140]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:44`
[^141]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_armored_tire.txt:7`
[^142]: `3171167894/mods/damnlib/42.20/media/scripts/runFlat/template_runFlatsMediumFront.txt:7`
[^143]: `3171167894/mods/damnlib/42.20/media/scripts/runFlat/template_runFlatsMediumFront.txt:22`
[^144]: `3171167894/mods/damnlib/42.20/media/scripts/runFlat/template_runFlatsMedium4AxleRear.txt:28`
[^145]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_4tire_axle.txt:7`
[^146]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_4tire_axle.txt:16`
[^147]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_trunk.txt:23`
[^148]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_trunkdoor.txt:22`
[^149]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_windows.txt:78`
[^150]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_windows.txt:24`
[^151]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_windows.txt:51`
[^152]: `2799152995/mods/78amgeneralM35A2/42.13/media/scripts/vehicles/template_M35A2_windshield.txt:14`
[^153]: `3171167894/mods/damnlib/42.20/media/scripts/airBrake/template_airBrake.txt:5`
