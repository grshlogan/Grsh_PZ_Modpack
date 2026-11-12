# 小型 MPV（'89 Dodge Caravan）

家用 MPV 的开山作，能装人能装货，适合当撤离用车。

归属：**日常组合（玩法待验收）**；档案视图 `b422-compat`。
当前版本定义：**整车 3、本地物品定义 24、配方 23**；另引用共享物品 24。本地定义数含内部保留项，见独立列表；整车定义包括覆盖原版的条目，不等于新增车型数。

## 如何查找

- **生成整车**：在生成车辆菜单搜索下表完整 ID；显示译名时搜索中文列。联机管理命令用 `/addvehicle 完整ID`。
- **添加到背包**：普通物品、维修件、改装件都在添加物品菜单使用完整物品 ID；不要拿配方或内部槽位去刷车。
- **制作配方**：在制作界面查译名；配方 ID 用于排查，不是可放进背包的物品。
- 中文解释说明用途；只有翻译文件中找到的文字才称为游戏中文名。缺译保留脚本显示名，冲突列出各译文。

## 整车

| 完整生成车辆 ID | 当前中文名 / 名称状态 | 英文名或脚本名 | 变体说明 | 来源 |
| --- | --- | --- | --- | --- |
| `Base.89dodgeCaravan` | 89款道奇凯领[^1] | '89 Dodge Caravan[^2] | 脚本座位数 4；机修类型 1；具体外观与性能待游戏实刷 | [^3] |
| `Base.89dodgeCaravanLE` | 89款道奇凯领LE[^4] | '89 Dodge Caravan LE[^5] | 脚本座位数 6；机修类型 1；具体外观与性能待游戏实刷 | [^6] |
| `Base.89dodgeCaravanNomad` | 89款道奇凯领Nomad[^7] | '89 Dodge Caravan Nomad[^8] | 脚本座位数 3；机修类型 1；具体外观与性能待游戏实刷 | [^9] |

## 普通物品与书籍

| 完整物品 ID | 游戏显示名 / 名称状态 | 中文用途 / 类别 | 菜单 | 适用车辆与安装位置 | 来源 / 状态 |
| --- | --- | --- | --- | --- | --- |
| `Base.89dodgeCaravanMagazine` | 89 Dodge Caravan Auto Manual（未找到有效中文译文） | 阅读资料；脚本声明解锁：制作89款道奇凯领引擎盖（Base.89dodgeCaravanMakeHood）、制作89款道奇凯领前车门（Base.89dodgeCaravanMakeFrontDoor）、制作89款道奇凯领后车门（Base.89dodgeCaravanMakeRearDoor）、制作89款道奇凯领后备箱盖（Base.89dodgeCaravanMakeTrunkLid）、制作89款道奇凯领前座椅（Base.89dodgeCaravanMakeFrontSeat）、制作89款道奇凯领前挡风玻璃（Base.89dodgeCaravanMakeFrontWindshield）、制作89款道奇凯领前侧窗（Base.89dodgeCaravanMakeFrontSideWindow）、制作89款道奇凯领后侧窗（Base.89dodgeCaravanMakeRearSideWindow）、制作89款道奇凯领后挡风玻璃（Base.89dodgeCaravanMakeRearWindshield）、制作89款道奇凯领前挡风玻璃装甲（Base.89dodgeCaravanMakeFrontWindshieldArmor）、制作89款道奇凯领车顶行李架（Base.89dodgeCaravanMakeRoofrack）、制作89款道奇凯领挡泥板（Base.89dodgeCaravanMakeMudflaps）、制作89款道奇凯领侧踏板（Base.89dodgeCaravanMakeSidesteps） / 普通物品 / 书籍 | 添加物品 | 未定位整车安装关系 | 89dodgeCaravan[^10] |

## 维修配件

