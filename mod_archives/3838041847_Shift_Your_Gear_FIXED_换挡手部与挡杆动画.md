# 换挡动画（Shift Your Gear (FIXED)）

给原版车加挡杆动作：角色伸手握杆、按 1-5 挡/空挡/倒挡做换挡手势；挡杆在靠近车辆与副驾视角可见。作者说明这是纯视觉 mod，动力、齿比、操控都不变。标注"FIXED"是因为原版由 Dato 2 制作，这个分支适配其它游戏版本。

归属：**日常组合（玩法待验收）**；档案视图 `b422-compat`。
当前版本定义：**整车 26、本地物品定义 0、配方 0**；另引用共享物品 87。本地定义数含内部保留项，见独立列表；整车定义包括覆盖原版的条目，不等于新增车型数。

## 如何查找

- **生成整车**：在生成车辆菜单搜索下表完整 ID；显示译名时搜索中文列。联机管理命令用 `/addvehicle 完整ID`。
- **添加到背包**：普通物品、维修件、改装件都在添加物品菜单使用完整物品 ID；不要拿配方或内部槽位去刷车。
- **制作配方**：在制作界面查译名；配方 ID 用于排查，不是可放进背包的物品。
- 中文解释说明用途；只有翻译文件中找到的文字才称为游戏中文名。缺译保留脚本显示名，冲突列出各译文。

## 整车

| 完整生成车辆 ID | 当前中文名 / 名称状态 | 英文名或脚本名 | 变体说明 | 来源 |
| --- | --- | --- | --- | --- |
| `Base.GSA_CarNormalStandardGearbox` | GSA_CarNormalStandardGearbox（未找到有效中文译文） | GSA_CarNormalStandardGearbox | ；；具体外观与性能待游戏实刷 | [^1] |
| `Base.GSA_Fleet_CarLuxury` | GSA_Fleet_CarLuxury（未找到有效中文译文） | GSA_Fleet_CarLuxury | ；；具体外观与性能待游戏实刷 | [^2] |
| `Base.GSA_Fleet_CarStationWagon` | GSA_Fleet_CarStationWagon（未找到有效中文译文） | GSA_Fleet_CarStationWagon | ；；具体外观与性能待游戏实刷 | [^3] |
| `Base.GSA_Fleet_CarStationWagon2` | GSA_Fleet_CarStationWagon2（未找到有效中文译文） | GSA_Fleet_CarStationWagon2 | ；；具体外观与性能待游戏实刷 | [^4] |
| `Base.GSA_Fleet_RaceCar12` | GSA_Fleet_RaceCar12（未找到有效中文译文） | GSA_Fleet_RaceCar12 | ；；具体外观与性能待游戏实刷 | [^5] |
| `Base.GSA_Fleet_SmallCar02` | GSA_Fleet_SmallCar02（未找到有效中文译文） | GSA_Fleet_SmallCar02 | ；；具体外观与性能待游戏实刷 | [^6] |
| `Base.GSA_Fleet_SportsCar` | GSA_Fleet_SportsCar（未找到有效中文译文） | GSA_Fleet_SportsCar | 脚本座位数 2；机修类型 3；具体外观与性能待游戏实刷 | [^7] |
| `Base.GSA_Fleet_SportsCar_ez` | GSA_Fleet_SportsCar_ez（未找到有效中文译文） | GSA_Fleet_SportsCar_ez | 脚本座位数 2；机修类型 3；具体外观与性能待游戏实刷 | [^8] |
| `Base.GSA_HeavyCabin01` | GSA_HeavyCabin01（未找到有效中文译文） | GSA_HeavyCabin01 | ；；具体外观与性能待游戏实刷 | [^9] |
| `Base.GSA_HeavyCabin03` | GSA_HeavyCabin03（未找到有效中文译文） | GSA_HeavyCabin03 | 脚本座位数 2；机修类型 2；具体外观与性能待游戏实刷 | [^10] |
| `Base.GSA_HeavyCabin04` | GSA_HeavyCabin04（未找到有效中文译文） | GSA_HeavyCabin04 | ；；具体外观与性能待游戏实刷 | [^11] |
| `Base.GSA_HeavyCabin05` | GSA_HeavyCabin05（未找到有效中文译文） | GSA_HeavyCabin05 | ；；具体外观与性能待游戏实刷 | [^12] |
| `Base.GSA_HeavyCabin06` | GSA_HeavyCabin06（未找到有效中文译文） | GSA_HeavyCabin06 | ；；具体外观与性能待游戏实刷 | [^13] |
| `Base.GSA_HeavyCabin07` | GSA_HeavyCabin07（未找到有效中文译文） | GSA_HeavyCabin07 | ；；具体外观与性能待游戏实刷 | [^14] |
| `Base.GSA_HeavyCabin08` | GSA_HeavyCabin08（未找到有效中文译文） | GSA_HeavyCabin08 | 脚本座位数 2；机修类型 2；具体外观与性能待游戏实刷 | [^15] |
| `Base.GSA_HeavyCabin09` | GSA_HeavyCabin09（未找到有效中文译文） | GSA_HeavyCabin09 | 脚本座位数 2；机修类型 2；具体外观与性能待游戏实刷 | [^16] |
| `Base.GSA_HeavyCabin10` | GSA_HeavyCabin10（未找到有效中文译文） | GSA_HeavyCabin10 | 脚本座位数 2；机修类型 2；具体外观与性能待游戏实刷 | [^17] |
| `Base.GSA_HeavyCabin11` | GSA_HeavyCabin11（未找到有效中文译文） | GSA_HeavyCabin11 | 脚本座位数 2；机修类型 2；具体外观与性能待游戏实刷 | [^18] |
| `Base.GSA_HeavyCabin12` | GSA_HeavyCabin12（未找到有效中文译文） | GSA_HeavyCabin12 | 脚本座位数 2；机修类型 2；具体外观与性能待游戏实刷 | [^19] |
| `Base.GSA_HeavyCabin13` | GSA_HeavyCabin13（未找到有效中文译文） | GSA_HeavyCabin13 | 脚本座位数 6；机修类型 2；具体外观与性能待游戏实刷 | [^20] |
| `Base.GSA_ModernCar02Gearbox` | GSA_ModernCar02Gearbox（未找到有效中文译文） | GSA_ModernCar02Gearbox | ；；具体外观与性能待游戏实刷 | [^21] |
| `Base.GSA_ModernCarFirstGear` | GSA_ModernCarFirstGear（未找到有效中文译文） | GSA_ModernCarFirstGear | ；；具体外观与性能待游戏实刷 | [^22] |
| `Base.GSA_ModernCarMartinGearbox` | GSA_ModernCarMartinGearbox（未找到有效中文译文） | GSA_ModernCarMartinGearbox | 脚本座位数 4；机修类型 3；具体外观与性能待游戏实刷 | [^23] |
| `Base.GSA_PickupHeavyGearbox` | GSA_PickupHeavyGearbox（未找到有效中文译文） | GSA_PickupHeavyGearbox | ；；具体外观与性能待游戏实刷 | [^24] |
| `Base.GSA_PoliceNyalaGearbox` | GSA_PoliceNyalaGearbox（未找到有效中文译文） | GSA_PoliceNyalaGearbox | 脚本座位数 4；机修类型 1；具体外观与性能待游戏实刷 | [^25] |
| `Base.GSA_SmallCarGearbox` | GSA_SmallCarGearbox（未找到有效中文译文） | GSA_SmallCarGearbox | ；；具体外观与性能待游戏实刷 | [^26] |

## 普通物品与书籍

无当前有效条目。

## 维修配件

无当前有效条目。

## 改装配件

无当前有效条目。

## 共享配件

下列物品由已启用依赖或游戏原版提供，不计入本 Mod 的本地物品数。