| 完整物品 ID | 游戏显示名 / 名称状态 | 中文用途 / 类别 | 菜单 | 适用车辆与安装位置 | 来源 / 状态 |
| --- | --- | --- | --- | --- | --- |
| `Base.89dodgeCaravanEngineDoor1` | 89 Dodge Caravan Hood（未找到有效中文译文） | 车辆安装件，用于引擎盖（EngineDoor）；适用车型见右列 / 维修配件 | 添加物品 | Base.89dodgeCaravan → EngineDoor；Base.89dodgeCaravanLE → EngineDoor；Base.89dodgeCaravanNomad → EngineDoor | 89dodgeCaravan[^11] |
| `Base.89dodgeCaravanFrontDoor1` | 89 Dodge Caravan Front Door（未找到有效中文译文） | 车辆安装件，用于车门（DoorFrontLeft）、车门（DoorFrontRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.89dodgeCaravan → DoorFrontLeft；Base.89dodgeCaravan → DoorFrontRight；Base.89dodgeCaravanLE → DoorFrontLeft；Base.89dodgeCaravanLE → DoorFrontRight；Base.89dodgeCaravanNomad → DoorFrontLeft；Base.89dodgeCaravanNomad → DoorFrontRight | 89dodgeCaravan[^12] |
| `Base.89dodgeCaravanFrontSideWindow1` | 89 Dodge Caravan Front Side Window（未找到有效中文译文） | 车辆安装件，用于车窗（WindowFrontLeft）、车窗（WindowFrontRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.89dodgeCaravan → WindowFrontLeft；Base.89dodgeCaravan → WindowFrontRight；Base.89dodgeCaravanLE → WindowFrontLeft；Base.89dodgeCaravanLE → WindowFrontRight；Base.89dodgeCaravanNomad → WindowFrontLeft；Base.89dodgeCaravanNomad → WindowFrontRight | 89dodgeCaravan[^13] |
| `Base.89dodgeCaravanMudflaps0` | 89 Dodge Caravan Mudflaps（未找到有效中文译文） | 车辆安装件，用于车辆安装位（DAMNMudflaps）；适用车型见右列 / 维修配件 | 添加物品 | Base.89dodgeCaravan → DAMNMudflaps；Base.89dodgeCaravanLE → DAMNMudflaps；Base.89dodgeCaravanNomad → DAMNMudflaps | 89dodgeCaravan[^14] |
| `Base.89dodgeCaravanRearSideWindow1` | 89 Dodge Caravan Rear Side Window（未找到有效中文译文） | 车辆安装件，用于车窗（WindowRearLeft）、车窗（WindowRearRight）、车窗（WindowBackLeft）、车窗（WindowBackRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.89dodgeCaravan → WindowRearLeft；Base.89dodgeCaravan → WindowRearRight；Base.89dodgeCaravan → WindowBackLeft；Base.89dodgeCaravan → WindowBackRight；Base.89dodgeCaravanLE → WindowRearLeft；Base.89dodgeCaravanLE → WindowRearRight；Base.89dodgeCaravanLE → WindowBackLeft；Base.89dodgeCaravanLE → WindowBackRight；Base.89dodgeCaravanNomad → WindowRearLeft；Base.89dodgeCaravanNomad → WindowRearRight；Base.89dodgeCaravanNomad → WindowBackLeft；Base.89dodgeCaravanNomad → WindowBackRight | 89dodgeCaravan[^15] |
| `Base.89dodgeCaravanSeat1` | 89 Dodge Caravan Seat（未找到有效中文译文） | 车辆安装件，用于座椅（SeatFrontLeft）、座椅（SeatFrontRight）、座椅（SeatRearLeft）、座椅（SeatRearRight）、座椅（SeatMiddleLeft）、座椅（SeatMiddleRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.89dodgeCaravan → SeatFrontLeft；Base.89dodgeCaravan → SeatFrontRight；Base.89dodgeCaravan → SeatRearLeft；Base.89dodgeCaravan → SeatRearRight；Base.89dodgeCaravanLE → SeatFrontLeft；Base.89dodgeCaravanLE → SeatFrontRight；Base.89dodgeCaravanLE → SeatMiddleLeft；Base.89dodgeCaravanLE → SeatMiddleRight；Base.89dodgeCaravanLE → SeatRearLeft；Base.89dodgeCaravanLE → SeatRearRight；Base.89dodgeCaravanNomad → SeatFrontLeft；Base.89dodgeCaravanNomad → SeatFrontRight；Base.89dodgeCaravanNomad → SeatRearLeft | 89dodgeCaravan[^16] |
| `Base.89dodgeCaravanSidesteps0` | 89 Dodge Caravan Sidesteps（未找到有效中文译文） | 车辆安装件，用于车辆安装位（DAMNSideSteps）；适用车型见右列 / 维修配件 | 添加物品 | Base.89dodgeCaravan → DAMNSideSteps；Base.89dodgeCaravanLE → DAMNSideSteps；Base.89dodgeCaravanNomad → DAMNSideSteps | 89dodgeCaravan[^17] |
| `Base.89dodgeCaravanSlideDoor1` | 89 Dodge Caravan Slide Door（未找到有效中文译文） | 车辆安装件，用于车门（DoorRearRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.89dodgeCaravan → DoorRearRight；Base.89dodgeCaravanLE → DoorRearRight；Base.89dodgeCaravanNomad → DoorRearRight | 89dodgeCaravan[^18] |
| `Base.89dodgeCaravanTire1` | 89 Dodge Caravan Tire（未找到有效中文译文） | 车辆安装件，用于轮胎（Tire*）、轮胎（DAMNSpareTire）；适用车型见右列 / 维修配件 | 添加物品 | Base.89dodgeCaravan → Tire*；Base.89dodgeCaravan → DAMNSpareTire；Base.89dodgeCaravanLE → Tire*；Base.89dodgeCaravanLE → DAMNSpareTire；Base.89dodgeCaravanNomad → Tire*；Base.89dodgeCaravanNomad → DAMNSpareTire | 89dodgeCaravan[^19] |
| `Base.89dodgeCaravanTireOffroad2` | 89 Dodge Caravan Offroad Tire（未找到有效中文译文） | 车辆安装件，用于轮胎（Tire*）、轮胎（DAMNSpareTire）；适用车型见右列 / 维修配件 | 添加物品 | Base.89dodgeCaravan → Tire*；Base.89dodgeCaravan → DAMNSpareTire；Base.89dodgeCaravanLE → Tire*；Base.89dodgeCaravanLE → DAMNSpareTire；Base.89dodgeCaravanNomad → Tire*；Base.89dodgeCaravanNomad → DAMNSpareTire | 89dodgeCaravan[^20] |
| `Base.89dodgeCaravanTrunkDoor1` | 89 Dodge Caravan Trunk Lid（未找到有效中文译文） | 车辆安装件，用于后备箱（TrunkDoor）；适用车型见右列 / 维修配件 | 添加物品 | Base.89dodgeCaravan → TrunkDoor；Base.89dodgeCaravanLE → TrunkDoor；Base.89dodgeCaravanNomad → TrunkDoor | 89dodgeCaravan[^21] |
| `Base.89dodgeCaravanWindshield1` | 89 Dodge Caravan Windshield（未找到有效中文译文） | 车辆安装件，用于挡风玻璃（Windshield）；适用车型见右列 / 维修配件 | 添加物品 | Base.89dodgeCaravan → Windshield；Base.89dodgeCaravanLE → Windshield；Base.89dodgeCaravanNomad → Windshield | 89dodgeCaravan[^22] |
| `Base.89dodgeCaravanWindshieldRear1` | 89 Dodge Caravan Rear Windshield（未找到有效中文译文） | 车辆安装件，用于挡风玻璃（WindshieldRear）；适用车型见右列 / 维修配件 | 添加物品 | Base.89dodgeCaravan → WindshieldRear；Base.89dodgeCaravanLE → WindshieldRear；Base.89dodgeCaravanNomad → WindshieldRear | 89dodgeCaravan[^23] |

## 改装配件

| 完整物品 ID | 游戏显示名 / 名称状态 | 中文用途 / 类别 | 菜单 | 适用车辆与安装位置 | 来源 / 状态 |
| --- | --- | --- | --- | --- | --- |
| `Base.89dodgeCaravanBackWindowArmor` | 89 Dodge Caravan Back Window Armor（未找到有效中文译文） | 车辆安装件，用于防护件（DAMNBackLeftArmor）、防护件（DAMNBackRightArmor）；适用车型见右列 / 改装配件 | 添加物品 | Base.89dodgeCaravan → DAMNBackLeftArmor；Base.89dodgeCaravan → DAMNBackRightArmor；Base.89dodgeCaravanLE → DAMNBackLeftArmor；Base.89dodgeCaravanLE → DAMNBackRightArmor；Base.89dodgeCaravanNomad → DAMNBackLeftArmor；Base.89dodgeCaravanNomad → DAMNBackRightArmor | 89dodgeCaravan[^24] |
| `Base.89dodgeCaravanBullbarFrontA` | 89 Dodge Caravan Front Bullbar（未找到有效中文译文） | 车辆安装件，用于保险杠（DAMNBumperFront）；适用车型见右列 / 改装配件 | 添加物品 | Base.89dodgeCaravan → DAMNBumperFront；Base.89dodgeCaravanLE → DAMNBumperFront；Base.89dodgeCaravanNomad → DAMNBumperFront | 89dodgeCaravan[^25] |
| `Base.89dodgeCaravanBumperFront0` | 89 Dodge Caravan Front Bumper（未找到有效中文译文） | 车辆安装件，用于保险杠（DAMNBumperFront）；适用车型见右列 / 改装配件 | 添加物品 | Base.89dodgeCaravan → DAMNBumperFront；Base.89dodgeCaravanLE → DAMNBumperFront；Base.89dodgeCaravanNomad → DAMNBumperFront | 89dodgeCaravan[^26] |
| `Base.89dodgeCaravanBumperFrontA` | 89 Dodge Caravan Reinforced Front Bumper（未找到有效中文译文） | 车辆安装件，用于保险杠（DAMNBumperFront）；适用车型见右列 / 改装配件 | 添加物品 | Base.89dodgeCaravan → DAMNBumperFront；Base.89dodgeCaravanLE → DAMNBumperFront；Base.89dodgeCaravanNomad → DAMNBumperFront | 89dodgeCaravan[^27] |
| `Base.89dodgeCaravanBumperRear0` | 89 Dodge Caravan Rear Bumper（未找到有效中文译文） | 车辆安装件，用于保险杠（DAMNBumperRear）；适用车型见右列 / 改装配件 | 添加物品 | Base.89dodgeCaravan → DAMNBumperRear；Base.89dodgeCaravanLE → DAMNBumperRear；Base.89dodgeCaravanNomad → DAMNBumperRear | 89dodgeCaravan[^28] |
| `Base.89dodgeCaravanFrontWindowArmor` | 89 Dodge Caravan Front Window Armor（未找到有效中文译文） | 车辆安装件，用于防护件（DAMNFrontLeftArmor）、防护件（DAMNFrontRightArmor）；适用车型见右列 / 改装配件 | 添加物品 | Base.89dodgeCaravan → DAMNFrontLeftArmor；Base.89dodgeCaravan → DAMNFrontRightArmor；Base.89dodgeCaravanLE → DAMNFrontLeftArmor；Base.89dodgeCaravanLE → DAMNFrontRightArmor；Base.89dodgeCaravanNomad → DAMNFrontLeftArmor；Base.89dodgeCaravanNomad → DAMNFrontRightArmor | 89dodgeCaravan[^29] |
| `Base.89dodgeCaravanRearWindowArmor` | 89 Dodge Caravan Rear Window Armor（未找到有效中文译文） | 车辆安装件，用于防护件（DAMNRearLeftArmor）、防护件（DAMNRearRightArmor）；适用车型见右列 / 改装配件 | 添加物品 | Base.89dodgeCaravan → DAMNRearLeftArmor；Base.89dodgeCaravan → DAMNRearRightArmor；Base.89dodgeCaravanLE → DAMNRearLeftArmor；Base.89dodgeCaravanLE → DAMNRearRightArmor；Base.89dodgeCaravanNomad → DAMNRearLeftArmor；Base.89dodgeCaravanNomad → DAMNRearRightArmor | 89dodgeCaravan[^30] |
| `Base.89dodgeCaravanRoofrack0` | 89 Dodge Caravan Roofrack（未找到有效中文译文） | 车辆安装件，用于车顶行李架（DGC89Roofrack）；适用车型见右列 / 改装配件 | 添加物品 | Base.89dodgeCaravan → DGC89Roofrack；Base.89dodgeCaravanLE → DGC89Roofrack；Base.89dodgeCaravanNomad → DGC89Roofrack | 89dodgeCaravan[^31] |
| `Base.89dodgeCaravanWindshieldArmor` | 89 Dodge Caravan Windshield Armor（未找到有效中文译文） | 车辆安装件，用于挡风玻璃（DAMNWindshieldArmor）；适用车型见右列 / 改装配件 | 添加物品 | Base.89dodgeCaravan → DAMNWindshieldArmor；Base.89dodgeCaravanLE → DAMNWindshieldArmor；Base.89dodgeCaravanNomad → DAMNWindshieldArmor | 89dodgeCaravan[^32] |
| `Base.89dodgeCaravanWindshieldRearArmor` | 89 Dodge Caravan Rear Windshield Armor（未找到有效中文译文） | 车辆安装件，用于挡风玻璃（DAMNWindshieldRearArmor）；适用车型见右列 / 改装配件 | 添加物品 | Base.89dodgeCaravan → DAMNWindshieldRearArmor；Base.89dodgeCaravanLE → DAMNWindshieldRearArmor；Base.89dodgeCaravanNomad → DAMNWindshieldRearArmor | 89dodgeCaravan[^33] |

## 共享配件

下列物品由已启用依赖或游戏原版提供，不计入本 Mod 的本地物品数。