| 完整物品 ID | 游戏显示名 / 名称状态 | 中文用途 / 类别 | 菜单 | 适用车辆与安装位置 | 来源 / 状态 |
| --- | --- | --- | --- | --- | --- |
| `Base.BigGasTank1` | 油箱 (大型)（翻译文件含非标准语法，待游戏核实）[^28] | 车辆安装件，用于油箱（GasTank）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_PoliceNyalaGearbox → GasTank | 游戏原版[^27] |
| `Base.BigGasTank2` | 油箱 (大型)（翻译文件含非标准语法，待游戏核实）[^30] | 车辆安装件，用于油箱（GasTank）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_HeavyCabin03 → GasTank；Base.GSA_HeavyCabin08 → GasTank；Base.GSA_HeavyCabin09 → GasTank；Base.GSA_HeavyCabin10 → GasTank；Base.GSA_HeavyCabin11 → GasTank；Base.GSA_HeavyCabin12 → GasTank；Base.GSA_HeavyCabin13 → GasTank | 游戏原版[^29] |
| `Base.BigGasTank3` | 油箱 (大型)（翻译文件含非标准语法，待游戏核实）[^32] | 车辆安装件，用于油箱（GasTank）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_Fleet_SportsCar → GasTank；Base.GSA_Fleet_SportsCar_ez → GasTank；Base.GSA_ModernCarMartinGearbox → GasTank | 游戏原版[^31] |
| `Base.BigTrunk2` | 后备箱 (大型)（翻译文件含非标准语法，待游戏核实）[^34] | 车辆安装件，用于车辆安装位（TruckBed）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_HeavyCabin11 → TruckBed | 游戏原版[^33] |
| `Base.CarBattery1` | 汽车电池（翻译文件含非标准语法，待游戏核实）[^36] | 车辆安装件，用于蓄电池（Battery）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_PoliceNyalaGearbox → Battery | 游戏原版[^35] |
| `Base.CarBattery2` | 汽车电池（翻译文件含非标准语法，待游戏核实）[^38] | 车辆安装件，用于蓄电池（Battery）、蓄电池（GRHouseBattery1）、蓄电池（GRHouseBattery2）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_HeavyCabin03 → Battery；Base.GSA_HeavyCabin08 → Battery；Base.GSA_HeavyCabin09 → Battery；Base.GSA_HeavyCabin10 → Battery；Base.GSA_HeavyCabin11 → Battery；Base.GSA_HeavyCabin12 → Battery；Base.GSA_HeavyCabin13 → Battery | 游戏原版[^37] |
| `Base.CarBattery3` | 汽车电池（翻译文件含非标准语法，待游戏核实）[^40] | 车辆安装件，用于蓄电池（Battery）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_Fleet_SportsCar → Battery；Base.GSA_Fleet_SportsCar_ez → Battery；Base.GSA_ModernCarMartinGearbox → Battery | 游戏原版[^39] |
| `Base.EngineDoor1` | 引擎罩（翻译文件含非标准语法，待游戏核实）[^42] | 车辆安装件，用于引擎盖（EngineDoor）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_PoliceNyalaGearbox → EngineDoor | 游戏原版[^41] |
| `Base.EngineDoor2` | 引擎罩（翻译文件含非标准语法，待游戏核实）[^44] | 车辆安装件，用于引擎盖（EngineDoor）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_HeavyCabin03 → EngineDoor；Base.GSA_HeavyCabin08 → EngineDoor；Base.GSA_HeavyCabin09 → EngineDoor；Base.GSA_HeavyCabin10 → EngineDoor；Base.GSA_HeavyCabin11 → EngineDoor；Base.GSA_HeavyCabin12 → EngineDoor；Base.GSA_HeavyCabin13 → EngineDoor | 游戏原版[^43] |
| `Base.EngineDoor3` | 引擎罩（翻译文件含非标准语法，待游戏核实）[^46] | 车辆安装件，用于引擎盖（EngineDoor）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_Fleet_SportsCar → EngineDoor；Base.GSA_Fleet_SportsCar_ez → EngineDoor；Base.GSA_ModernCarMartinGearbox → EngineDoor | 游戏原版[^45] |
| `Base.FrontCarDoor1` | 车前门（翻译文件含非标准语法，待游戏核实）[^48] | 车辆安装件，用于车门（DoorFrontLeft）、车门（DoorFrontRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_PoliceNyalaGearbox → DoorFrontLeft；Base.GSA_PoliceNyalaGearbox → DoorFrontRight | 游戏原版[^47] |
| `Base.FrontCarDoor2` | 车前门（翻译文件含非标准语法，待游戏核实）[^50] | 车辆安装件，用于车门（DoorFrontLeft）、车门（DoorFrontRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_HeavyCabin03 → DoorFrontLeft；Base.GSA_HeavyCabin03 → DoorFrontRight；Base.GSA_HeavyCabin08 → DoorFrontLeft；Base.GSA_HeavyCabin08 → DoorFrontRight；Base.GSA_HeavyCabin09 → DoorFrontLeft；Base.GSA_HeavyCabin09 → DoorFrontRight；Base.GSA_HeavyCabin10 → DoorFrontLeft；Base.GSA_HeavyCabin10 → DoorFrontRight；Base.GSA_HeavyCabin11 → DoorFrontLeft；Base.GSA_HeavyCabin11 → DoorFrontRight；Base.GSA_HeavyCabin12 → DoorFrontLeft；Base.GSA_HeavyCabin12 → DoorFrontRight；Base.GSA_HeavyCabin13 → DoorFrontLeft；Base.GSA_HeavyCabin13 → DoorFrontRight | 游戏原版[^49] |
| `Base.FrontCarDoor3` | 车前门（翻译文件含非标准语法，待游戏核实）[^52] | 车辆安装件，用于车门（DoorFrontLeft）、车门（DoorFrontRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_Fleet_SportsCar → DoorFrontLeft；Base.GSA_Fleet_SportsCar → DoorFrontRight；Base.GSA_Fleet_SportsCar_ez → DoorFrontLeft；Base.GSA_Fleet_SportsCar_ez → DoorFrontRight；Base.GSA_ModernCarMartinGearbox → DoorFrontLeft；Base.GSA_ModernCarMartinGearbox → DoorFrontRight | 游戏原版[^51] |
| `Base.FrontWindow1` | 车前窗（翻译文件含非标准语法，待游戏核实）[^54] | 车辆安装件，用于车窗（WindowFrontLeft）、车窗（WindowFrontRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_PoliceNyalaGearbox → WindowFrontLeft；Base.GSA_PoliceNyalaGearbox → WindowFrontRight | 游戏原版[^53] |
| `Base.FrontWindow2` | 车前窗（翻译文件含非标准语法，待游戏核实）[^56] | 车辆安装件，用于车窗（WindowFrontLeft）、车窗（WindowFrontRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_HeavyCabin03 → WindowFrontLeft；Base.GSA_HeavyCabin03 → WindowFrontRight；Base.GSA_HeavyCabin08 → WindowFrontLeft；Base.GSA_HeavyCabin08 → WindowFrontRight；Base.GSA_HeavyCabin09 → WindowFrontLeft；Base.GSA_HeavyCabin09 → WindowFrontRight；Base.GSA_HeavyCabin10 → WindowFrontLeft；Base.GSA_HeavyCabin10 → WindowFrontRight；Base.GSA_HeavyCabin11 → WindowFrontLeft；Base.GSA_HeavyCabin11 → WindowFrontRight；Base.GSA_HeavyCabin12 → WindowFrontLeft；Base.GSA_HeavyCabin12 → WindowFrontRight；Base.GSA_HeavyCabin13 → WindowFrontLeft；Base.GSA_HeavyCabin13 → WindowFrontRight | 游戏原版[^55] |
| `Base.FrontWindow3` | 车前窗（翻译文件含非标准语法，待游戏核实）[^58] | 车辆安装件，用于车窗（WindowFrontLeft）、车窗（WindowFrontRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_Fleet_SportsCar → WindowFrontLeft；Base.GSA_Fleet_SportsCar → WindowFrontRight；Base.GSA_Fleet_SportsCar_ez → WindowFrontLeft；Base.GSA_Fleet_SportsCar_ez → WindowFrontRight；Base.GSA_ModernCarMartinGearbox → WindowFrontLeft；Base.GSA_ModernCarMartinGearbox → WindowFrontRight | 游戏原版[^57] |
| `Base.GloveBox1` | 手套箱（翻译文件含非标准语法，待游戏核实）[^60] | 车辆安装件，用于车辆安装位（GloveBox）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_PoliceNyalaGearbox → GloveBox | 游戏原版[^59] |
| `Base.GloveBox2` | 手套箱（翻译文件含非标准语法，待游戏核实）[^62] | 车辆安装件，用于车辆安装位（GloveBox）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_HeavyCabin03 → GloveBox；Base.GSA_HeavyCabin08 → GloveBox；Base.GSA_HeavyCabin09 → GloveBox；Base.GSA_HeavyCabin10 → GloveBox；Base.GSA_HeavyCabin11 → GloveBox；Base.GSA_HeavyCabin12 → GloveBox；Base.GSA_HeavyCabin13 → GloveBox | 游戏原版[^61] |
| `Base.GloveBox3` | 手套箱（翻译文件含非标准语法，待游戏核实）[^64] | 车辆安装件，用于车辆安装位（GloveBox）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_Fleet_SportsCar → GloveBox；Base.GSA_Fleet_SportsCar_ez → GloveBox | 游戏原版[^63] |
| `Base.HamRadio1` | 微型导航仪 / 收音机 (业余电台) / 民用无线电台 (昂科) / 民用无线电台 - 昂科公司（译文冲突，待游戏核实）[^66] | 车辆安装件，用于车辆安装位（Radio）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_HeavyCabin04 → Radio；Base.GSA_HeavyCabin07 → Radio；Base.GSA_HeavyCabin09 → Radio；Base.GSA_HeavyCabin12 → Radio；Base.GSA_PoliceNyalaGearbox → Radio | 游戏原版[^65] |
| `Base.HamRadio2` | 收音机 (军用) / 军用无线电台（译文冲突，待游戏核实）[^68] | 车辆安装件，用于车辆安装位（Radio）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_HeavyCabin04 → Radio；Base.GSA_HeavyCabin07 → Radio；Base.GSA_HeavyCabin09 → Radio；Base.GSA_HeavyCabin12 → Radio；Base.GSA_PoliceNyalaGearbox → Radio | 游戏原版[^67] |
| `Base.HamRadioMakeShift` | 收音机 (简易业余无线电) / 收音机 (简易业余电台) / 自制无线电台（译文冲突，待游戏核实）[^70] | 车辆安装件，用于车辆安装位（Radio）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_HeavyCabin04 → Radio；Base.GSA_HeavyCabin07 → Radio；Base.GSA_HeavyCabin09 → Radio；Base.GSA_HeavyCabin12 → Radio；Base.GSA_PoliceNyalaGearbox → Radio | 游戏原版[^69] |
| `Base.HoodOrnament_Badger` | 獾鲍里斯车标（翻译文件含非标准语法，待游戏核实）[^72] | 车辆安装件，用于车辆安装位（HoodOrnament）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_ModernCarMartinGearbox → HoodOrnament | 游戏原版[^71] |
| `Base.HoodOrnament_Beaver` | 海狸雅克车标（翻译文件含非标准语法，待游戏核实）[^74] | 车辆安装件，用于车辆安装位（HoodOrnament）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_ModernCarMartinGearbox → HoodOrnament | 游戏原版[^73] |
| `Base.HoodOrnament_Spiffo` | 斯皮福车标（翻译文件含非标准语法，待游戏核实）[^76] | 车辆安装件，用于车辆安装位（HoodOrnament）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_ModernCarMartinGearbox → HoodOrnament | 游戏原版[^75] |
| `Base.LightBulb` | 灯泡-白色 / 灯泡 (白)（译文冲突，待游戏核实）[^78] | 车辆安装件，用于车灯（Headlight*）、车灯（JP82DorothyLights）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_CarNormalStandardGearbox → Headlight*；Base.GSA_Fleet_CarLuxury → Headlight*；Base.GSA_Fleet_CarStationWagon → Headlight*；Base.GSA_Fleet_CarStationWagon2 → Headlight*；Base.GSA_Fleet_RaceCar12 → Headlight*；Base.GSA_Fleet_SmallCar02 → Headlight*；Base.GSA_Fleet_SportsCar → Headlight*；Base.GSA_Fleet_SportsCar_ez → Headlight*；Base.GSA_HeavyCabin01 → Headlight*；Base.GSA_HeavyCabin03 → Headlight*；Base.GSA_HeavyCabin04 → Headlight*；Base.GSA_HeavyCabin05 → Headlight*；Base.GSA_HeavyCabin06 → Headlight*；Base.GSA_HeavyCabin07 → Headlight*；Base.GSA_HeavyCabin08 → Headlight*；Base.GSA_HeavyCabin09 → Headlight*；Base.GSA_HeavyCabin10 → Headlight*；Base.GSA_HeavyCabin11 → Headlight*；Base.GSA_HeavyCabin12 → Headlight*；Base.GSA_HeavyCabin13 → Headlight*；Base.GSA_ModernCar02Gearbox → Headlight*；Base.GSA_ModernCarFirstGear → Headlight*；Base.GSA_ModernCarMartinGearbox → Headlight*；Base.GSA_PickupHeavyGearbox → Headlight*；Base.GSA_PoliceNyalaGearbox → Headlight*；Base.GSA_SmallCarGearbox → Headlight* | 游戏原版[^77] |
| `Base.ModernBrake1` | 制动器 (高级)（翻译文件含非标准语法，待游戏核实）[^80] | 车辆安装件，用于制动器（Brake*）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_PoliceNyalaGearbox → Brake* | 游戏原版[^79] |
| `Base.ModernBrake2` | 制动器 (高级)（翻译文件含非标准语法，待游戏核实）[^82] | 车辆安装件，用于制动器（Brake*）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_HeavyCabin03 → Brake*；Base.GSA_HeavyCabin08 → Brake*；Base.GSA_HeavyCabin09 → Brake*；Base.GSA_HeavyCabin10 → Brake*；Base.GSA_HeavyCabin11 → Brake*；Base.GSA_HeavyCabin12 → Brake*；Base.GSA_HeavyCabin13 → Brake* | 游戏原版[^81] |
| `Base.ModernBrake3` | 制动器 (高级)（翻译文件含非标准语法，待游戏核实）[^84] | 车辆安装件，用于制动器（Brake*）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_Fleet_SportsCar → Brake*；Base.GSA_Fleet_SportsCar_ez → Brake*；Base.GSA_ModernCarMartinGearbox → Brake* | 游戏原版[^83] |
| `Base.ModernCarMuffler1` | 消声器 (高级)（翻译文件含非标准语法，待游戏核实）[^86] | 车辆安装件，用于消声器（Muffler）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_PoliceNyalaGearbox → Muffler | 游戏原版[^85] |
| `Base.ModernCarMuffler2` | 消声器 (高级)（翻译文件含非标准语法，待游戏核实）[^88] | 车辆安装件，用于消声器（Muffler）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_HeavyCabin03 → Muffler；Base.GSA_HeavyCabin08 → Muffler；Base.GSA_HeavyCabin09 → Muffler；Base.GSA_HeavyCabin10 → Muffler；Base.GSA_HeavyCabin11 → Muffler；Base.GSA_HeavyCabin12 → Muffler；Base.GSA_HeavyCabin13 → Muffler | 游戏原版[^87] |
| `Base.ModernCarMuffler3` | 消声器 (高级)（翻译文件含非标准语法，待游戏核实）[^90] | 车辆安装件，用于消声器（Muffler）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_Fleet_SportsCar → Muffler；Base.GSA_Fleet_SportsCar_ez → Muffler；Base.GSA_ModernCarMartinGearbox → Muffler | 游戏原版[^89] |
| `Base.ModernSuspension1` | 悬挂 (高级)（翻译文件含非标准语法，待游戏核实）[^92] | 车辆安装件，用于悬挂（Suspension*）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_PoliceNyalaGearbox → Suspension* | 游戏原版[^91] |
| `Base.ModernSuspension2` | 悬挂 (高级)（翻译文件含非标准语法，待游戏核实）[^94] | 车辆安装件，用于悬挂（Suspension*）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_HeavyCabin03 → Suspension*；Base.GSA_HeavyCabin08 → Suspension*；Base.GSA_HeavyCabin09 → Suspension*；Base.GSA_HeavyCabin10 → Suspension*；Base.GSA_HeavyCabin11 → Suspension*；Base.GSA_HeavyCabin12 → Suspension*；Base.GSA_HeavyCabin13 → Suspension* | 游戏原版[^93] |
| `Base.ModernSuspension3` | 悬挂 (高级)（翻译文件含非标准语法，待游戏核实）[^96] | 车辆安装件，用于悬挂（Suspension*）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_Fleet_SportsCar → Suspension*；Base.GSA_Fleet_SportsCar_ez → Suspension*；Base.GSA_ModernCarMartinGearbox → Suspension* | 游戏原版[^95] |
| `Base.ModernTire1` | 轮胎 (高级)（翻译文件含非标准语法，待游戏核实）[^98] | 车辆安装件，用于轮胎（Tire*）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_PoliceNyalaGearbox → Tire* | 游戏原版[^97] |
| `Base.ModernTire2` | 轮胎 (高级)（翻译文件含非标准语法，待游戏核实）[^100] | 车辆安装件，用于轮胎（Tire*）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_HeavyCabin03 → Tire*；Base.GSA_HeavyCabin08 → Tire*；Base.GSA_HeavyCabin09 → Tire*；Base.GSA_HeavyCabin10 → Tire*；Base.GSA_HeavyCabin11 → Tire*；Base.GSA_HeavyCabin12 → Tire*；Base.GSA_HeavyCabin13 → Tire* | 游戏原版[^99] |
| `Base.ModernTire3` | 轮胎 (高级)（翻译文件含非标准语法，待游戏核实）[^102] | 车辆安装件，用于轮胎（Tire*）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_Fleet_SportsCar → Tire*；Base.GSA_Fleet_SportsCar_ez → Tire*；Base.GSA_ModernCarMartinGearbox → Tire* | 游戏原版[^101] |
| `Base.NormalBrake1` | 制动器 (普通)（翻译文件含非标准语法，待游戏核实）[^104] | 车辆安装件，用于制动器（Brake*）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_PoliceNyalaGearbox → Brake* | 游戏原版[^103] |
| `Base.NormalBrake2` | 制动器 (普通)（翻译文件含非标准语法，待游戏核实）[^106] | 车辆安装件，用于制动器（Brake*）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_HeavyCabin03 → Brake*；Base.GSA_HeavyCabin08 → Brake*；Base.GSA_HeavyCabin09 → Brake*；Base.GSA_HeavyCabin10 → Brake*；Base.GSA_HeavyCabin11 → Brake*；Base.GSA_HeavyCabin12 → Brake*；Base.GSA_HeavyCabin13 → Brake* | 游戏原版[^105] |
| `Base.NormalBrake3` | 制动器 (普通)（翻译文件含非标准语法，待游戏核实）[^108] | 车辆安装件，用于制动器（Brake*）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_Fleet_SportsCar → Brake*；Base.GSA_Fleet_SportsCar_ez → Brake*；Base.GSA_ModernCarMartinGearbox → Brake* | 游戏原版[^107] |
| `Base.NormalCarMuffler1` | 消声器 (普通)（翻译文件含非标准语法，待游戏核实）[^110] | 车辆安装件，用于消声器（Muffler）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_PoliceNyalaGearbox → Muffler | 游戏原版[^109] |
| `Base.NormalCarMuffler2` | 消声器 (普通)（翻译文件含非标准语法，待游戏核实）[^112] | 车辆安装件，用于消声器（Muffler）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_HeavyCabin03 → Muffler；Base.GSA_HeavyCabin08 → Muffler；Base.GSA_HeavyCabin09 → Muffler；Base.GSA_HeavyCabin10 → Muffler；Base.GSA_HeavyCabin11 → Muffler；Base.GSA_HeavyCabin12 → Muffler；Base.GSA_HeavyCabin13 → Muffler | 游戏原版[^111] |
| `Base.NormalCarMuffler3` | 消声器 (普通)（翻译文件含非标准语法，待游戏核实）[^114] | 车辆安装件，用于消声器（Muffler）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_Fleet_SportsCar → Muffler；Base.GSA_Fleet_SportsCar_ez → Muffler；Base.GSA_ModernCarMartinGearbox → Muffler | 游戏原版[^113] |
| `Base.NormalGasTank1` | 油箱 (标准)（翻译文件含非标准语法，待游戏核实）[^116] | 车辆安装件，用于油箱（GasTank）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_PoliceNyalaGearbox → GasTank | 游戏原版[^115] |
| `Base.NormalGasTank2` | 油箱 (标准)（翻译文件含非标准语法，待游戏核实）[^118] | 车辆安装件，用于油箱（GasTank）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_HeavyCabin03 → GasTank；Base.GSA_HeavyCabin08 → GasTank；Base.GSA_HeavyCabin09 → GasTank；Base.GSA_HeavyCabin10 → GasTank；Base.GSA_HeavyCabin11 → GasTank；Base.GSA_HeavyCabin12 → GasTank；Base.GSA_HeavyCabin13 → GasTank | 游戏原版[^117] |
| `Base.NormalGasTank3` | 油箱 (标准)（翻译文件含非标准语法，待游戏核实）[^120] | 车辆安装件，用于油箱（GasTank）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_Fleet_SportsCar → GasTank；Base.GSA_Fleet_SportsCar_ez → GasTank；Base.GSA_ModernCarMartinGearbox → GasTank | 游戏原版[^119] |
| `Base.NormalSuspension1` | 悬挂 (普通)（翻译文件含非标准语法，待游戏核实）[^122] | 车辆安装件，用于悬挂（Suspension*）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_PoliceNyalaGearbox → Suspension* | 游戏原版[^121] |
| `Base.NormalSuspension2` | 悬挂 (普通)（翻译文件含非标准语法，待游戏核实）[^124] | 车辆安装件，用于悬挂（Suspension*）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_HeavyCabin03 → Suspension*；Base.GSA_HeavyCabin08 → Suspension*；Base.GSA_HeavyCabin09 → Suspension*；Base.GSA_HeavyCabin10 → Suspension*；Base.GSA_HeavyCabin11 → Suspension*；Base.GSA_HeavyCabin12 → Suspension*；Base.GSA_HeavyCabin13 → Suspension* | 游戏原版[^123] |
| `Base.NormalSuspension3` | 悬挂 (普通)（翻译文件含非标准语法，待游戏核实）[^126] | 车辆安装件，用于悬挂（Suspension*）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_Fleet_SportsCar → Suspension*；Base.GSA_Fleet_SportsCar_ez → Suspension*；Base.GSA_ModernCarMartinGearbox → Suspension* | 游戏原版[^125] |
| `Base.NormalTire1` | 轮胎 (普通)（翻译文件含非标准语法，待游戏核实）[^128] | 车辆安装件，用于轮胎（Tire*）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_PoliceNyalaGearbox → Tire* | 游戏原版[^127] |
| `Base.NormalTire2` | 轮胎 (普通)（翻译文件含非标准语法，待游戏核实）[^130] | 车辆安装件，用于轮胎（Tire*）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_HeavyCabin03 → Tire*；Base.GSA_HeavyCabin08 → Tire*；Base.GSA_HeavyCabin09 → Tire*；Base.GSA_HeavyCabin10 → Tire*；Base.GSA_HeavyCabin11 → Tire*；Base.GSA_HeavyCabin12 → Tire*；Base.GSA_HeavyCabin13 → Tire* | 游戏原版[^129] |
| `Base.NormalTire3` | 轮胎 (普通)（翻译文件含非标准语法，待游戏核实）[^132] | 车辆安装件，用于轮胎（Tire*）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_Fleet_SportsCar → Tire*；Base.GSA_Fleet_SportsCar_ez → Tire*；Base.GSA_ModernCarMartinGearbox → Tire* | 游戏原版[^131] |
| `Base.NormalTrunk1` | 后备箱 (标准)（翻译文件含非标准语法，待游戏核实）[^134] | 车辆安装件，用于车辆安装位（TruckBed）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_PoliceNyalaGearbox → TruckBed | 游戏原版[^133] |
| `Base.NormalTrunk2` | 后备箱 (标准)（翻译文件含非标准语法，待游戏核实）[^136] | 车辆安装件，用于车辆安装位（TruckBedOpen）、车辆安装位（TruckBed）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_HeavyCabin03 → TruckBedOpen；Base.GSA_HeavyCabin08 → TruckBed；Base.GSA_HeavyCabin09 → TruckBed；Base.GSA_HeavyCabin10 → TruckBed；Base.GSA_HeavyCabin12 → TruckBed | 游戏原版[^135] |
| `Base.NormalTrunk3` | 后备箱 (标准)（翻译文件含非标准语法，待游戏核实）[^138] | 车辆安装件，用于车辆安装位（TruckBed）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_ModernCarMartinGearbox → TruckBed | 游戏原版[^137] |
| `Base.OldBrake1` | 制动器 (老式)（翻译文件含非标准语法，待游戏核实）[^140] | 车辆安装件，用于制动器（Brake*）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_PoliceNyalaGearbox → Brake* | 游戏原版[^139] |
| `Base.OldBrake2` | 制动器 (老式)（翻译文件含非标准语法，待游戏核实）[^142] | 车辆安装件，用于制动器（Brake*）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_HeavyCabin03 → Brake*；Base.GSA_HeavyCabin08 → Brake*；Base.GSA_HeavyCabin09 → Brake*；Base.GSA_HeavyCabin10 → Brake*；Base.GSA_HeavyCabin11 → Brake*；Base.GSA_HeavyCabin12 → Brake*；Base.GSA_HeavyCabin13 → Brake* | 游戏原版[^141] |
| `Base.OldBrake3` | 制动器 (老式)（翻译文件含非标准语法，待游戏核实）[^144] | 车辆安装件，用于制动器（Brake*）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_Fleet_SportsCar → Brake*；Base.GSA_Fleet_SportsCar_ez → Brake*；Base.GSA_ModernCarMartinGearbox → Brake* | 游戏原版[^143] |
| `Base.OldCarMuffler1` | 消声器 (老式)（翻译文件含非标准语法，待游戏核实）[^146] | 车辆安装件，用于消声器（Muffler）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_PoliceNyalaGearbox → Muffler | 游戏原版[^145] |
| `Base.OldCarMuffler2` | 消声器 (老式)（翻译文件含非标准语法，待游戏核实）[^148] | 车辆安装件，用于消声器（Muffler）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_HeavyCabin03 → Muffler；Base.GSA_HeavyCabin08 → Muffler；Base.GSA_HeavyCabin09 → Muffler；Base.GSA_HeavyCabin10 → Muffler；Base.GSA_HeavyCabin11 → Muffler；Base.GSA_HeavyCabin12 → Muffler；Base.GSA_HeavyCabin13 → Muffler | 游戏原版[^147] |
| `Base.OldCarMuffler3` | 消声器 (老式)（翻译文件含非标准语法，待游戏核实）[^150] | 车辆安装件，用于消声器（Muffler）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_Fleet_SportsCar → Muffler；Base.GSA_Fleet_SportsCar_ez → Muffler；Base.GSA_ModernCarMartinGearbox → Muffler | 游戏原版[^149] |
| `Base.OldTire1` | 轮胎 (廉价)（翻译文件含非标准语法，待游戏核实）[^152] | 车辆安装件，用于轮胎（Tire*）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_PoliceNyalaGearbox → Tire* | 游戏原版[^151] |
| `Base.OldTire2` | 轮胎 (廉价)（翻译文件含非标准语法，待游戏核实）[^154] | 车辆安装件，用于轮胎（TireFrontLeft）、轮胎（TireFrontRight）、轮胎（Tire*）、轮胎（TireRearLeft）、轮胎（TireRearRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_HeavyCabin03 → Tire*；Base.GSA_HeavyCabin08 → Tire*；Base.GSA_HeavyCabin09 → Tire*；Base.GSA_HeavyCabin10 → Tire*；Base.GSA_HeavyCabin11 → Tire*；Base.GSA_HeavyCabin12 → Tire*；Base.GSA_HeavyCabin13 → Tire* | 游戏原版[^153] |
| `Base.OldTire3` | 轮胎 (廉价)（翻译文件含非标准语法，待游戏核实）[^156] | 车辆安装件，用于轮胎（Tire*）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_Fleet_SportsCar → Tire*；Base.GSA_Fleet_SportsCar_ez → Tire*；Base.GSA_ModernCarMartinGearbox → Tire* | 游戏原版[^155] |
| `Base.RadioBlack` | 收音机 (超值科技) / 收音机 (廉科) / 廉科牌收音机（译文冲突，待游戏核实）[^158] | 车辆安装件，用于车辆安装位（Radio）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_CarNormalStandardGearbox → Radio；Base.GSA_Fleet_CarLuxury → Radio；Base.GSA_Fleet_CarStationWagon → Radio；Base.GSA_Fleet_CarStationWagon2 → Radio；Base.GSA_Fleet_RaceCar12 → Radio；Base.GSA_Fleet_SmallCar02 → Radio；Base.GSA_Fleet_SportsCar → Radio；Base.GSA_Fleet_SportsCar_ez → Radio；Base.GSA_HeavyCabin01 → Radio；Base.GSA_HeavyCabin03 → Radio；Base.GSA_HeavyCabin05 → Radio；Base.GSA_HeavyCabin06 → Radio；Base.GSA_HeavyCabin08 → Radio；Base.GSA_HeavyCabin10 → Radio；Base.GSA_HeavyCabin11 → Radio；Base.GSA_HeavyCabin13 → Radio；Base.GSA_ModernCar02Gearbox → Radio；Base.GSA_ModernCarFirstGear → Radio；Base.GSA_ModernCarMartinGearbox → Radio；Base.GSA_PickupHeavyGearbox → Radio；Base.GSA_SmallCarGearbox → Radio | 游戏原版[^157] |
| `Base.RadioMakeShift` | 收音机 (简易) / 自制收音机（译文冲突，待游戏核实）[^160] | 车辆安装件，用于车辆安装位（Radio）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_CarNormalStandardGearbox → Radio；Base.GSA_Fleet_CarLuxury → Radio；Base.GSA_Fleet_CarStationWagon → Radio；Base.GSA_Fleet_CarStationWagon2 → Radio；Base.GSA_Fleet_RaceCar12 → Radio；Base.GSA_Fleet_SmallCar02 → Radio；Base.GSA_Fleet_SportsCar → Radio；Base.GSA_Fleet_SportsCar_ez → Radio；Base.GSA_HeavyCabin01 → Radio；Base.GSA_HeavyCabin03 → Radio；Base.GSA_HeavyCabin05 → Radio；Base.GSA_HeavyCabin06 → Radio；Base.GSA_HeavyCabin08 → Radio；Base.GSA_HeavyCabin10 → Radio；Base.GSA_HeavyCabin11 → Radio；Base.GSA_HeavyCabin13 → Radio；Base.GSA_ModernCar02Gearbox → Radio；Base.GSA_ModernCarFirstGear → Radio；Base.GSA_ModernCarMartinGearbox → Radio；Base.GSA_PickupHeavyGearbox → Radio；Base.GSA_SmallCarGearbox → Radio | 游戏原版[^159] |
| `Base.RadioRed` | 导航仪 / 收音机 (昂科) / 昂科牌收音机（译文冲突，待游戏核实）[^162] | 车辆安装件，用于车辆安装位（Radio）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_CarNormalStandardGearbox → Radio；Base.GSA_Fleet_CarLuxury → Radio；Base.GSA_Fleet_CarStationWagon → Radio；Base.GSA_Fleet_CarStationWagon2 → Radio；Base.GSA_Fleet_RaceCar12 → Radio；Base.GSA_Fleet_SmallCar02 → Radio；Base.GSA_Fleet_SportsCar → Radio；Base.GSA_Fleet_SportsCar_ez → Radio；Base.GSA_HeavyCabin01 → Radio；Base.GSA_HeavyCabin03 → Radio；Base.GSA_HeavyCabin05 → Radio；Base.GSA_HeavyCabin06 → Radio；Base.GSA_HeavyCabin08 → Radio；Base.GSA_HeavyCabin10 → Radio；Base.GSA_HeavyCabin11 → Radio；Base.GSA_HeavyCabin13 → Radio；Base.GSA_ModernCar02Gearbox → Radio；Base.GSA_ModernCarFirstGear → Radio；Base.GSA_ModernCarMartinGearbox → Radio；Base.GSA_PickupHeavyGearbox → Radio；Base.GSA_SmallCarGearbox → Radio | 游戏原版[^161] |
| `Base.RearCarDoor1` | 车后门（翻译文件含非标准语法，待游戏核实）[^164] | 车辆安装件，用于车门（DoorRearLeft）、车门（DoorRearRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_PoliceNyalaGearbox → DoorRearLeft；Base.GSA_PoliceNyalaGearbox → DoorRearRight | 游戏原版[^163] |
| `Base.RearCarDoor2` | 车后门（翻译文件含非标准语法，待游戏核实）[^166] | 车辆安装件，用于车门（DoorMiddleLeft）、车门（DoorMiddleRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_HeavyCabin13 → DoorMiddleLeft；Base.GSA_HeavyCabin13 → DoorMiddleRight | 游戏原版[^165] |
| `Base.RearCarDoor3` | 车后门（翻译文件含非标准语法，待游戏核实）[^168] | 车辆安装件，用于车门（DoorRearLeft）、车门（DoorRearRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_ModernCarMartinGearbox → DoorRearLeft；Base.GSA_ModernCarMartinGearbox → DoorRearRight | 游戏原版[^167] |
| `Base.RearWindow1` | 车后窗（翻译文件含非标准语法，待游戏核实）[^170] | 车辆安装件，用于车窗（WindowRearLeft）、车窗（WindowRearRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_PoliceNyalaGearbox → WindowRearLeft；Base.GSA_PoliceNyalaGearbox → WindowRearRight | 游戏原版[^169] |
| `Base.RearWindow2` | 车后窗（翻译文件含非标准语法，待游戏核实）[^172] | 车辆安装件，用于车窗（WindowRearLeft）、车窗（WindowRearRight）、车窗（WindowMiddleLeft）、车窗（WindowMiddleRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_HeavyCabin13 → WindowMiddleLeft；Base.GSA_HeavyCabin13 → WindowMiddleRight | 游戏原版[^171] |
| `Base.RearWindow3` | 车后窗（翻译文件含非标准语法，待游戏核实）[^174] | 车辆安装件，用于车窗（WindowRearLeft）、车窗（WindowRearRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_ModernCarMartinGearbox → WindowRearLeft；Base.GSA_ModernCarMartinGearbox → WindowRearRight | 游戏原版[^173] |
| `Base.RearWindshield1` | 后挡风玻璃（翻译文件含非标准语法，待游戏核实）[^176] | 车辆安装件，用于挡风玻璃（WindshieldRear）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_PoliceNyalaGearbox → WindshieldRear | 游戏原版[^175] |
| `Base.RearWindshield2` | 后挡风玻璃（翻译文件含非标准语法，待游戏核实）[^178] | 车辆安装件，用于挡风玻璃（WindshieldRear）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_HeavyCabin03 → WindshieldRear；Base.GSA_HeavyCabin08 → WindshieldRear；Base.GSA_HeavyCabin09 → WindshieldRear；Base.GSA_HeavyCabin10 → WindshieldRear；Base.GSA_HeavyCabin11 → WindshieldRear；Base.GSA_HeavyCabin12 → WindshieldRear；Base.GSA_HeavyCabin13 → WindshieldRear | 游戏原版[^177] |
| `Base.RearWindshield3` | 后挡风玻璃（翻译文件含非标准语法，待游戏核实）[^180] | 车辆安装件，用于挡风玻璃（WindshieldRear）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_Fleet_SportsCar → WindshieldRear；Base.GSA_Fleet_SportsCar_ez → WindshieldRear；Base.GSA_ModernCarMartinGearbox → WindshieldRear | 游戏原版[^179] |
| `Base.SmallGasTank1` | 油箱 (小型)（翻译文件含非标准语法，待游戏核实）[^182] | 车辆安装件，用于油箱（GasTank）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_PoliceNyalaGearbox → GasTank | 游戏原版[^181] |
| `Base.SmallGasTank2` | 油箱 (小型)（翻译文件含非标准语法，待游戏核实）[^184] | 车辆安装件，用于油箱（GasTank）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_HeavyCabin03 → GasTank；Base.GSA_HeavyCabin08 → GasTank；Base.GSA_HeavyCabin09 → GasTank；Base.GSA_HeavyCabin10 → GasTank；Base.GSA_HeavyCabin11 → GasTank；Base.GSA_HeavyCabin12 → GasTank；Base.GSA_HeavyCabin13 → GasTank | 游戏原版[^183] |
| `Base.SmallGasTank3` | 油箱 (小型)（翻译文件含非标准语法，待游戏核实）[^186] | 车辆安装件，用于油箱（GasTank）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_Fleet_SportsCar → GasTank；Base.GSA_Fleet_SportsCar_ez → GasTank；Base.GSA_ModernCarMartinGearbox → GasTank | 游戏原版[^185] |
| `Base.SmallTrunk3` | 后备箱 (小型)（翻译文件含非标准语法，待游戏核实）[^188] | 车辆安装件，用于车辆安装位（TruckBed）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_Fleet_SportsCar → TruckBed；Base.GSA_Fleet_SportsCar_ez → TruckBed | 游戏原版[^187] |
| `Base.TrunkDoor1` | 后备箱盖（翻译文件含非标准语法，待游戏核实）[^190] | 车辆安装件，用于后备箱（TrunkDoor）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_PoliceNyalaGearbox → TrunkDoor | 游戏原版[^189] |
| `Base.TrunkDoor3` | 后备箱盖（翻译文件含非标准语法，待游戏核实）[^192] | 车辆安装件，用于后备箱（TrunkDoor）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_Fleet_SportsCar → TrunkDoor；Base.GSA_Fleet_SportsCar_ez → TrunkDoor；Base.GSA_ModernCarMartinGearbox → TrunkDoor | 游戏原版[^191] |
| `Base.VanSeatsTrunk2` | 后备箱 (小型)（翻译文件含非标准语法，待游戏核实）[^194] | 车辆安装件，用于车辆安装位（TruckBed）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_HeavyCabin13 → TruckBed | 游戏原版[^193] |
| `Base.Windshield1` | 挡风玻璃（翻译文件含非标准语法，待游戏核实）[^196] | 车辆安装件，用于挡风玻璃（Windshield）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_PoliceNyalaGearbox → Windshield | 游戏原版[^195] |
| `Base.Windshield2` | 挡风玻璃（翻译文件含非标准语法，待游戏核实）[^198] | 车辆安装件，用于挡风玻璃（Windshield）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_HeavyCabin03 → Windshield；Base.GSA_HeavyCabin08 → Windshield；Base.GSA_HeavyCabin09 → Windshield；Base.GSA_HeavyCabin10 → Windshield；Base.GSA_HeavyCabin11 → Windshield；Base.GSA_HeavyCabin12 → Windshield；Base.GSA_HeavyCabin13 → Windshield | 游戏原版[^197] |
| `Base.Windshield3` | 挡风玻璃（翻译文件含非标准语法，待游戏核实）[^200] | 车辆安装件，用于挡风玻璃（Windshield）；适用车型见右列 / 维修配件 | 添加物品 | Base.GSA_Fleet_SportsCar → Windshield；Base.GSA_Fleet_SportsCar_ez → Windshield；Base.GSA_ModernCarMartinGearbox → Windshield | 游戏原版[^199] |