| 完整物品 ID | 游戏显示名 / 名称状态 | 中文用途 / 类别 | 菜单 | 适用车辆与安装位置 | 来源 / 状态 |
| --- | --- | --- | --- | --- | --- |
| `Base.BigGasTank1` | 油箱 (大型)（翻译文件含非标准语法，待游戏核实）[^35] | 车辆安装件，用于油箱（GasTank）；适用车型见右列 / 维修配件 | 添加物品 | Base.89dodgeCaravan → GasTank；Base.89dodgeCaravanLE → GasTank；Base.89dodgeCaravanNomad → GasTank | 游戏原版[^34] |
| `Base.CarBattery1` | 汽车电池（翻译文件含非标准语法，待游戏核实）[^37] | 车辆安装件，用于蓄电池（Battery）；适用车型见右列 / 维修配件 | 添加物品 | Base.89dodgeCaravan → Battery；Base.89dodgeCaravanLE → Battery；Base.89dodgeCaravanNomad → Battery | 游戏原版[^36] |
| `Base.Generator` | 发电机 (极电制造)（翻译文件含非标准语法，待游戏核实）[^39] | 车辆安装件，用于车辆安装位（DAMNGenerator）；适用车型见右列 / 维修配件 | 添加物品 | Base.89dodgeCaravan → DAMNGenerator；Base.89dodgeCaravanLE → DAMNGenerator；Base.89dodgeCaravanNomad → DAMNGenerator | 游戏原版[^38] |
| `Base.Generator_Blue` | 发电机 (廉科牌)（翻译文件含非标准语法，待游戏核实）[^41] | 车辆安装件，用于车辆安装位（DAMNGenerator）；适用车型见右列 / 维修配件 | 添加物品 | Base.89dodgeCaravan → DAMNGenerator；Base.89dodgeCaravanLE → DAMNGenerator；Base.89dodgeCaravanNomad → DAMNGenerator | 游戏原版[^40] |
| `Base.Generator_Old` | 发电机 (老式)（翻译文件含非标准语法，待游戏核实）[^43] | 车辆安装件，用于车辆安装位（DAMNGenerator）；适用车型见右列 / 维修配件 | 添加物品 | Base.89dodgeCaravan → DAMNGenerator；Base.89dodgeCaravanLE → DAMNGenerator；Base.89dodgeCaravanNomad → DAMNGenerator | 游戏原版[^42] |
| `Base.Generator_Yellow` | 发电机 (昂科牌)（翻译文件含非标准语法，待游戏核实）[^45] | 车辆安装件，用于车辆安装位（DAMNGenerator）；适用车型见右列 / 维修配件 | 添加物品 | Base.89dodgeCaravan → DAMNGenerator；Base.89dodgeCaravanLE → DAMNGenerator；Base.89dodgeCaravanNomad → DAMNGenerator | 游戏原版[^44] |
| `Base.GloveBox1` | 手套箱（翻译文件含非标准语法，待游戏核实）[^47] | 车辆安装件，用于车辆安装位（GloveBox）；适用车型见右列 / 维修配件 | 添加物品 | Base.89dodgeCaravan → GloveBox；Base.89dodgeCaravanLE → GloveBox；Base.89dodgeCaravanNomad → GloveBox | 游戏原版[^46] |
| `Base.LightBulb` | 灯泡-白色 / 灯泡 (白)（译文冲突，待游戏核实）[^49] | 车辆安装件，用于车灯（Headlight*）、车灯（JP82DorothyLights）；适用车型见右列 / 维修配件 | 添加物品 | Base.89dodgeCaravan → Headlight*；Base.89dodgeCaravanLE → Headlight*；Base.89dodgeCaravanNomad → Headlight* | 游戏原版[^48] |
| `Base.ModernBrake1` | 制动器 (高级)（翻译文件含非标准语法，待游戏核实）[^51] | 车辆安装件，用于制动器（Brake*）；适用车型见右列 / 维修配件 | 添加物品 | Base.89dodgeCaravan → Brake*；Base.89dodgeCaravanLE → Brake*；Base.89dodgeCaravanNomad → Brake* | 游戏原版[^50] |
| `Base.ModernCarMuffler1` | 消声器 (高级)（翻译文件含非标准语法，待游戏核实）[^53] | 车辆安装件，用于消声器（Muffler）；适用车型见右列 / 维修配件 | 添加物品 | Base.89dodgeCaravan → Muffler；Base.89dodgeCaravanLE → Muffler；Base.89dodgeCaravanNomad → Muffler | 游戏原版[^52] |
| `Base.ModernSuspension1` | 悬挂 (高级)（翻译文件含非标准语法，待游戏核实）[^55] | 车辆安装件，用于悬挂（Suspension*）；适用车型见右列 / 维修配件 | 添加物品 | Base.89dodgeCaravan → Suspension*；Base.89dodgeCaravanLE → Suspension*；Base.89dodgeCaravanNomad → Suspension* | 游戏原版[^54] |
| `Base.NormalBrake1` | 制动器 (普通)（翻译文件含非标准语法，待游戏核实）[^57] | 车辆安装件，用于制动器（Brake*）；适用车型见右列 / 维修配件 | 添加物品 | Base.89dodgeCaravan → Brake*；Base.89dodgeCaravanLE → Brake*；Base.89dodgeCaravanNomad → Brake* | 游戏原版[^56] |
| `Base.NormalCarMuffler1` | 消声器 (普通)（翻译文件含非标准语法，待游戏核实）[^59] | 车辆安装件，用于消声器（Muffler）；适用车型见右列 / 维修配件 | 添加物品 | Base.89dodgeCaravan → Muffler；Base.89dodgeCaravanLE → Muffler；Base.89dodgeCaravanNomad → Muffler | 游戏原版[^58] |
| `Base.NormalGasTank1` | 油箱 (标准)（翻译文件含非标准语法，待游戏核实）[^61] | 车辆安装件，用于油箱（GasTank）；适用车型见右列 / 维修配件 | 添加物品 | Base.89dodgeCaravan → GasTank；Base.89dodgeCaravanLE → GasTank；Base.89dodgeCaravanNomad → GasTank | 游戏原版[^60] |
| `Base.NormalSuspension1` | 悬挂 (普通)（翻译文件含非标准语法，待游戏核实）[^63] | 车辆安装件，用于悬挂（Suspension*）；适用车型见右列 / 维修配件 | 添加物品 | Base.89dodgeCaravan → Suspension*；Base.89dodgeCaravanLE → Suspension*；Base.89dodgeCaravanNomad → Suspension* | 游戏原版[^62] |
| `Base.OldBrake1` | 制动器 (老式)（翻译文件含非标准语法，待游戏核实）[^65] | 车辆安装件，用于制动器（Brake*）；适用车型见右列 / 维修配件 | 添加物品 | Base.89dodgeCaravan → Brake*；Base.89dodgeCaravanLE → Brake*；Base.89dodgeCaravanNomad → Brake* | 游戏原版[^64] |
| `Base.OldCarMuffler1` | 消声器 (老式)（翻译文件含非标准语法，待游戏核实）[^67] | 车辆安装件，用于消声器（Muffler）；适用车型见右列 / 维修配件 | 添加物品 | Base.89dodgeCaravan → Muffler；Base.89dodgeCaravanLE → Muffler；Base.89dodgeCaravanNomad → Muffler | 游戏原版[^66] |
| `Base.PetrolCan` | 汽油罐 (油)（翻译文件含非标准语法，待游戏核实）[^69] | 车辆安装件，用于车辆安装位（DAMNGasCanOne）、车辆安装位（DAMNGasCanTwo）、车辆安装位（DAMNGasCanThree）；适用车型见右列 / 维修配件 | 添加物品 | Base.89dodgeCaravan → DAMNGasCanOne；Base.89dodgeCaravan → DAMNGasCanTwo；Base.89dodgeCaravan → DAMNGasCanThree；Base.89dodgeCaravanLE → DAMNGasCanOne；Base.89dodgeCaravanLE → DAMNGasCanTwo；Base.89dodgeCaravanLE → DAMNGasCanThree；Base.89dodgeCaravanNomad → DAMNGasCanOne；Base.89dodgeCaravanNomad → DAMNGasCanTwo；Base.89dodgeCaravanNomad → DAMNGasCanThree | 游戏原版[^68] |
| `Base.RadioBlack` | 收音机 (超值科技) / 收音机 (廉科) / 廉科牌收音机（译文冲突，待游戏核实）[^71] | 车辆安装件，用于车辆安装位（Radio）；适用车型见右列 / 维修配件 | 添加物品 | Base.89dodgeCaravan → Radio；Base.89dodgeCaravanLE → Radio；Base.89dodgeCaravanNomad → Radio | 游戏原版[^70] |
| `Base.RadioMakeShift` | 收音机 (简易) / 自制收音机（译文冲突，待游戏核实）[^73] | 车辆安装件，用于车辆安装位（Radio）；适用车型见右列 / 维修配件 | 添加物品 | Base.89dodgeCaravan → Radio；Base.89dodgeCaravanLE → Radio；Base.89dodgeCaravanNomad → Radio | 游戏原版[^72] |
| `Base.RadioRed` | 导航仪 / 收音机 (昂科) / 昂科牌收音机（译文冲突，待游戏核实）[^75] | 车辆安装件，用于车辆安装位（Radio）；适用车型见右列 / 维修配件 | 添加物品 | Base.89dodgeCaravan → Radio；Base.89dodgeCaravanLE → Radio；Base.89dodgeCaravanNomad → Radio | 游戏原版[^74] |
| `Base.SmallGasTank1` | 油箱 (小型)（翻译文件含非标准语法，待游戏核实）[^77] | 车辆安装件，用于油箱（GasTank）；适用车型见右列 / 维修配件 | 添加物品 | Base.89dodgeCaravan → GasTank；Base.89dodgeCaravanLE → GasTank；Base.89dodgeCaravanNomad → GasTank | 游戏原版[^76] |
| `damnCraft.SmallTire1` | Small Universal Tire（未找到有效中文译文） | 车辆安装件，用于轮胎（Tire*）、轮胎（KI5TRSpareTire）、轮胎（DAMNSpareTire）、轮胎（DAMNSpareTireRoof）；适用车型见右列 / 维修配件 | 添加物品 | Base.89dodgeCaravan → Tire*；Base.89dodgeCaravan → DAMNSpareTire；Base.89dodgeCaravanLE → Tire*；Base.89dodgeCaravanLE → DAMNSpareTire；Base.89dodgeCaravanNomad → Tire*；Base.89dodgeCaravanNomad → DAMNSpareTire | damnlib[^78] |