## 制作配方

无当前有效的脚本制作配方。Lua 动态添加的内容不在本次静态统计内。

## 内部定义、历史分支与未解析引用

有效资源层：42；仅合并 common 与所选版本，Overlay 按相对路径覆盖。
车辆模板 0 个、内部槽位 66 个，均不算整车或背包物品。旧根目录和未选中版本的定义不列入当前可用表。模板中短物品引用若追加机修类型后缀才匹配定义，属于静态映射，安装仍待实测。

<details><summary>查看内部槽位（不能直接刷取）</summary>

| 槽位 | 名称或说明 | 来源 |
| --- | --- | --- |
| `Battery` | 电池 / 蓄电池 | [^201] |
| `Brake*` | Brake* / 制动器 | [^202] |
| `BrakeFrontLeft` | 左前制动 / 制动器 | [^203] |
| `BrakeFrontRight` | 右前制动 / 制动器 | [^204] |
| `BrakeRearLeft` | 左后制动 / 制动器 | [^205] |
| `BrakeRearRight` | 右后制动 / 制动器 | [^206] |
| `Door*` | Door* / 车门 | [^207] |
| `DoorFrontLeft` | 左前门 / 车门 | [^208] |
| `DoorFrontRight` | 右前门 / 车门 | [^209] |
| `DoorMiddleLeft` | 左中门 / 车门 | [^210] |
| `DoorMiddleRight` | 右中门 / 车门 | [^211] |
| `DoorRear` | 后门 / 车门 | [^212] |
| `DoorRear*` | DoorRear* / 车门 | [^213] |
| `DoorRearLeft` | 左后门 / 车门 | [^214] |
| `DoorRearRight` | 右后门 / 车门 | [^215] |
| `Engine` | 引擎 / 发动机 | [^216] |
| `EngineDoor` | 引擎盖 / 引擎盖 | [^217] |
| `EngineDoor*` | EngineDoor* / 引擎盖 | [^218] |
| `GSAFirstGearbox` | GSAFirstGearbox / 车辆安装位 | [^219] |
| `GasTank` | 油箱 / 油箱 | [^220] |
| `GloveBox` | 手套箱 / 车辆安装位 | [^221] |
| `Headlight*` | Headlight* / 车灯 | [^222] |
| `HeadlightLeft` | 左大灯 / 车灯 | [^223] |
| `HeadlightRearLeft` | 左尾灯 / 车灯 | [^224] |
| `HeadlightRearRight` | 右尾灯 / 车灯 | [^225] |
| `HeadlightRight` | 右大灯 / 车灯 | [^226] |
| `Heater` | 加热器 / 车辆安装位 | [^227] |
| `HoodOrnament` | HoodOrnament / 车辆安装位 | [^228] |
| `Muffler` | 排气消声器 / 消声器 | [^229] |
| `PassengerCompartment` | 乘员舱 / 车辆安装位 | [^230] |
| `Radio` | 电台 / 车辆安装位 | [^231] |
| `Radio*` | Radio* / 车辆安装位 | [^232] |
| `Seat*` | Seat* / 座椅 | [^233] |
| `SeatFrontLeft` | 驾驶座 / 座椅 | [^234] |
| `SeatFrontRight` | 右前座 / 座椅 | [^235] |
| `SeatMiddleLeft` | 左中座 / 座椅 | [^236] |
| `SeatMiddleRight` | 右中座 / 座椅 | [^237] |
| `SeatRear*` | SeatRear* / 座椅 | [^238] |
| `SeatRearLeft` | 左后座 / 座椅 | [^239] |
| `SeatRearRight` | 右后座 / 座椅 | [^240] |
| `Suspension*` | Suspension* / 悬挂 | [^241] |
| `SuspensionFrontLeft` | 左前悬挂 / 悬挂 | [^242] |
| `SuspensionFrontRight` | 右前悬挂 / 悬挂 | [^243] |
| `SuspensionRearLeft` | 左后悬挂 / 悬挂 | [^244] |
| `SuspensionRearRight` | 右后悬挂 / 悬挂 | [^245] |
| `TestPart1` | TestPart1 / 车辆安装位 | [^246] |
| `Tire*` | Tire* / 轮胎 | [^247] |
| `TireFrontLeft` | 左前胎 / 轮胎 | [^248] |
| `TireFrontRight` | 右前胎 / 轮胎 | [^249] |
| `TireRearLeft` | 左后胎 / 轮胎 | [^250] |
| `TireRearRight` | 右后胎 / 轮胎 | [^251] |
| `TruckBed` | 补给箱 / 行李箱 / 车辆安装位 | [^252] |
| `TruckBedOpen` | 行李箱 / 车辆安装位 | [^253] |
| `TrunkDoor` | 后车盖 / 后备箱 | [^254] |
| `TrunkDoor*` | TrunkDoor* / 后备箱 | [^255] |
| `Window*` | Window* / 车窗 | [^256] |
| `WindowFrontLeft` | 左前窗 / 车窗 | [^257] |
| `WindowFrontRight` | 右前窗 / 车窗 | [^258] |
| `WindowMiddleLeft` | 左中部车窗 / 左中窗 / 车窗 | [^259] |
| `WindowMiddleRight` | 右中部车窗 / 右中窗 / 车窗 | [^260] |
| `WindowRearLeft` | 左后窗 / 车窗 | [^261] |
| `WindowRearRight` | 右后窗 / 车窗 | [^262] |
| `Windshield` | 挡风玻璃 / 挡风玻璃 | [^263] |
| `Windshield*` | Windshield* / 挡风玻璃 | [^264] |
| `WindshieldRear` | 后挡风玻璃 / 挡风玻璃 | [^265] |
| `lightbar` | 信标灯 / 爆闪灯 / 车灯 | [^266] |