## 制作配方

| 配方完整 ID（排查用） | 游戏配方名 / 名称状态 | 中文用途 | 菜单 | 来源 |
| --- | --- | --- | --- | --- |
| `Base.89dodgeCaravanMakeBackWindowArmor` | 制作89款道奇凯领后部车窗装甲[^79] | 制作产出：89 Dodge Caravan Back Window Armor（车辆安装件，用于防护件（DAMNBackLeftArmor）、防护件（DAMNBackRightArmor）；适用车型见右列） | 制作界面 | [^80] |
| `Base.89dodgeCaravanMakeFrontBullbar` | 制作89款道奇凯领前防撞杠[^81] | 制作产出：89 Dodge Caravan Front Bullbar（车辆安装件，用于保险杠（DAMNBumperFront）；适用车型见右列） | 制作界面 | [^82] |
| `Base.89dodgeCaravanMakeFrontBumper` | 制作89款道奇凯领前保险杠[^83] | 制作产出：89 Dodge Caravan Front Bumper（车辆安装件，用于保险杠（DAMNBumperFront）；适用车型见右列） | 制作界面 | [^84] |
| `Base.89dodgeCaravanMakeFrontDoor` | 制作89款道奇凯领前车门[^85] | 制作产出：89 Dodge Caravan Front Door（车辆安装件，用于车门（DoorFrontLeft）、车门（DoorFrontRight）；适用车型见右列） | 制作界面 | [^86] |
| `Base.89dodgeCaravanMakeFrontSeat` | 制作89款道奇凯领前座椅[^87] | 制作产出：89 Dodge Caravan Seat（车辆安装件，用于座椅（SeatFrontLeft）、座椅（SeatFrontRight）、座椅（SeatRearLeft）、座椅（SeatRearRight）、座椅（SeatMiddleLeft）、座椅（SeatMiddleRight）；适用车型见右列） | 制作界面 | [^88] |
| `Base.89dodgeCaravanMakeFrontSideWindow` | 制作89款道奇凯领前侧窗[^89] | 制作产出：89 Dodge Caravan Front Side Window（车辆安装件，用于车窗（WindowFrontLeft）、车窗（WindowFrontRight）；适用车型见右列） | 制作界面 | [^90] |
| `Base.89dodgeCaravanMakeFrontWindowArmor` | 制作89款道奇凯领前车窗装甲[^91] | 制作产出：89 Dodge Caravan Front Window Armor（车辆安装件，用于防护件（DAMNFrontLeftArmor）、防护件（DAMNFrontRightArmor）；适用车型见右列） | 制作界面 | [^92] |
| `Base.89dodgeCaravanMakeFrontWindshield` | 制作89款道奇凯领前挡风玻璃[^93] | 制作产出：89 Dodge Caravan Windshield（车辆安装件，用于挡风玻璃（Windshield）；适用车型见右列） | 制作界面 | [^94] |
| `Base.89dodgeCaravanMakeFrontWindshieldArmor` | 制作89款道奇凯领前挡风玻璃装甲[^95] | 制作产出：89 Dodge Caravan Windshield Armor（车辆安装件，用于挡风玻璃（DAMNWindshieldArmor）；适用车型见右列） | 制作界面 | [^96] |
| `Base.89dodgeCaravanMakeHood` | 制作89款道奇凯领引擎盖[^97] | 制作产出：89 Dodge Caravan Hood（车辆安装件，用于引擎盖（EngineDoor）；适用车型见右列） | 制作界面 | [^98] |
| `Base.89dodgeCaravanMakeMudflaps` | 制作89款道奇凯领挡泥板[^99] | 制作产出：89 Dodge Caravan Mudflaps（车辆安装件，用于车辆安装位（DAMNMudflaps）；适用车型见右列） | 制作界面 | [^100] |
| `Base.89dodgeCaravanMakeOffroadTire` | 制作89款道奇凯领越野轮胎[^101] | 制作产出：89 Dodge Caravan Offroad Tire（车辆安装件，用于轮胎（Tire*）、轮胎（DAMNSpareTire）；适用车型见右列） | 制作界面 | [^102] |
| `Base.89dodgeCaravanMakeRearBumper` | 制作89款道奇凯领后保险杠[^103] | 制作产出：89 Dodge Caravan Rear Bumper（车辆安装件，用于保险杠（DAMNBumperRear）；适用车型见右列） | 制作界面 | [^104] |
| `Base.89dodgeCaravanMakeRearDoor` | 制作89款道奇凯领后车门[^105] | 制作产出：89 Dodge Caravan Slide Door（车辆安装件，用于车门（DoorRearRight）；适用车型见右列） | 制作界面 | [^106] |
| `Base.89dodgeCaravanMakeRearSideWindow` | 制作89款道奇凯领后侧窗[^107] | 制作产出：89 Dodge Caravan Rear Side Window（车辆安装件，用于车窗（WindowRearLeft）、车窗（WindowRearRight）、车窗（WindowBackLeft）、车窗（WindowBackRight）；适用车型见右列） | 制作界面 | [^108] |
| `Base.89dodgeCaravanMakeRearWindowArmor` | 制作89款道奇凯领后车窗装甲[^109] | 制作产出：89 Dodge Caravan Rear Window Armor（车辆安装件，用于防护件（DAMNRearLeftArmor）、防护件（DAMNRearRightArmor）；适用车型见右列） | 制作界面 | [^110] |
| `Base.89dodgeCaravanMakeRearWindshield` | 制作89款道奇凯领后挡风玻璃[^111] | 制作产出：89 Dodge Caravan Rear Windshield（车辆安装件，用于挡风玻璃（WindshieldRear）；适用车型见右列） | 制作界面 | [^112] |
| `Base.89dodgeCaravanMakeRearWindshieldArmor` | 制作89款道奇凯领后挡风玻璃装甲[^113] | 制作产出：89 Dodge Caravan Rear Windshield Armor（车辆安装件，用于挡风玻璃（DAMNWindshieldRearArmor）；适用车型见右列） | 制作界面 | [^114] |
| `Base.89dodgeCaravanMakeReinforcedFrontBumper` | 制作89款道奇凯领加固前保险杠[^115] | 制作产出：89 Dodge Caravan Reinforced Front Bumper（车辆安装件，用于保险杠（DAMNBumperFront）；适用车型见右列） | 制作界面 | [^116] |
| `Base.89dodgeCaravanMakeRoofrack` | 制作89款道奇凯领车顶行李架[^117] | 制作产出：89 Dodge Caravan Roofrack（车辆安装件，用于车顶行李架（DGC89Roofrack）；适用车型见右列） | 制作界面 | [^118] |
| `Base.89dodgeCaravanMakeSidesteps` | 制作89款道奇凯领侧踏板[^119] | 制作产出：89 Dodge Caravan Sidesteps（车辆安装件，用于车辆安装位（DAMNSideSteps）；适用车型见右列） | 制作界面 | [^120] |
| `Base.89dodgeCaravanMakeTire` | 制作89款道奇凯领轮胎[^121] | 制作产出：89 Dodge Caravan Tire（车辆安装件，用于轮胎（Tire*）、轮胎（DAMNSpareTire）；适用车型见右列） | 制作界面 | [^122] |
| `Base.89dodgeCaravanMakeTrunkLid` | 制作89款道奇凯领后备箱盖[^123] | 制作产出：89 Dodge Caravan Trunk Lid（车辆安装件，用于后备箱（TrunkDoor）；适用车型见右列） | 制作界面 | [^124] |

## 内部定义、历史分支与未解析引用

有效资源层：42.20, common；仅合并 common 与所选版本，Overlay 按相对路径覆盖。
车辆模板 20 个、内部槽位 70 个，均不算整车或背包物品。旧根目录和未选中版本的定义不列入当前可用表。模板中短物品引用若追加机修类型后缀才匹配定义，属于静态映射，安装仍待实测。

内部或过时的 item 定义单列于此，不在上面的背包刷取建议中；它们仍计入各自来源的定义数量。

| 保留定义 ID（不作正常刷取建议） | 脚本显示名 | 中文说明 / 状态 | 来源 |
| --- | --- | --- | --- |
| `damnCraft.Trunk1` | no | 车辆后备箱的内部容量载体，脚本含 MaxCapacity、ConditionAffectsCapacity 并由 Trunk 槽位引用；不是行李箱或可背负背包；显示名 no、图标 na；仅供车辆内部使用 | [^125] |

<details><summary>查看内部槽位（不能直接刷取）</summary>

| 槽位 | 名称或说明 | 来源 |
| --- | --- | --- |
| `Battery` | 电池 / 蓄电池 | [^126] |
| `Brake*` | Brake* / 制动器 | [^127] |
| `BrakeFrontLeft` | 左前制动 / 制动器 | [^128] |
| `BrakeFrontRight` | 右前制动 / 制动器 | [^129] |
| `BrakeRearLeft` | 左后制动 / 制动器 | [^130] |
| `BrakeRearRight` | 右后制动 / 制动器 | [^131] |
| `DAMNBackLeftArmor` | 左后部车窗装甲 / 防护件 | [^132] |
| `DAMNBackRightArmor` | 右后部车窗装甲 / 防护件 | [^133] |
| `DAMNBumperFront` | 前保险杠 / 保险杠 | [^134] |
| `DAMNBumperRear` | 后保险杠 / 保险杠 | [^135] |
| `DAMNFrontLeftArmor` | 左前车窗装甲 / 防护件 | [^136] |
| `DAMNFrontRightArmor` | 右前车窗装甲 / 防护件 | [^137] |
| `DAMNGasCanOne` | 汽油桶 / 车辆安装位 | [^138] |
| `DAMNGasCanThree` | 汽油桶 / 车辆安装位 | [^139] |
| `DAMNGasCanTwo` | 汽油桶 / 车辆安装位 | [^140] |
| `DAMNGenerator` | 发电机 / 车辆安装位 | [^141] |
| `DAMNMudflaps` | 挡泥板 / 车辆安装位 | [^142] |
| `DAMNRearLeftArmor` | 左后车窗装甲 / 防护件 | [^143] |
| `DAMNRearRightArmor` | 右后车窗装甲 / 防护件 | [^144] |
| `DAMNSideSteps` | 侧踏板 / 车辆安装位 | [^145] |
| `DAMNSpareTire` | 备胎 / 轮胎 | [^146] |
| `DAMNWindshieldArmor` | 挡风玻璃装甲 / 挡风玻璃 | [^147] |
| `DAMNWindshieldRearArmor` | 后挡风玻璃装甲 / 挡风玻璃 | [^148] |
| `DGC89Roofrack` | 车顶行李架 / 车顶行李架 | [^149] |
| `DGC89Trunk` | 后备箱 / 后备箱 | [^150] |
| `Door*` | Door* / 车门 | [^151] |
| `DoorFrontLeft` | 左前门 / 车门 | [^152] |
| `DoorFrontRight` | 右前门 / 车门 | [^153] |
| `DoorRearRight` | 右后门 / 车门 | [^154] |
| `Engine` | 引擎 / 发动机 | [^155] |
| `EngineDoor` | 引擎盖 / 引擎盖 | [^156] |
| `GasTank` | 油箱 / 油箱 | [^157] |
| `GloveBox` | 手套箱 / 车辆安装位 | [^158] |
| `Headlight*` | Headlight* / 车灯 | [^159] |
| `HeadlightLeft` | 左大灯 / 车灯 | [^160] |
| `HeadlightRearLeft` | 左尾灯 / 车灯 | [^161] |
| `HeadlightRearRight` | 右尾灯 / 车灯 | [^162] |
| `HeadlightRight` | 右大灯 / 车灯 | [^163] |
| `Heater` | 加热器 / 车辆安装位 | [^164] |
| `Muffler` | 排气消声器 / 消声器 | [^165] |
| `PassengerCompartment` | 乘员舱 / 车辆安装位 | [^166] |
| `Radio` | 电台 / 车辆安装位 | [^167] |
| `Seat*` | Seat* / 座椅 | [^168] |
| `SeatFrontLeft` | 驾驶座 / 座椅 | [^169] |
| `SeatFrontRight` | 右前座 / 座椅 | [^170] |
| `SeatMiddleLeft` | 左中座 / 座椅 | [^171] |
| `SeatMiddleRight` | 右中座 / 座椅 | [^172] |
| `SeatRearLeft` | 左后座 / 座椅 | [^173] |
| `SeatRearRight` | 右后座 / 座椅 | [^174] |
| `Suspension*` | Suspension* / 悬挂 | [^175] |
| `SuspensionFrontLeft` | 左前悬挂 / 悬挂 | [^176] |
| `SuspensionFrontRight` | 右前悬挂 / 悬挂 | [^177] |
| `SuspensionRearLeft` | 左后悬挂 / 悬挂 | [^178] |
| `SuspensionRearRight` | 右后悬挂 / 悬挂 | [^179] |
| `Tire*` | Tire* / 轮胎 | [^180] |
| `TireFrontLeft` | 左前胎 / 轮胎 | [^181] |
| `TireFrontRight` | 右前胎 / 轮胎 | [^182] |
| `TireRearLeft` | 左后胎 / 轮胎 | [^183] |
| `TireRearRight` | 右后胎 / 轮胎 | [^184] |
| `TruckBed` | 补给箱 / 行李箱 / 车辆安装位 | [^185] |
| `TrunkDoor` | 后车盖 / 后备箱 | [^186] |
| `Window*` | Window* / 车窗 | [^187] |
| `WindowBackLeft` | 左后部车窗 / 车窗 | [^188] |
| `WindowBackRight` | 右后部车窗 / 车窗 | [^189] |
| `WindowFrontLeft` | 左前窗 / 车窗 | [^190] |
| `WindowFrontRight` | 右前窗 / 车窗 | [^191] |
| `WindowRearLeft` | 左后窗 / 车窗 | [^192] |
| `WindowRearRight` | 右后窗 / 车窗 | [^193] |
| `Windshield` | 挡风玻璃 / 挡风玻璃 | [^194] |
| `WindshieldRear` | 后挡风玻璃 / 挡风玻璃 | [^195] |