</details>

<details><summary>未定位引用：保留排查线索，不作为可刷 ID</summary>

| 引用（不可直接刷取） | 原因 | 来源 |
| --- | --- | --- |
| Base.BigGasTank | 配件引用缺少有效物品定义 | [^220] |
| Base.BigGasTank | 配件引用缺少有效物品定义 | [^267] |
| Base.BigGasTank | 配件引用缺少有效物品定义 | [^268] |
| Base.BigGasTank | 配件引用缺少有效物品定义 | [^269] |
| Base.BigGasTank | 配件引用缺少有效物品定义 | [^270] |
| Base.BigGasTank | 配件引用缺少有效物品定义 | [^271] |
| Base.BigGasTank | 配件引用缺少有效物品定义 | [^272] |
| Base.BigGasTank | 配件引用缺少有效物品定义 | [^273] |
| Base.BigGasTank | 配件引用缺少有效物品定义 | [^274] |
| Base.BigGasTank | 配件引用缺少有效物品定义 | [^275] |
| Base.BigTrunk | 配件引用缺少有效物品定义 | [^276] |
| Base.BigTrunk | 配件引用缺少有效物品定义 | [^277] |
| Base.CarBattery | 配件引用缺少有效物品定义 | [^201] |
| Base.EngineDoor | 配件引用缺少有效物品定义 | [^217] |
| Base.EngineDoor | 配件引用缺少有效物品定义 | [^278] |
| Base.EngineDoor | 配件引用缺少有效物品定义 | [^279] |
| Base.EngineDoor | 配件引用缺少有效物品定义 | [^280] |
| Base.EngineDoor | 配件引用缺少有效物品定义 | [^281] |
| Base.EngineDoor | 配件引用缺少有效物品定义 | [^282] |
| Base.EngineDoor | 配件引用缺少有效物品定义 | [^283] |
| Base.EngineDoor | 配件引用缺少有效物品定义 | [^284] |
| Base.EngineDoor | 配件引用缺少有效物品定义 | [^285] |
| Base.EngineDoor | 配件引用缺少有效物品定义 | [^286] |
| Base.EngineDoor | 配件引用缺少有效物品定义 | [^287] |
| Base.EngineDoor | 配件引用缺少有效物品定义 | [^288] |
| Base.FrontCarDoor | 配件引用缺少有效物品定义 | [^209] |
| Base.FrontCarDoor | 配件引用缺少有效物品定义 | [^208] |
| Base.FrontWindow | 配件引用缺少有效物品定义 | [^258] |
| Base.FrontWindow | 配件引用缺少有效物品定义 | [^257] |
| Base.GloveBox | 配件引用缺少有效物品定义 | [^289] |
| Base.GloveBox | 配件引用缺少有效物品定义 | [^221] |
| Base.GloveBox | 配件引用缺少有效物品定义 | [^290] |
| Base.GloveBox | 配件引用缺少有效物品定义 | [^291] |
| Base.ModernBrake | 配件引用缺少有效物品定义 | [^202] |
| Base.ModernBrake | 配件引用缺少有效物品定义 | [^292] |
| Base.ModernBrake | 配件引用缺少有效物品定义 | [^293] |
| Base.ModernBrake | 配件引用缺少有效物品定义 | [^294] |
| Base.ModernBrake | 配件引用缺少有效物品定义 | [^295] |
| Base.ModernBrake | 配件引用缺少有效物品定义 | [^296] |
| Base.ModernBrake | 配件引用缺少有效物品定义 | [^297] |
| Base.ModernBrake | 配件引用缺少有效物品定义 | [^298] |
| Base.ModernBrake | 配件引用缺少有效物品定义 | [^299] |
| Base.ModernCarMuffler | 配件引用缺少有效物品定义 | [^229] |
| Base.ModernCarMuffler | 配件引用缺少有效物品定义 | [^300] |
| Base.ModernCarMuffler | 配件引用缺少有效物品定义 | [^301] |
| Base.ModernCarMuffler | 配件引用缺少有效物品定义 | [^302] |
| Base.ModernCarMuffler | 配件引用缺少有效物品定义 | [^303] |
| Base.ModernCarMuffler | 配件引用缺少有效物品定义 | [^304] |
| Base.ModernCarMuffler | 配件引用缺少有效物品定义 | [^305] |
| Base.ModernCarMuffler | 配件引用缺少有效物品定义 | [^306] |
| Base.ModernCarMuffler | 配件引用缺少有效物品定义 | [^307] |
| Base.ModernSuspension | 配件引用缺少有效物品定义 | [^241] |
| Base.ModernSuspension | 配件引用缺少有效物品定义 | [^308] |
| Base.ModernSuspension | 配件引用缺少有效物品定义 | [^309] |
| Base.ModernSuspension | 配件引用缺少有效物品定义 | [^310] |
| Base.ModernSuspension | 配件引用缺少有效物品定义 | [^311] |
| Base.ModernSuspension | 配件引用缺少有效物品定义 | [^312] |
| Base.ModernSuspension | 配件引用缺少有效物品定义 | [^313] |
| Base.ModernSuspension | 配件引用缺少有效物品定义 | [^314] |
| Base.ModernSuspension | 配件引用缺少有效物品定义 | [^315] |
| Base.ModernTire | 配件引用缺少有效物品定义 | [^247] |
| Base.NormalBrake | 配件引用缺少有效物品定义 | [^202] |
| Base.NormalBrake | 配件引用缺少有效物品定义 | [^292] |
| Base.NormalBrake | 配件引用缺少有效物品定义 | [^293] |
| Base.NormalBrake | 配件引用缺少有效物品定义 | [^294] |
| Base.NormalBrake | 配件引用缺少有效物品定义 | [^295] |
| Base.NormalBrake | 配件引用缺少有效物品定义 | [^296] |
| Base.NormalBrake | 配件引用缺少有效物品定义 | [^297] |
| Base.NormalBrake | 配件引用缺少有效物品定义 | [^298] |
| Base.NormalBrake | 配件引用缺少有效物品定义 | [^299] |
| Base.NormalCarMuffler | 配件引用缺少有效物品定义 | [^229] |
| Base.NormalCarMuffler | 配件引用缺少有效物品定义 | [^300] |
| Base.NormalCarMuffler | 配件引用缺少有效物品定义 | [^301] |
| Base.NormalCarMuffler | 配件引用缺少有效物品定义 | [^302] |
| Base.NormalCarMuffler | 配件引用缺少有效物品定义 | [^303] |
| Base.NormalCarMuffler | 配件引用缺少有效物品定义 | [^304] |
| Base.NormalCarMuffler | 配件引用缺少有效物品定义 | [^305] |
| Base.NormalCarMuffler | 配件引用缺少有效物品定义 | [^306] |
| Base.NormalCarMuffler | 配件引用缺少有效物品定义 | [^307] |
| Base.NormalGasTank | 配件引用缺少有效物品定义 | [^220] |
| Base.NormalGasTank | 配件引用缺少有效物品定义 | [^267] |
| Base.NormalGasTank | 配件引用缺少有效物品定义 | [^268] |
| Base.NormalGasTank | 配件引用缺少有效物品定义 | [^269] |
| Base.NormalGasTank | 配件引用缺少有效物品定义 | [^270] |
| Base.NormalGasTank | 配件引用缺少有效物品定义 | [^271] |
| Base.NormalGasTank | 配件引用缺少有效物品定义 | [^272] |
| Base.NormalGasTank | 配件引用缺少有效物品定义 | [^273] |
| Base.NormalGasTank | 配件引用缺少有效物品定义 | [^274] |
| Base.NormalGasTank | 配件引用缺少有效物品定义 | [^275] |
| Base.NormalSuspension | 配件引用缺少有效物品定义 | [^241] |
| Base.NormalSuspension | 配件引用缺少有效物品定义 | [^308] |
| Base.NormalSuspension | 配件引用缺少有效物品定义 | [^309] |
| Base.NormalSuspension | 配件引用缺少有效物品定义 | [^310] |
| Base.NormalSuspension | 配件引用缺少有效物品定义 | [^311] |
| Base.NormalSuspension | 配件引用缺少有效物品定义 | [^312] |
| Base.NormalSuspension | 配件引用缺少有效物品定义 | [^313] |
| Base.NormalSuspension | 配件引用缺少有效物品定义 | [^314] |
| Base.NormalSuspension | 配件引用缺少有效物品定义 | [^315] |
| Base.NormalTire | 配件引用缺少有效物品定义 | [^247] |
| Base.NormalTrunk | 配件引用缺少有效物品定义 | [^252] |
| Base.NormalTrunk | 配件引用缺少有效物品定义 | [^316] |
| Base.NormalTrunk | 配件引用缺少有效物品定义 | [^317] |
| Base.NormalTrunk | 配件引用缺少有效物品定义 | [^318] |
| Base.NormalTrunk | 配件引用缺少有效物品定义 | [^319] |
| Base.NormalTrunk | 配件引用缺少有效物品定义 | [^320] |
| Base.OldBrake | 配件引用缺少有效物品定义 | [^202] |
| Base.OldBrake | 配件引用缺少有效物品定义 | [^292] |
| Base.OldBrake | 配件引用缺少有效物品定义 | [^293] |
| Base.OldBrake | 配件引用缺少有效物品定义 | [^294] |
| Base.OldBrake | 配件引用缺少有效物品定义 | [^295] |
| Base.OldBrake | 配件引用缺少有效物品定义 | [^296] |
| Base.OldBrake | 配件引用缺少有效物品定义 | [^297] |
| Base.OldBrake | 配件引用缺少有效物品定义 | [^298] |
| Base.OldBrake | 配件引用缺少有效物品定义 | [^299] |
| Base.OldCarMuffler | 配件引用缺少有效物品定义 | [^229] |
| Base.OldCarMuffler | 配件引用缺少有效物品定义 | [^300] |
| Base.OldCarMuffler | 配件引用缺少有效物品定义 | [^301] |
| Base.OldCarMuffler | 配件引用缺少有效物品定义 | [^302] |
| Base.OldCarMuffler | 配件引用缺少有效物品定义 | [^303] |
| Base.OldCarMuffler | 配件引用缺少有效物品定义 | [^304] |
| Base.OldCarMuffler | 配件引用缺少有效物品定义 | [^305] |
| Base.OldCarMuffler | 配件引用缺少有效物品定义 | [^306] |
| Base.OldCarMuffler | 配件引用缺少有效物品定义 | [^307] |
| Base.OldTire | 配件引用缺少有效物品定义 | [^247] |
| Base.RearCarDoor | 配件引用缺少有效物品定义 | [^214] |
| Base.RearCarDoor | 配件引用缺少有效物品定义 | [^215] |
| Base.RearWindow | 配件引用缺少有效物品定义 | [^261] |
| Base.RearWindow | 配件引用缺少有效物品定义 | [^262] |
| Base.RearWindow | 配件引用缺少有效物品定义 | [^321] |
| Base.RearWindow | 配件引用缺少有效物品定义 | [^322] |
| Base.RearWindshield | 配件引用缺少有效物品定义 | [^265] |
| Base.RearWindshield | 配件引用缺少有效物品定义 | [^323] |
| Base.SmallGasTank | 配件引用缺少有效物品定义 | [^220] |
| Base.SmallGasTank | 配件引用缺少有效物品定义 | [^267] |
| Base.SmallGasTank | 配件引用缺少有效物品定义 | [^268] |
| Base.SmallGasTank | 配件引用缺少有效物品定义 | [^269] |
| Base.SmallGasTank | 配件引用缺少有效物品定义 | [^270] |
| Base.SmallGasTank | 配件引用缺少有效物品定义 | [^271] |
| Base.SmallGasTank | 配件引用缺少有效物品定义 | [^272] |
| Base.SmallGasTank | 配件引用缺少有效物品定义 | [^273] |
| Base.SmallGasTank | 配件引用缺少有效物品定义 | [^274] |
| Base.SmallGasTank | 配件引用缺少有效物品定义 | [^275] |
| Base.SmallTrunk | 配件引用缺少有效物品定义 | [^324] |
| Base.SmallTrunk | 配件引用缺少有效物品定义 | [^325] |
| Base.SmallTrunk | 配件引用缺少有效物品定义 | [^326] |
| Base.TrunkDoor | 配件引用缺少有效物品定义 | [^254] |
| Base.TrunkDoor | 配件引用缺少有效物品定义 | [^327] |
| Base.TrunkDoor | 配件引用缺少有效物品定义 | [^328] |
| Base.TrunkDoor | 配件引用缺少有效物品定义 | [^329] |
| Base.TrunkDoor | 配件引用缺少有效物品定义 | [^330] |
| Base.TrunkDoor | 配件引用缺少有效物品定义 | [^331] |
| Base.TrunkDoor | 配件引用缺少有效物品定义 | [^332] |
| Base.Windshield | 配件引用缺少有效物品定义 | [^263] |