</details>


## 概览

| Mod ID / 文件夹 | 分发端 | 版本 | 选择的 mod.info | 原件范围 → 当前范围 |
| --- | --- | --- | --- | --- |
| `89dodgeCaravan` / `89dodgeCaravan` | both（双端） | 未标注 | `42.20/mod.info` | 42.20.0 … - → 42.20.0 … - |

原件体积 25.4 MB；体积按完整目录统计，与当前内容定义数分开。
工作坊：[查看作者页面](https://steamcommunity.com/sharedfiles/filedetails/?id=3034636011)。

## 证据与使用边界

**verified：有效源码静态确认。** 每个当前可复制 ID 均来自所选版本的定义；这不保证游戏已成功注册、生成、安装或联机同步。
挑战者 5 个车辆中文名另有 Owner 截图确认；本轮没有启动游戏。译文冲突、动态 Lua 内容和玩法效果仍需 Owner 游戏内核实。
以下人工记录保留原始语境；其中旧组合、旧数量和旧候选状态仅供追溯，当前统计与归属以上表和 profile 为准。

<!-- retained:start -->
## 依赖与冲突

- require：无（`damnlib` 为共用依赖）
- 互斥：未声明
- 加载位次：`DeadWorksDaleRV` 之后、`ImmersiveDriving` 之前（KI5 车队段）

## 双端与联机

双端；require `damnlib`。 本包在 `b422-main` 与 `b422-compat` 同时启用。

## 实测与排查

**planned：仅完成依赖、版本与加载顺序静态检查（`check` 0 problem）与同步落盘（`runs/ki5-fleet-20261112/`）。** 未启动游戏，刷车分布、车辆物理与联机同步都没有运行证据。
<!-- retained:end -->

## 静态来源

路径相对 `A004/workspace/mods_library/`；`Overlay/<文件夹>/` 指 `A004/workspace/patches/mods/<文件夹>/`，`游戏原版/` 指当前 B42.22 客户端 Game 目录。翻译来源列出所有候选，未按加载顺序擅自消解异文。

[^1]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/IG_UI.json:14389`
[^2]: `3034636011/mods/89dodgeCaravan/common/media/lua/shared/Translate/EN/IG_UI.json:2`
[^3]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan.txt:44`
[^4]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/IG_UI.json:14390`
[^5]: `3034636011/mods/89dodgeCaravan/common/media/lua/shared/Translate/EN/IG_UI.json:3`
[^6]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravanLE.txt:3`
[^7]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/IG_UI.json:14391`
[^8]: `3034636011/mods/89dodgeCaravan/common/media/lua/shared/Translate/EN/IG_UI.json:4`
[^9]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravanNomad.txt:16`
[^10]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_vehiclesitems.txt:6`
[^11]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_vehiclesitems.txt:215`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_hood.txt:14`
[^12]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_vehiclesitems.txt:101`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_doors.txt:34`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_doors.txt:88`
[^13]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_vehiclesitems.txt:344`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_windows.txt:54`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_windows.txt:85`
[^14]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_vehiclesitems.txt:391`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_mudflaps.txt:13`
[^15]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_vehiclesitems.txt:359`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_windows.txt:116`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_windows.txt:137`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_windows.txt:168`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_windows.txt:188`
[^16]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_vehiclesitems.txt:249`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_seats.txt:161`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_seats.txt:180`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_seats.txt:199`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_seats.txt:218`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_seats.txt:292`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_seats.txt:311`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_seats.txt:330`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_seats.txt:349`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_seats.txt:368`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_seats.txt:387`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_seats.txt:49`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_seats.txt:68`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_seats.txt:87`
[^17]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_vehiclesitems.txt:85`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_sidesteps.txt:13`
[^18]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_vehiclesitems.txt:116`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_doors.txt:142`
[^19]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_vehiclesitems.txt:24`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_tires.txt:186`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_spare_tires.txt:6`
[^20]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_vehiclesitems.txt:44`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_tires.txt:186`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_spare_tires.txt:6`
[^21]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_vehiclesitems.txt:232`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_trunkdoors.txt:14`
[^22]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_vehiclesitems.txt:329`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_windshields.txt:22`
[^23]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_vehiclesitems.txt:374`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_windshields.txt:80`
[^24]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_vehiclesitems.txt:165`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_armor.txt:383`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_armor.txt:446`
[^25]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_vehiclesitems.txt:297`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_frontBumper.txt:26`
[^26]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_vehiclesitems.txt:267`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_frontBumper.txt:26`
[^27]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_vehiclesitems.txt:282`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_frontBumper.txt:26`
[^28]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_vehiclesitems.txt:312`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_rearBumper.txt:26`
[^29]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_vehiclesitems.txt:133`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_armor.txt:128`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_armor.txt:192`
[^30]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_vehiclesitems.txt:149`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_armor.txt:256`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_armor.txt:319`
[^31]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_vehiclesitems.txt:66`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_roofrack.txt:14`
[^32]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_vehiclesitems.txt:181`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_armor.txt:65`
[^33]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_vehiclesitems.txt:197`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_armor.txt:509`
[^34]: `游戏原版/media/scripts/generated/items/normal.txt:12363`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan.txt:424`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravanLE.txt:427`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravanNomad.txt:380`
[^35]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:447`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:162`
[^36]: `游戏原版/media/scripts/generated/items/drainable.txt:2349`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan.txt:440`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravanLE.txt:443`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravanNomad.txt:396`
[^37]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:969`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:379`
[^38]: `游戏原版/media/scripts/generated/items/normal.txt:4800`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_gearNomad.txt:157`
[^39]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1708`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:665`
[^40]: `游戏原版/media/scripts/generated/items/normal.txt:4834`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_gearNomad.txt:157`
[^41]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1709`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:3355`
[^42]: `游戏原版/media/scripts/generated/items/normal.txt:4851`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_gearNomad.txt:157`
[^43]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1710`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:3356`
[^44]: `游戏原版/media/scripts/generated/items/normal.txt:4817`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_gearNomad.txt:157`
[^45]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1711`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:3357`
[^46]: `游戏原版/media/scripts/generated/items/normal.txt:13013`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan.txt:390`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravanLE.txt:397`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravanNomad.txt:350`
[^47]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1775`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:686`
[^48]: `游戏原版/media/scripts/generated/items/normal.txt:4661`；`游戏原版/media/scripts/generated/vehicles/template_headlight.txt:25`
[^49]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:6727`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25103`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2563`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:965`
[^50]: `游戏原版/media/scripts/generated/items/normal.txt:12112`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan.txt:495`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravanLE.txt:494`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravanNomad.txt:447`
[^51]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2779`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1049`
[^52]: `游戏原版/media/scripts/generated/items/normal.txt:13121`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan.txt:453`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravanLE.txt:454`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravanNomad.txt:407`
[^53]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2782`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1052`
[^54]: `游戏原版/media/scripts/generated/items/normal.txt:12248`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan.txt:512`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravanLE.txt:511`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravanNomad.txt:464`
[^55]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2785`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1055`
[^56]: `游戏原版/media/scripts/generated/items/normal.txt:12095`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan.txt:495`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravanLE.txt:494`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravanNomad.txt:447`
[^57]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3218`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1134`
[^58]: `游戏原版/media/scripts/generated/items/normal.txt:13106`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan.txt:453`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravanLE.txt:454`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravanNomad.txt:407`
[^59]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3221`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1137`
[^60]: `游戏原版/media/scripts/generated/items/normal.txt:12348`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan.txt:424`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravanLE.txt:427`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravanNomad.txt:380`
[^61]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3227`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1143`
[^62]: `游戏原版/media/scripts/generated/items/normal.txt:12231`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan.txt:512`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravanLE.txt:511`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravanNomad.txt:464`
[^63]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3230`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1146`
[^64]: `游戏原版/media/scripts/generated/items/normal.txt:12078`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan.txt:495`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravanLE.txt:494`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravanNomad.txt:447`
[^65]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3254`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1164`
[^66]: `游戏原版/media/scripts/generated/items/normal.txt:13091`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan.txt:453`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravanLE.txt:454`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravanNomad.txt:407`
[^67]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3257`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1167`
[^68]: `游戏原版/media/scripts/generated/items/normal.txt:7216`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_gearNomad.txt:37`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_gearNomad.txt:77`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_gearNomad.txt:117`
[^69]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3425`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1239`
[^70]: `游戏原版/media/scripts/generated/items/radio.txt:308`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan.txt:529`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravanLE.txt:528`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravanNomad.txt:481`
[^71]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:7374`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25092`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3645`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:5128`
[^72]: `游戏原版/media/scripts/generated/items/radio.txt:335`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan.txt:529`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravanLE.txt:528`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravanNomad.txt:481`
[^73]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:7375`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25093`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3649`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:5132`
[^74]: `游戏原版/media/scripts/generated/items/radio.txt:361`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan.txt:529`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravanLE.txt:528`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravanNomad.txt:481`
[^75]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:3001`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25091`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3651`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:5134`
[^76]: `游戏原版/media/scripts/generated/items/normal.txt:12333`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan.txt:424`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravanLE.txt:427`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravanNomad.txt:380`
[^77]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:4151`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1542`
[^78]: `3171167894/mods/damnlib/42.20/media/scripts/damnCraft/items_damnCraft.txt:473`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_tires.txt:186`；`3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_spare_tires.txt:6`
[^79]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:5771`
[^80]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_recipes.txt:329`
[^81]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:5774`
[^82]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_recipes.txt:400`
[^83]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:5773`
[^84]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_recipes.txt:376`
[^85]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:5760`
[^86]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_recipes.txt:71`
[^87]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:5763`
[^88]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_recipes.txt:148`
[^89]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:5765`
[^90]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_recipes.txt:194`
[^91]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:5769`
[^92]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_recipes.txt:283`
[^93]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:5764`
[^94]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_recipes.txt:172`
[^95]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:5768`
[^96]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_recipes.txt:260`
[^97]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:5759`
[^98]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_recipes.txt:47`
[^99]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:5778`
[^100]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_recipes.txt:492`
[^101]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:5758`
[^102]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_recipes.txt:25`
[^103]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:5776`
[^104]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_recipes.txt:444`
[^105]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:5761`
[^106]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_recipes.txt:97`
[^107]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:5766`
[^108]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_recipes.txt:216`
[^109]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:5770`
[^110]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_recipes.txt:306`
[^111]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:5767`
[^112]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_recipes.txt:238`
[^113]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:5772`
[^114]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_recipes.txt:352`
[^115]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:5775`
[^116]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_recipes.txt:423`
[^117]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:5777`
[^118]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_recipes.txt:467`
[^119]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:5779`
[^120]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_recipes.txt:513`
[^121]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:5757`
[^122]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_recipes.txt:3`
[^123]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:5762`
[^124]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan_recipes.txt:123`
[^125]: `3171167894/mods/damnlib/42.20/media/scripts/damnCraft/items_damnCraft.txt:558`
[^126]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan.txt:440`
[^127]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan.txt:495`
[^128]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:5`
[^129]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:18`
[^130]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:31`
[^131]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:44`
[^132]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_armor.txt:383`
[^133]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_armor.txt:446`
[^134]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_frontBumper.txt:26`
[^135]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_rearBumper.txt:26`
[^136]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_armor.txt:128`
[^137]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_armor.txt:192`
[^138]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_gearNomad.txt:37`
[^139]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_gearNomad.txt:117`
[^140]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_gearNomad.txt:77`
[^141]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_gearNomad.txt:157`
[^142]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_mudflaps.txt:13`
[^143]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_armor.txt:256`
[^144]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_armor.txt:319`
[^145]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_sidesteps.txt:13`
[^146]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_spare_tires.txt:6`
[^147]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_armor.txt:65`
[^148]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_armor.txt:509`
[^149]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_roofrack.txt:14`
[^150]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_trunk.txt:5`
[^151]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_doors.txt:197`
[^152]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_doors.txt:34`
[^153]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_doors.txt:88`
[^154]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_doors.txt:142`
[^155]: `游戏原版/media/scripts/generated/vehicles/template_engine.txt:5`
[^156]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_hood.txt:14`
[^157]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan.txt:424`
[^158]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan.txt:390`
[^159]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:25`
[^160]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:5`
[^161]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:15`
[^162]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:20`
[^163]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:10`
[^164]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan.txt:473`
[^165]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan.txt:453`
[^166]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan.txt:483`
[^167]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan.txt:529`
[^168]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_seats.txt:237`
[^169]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_seats.txt:161`
[^170]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_seats.txt:180`
[^171]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_seats.txt:330`
[^172]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_seats.txt:349`
[^173]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_seats.txt:199`
[^174]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_seats.txt:218`
[^175]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/89dodgeCaravan.txt:512`
[^176]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:5`
[^177]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:18`
[^178]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:31`
[^179]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:44`
[^180]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_tires.txt:186`
[^181]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_tires.txt:38`
[^182]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_tires.txt:77`
[^183]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_tires.txt:114`
[^184]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_tires.txt:148`
[^185]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_trunk.txt:24`
[^186]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_trunkdoors.txt:14`
[^187]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_windows.txt:209`
[^188]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_windows.txt:168`
[^189]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_windows.txt:188`
[^190]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_windows.txt:54`
[^191]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_windows.txt:85`
[^192]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_windows.txt:116`
[^193]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_windows.txt:137`
[^194]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_windshields.txt:22`
[^195]: `3034636011/mods/89dodgeCaravan/42.20/media/scripts/vehicles/template_DGC89_windshields.txt:80`