</details>


## 概览

| Mod ID / 文件夹 | 分发端 | 版本 | 选择的 mod.info | 原件范围 → 当前范围 |
| --- | --- | --- | --- | --- |
| `ShiftYourGear` / `ShiftYourGear` | both（双端） | 0.1.37 | `42/mod.info` | 42.21.0 … - → 42.21.0 … - |

原件体积 55.4 MB；体积按完整目录统计，与当前内容定义数分开。
工作坊：[查看作者页面](https://steamcommunity.com/sharedfiles/filedetails/?id=3838041847)。

## 证据与使用边界

**verified：有效源码静态确认。** 每个当前可复制 ID 均来自所选版本的定义；这不保证游戏已成功注册、生成、安装或联机同步。
挑战者 5 个车辆中文名另有 Owner 截图确认；本轮没有启动游戏。译文冲突、动态 Lua 内容和玩法效果仍需 Owner 游戏内核实。
以下人工记录保留原始语境；其中旧组合、旧数量和旧候选状态仅供追溯，当前统计与归属以上表和 profile 为准。

<!-- retained:start -->
## 依赖与冲突

- 需要：`Viewpoint`、`ZombieBuddy`（`ZBVersionMin=2.3.4`）
- `loadModAfter=ImmersiveDriving`：必须排在本包 `ImmersiveDriving` 之后
- 作者提示：若 `ViewpointDrivingGearPatch` 或 `ViewpointDriveByShooting` 生效，内置的 Immersive Driving 兼容补丁会自动关闭，避免重复打补丁（本包两者都装，属于预期路径）
- 本包没有下载 `ShiftYourGearMPTest` 子 mod，作者要求保持关闭，正好一致

## 双端与联机

作者标注多人 **beta**：其他玩家能看到换挡手与挡杆。要求双端同版本。本包 `distribution: both`。

## 实测与排查

**planned：仅完成依赖、版本与加载顺序静态检查（`check` 0 problem）与同步落盘。** 未启动游戏；换挡手势、挡杆可见性与联机同步均未验证。作者自述原版车已测，改装车、分屏、拖挂、烧毁车不在测试范围。
<!-- retained:end -->

## 静态来源

路径相对 `A004/workspace/mods_library/`；`Overlay/<文件夹>/` 指 `A004/workspace/patches/mods/<文件夹>/`，`游戏原版/` 指当前 B42.22 客户端 Game 目录。翻译来源列出所有候选，未按加载顺序擅自消解异文。

[^1]: `3838041847/mods/ShiftYourGear/42/media/scripts/gsa_carnormal_standard_gearbox.txt:3`
[^2]: `3838041847/mods/ShiftYourGear/42/media/scripts/gsa_fleet_carluxury.txt:3`
[^3]: `3838041847/mods/ShiftYourGear/42/media/scripts/gsa_fleet_carstationwagon.txt:3`
[^4]: `3838041847/mods/ShiftYourGear/42/media/scripts/gsa_fleet_carstationwagon2.txt:3`
[^5]: `3838041847/mods/ShiftYourGear/42/media/scripts/gsa_fleet_racecar12.txt:3`
[^6]: `3838041847/mods/ShiftYourGear/42/media/scripts/gsa_fleet_smallcar02.txt:3`
[^7]: `3838041847/mods/ShiftYourGear/42/media/scripts/gsa_fleet_sportscar.txt:3`
[^8]: `3838041847/mods/ShiftYourGear/42/media/scripts/gsa_fleet_sportscar_ez.txt:3`
[^9]: `3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin01.txt:3`
[^10]: `3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin03.txt:3`
[^11]: `3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin04.txt:3`
[^12]: `3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin05.txt:3`
[^13]: `3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin06.txt:3`
[^14]: `3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin07.txt:3`
[^15]: `3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin08.txt:3`
[^16]: `3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin09.txt:3`
[^17]: `3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin10.txt:3`
[^18]: `3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin11.txt:3`
[^19]: `3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin12.txt:3`
[^20]: `3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin13.txt:3`
[^21]: `3838041847/mods/ShiftYourGear/42/media/scripts/gsa_moderncar02_gearbox.txt:3`
[^22]: `3838041847/mods/ShiftYourGear/42/media/scripts/gsa_moderncar_first_gear.txt:3`
[^23]: `3838041847/mods/ShiftYourGear/42/media/scripts/gsa_moderncar_martin_gearbox.txt:3`
[^24]: `3838041847/mods/ShiftYourGear/42/media/scripts/gsa_pickup_heavy_gearbox.txt:3`
[^25]: `3838041847/mods/ShiftYourGear/42/media/scripts/gsa_police_nyala_gearbox.txt:3`
[^26]: `3838041847/mods/ShiftYourGear/42/media/scripts/gsa_smallcar_gearbox.txt:3`
[^27]: `游戏原版/media/scripts/generated/items/normal.txt:12363`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_police_nyala_gearbox.txt:264`
[^28]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:447`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:162`
[^29]: `游戏原版/media/scripts/generated/items/normal.txt:12408`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin03.txt:193`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin08.txt:206`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin09.txt:214`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin10.txt:196`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin11.txt:213`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin12.txt:189`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin13.txt:267`
[^30]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:448`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:163`
[^31]: `游戏原版/media/scripts/generated/items/normal.txt:12453`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_fleet_sportscar.txt:203`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_fleet_sportscar_ez.txt:213`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_moderncar_martin_gearbox.txt:273`
[^32]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:449`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:164`
[^33]: `游戏原版/media/scripts/generated/items/normal.txt:12552`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin11.txt:191`
[^34]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:451`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:166`
[^35]: `游戏原版/media/scripts/generated/items/drainable.txt:2349`；`游戏原版/media/scripts/generated/vehicles/template_battery.txt:5`
[^36]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:969`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:379`
[^37]: `游戏原版/media/scripts/generated/items/drainable.txt:2368`；`游戏原版/media/scripts/generated/vehicles/template_battery.txt:5`
[^38]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:970`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:380`
[^39]: `游戏原版/media/scripts/generated/items/drainable.txt:2387`；`游戏原版/media/scripts/generated/vehicles/template_battery.txt:5`
[^40]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:971`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:381`
[^41]: `游戏原版/media/scripts/generated/items/normal.txt:12935`；`游戏原版/media/scripts/generated/vehicles/template_engine_door.txt:5`
[^42]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1529`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:597`
[^43]: `游戏原版/media/scripts/generated/items/normal.txt:12948`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin03.txt:217`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin08.txt:230`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin09.txt:238`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin10.txt:220`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin11.txt:237`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin12.txt:213`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin13.txt:291`
[^44]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1530`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:598`
[^45]: `游戏原版/media/scripts/generated/items/normal.txt:12961`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_fleet_sportscar.txt:227`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_fleet_sportscar_ez.txt:237`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_moderncar_martin_gearbox.txt:297`
[^46]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1531`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:599`
[^47]: `游戏原版/media/scripts/generated/items/normal.txt:12818`；`游戏原版/media/scripts/generated/vehicles/template_door.txt:5`；`游戏原版/media/scripts/generated/vehicles/template_door.txt:23`
[^48]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1658`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:648`
[^49]: `游戏原版/media/scripts/generated/items/normal.txt:12857`；`游戏原版/media/scripts/generated/vehicles/template_door.txt:5`；`游戏原版/media/scripts/generated/vehicles/template_door.txt:23`
[^50]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1659`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:649`
[^51]: `游戏原版/media/scripts/generated/items/normal.txt:12896`；`游戏原版/media/scripts/generated/vehicles/template_door.txt:5`；`游戏原版/media/scripts/generated/vehicles/template_door.txt:23`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_fleet_sportscar_ez.txt:323`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_fleet_sportscar_ez.txt:352`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_moderncar_martin_gearbox.txt:403`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_moderncar_martin_gearbox.txt:434`
[^52]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1660`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:650`
[^53]: `游戏原版/media/scripts/generated/items/normal.txt:12678`；`游戏原版/media/scripts/generated/vehicles/template_window.txt:6`；`游戏原版/media/scripts/generated/vehicles/template_window.txt:14`
[^54]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1661`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:651`
[^55]: `游戏原版/media/scripts/generated/items/normal.txt:12734`；`游戏原版/media/scripts/generated/vehicles/template_window.txt:6`；`游戏原版/media/scripts/generated/vehicles/template_window.txt:14`
[^56]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1662`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:652`
[^57]: `游戏原版/media/scripts/generated/items/normal.txt:12790`；`游戏原版/media/scripts/generated/vehicles/template_window.txt:6`；`游戏原版/media/scripts/generated/vehicles/template_window.txt:14`
[^58]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1663`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:653`
[^59]: `游戏原版/media/scripts/generated/items/normal.txt:13013`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_police_nyala_gearbox.txt:257`
[^60]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1775`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:686`
[^61]: `游戏原版/media/scripts/generated/items/normal.txt:13025`；`游戏原版/media/scripts/generated/vehicles/template_glovebox.txt:5`
[^62]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1776`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:687`
[^63]: `游戏原版/media/scripts/generated/items/normal.txt:13037`；`游戏原版/media/scripts/generated/vehicles/template_glovebox.txt:5`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_fleet_sportscar_ez.txt:198`
[^64]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1777`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:688`
[^65]: `游戏原版/media/scripts/generated/items/radio.txt:203`；`游戏原版/media/scripts/generated/vehicles/template_radio_HAM.txt:5`
[^66]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:3000`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25094`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1908`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:3486`
[^67]: `游戏原版/media/scripts/generated/items/radio.txt:229`；`游戏原版/media/scripts/generated/vehicles/template_radio_HAM.txt:5`
[^68]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:7376`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25095`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1909`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:3487`
[^69]: `游戏原版/media/scripts/generated/items/radio.txt:255`；`游戏原版/media/scripts/generated/vehicles/template_radio_HAM.txt:5`
[^70]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:7377`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25096`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1910`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:3488`
[^71]: `游戏原版/media/scripts/generated/items/normal.txt:14596`；`游戏原版/media/scripts/generated/vehicles/vehicle_car_modern_martin_template.txt:5`
[^72]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2226`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:3679`
[^73]: `游戏原版/media/scripts/generated/items/normal.txt:14607`；`游戏原版/media/scripts/generated/vehicles/vehicle_car_modern_martin_template.txt:5`
[^74]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2227`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:3680`
[^75]: `游戏原版/media/scripts/generated/items/normal.txt:14618`；`游戏原版/media/scripts/generated/vehicles/vehicle_car_modern_martin_template.txt:5`
[^76]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2228`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:3681`
[^77]: `游戏原版/media/scripts/generated/items/normal.txt:4661`；`游戏原版/media/scripts/generated/vehicles/template_headlight.txt:25`；`游戏原版/media/scripts/generated/vehicles/vehicle_car_racecar_template.txt:126`
[^78]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:6727`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25103`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2563`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:965`
[^79]: `游戏原版/media/scripts/generated/items/normal.txt:12112`；`游戏原版/media/scripts/generated/vehicles/template_brake.txt:57`
[^80]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2779`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1049`
[^81]: `游戏原版/media/scripts/generated/items/normal.txt:12163`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin03.txt:277`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin08.txt:311`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin09.txt:313`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin10.txt:295`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin11.txt:312`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin12.txt:281`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin13.txt:370`
[^82]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2780`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1050`
[^83]: `游戏原版/media/scripts/generated/items/normal.txt:12214`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_fleet_sportscar.txt:295`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_fleet_sportscar_ez.txt:381`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_moderncar_martin_gearbox.txt:527`
[^84]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2781`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1051`
[^85]: `游戏原版/media/scripts/generated/items/normal.txt:13121`；`游戏原版/media/scripts/generated/vehicles/template_muffler.txt:5`
[^86]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2782`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1052`
[^87]: `游戏原版/media/scripts/generated/items/normal.txt:13166`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin03.txt:206`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin08.txt:219`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin09.txt:227`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin10.txt:209`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin11.txt:226`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin12.txt:202`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin13.txt:280`
[^88]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2783`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1053`
[^89]: `游戏原版/media/scripts/generated/items/normal.txt:13211`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_fleet_sportscar.txt:216`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_fleet_sportscar_ez.txt:226`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_moderncar_martin_gearbox.txt:286`
[^90]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2784`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1054`
[^91]: `游戏原版/media/scripts/generated/items/normal.txt:12248`；`游戏原版/media/scripts/generated/vehicles/template_suspension.txt:57`
[^92]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2785`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1055`
[^93]: `游戏原版/media/scripts/generated/items/normal.txt:12282`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin03.txt:290`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin08.txt:324`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin09.txt:326`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin10.txt:308`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin11.txt:325`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin12.txt:294`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin13.txt:383`
[^94]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2786`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1056`
[^95]: `游戏原版/media/scripts/generated/items/normal.txt:12316`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_fleet_sportscar.txt:308`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_fleet_sportscar_ez.txt:394`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_moderncar_martin_gearbox.txt:540`
[^96]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2787`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1057`
[^97]: `游戏原版/media/scripts/generated/items/normal.txt:11938`；`游戏原版/media/scripts/generated/vehicles/template_tire.txt:45`
[^98]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2788`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1058`
[^99]: `游戏原版/media/scripts/generated/items/normal.txt:11998`；`游戏原版/media/scripts/generated/vehicles/template_tire.txt:45`
[^100]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2789`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1059`
[^101]: `游戏原版/media/scripts/generated/items/normal.txt:12058`；`游戏原版/media/scripts/generated/vehicles/template_tire.txt:45`
[^102]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2790`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1060`
[^103]: `游戏原版/media/scripts/generated/items/normal.txt:12095`；`游戏原版/media/scripts/generated/vehicles/template_brake.txt:57`
[^104]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3218`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1134`
[^105]: `游戏原版/media/scripts/generated/items/normal.txt:12146`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin03.txt:277`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin08.txt:311`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin09.txt:313`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin10.txt:295`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin11.txt:312`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin12.txt:281`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin13.txt:370`
[^106]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3219`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1135`
[^107]: `游戏原版/media/scripts/generated/items/normal.txt:12197`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_fleet_sportscar.txt:295`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_fleet_sportscar_ez.txt:381`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_moderncar_martin_gearbox.txt:527`
[^108]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3220`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1136`
[^109]: `游戏原版/media/scripts/generated/items/normal.txt:13106`；`游戏原版/media/scripts/generated/vehicles/template_muffler.txt:5`
[^110]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3221`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1137`
[^111]: `游戏原版/media/scripts/generated/items/normal.txt:13151`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin03.txt:206`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin08.txt:219`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin09.txt:227`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin10.txt:209`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin11.txt:226`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin12.txt:202`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin13.txt:280`
[^112]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3222`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1138`
[^113]: `游戏原版/media/scripts/generated/items/normal.txt:13196`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_fleet_sportscar.txt:216`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_fleet_sportscar_ez.txt:226`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_moderncar_martin_gearbox.txt:286`
[^114]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3223`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1139`
[^115]: `游戏原版/media/scripts/generated/items/normal.txt:12348`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_police_nyala_gearbox.txt:264`
[^116]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3227`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1143`
[^117]: `游戏原版/media/scripts/generated/items/normal.txt:12393`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin03.txt:193`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin08.txt:206`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin09.txt:214`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin10.txt:196`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin11.txt:213`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin12.txt:189`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin13.txt:267`
[^118]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3228`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1144`
[^119]: `游戏原版/media/scripts/generated/items/normal.txt:12438`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_fleet_sportscar.txt:203`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_fleet_sportscar_ez.txt:213`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_moderncar_martin_gearbox.txt:273`
[^120]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3229`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1145`
[^121]: `游戏原版/media/scripts/generated/items/normal.txt:12231`；`游戏原版/media/scripts/generated/vehicles/template_suspension.txt:57`
[^122]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3230`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1146`
[^123]: `游戏原版/media/scripts/generated/items/normal.txt:12265`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin03.txt:290`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin08.txt:324`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin09.txt:326`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin10.txt:308`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin11.txt:325`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin12.txt:294`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin13.txt:383`
[^124]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3231`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1147`
[^125]: `游戏原版/media/scripts/generated/items/normal.txt:12299`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_fleet_sportscar.txt:308`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_fleet_sportscar_ez.txt:394`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_moderncar_martin_gearbox.txt:540`
[^126]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3232`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1148`
[^127]: `游戏原版/media/scripts/generated/items/normal.txt:11918`；`游戏原版/media/scripts/generated/vehicles/template_tire.txt:45`
[^128]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3233`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1149`
[^129]: `游戏原版/media/scripts/generated/items/normal.txt:11978`；`游戏原版/media/scripts/generated/vehicles/template_tire.txt:45`
[^130]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3234`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1150`
[^131]: `游戏原版/media/scripts/generated/items/normal.txt:12038`；`游戏原版/media/scripts/generated/vehicles/template_tire.txt:45`
[^132]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3235`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1151`
[^133]: `游戏原版/media/scripts/generated/items/normal.txt:12482`；`游戏原版/media/scripts/generated/vehicles/template_trunk.txt:5`
[^134]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3236`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1152`
[^135]: `游戏原版/media/scripts/generated/items/normal.txt:12538`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin03.txt:173`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin08.txt:182`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin09.txt:193`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin10.txt:175`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin12.txt:168`
[^136]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3237`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1153`
[^137]: `游戏原版/media/scripts/generated/items/normal.txt:12580`；`游戏原版/media/scripts/generated/vehicles/template_trunk.txt:5`
[^138]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3238`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1154`
[^139]: `游戏原版/media/scripts/generated/items/normal.txt:12078`；`游戏原版/media/scripts/generated/vehicles/template_brake.txt:57`
[^140]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3254`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1164`
[^141]: `游戏原版/media/scripts/generated/items/normal.txt:12129`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin03.txt:277`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin08.txt:311`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin09.txt:313`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin10.txt:295`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin11.txt:312`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin12.txt:281`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin13.txt:370`
[^142]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3255`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1165`
[^143]: `游戏原版/media/scripts/generated/items/normal.txt:12180`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_fleet_sportscar.txt:295`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_fleet_sportscar_ez.txt:381`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_moderncar_martin_gearbox.txt:527`
[^144]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3256`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1166`
[^145]: `游戏原版/media/scripts/generated/items/normal.txt:13091`；`游戏原版/media/scripts/generated/vehicles/template_muffler.txt:5`
[^146]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3257`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1167`
[^147]: `游戏原版/media/scripts/generated/items/normal.txt:13136`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin03.txt:206`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin08.txt:219`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin09.txt:227`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin10.txt:209`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin11.txt:226`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin12.txt:202`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin13.txt:280`
[^148]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3258`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1168`
[^149]: `游戏原版/media/scripts/generated/items/normal.txt:13181`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_fleet_sportscar.txt:216`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_fleet_sportscar_ez.txt:226`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_moderncar_martin_gearbox.txt:286`
[^150]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3259`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1169`
[^151]: `游戏原版/media/scripts/generated/items/normal.txt:11898`；`游戏原版/media/scripts/generated/vehicles/template_tire.txt:45`
[^152]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3261`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1170`
[^153]: `游戏原版/media/scripts/generated/items/normal.txt:11958`；`游戏原版/media/scripts/generated/vehicles/template_tire.txt:45`
[^154]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3262`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1171`
[^155]: `游戏原版/media/scripts/generated/items/normal.txt:12018`；`游戏原版/media/scripts/generated/vehicles/template_tire.txt:45`
[^156]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3263`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1172`
[^157]: `游戏原版/media/scripts/generated/items/radio.txt:308`；`游戏原版/media/scripts/generated/vehicles/template_radio.txt:5`
[^158]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:7374`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25092`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3645`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:5128`
[^159]: `游戏原版/media/scripts/generated/items/radio.txt:335`；`游戏原版/media/scripts/generated/vehicles/template_radio.txt:5`
[^160]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:7375`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25093`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3649`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:5132`
[^161]: `游戏原版/media/scripts/generated/items/radio.txt:361`；`游戏原版/media/scripts/generated/vehicles/template_radio.txt:5`
[^162]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:3001`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25091`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3651`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:5134`
[^163]: `游戏原版/media/scripts/generated/items/normal.txt:12831`；`游戏原版/media/scripts/generated/vehicles/template_door.txt:77`；`游戏原版/media/scripts/generated/vehicles/template_door.txt:95`
[^164]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3667`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1332`
[^165]: `游戏原版/media/scripts/generated/items/normal.txt:12870`；`游戏原版/media/scripts/generated/vehicles/template_door.txt:41`；`游戏原版/media/scripts/generated/vehicles/template_door.txt:59`
[^166]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3668`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1333`
[^167]: `游戏原版/media/scripts/generated/items/normal.txt:12909`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_moderncar_martin_gearbox.txt:465`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_moderncar_martin_gearbox.txt:496`
[^168]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3669`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1334`
[^169]: `游戏原版/media/scripts/generated/items/normal.txt:12692`；`游戏原版/media/scripts/generated/vehicles/template_window.txt:38`；`游戏原版/media/scripts/generated/vehicles/template_window.txt:47`
[^170]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3673`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1338`
[^171]: `游戏原版/media/scripts/generated/items/normal.txt:12748`；`游戏原版/media/scripts/generated/vehicles/template_window.txt:22`；`游戏原版/media/scripts/generated/vehicles/template_window.txt:30`
[^172]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3674`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1339`
[^173]: `游戏原版/media/scripts/generated/items/normal.txt:12804`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_moderncar_martin_gearbox.txt:374`；`游戏原版/media/scripts/generated/vehicles/template_window.txt:47`
[^174]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3675`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1340`
[^175]: `游戏原版/media/scripts/generated/items/normal.txt:12664`；`游戏原版/media/scripts/generated/vehicles/template_windshield.txt:57`
[^176]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3676`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1341`
[^177]: `游戏原版/media/scripts/generated/items/normal.txt:12720`；`游戏原版/media/scripts/generated/vehicles/template_windshield.txt:57`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin08.txt:268`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin09.txt:276`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin10.txt:258`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin11.txt:275`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin12.txt:251`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin13.txt:329`
[^178]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3677`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1342`
[^179]: `游戏原版/media/scripts/generated/items/normal.txt:12776`；`游戏原版/media/scripts/generated/vehicles/template_windshield.txt:57`
[^180]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3678`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1343`
[^181]: `游戏原版/media/scripts/generated/items/normal.txt:12333`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_police_nyala_gearbox.txt:264`
[^182]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:4151`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1542`
[^183]: `游戏原版/media/scripts/generated/items/normal.txt:12378`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin03.txt:193`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin08.txt:206`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin09.txt:214`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin10.txt:196`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin11.txt:213`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin12.txt:189`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin13.txt:267`
[^184]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:4152`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1543`
[^185]: `游戏原版/media/scripts/generated/items/normal.txt:12423`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_fleet_sportscar.txt:203`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_fleet_sportscar_ez.txt:213`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_moderncar_martin_gearbox.txt:273`
[^186]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:4153`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1544`
[^187]: `游戏原版/media/scripts/generated/items/normal.txt:12566`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_fleet_sportscar.txt:186`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_fleet_sportscar_ez.txt:181`
[^188]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:4164`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1548`
[^189]: `游戏原版/media/scripts/generated/items/normal.txt:12974`；`游戏原版/media/scripts/generated/vehicles/template_trunk_door.txt:5`
[^190]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:4625`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1733`
[^191]: `游戏原版/media/scripts/generated/items/normal.txt:13000`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_fleet_sportscar.txt:175`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_fleet_sportscar_ez.txt:170`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_moderncar_martin_gearbox.txt:213`
[^192]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:4627`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1735`
[^193]: `游戏原版/media/scripts/generated/items/normal.txt:12510`；`3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin13.txt:243`
[^194]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:4762`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1797`
[^195]: `游戏原版/media/scripts/generated/items/normal.txt:12650`；`游戏原版/media/scripts/generated/vehicles/template_windshield.txt:5`
[^196]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:4891`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1863`
[^197]: `游戏原版/media/scripts/generated/items/normal.txt:12706`；`游戏原版/media/scripts/generated/vehicles/template_windshield.txt:5`
[^198]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:4892`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1864`
[^199]: `游戏原版/media/scripts/generated/items/normal.txt:12762`；`游戏原版/media/scripts/generated/vehicles/template_windshield.txt:5`
[^200]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:4893`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1865`
[^201]: `游戏原版/media/scripts/generated/vehicles/template_battery.txt:5`
[^202]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:57`
[^203]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:5`
[^204]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:18`
[^205]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:31`
[^206]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:44`
[^207]: `游戏原版/media/scripts/generated/vehicles/vehicle_car_luxury_template.txt:233`
[^208]: `游戏原版/media/scripts/generated/vehicles/template_door.txt:5`
[^209]: `游戏原版/media/scripts/generated/vehicles/template_door.txt:23`
[^210]: `游戏原版/media/scripts/generated/vehicles/template_door.txt:41`
[^211]: `游戏原版/media/scripts/generated/vehicles/template_door.txt:59`
[^212]: `游戏原版/media/scripts/generated/vehicles/vehicle_stepvan_template.txt:232`
[^213]: `游戏原版/media/scripts/generated/vehicles/template_sounds_van.txt:37`
[^214]: `游戏原版/media/scripts/generated/vehicles/template_door.txt:77`
[^215]: `游戏原版/media/scripts/generated/vehicles/template_door.txt:95`
[^216]: `游戏原版/media/scripts/generated/vehicles/template_engine.txt:5`
[^217]: `游戏原版/media/scripts/generated/vehicles/template_engine_door.txt:5`
[^218]: `游戏原版/media/scripts/generated/vehicles/template_sounds_sports.txt:38`
[^219]: `3838041847/mods/ShiftYourGear/42/media/scripts/gsa_carnormal_standard_gearbox.txt:103`
[^220]: `游戏原版/media/scripts/generated/vehicles/template_gastank.txt:5`
[^221]: `游戏原版/media/scripts/generated/vehicles/vehicle_car_normal_template.txt:141`
[^222]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:25`
[^223]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:5`
[^224]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:15`
[^225]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:20`
[^226]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:10`
[^227]: `游戏原版/media/scripts/generated/vehicles/vehicle_car_normal_template.txt:148`
[^228]: `游戏原版/media/scripts/generated/vehicles/vehicle_car_modern_martin_template.txt:5`
[^229]: `游戏原版/media/scripts/generated/vehicles/template_muffler.txt:5`
[^230]: `游戏原版/media/scripts/generated/vehicles/vehicle_car_normal_template.txt:156`
[^231]: `游戏原版/media/scripts/generated/vehicles/template_radio.txt:5`
[^232]: `游戏原版/media/scripts/generated/vehicles/vehicle_car_racecar_template.txt:287`
[^233]: `游戏原版/media/scripts/generated/vehicles/vehicle_car_luxury_template.txt:141`
[^234]: `游戏原版/media/scripts/generated/vehicles/template_seat.txt:5`
[^235]: `游戏原版/media/scripts/generated/vehicles/template_seat.txt:14`
[^236]: `游戏原版/media/scripts/generated/vehicles/template_seat.txt:23`
[^237]: `游戏原版/media/scripts/generated/vehicles/template_seat.txt:32`
[^238]: `3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin08.txt:190`
[^239]: `游戏原版/media/scripts/generated/vehicles/template_seat.txt:41`
[^240]: `游戏原版/media/scripts/generated/vehicles/template_seat.txt:50`
[^241]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:57`
[^242]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:5`
[^243]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:18`
[^244]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:31`
[^245]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:44`
[^246]: `3838041847/mods/ShiftYourGear/42/media/scripts/gsa_moderncar_martin_gearbox.txt:553`
[^247]: `游戏原版/media/scripts/generated/vehicles/template_tire.txt:45`
[^248]: `游戏原版/media/scripts/generated/vehicles/template_tire.txt:5`
[^249]: `游戏原版/media/scripts/generated/vehicles/template_tire.txt:15`
[^250]: `游戏原版/media/scripts/generated/vehicles/template_tire.txt:25`
[^251]: `游戏原版/media/scripts/generated/vehicles/template_tire.txt:35`
[^252]: `游戏原版/media/scripts/generated/vehicles/template_trunk.txt:5`
[^253]: `3838041847/mods/ShiftYourGear/42/media/scripts/gsa_heavy_cabin03.txt:173`
[^254]: `游戏原版/media/scripts/generated/vehicles/template_trunk_door.txt:5`
[^255]: `游戏原版/media/scripts/generated/vehicles/template_sounds_sports.txt:49`
[^256]: `游戏原版/media/scripts/generated/vehicles/vehicle_car_luxury_template.txt:214`
[^257]: `游戏原版/media/scripts/generated/vehicles/template_window.txt:6`
[^258]: `游戏原版/media/scripts/generated/vehicles/template_window.txt:14`
[^259]: `游戏原版/media/scripts/generated/vehicles/template_window.txt:22`
[^260]: `游戏原版/media/scripts/generated/vehicles/template_window.txt:30`
[^261]: `游戏原版/media/scripts/generated/vehicles/template_window.txt:38`
[^262]: `游戏原版/media/scripts/generated/vehicles/template_window.txt:47`
[^263]: `游戏原版/media/scripts/generated/vehicles/template_windshield.txt:5`
[^264]: `游戏原版/media/scripts/generated/vehicles/vehicle_car_luxury_template.txt:203`
[^265]: `游戏原版/media/scripts/generated/vehicles/template_windshield.txt:57`
[^266]: `游戏原版/media/scripts/generated/vehicles/template_lightbar.txt:5`
[^267]: `游戏原版/media/scripts/generated/vehicles/vehicle_car_luxury_template.txt:152`
[^268]: `游戏原版/media/scripts/generated/vehicles/vehicle_car_modern02_template.txt:167`
[^269]: `游戏原版/media/scripts/generated/vehicles/vehicle_car_modern_template.txt:158`
[^270]: `游戏原版/media/scripts/generated/vehicles/vehicle_car_racecar_template.txt:169`
[^271]: `游戏原版/media/scripts/generated/vehicles/vehicle_car_stationwagon_template.txt:146`
[^272]: `游戏原版/media/scripts/generated/vehicles/vehicle_pickuptruck_template.txt:144`
[^273]: `游戏原版/media/scripts/generated/vehicles/vehicle_pickupvan_lights_ranger_template.txt:155`
[^274]: `游戏原版/media/scripts/generated/vehicles/vehicle_stepvan_template.txt:141`
[^275]: `游戏原版/media/scripts/generated/vehicles/vehicle_suv_template.txt:167`
[^276]: `游戏原版/media/scripts/generated/vehicles/vehicle_pickupvan_lights_ranger_template.txt:134`
[^277]: `游戏原版/media/scripts/generated/vehicles/vehicle_stepvan_template.txt:119`
[^278]: `游戏原版/media/scripts/generated/vehicles/vehicle_car_luxury_template.txt:176`
[^279]: `游戏原版/media/scripts/generated/vehicles/vehicle_car_modern02_template.txt:191`
[^280]: `游戏原版/media/scripts/generated/vehicles/vehicle_car_modern_template.txt:182`
[^281]: `游戏原版/media/scripts/generated/vehicles/vehicle_car_racecar_template.txt:193`
[^282]: `游戏原版/media/scripts/generated/vehicles/vehicle_car_small02_template.txt:177`
[^283]: `游戏原版/media/scripts/generated/vehicles/vehicle_car_small_template.txt:176`
[^284]: `游戏原版/media/scripts/generated/vehicles/vehicle_offroad_template.txt:158`
[^285]: `游戏原版/media/scripts/generated/vehicles/vehicle_pickuptruck_template.txt:168`
[^286]: `游戏原版/media/scripts/generated/vehicles/vehicle_pickupvan_lights_ranger_template.txt:179`
[^287]: `游戏原版/media/scripts/generated/vehicles/vehicle_stepvan_template.txt:165`
[^288]: `游戏原版/media/scripts/generated/vehicles/vehicle_suv_template.txt:191`
[^289]: `游戏原版/media/scripts/generated/vehicles/template_glovebox.txt:5`
[^290]: `游戏原版/media/scripts/generated/vehicles/vehicle_car_stationwagon_template.txt:139`
[^291]: `游戏原版/media/scripts/generated/vehicles/vehicle_offroad_template.txt:151`
[^292]: `游戏原版/media/scripts/generated/vehicles/vehicle_car_luxury_template.txt:244`
[^293]: `游戏原版/media/scripts/generated/vehicles/vehicle_car_modern02_template.txt:259`
[^294]: `游戏原版/media/scripts/generated/vehicles/vehicle_car_modern_template.txt:250`
[^295]: `游戏原版/media/scripts/generated/vehicles/vehicle_car_racecar_template.txt:261`
[^296]: `游戏原版/media/scripts/generated/vehicles/vehicle_pickuptruck_template.txt:228`
[^297]: `游戏原版/media/scripts/generated/vehicles/vehicle_pickupvan_lights_ranger_template.txt:239`
[^298]: `游戏原版/media/scripts/generated/vehicles/vehicle_stepvan_template.txt:240`
[^299]: `游戏原版/media/scripts/generated/vehicles/vehicle_suv_template.txt:251`
[^300]: `游戏原版/media/scripts/generated/vehicles/vehicle_car_luxury_template.txt:165`
[^301]: `游戏原版/media/scripts/generated/vehicles/vehicle_car_modern02_template.txt:180`
[^302]: `游戏原版/media/scripts/generated/vehicles/vehicle_car_modern_template.txt:171`
[^303]: `游戏原版/media/scripts/generated/vehicles/vehicle_car_racecar_template.txt:182`
[^304]: `游戏原版/media/scripts/generated/vehicles/vehicle_pickuptruck_template.txt:157`
[^305]: `游戏原版/media/scripts/generated/vehicles/vehicle_pickupvan_lights_ranger_template.txt:168`
[^306]: `游戏原版/media/scripts/generated/vehicles/vehicle_stepvan_template.txt:154`
[^307]: `游戏原版/media/scripts/generated/vehicles/vehicle_suv_template.txt:180`
[^308]: `游戏原版/media/scripts/generated/vehicles/vehicle_car_luxury_template.txt:257`
[^309]: `游戏原版/media/scripts/generated/vehicles/vehicle_car_modern02_template.txt:272`
[^310]: `游戏原版/media/scripts/generated/vehicles/vehicle_car_modern_template.txt:263`
[^311]: `游戏原版/media/scripts/generated/vehicles/vehicle_car_racecar_template.txt:274`
[^312]: `游戏原版/media/scripts/generated/vehicles/vehicle_pickuptruck_template.txt:241`
[^313]: `游戏原版/media/scripts/generated/vehicles/vehicle_pickupvan_lights_ranger_template.txt:252`
[^314]: `游戏原版/media/scripts/generated/vehicles/vehicle_stepvan_template.txt:253`
[^315]: `游戏原版/media/scripts/generated/vehicles/vehicle_suv_template.txt:264`
[^316]: `游戏原版/media/scripts/generated/vehicles/vehicle_car_modern02_template.txt:147`
[^317]: `游戏原版/media/scripts/generated/vehicles/vehicle_car_racecar_template.txt:296`
[^318]: `游戏原版/media/scripts/generated/vehicles/vehicle_car_stationwagon_template.txt:131`
[^319]: `游戏原版/media/scripts/generated/vehicles/vehicle_pickuptruck_template.txt:124`
[^320]: `游戏原版/media/scripts/generated/vehicles/vehicle_suv_template.txt:147`
[^321]: `游戏原版/media/scripts/generated/vehicles/template_window_nodoor.txt:29`
[^322]: `游戏原版/media/scripts/generated/vehicles/template_window_nodoor.txt:35`
[^323]: `游戏原版/media/scripts/generated/vehicles/vehicle_stepvan_template.txt:203`
[^324]: `游戏原版/media/scripts/generated/vehicles/vehicle_car_small02_template.txt:132`
[^325]: `游戏原版/media/scripts/generated/vehicles/vehicle_car_small_template.txt:130`
[^326]: `游戏原版/media/scripts/generated/vehicles/vehicle_offroad_template.txt:127`
[^327]: `游戏原版/media/scripts/generated/vehicles/vehicle_car_luxury_template.txt:130`
[^328]: `游戏原版/media/scripts/generated/vehicles/vehicle_car_modern02_template.txt:136`
[^329]: `游戏原版/media/scripts/generated/vehicles/vehicle_car_modern_template.txt:136`
[^330]: `游戏原版/media/scripts/generated/vehicles/vehicle_car_racecar_template.txt:143`
[^331]: `游戏原版/media/scripts/generated/vehicles/vehicle_offroad_template.txt:123`
[^332]: `游戏原版/media/scripts/generated/vehicles/vehicle_suv_template.txt:136`
