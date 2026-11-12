# 美国乡村 SUV（'89 Ford Bronco）

两门硬派 SUV，比 W460 和揽胜更贴肯塔基；农场、林道、乡间土路的常见车。

归属：**日常组合（玩法待验收）**；档案视图 `b422-compat`。
当前版本定义：**整车 3、本地物品定义 9、配方 9**；另引用共享物品 37。本地定义数含内部保留项，见独立列表；整车定义包括覆盖原版的条目，不等于新增车型数。

## 如何查找

- **生成整车**：在生成车辆菜单搜索下表完整 ID；显示译名时搜索中文列。联机管理命令用 `/addvehicle 完整ID`。
- **添加到背包**：普通物品、维修件、改装件都在添加物品菜单使用完整物品 ID；不要拿配方或内部槽位去刷车。
- **制作配方**：在制作界面查译名；配方 ID 用于排查，不是可放进背包的物品。
- 中文解释说明用途；只有翻译文件中找到的文字才称为游戏中文名。缺译保留脚本显示名，冲突列出各译文。

## 整车

| 完整生成车辆 ID | 当前中文名 / 名称状态 | 英文名或脚本名 | 变体说明 | 来源 |
| --- | --- | --- | --- | --- |
| `Base.89fordBronco` | 89款福特烈马[^1] | '89 Ford Bronco[^2] | 脚本座位数 4；机修类型 2；具体外观与性能待游戏实刷 | [^3] |
| `Base.89fordBroncoPD` | 89款福特烈马警用版[^4] | '89 Ford Bronco Police[^5] | 脚本座位数 4；机修类型 2；具体外观与性能待游戏实刷 | [^6] |
| `Base.89fordBroncoRanger` | 89款福特烈马护林员版[^7] | '89 Ford Bronco Ranger[^8] | 脚本座位数 4；机修类型 2；具体外观与性能待游戏实刷 | [^9] |

## 普通物品与书籍

| 完整物品 ID | 游戏显示名 / 名称状态 | 中文用途 / 类别 | 菜单 | 适用车辆与安装位置 | 来源 / 状态 |
| --- | --- | --- | --- | --- | --- |
| `Base.89BroncoMagazine` | 89 Ford Bronco Auto Manual（未找到有效中文译文） | 阅读资料；脚本声明解锁：制作第八代福特F系列引擎盖（Base.8thGenFordFseriesMakeHood）、制作第八代福特F系列前车门（Base.8thGenFordFseriesMakeFrontDoor）、制作第八代福特F系列挡风玻璃（Base.8thGenFordFseriesMakeFrontWindshield）、制作第八代福特F系列前侧窗（Base.8thGenFordFseriesMakeFrontSideWindow）、制作89款福特烈马后备箱盖（Base.89BroncoMakeTrunkLid）、制作89款福特烈马后侧窗（Base.89BroncoMakeRearSideWindow）、制作89款福特烈马后挡风玻璃（Base.89BroncoMakeRearWindshield）、制作89款福特烈马后斗硬顶（Base.89BroncoMakeBedCap）、制作89款福特烈马货箱隔栏（Base.89BroncoMakeBedBarrier）、制作80年代皮卡车顶行李架（Base.80sPickupMakeRoofrack）、制作80年代皮卡前座椅（Base.80sPickupMakeFrontSeat）、制作80年代皮卡后座椅（Base.80sPickupMakeRearSeat） / 普通物品 / 书籍 | 添加物品 | 未定位整车安装关系 | 89fordBronco[^10] |

## 维修配件

| 完整物品 ID | 游戏显示名 / 名称状态 | 中文用途 / 类别 | 菜单 | 适用车辆与安装位置 | 来源 / 状态 |
| --- | --- | --- | --- | --- | --- |
| `Base.89BroncoBarrier` | 89 Ford Bronco Bed Barrier（未找到有效中文译文） | 车辆安装件，用于车辆安装位（DAMNBarrier）；适用车型见右列 / 维修配件 | 添加物品 | Base.89fordBronco → DAMNBarrier；Base.89fordBroncoPD → DAMNBarrier；Base.89fordBroncoRanger → DAMNBarrier | 89fordBronco[^11] |
| `Base.89BroncoTrunkDoor2` | 89 Ford Bronco Trunk Lid（未找到有效中文译文） | 车辆安装件，用于后备箱（TrunkDoor）；适用车型见右列 / 维修配件 | 添加物品 | Base.89fordBronco → TrunkDoor；Base.89fordBroncoPD → TrunkDoor；Base.89fordBroncoRanger → TrunkDoor | 89fordBronco[^12] |
| `Base.89BroncoWindowSideRear2` | 89 Ford Bronco Rear Side Window（未找到有效中文译文） | 车辆安装件，用于车窗（WindowRearLeft）、车窗（WindowRearRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.89fordBronco → WindowRearLeft；Base.89fordBronco → WindowRearRight；Base.89fordBroncoPD → WindowRearLeft；Base.89fordBroncoPD → WindowRearRight；Base.89fordBroncoRanger → WindowRearLeft；Base.89fordBroncoRanger → WindowRearRight | 89fordBronco[^13] |
| `Base.89BroncoWindshieldRear2` | 89 Ford Bronco Rear Windshield（未找到有效中文译文） | 车辆安装件，用于挡风玻璃（WindshieldRear）；适用车型见右列 / 维修配件 | 添加物品 | Base.89fordBronco → WindshieldRear；Base.89fordBroncoPD → WindshieldRear；Base.89fordBroncoRanger → WindshieldRear | 89fordBronco[^14] |

## 改装配件

| 完整物品 ID | 游戏显示名 / 名称状态 | 中文用途 / 类别 | 菜单 | 适用车辆与安装位置 | 来源 / 状态 |
| --- | --- | --- | --- | --- | --- |
| `Base.89BroncoBedCover` | 89 Ford Bronco Bed Cover（未找到有效中文译文） | 车辆安装件，用于车辆安装位（BR89BedCover）；适用车型见右列 / 改装配件 | 添加物品 | Base.89fordBronco → BR89BedCover；Base.89fordBroncoPD → BR89BedCover；Base.89fordBroncoRanger → BR89BedCover | 89fordBronco[^15] |
| `Base.89BroncoBullbarFront` | 89 Ford Bronco Front Bullbar（未找到有效中文译文） | 车辆安装件，用于保险杠（DAMNBumperFront）；适用车型见右列 / 改装配件 | 添加物品 | Base.89fordBronco → DAMNBumperFront；Base.89fordBroncoPD → DAMNBumperFront；Base.89fordBroncoRanger → DAMNBumperFront | 89fordBronco[^16] |
| `Base.89BroncoBumperFront` | 89 Ford Bronco Front Bumper（未找到有效中文译文） | 车辆安装件，用于保险杠（DAMNBumperFront）；适用车型见右列 / 改装配件 | 添加物品 | Base.89fordBronco → DAMNBumperFront；Base.89fordBroncoPD → DAMNBumperFront；Base.89fordBroncoRanger → DAMNBumperFront | 89fordBronco[^17] |
| `Base.89BroncoBumperRear` | 89 Ford Bronco Rear Bumper（未找到有效中文译文） | 车辆安装件，用于保险杠（DAMNBumperRear）；适用车型见右列 / 改装配件 | 添加物品 | Base.89fordBronco → DAMNBumperRear；Base.89fordBroncoPD → DAMNBumperRear；Base.89fordBroncoRanger → DAMNBumperRear | 89fordBronco[^18] |

## 共享配件

下列物品由已启用依赖或游戏原版提供，不计入本 Mod 的本地物品数。

| 完整物品 ID | 游戏显示名 / 名称状态 | 中文用途 / 类别 | 菜单 | 适用车辆与安装位置 | 来源 / 状态 |
| --- | --- | --- | --- | --- | --- |
| `Base.76chevyKseriesTire2` | 76 Chevrolet K Series Tire（未找到有效中文译文） | 车辆安装件，用于轮胎（Tire*）、轮胎（DAMNSpareTire）、轮胎（DAMNSpareTireRoof）；适用车型见右列 / 维修配件 | 添加物品 | Base.89fordBronco → Tire*；Base.89fordBronco → DAMNSpareTire；Base.89fordBronco → DAMNSpareTireRoof；Base.89fordBroncoPD → Tire*；Base.89fordBroncoPD → DAMNSpareTire；Base.89fordBroncoPD → DAMNSpareTireRoof；Base.89fordBroncoRanger → Tire* | damnlib[^19] |
| `Base.80chevyCKseriesTire1` | 80s Chevrolet C/K Series Tire（未找到有效中文译文） | 车辆安装件，用于轮胎（Tire*）、轮胎（DAMNSpareTire）、轮胎（DAMNSpareTireRoof）；适用车型见右列 / 维修配件 | 添加物品 | Base.89fordBronco → Tire*；Base.89fordBronco → DAMNSpareTire；Base.89fordBronco → DAMNSpareTireRoof；Base.89fordBroncoPD → Tire*；Base.89fordBroncoPD → DAMNSpareTire；Base.89fordBroncoPD → DAMNSpareTireRoof；Base.89fordBroncoRanger → Tire* | damnlib[^20] |
| `Base.80chevyCKseriesTire2` | 80s Chevrolet C/K Series Tire（未找到有效中文译文） | 车辆安装件，用于轮胎（Tire*）、轮胎（DAMNSpareTire）、轮胎（DAMNSpareTireRoof）；适用车型见右列 / 维修配件 | 添加物品 | Base.89fordBronco → Tire*；Base.89fordBronco → DAMNSpareTire；Base.89fordBronco → DAMNSpareTireRoof；Base.89fordBroncoPD → Tire*；Base.89fordBroncoPD → DAMNSpareTire；Base.89fordBroncoPD → DAMNSpareTireRoof；Base.89fordBroncoRanger → Tire* | damnlib[^21] |
| `Base.80sOffroadTireA` | 80s Offroad Tire Type A（未找到有效中文译文） | 车辆安装件，用于轮胎（Tire*）、轮胎（DAMNSpareTire）、轮胎（DAMNSpareTireRoof）；适用车型见右列 / 维修配件 | 添加物品 | Base.89fordBronco → Tire*；Base.89fordBronco → DAMNSpareTire；Base.89fordBronco → DAMNSpareTireRoof；Base.89fordBroncoPD → Tire*；Base.89fordBroncoPD → DAMNSpareTire；Base.89fordBroncoPD → DAMNSpareTireRoof；Base.89fordBroncoRanger → Tire* | damnlib[^22] |
| `Base.80sPickupBullbarFront` | 80s Pickup Front Bullbar（未找到有效中文译文） | 车辆安装件，用于保险杠（DAMNBumperFront）；适用车型见右列 / 改装配件 | 添加物品 | Base.89fordBronco → DAMNBumperFront；Base.89fordBroncoPD → DAMNBumperFront；Base.89fordBroncoRanger → DAMNBumperFront | damnlib[^23] |
| `Base.80sPickupBullbarRear` | 80s Pickup Rear Bullbar（未找到有效中文译文） | 车辆安装件，用于保险杠（DAMNBumperRear）；适用车型见右列 / 改装配件 | 添加物品 | Base.89fordBronco → DAMNBumperRear；Base.89fordBroncoPD → DAMNBumperRear；Base.89fordBroncoRanger → DAMNBumperRear | damnlib[^24] |
| `Base.80sPickupRollbarB` | 80s Pickup Rollbar Type B（未找到有效中文译文） | 车辆安装件，用于车辆安装位（BR89Rollbar）；适用车型见右列 / 维修配件 | 添加物品 | Base.89fordBronco → BR89Rollbar；Base.89fordBroncoPD → BR89Rollbar；Base.89fordBroncoRanger → BR89Rollbar | damnlib[^25] |
| `Base.80sPickupRoofrackA` | 80s Pickup Roofrack（未找到有效中文译文） | 车辆安装件，用于车顶行李架（CH88Roofrack）、车顶行李架（JP82Roofrack）、车顶行李架（BR89Roofrack）；适用车型见右列 / 改装配件 | 添加物品 | Base.89fordBronco → BR89Roofrack；Base.89fordBroncoPD → BR89Roofrack；Base.89fordBroncoRanger → BR89Roofrack | damnlib[^26] |
| `Base.80sPickupSeatFront2` | 80s Pickup Front Seat（未找到有效中文译文） | 车辆安装件，用于座椅（SeatFront*）；适用车型见右列 / 维修配件 | 添加物品 | Base.89fordBronco → SeatFront*；Base.89fordBroncoPD → SeatFront*；Base.89fordBroncoRanger → SeatFront* | damnlib[^27] |
| `Base.80sPickupSeatRear2` | 80s Pickup Rear Seat（未找到有效中文译文） | 车辆安装件，用于座椅（SeatRear*）；适用车型见右列 / 维修配件 | 添加物品 | Base.89fordBronco → SeatRear*；Base.89fordBroncoPD → SeatRear*；Base.89fordBroncoRanger → SeatRear* | damnlib[^28] |
| `Base.80sPickupWindowFrontArmor` | 80s Pickup Front Window Armor（未找到有效中文译文） | 车辆安装件，用于防护件（DAMNFrontLeftArmor）、防护件（DAMNFrontRightArmor）；适用车型见右列 / 改装配件 | 添加物品 | Base.89fordBronco → DAMNFrontLeftArmor；Base.89fordBronco → DAMNFrontRightArmor；Base.89fordBroncoPD → DAMNFrontLeftArmor；Base.89fordBroncoPD → DAMNFrontRightArmor；Base.89fordBroncoRanger → DAMNFrontLeftArmor；Base.89fordBroncoRanger → DAMNFrontRightArmor | damnlib[^29] |
| `Base.80sPickupWindowRearArmor` | 80s Pickup Rear Window Armor（未找到有效中文译文） | 车辆安装件，用于防护件（DAMNRearLeftArmor）、防护件（DAMNRearRightArmor）；适用车型见右列 / 改装配件 | 添加物品 | Base.89fordBronco → DAMNRearLeftArmor；Base.89fordBronco → DAMNRearRightArmor；Base.89fordBroncoPD → DAMNRearLeftArmor；Base.89fordBroncoPD → DAMNRearRightArmor；Base.89fordBroncoRanger → DAMNRearLeftArmor；Base.89fordBroncoRanger → DAMNRearRightArmor | damnlib[^30] |
| `Base.80sPickupWindshieldArmor` | 80s Pickup Windshield Armor（未找到有效中文译文） | 车辆安装件，用于挡风玻璃（DAMNWindshieldArmor）；适用车型见右列 / 改装配件 | 添加物品 | Base.89fordBronco → DAMNWindshieldArmor；Base.89fordBroncoPD → DAMNWindshieldArmor；Base.89fordBroncoRanger → DAMNWindshieldArmor | damnlib[^31] |
| `Base.8thGenFordFseriesEngineDoor2` | 8th Gen Ford F Series Hood（未找到有效中文译文） | 车辆安装件，用于引擎盖（EngineDoor）；适用车型见右列 / 维修配件 | 添加物品 | Base.89fordBronco → EngineDoor；Base.89fordBroncoPD → EngineDoor；Base.89fordBroncoRanger → EngineDoor | damnlib[^32] |
| `Base.8thGenFordFseriesFrontDoor2` | 8th Gen Ford F Series Front Door（未找到有效中文译文） | 车辆安装件，用于车门（DoorFrontLeft）、车门（DoorFrontRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.89fordBronco → DoorFrontLeft；Base.89fordBronco → DoorFrontRight；Base.89fordBroncoPD → DoorFrontLeft；Base.89fordBroncoPD → DoorFrontRight；Base.89fordBroncoRanger → DoorFrontLeft；Base.89fordBroncoRanger → DoorFrontRight | damnlib[^33] |
| `Base.8thGenFordFseriesWindowFrontSide2` | 8th Gen Ford F Series Front Side Window（未找到有效中文译文） | 车辆安装件，用于车窗（WindowFrontLeft）、车窗（WindowFrontRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.89fordBronco → WindowFrontLeft；Base.89fordBronco → WindowFrontRight；Base.89fordBroncoPD → WindowFrontLeft；Base.89fordBroncoPD → WindowFrontRight；Base.89fordBroncoRanger → WindowFrontLeft；Base.89fordBroncoRanger → WindowFrontRight | damnlib[^34] |
| `Base.8thGenFordFseriesWindshield2` | 8th Gen Ford F Series Windshield（未找到有效中文译文） | 车辆安装件，用于挡风玻璃（Windshield）；适用车型见右列 / 维修配件 | 添加物品 | Base.89fordBronco → Windshield；Base.89fordBroncoPD → Windshield；Base.89fordBroncoRanger → Windshield | damnlib[^35] |
| `Base.90chevyCKseriesTire1` | 90s Chevrolet C/K Series Tire（未找到有效中文译文） | 车辆安装件，用于轮胎（Tire*）、轮胎（DAMNSpareTire）、轮胎（DAMNSpareTireRoof）；适用车型见右列 / 维修配件 | 添加物品 | Base.89fordBronco → Tire*；Base.89fordBronco → DAMNSpareTire；Base.89fordBronco → DAMNSpareTireRoof；Base.89fordBroncoPD → Tire*；Base.89fordBroncoPD → DAMNSpareTire；Base.89fordBroncoPD → DAMNSpareTireRoof；Base.89fordBroncoRanger → Tire* | damnlib[^36] |
| `Base.90chevyCKseriesTire2` | 90s Chevrolet C/K Series Tire（未找到有效中文译文） | 车辆安装件，用于轮胎（Tire*）、轮胎（DAMNSpareTire）、轮胎（DAMNSpareTireRoof）；适用车型见右列 / 维修配件 | 添加物品 | Base.89fordBronco → Tire*；Base.89fordBronco → DAMNSpareTire；Base.89fordBronco → DAMNSpareTireRoof；Base.89fordBroncoPD → Tire*；Base.89fordBroncoPD → DAMNSpareTire；Base.89fordBroncoPD → DAMNSpareTireRoof；Base.89fordBroncoRanger → Tire* | damnlib[^37] |
| `Base.BigGasTank2` | 油箱 (大型)（翻译文件含非标准语法，待游戏核实）[^39] | 车辆安装件，用于油箱（GasTank）；适用车型见右列 / 维修配件 | 添加物品 | Base.89fordBronco → GasTank；Base.89fordBroncoPD → GasTank；Base.89fordBroncoRanger → GasTank | 游戏原版[^38] |
| `Base.CarBattery2` | 汽车电池（翻译文件含非标准语法，待游戏核实）[^41] | 车辆安装件，用于蓄电池（Battery）、蓄电池（GRHouseBattery1）、蓄电池（GRHouseBattery2）；适用车型见右列 / 维修配件 | 添加物品 | Base.89fordBronco → Battery；Base.89fordBroncoPD → Battery；Base.89fordBroncoRanger → Battery | 游戏原版[^40] |
| `Base.GloveBox2` | 手套箱（翻译文件含非标准语法，待游戏核实）[^43] | 车辆安装件，用于车辆安装位（GloveBox）；适用车型见右列 / 维修配件 | 添加物品 | Base.89fordBronco → GloveBox；Base.89fordBroncoPD → GloveBox；Base.89fordBroncoRanger → GloveBox | 游戏原版[^42] |
| `Base.LightBulb` | 灯泡-白色 / 灯泡 (白)（译文冲突，待游戏核实）[^45] | 车辆安装件，用于车灯（Headlight*）、车灯（JP82DorothyLights）；适用车型见右列 / 维修配件 | 添加物品 | Base.89fordBronco → Headlight*；Base.89fordBroncoPD → Headlight*；Base.89fordBroncoRanger → Headlight* | 游戏原版[^44] |
| `Base.ModernBrake2` | 制动器 (高级)（翻译文件含非标准语法，待游戏核实）[^47] | 车辆安装件，用于制动器（Brake*）；适用车型见右列 / 维修配件 | 添加物品 | Base.89fordBronco → Brake*；Base.89fordBroncoPD → Brake*；Base.89fordBroncoRanger → Brake* | 游戏原版[^46] |
| `Base.ModernCarMuffler2` | 消声器 (高级)（翻译文件含非标准语法，待游戏核实）[^49] | 车辆安装件，用于消声器（Muffler）；适用车型见右列 / 维修配件 | 添加物品 | Base.89fordBronco → Muffler；Base.89fordBroncoPD → Muffler；Base.89fordBroncoRanger → Muffler | 游戏原版[^48] |
| `Base.ModernSuspension2` | 悬挂 (高级)（翻译文件含非标准语法，待游戏核实）[^51] | 车辆安装件，用于悬挂（Suspension*）；适用车型见右列 / 维修配件 | 添加物品 | Base.89fordBronco → Suspension*；Base.89fordBroncoPD → Suspension*；Base.89fordBroncoRanger → Suspension* | 游戏原版[^50] |
| `Base.NormalBrake2` | 制动器 (普通)（翻译文件含非标准语法，待游戏核实）[^53] | 车辆安装件，用于制动器（Brake*）；适用车型见右列 / 维修配件 | 添加物品 | Base.89fordBronco → Brake*；Base.89fordBroncoPD → Brake*；Base.89fordBroncoRanger → Brake* | 游戏原版[^52] |
| `Base.NormalCarMuffler2` | 消声器 (普通)（翻译文件含非标准语法，待游戏核实）[^55] | 车辆安装件，用于消声器（Muffler）；适用车型见右列 / 维修配件 | 添加物品 | Base.89fordBronco → Muffler；Base.89fordBroncoPD → Muffler；Base.89fordBroncoRanger → Muffler | 游戏原版[^54] |
| `Base.NormalGasTank2` | 油箱 (标准)（翻译文件含非标准语法，待游戏核实）[^57] | 车辆安装件，用于油箱（GasTank）；适用车型见右列 / 维修配件 | 添加物品 | Base.89fordBronco → GasTank；Base.89fordBroncoPD → GasTank；Base.89fordBroncoRanger → GasTank | 游戏原版[^56] |
| `Base.NormalSuspension2` | 悬挂 (普通)（翻译文件含非标准语法，待游戏核实）[^59] | 车辆安装件，用于悬挂（Suspension*）；适用车型见右列 / 维修配件 | 添加物品 | Base.89fordBronco → Suspension*；Base.89fordBroncoPD → Suspension*；Base.89fordBroncoRanger → Suspension* | 游戏原版[^58] |
| `Base.OldBrake2` | 制动器 (老式)（翻译文件含非标准语法，待游戏核实）[^61] | 车辆安装件，用于制动器（Brake*）；适用车型见右列 / 维修配件 | 添加物品 | Base.89fordBronco → Brake*；Base.89fordBroncoPD → Brake*；Base.89fordBroncoRanger → Brake* | 游戏原版[^60] |
| `Base.OldCarMuffler2` | 消声器 (老式)（翻译文件含非标准语法，待游戏核实）[^63] | 车辆安装件，用于消声器（Muffler）；适用车型见右列 / 维修配件 | 添加物品 | Base.89fordBronco → Muffler；Base.89fordBroncoPD → Muffler；Base.89fordBroncoRanger → Muffler | 游戏原版[^62] |
| `Base.RadioBlack` | 收音机 (超值科技) / 收音机 (廉科) / 廉科牌收音机（译文冲突，待游戏核实）[^65] | 车辆安装件，用于车辆安装位（Radio）；适用车型见右列 / 维修配件 | 添加物品 | Base.89fordBronco → Radio；Base.89fordBroncoPD → Radio；Base.89fordBroncoRanger → Radio | 游戏原版[^64] |
| `Base.RadioMakeShift` | 收音机 (简易) / 自制收音机（译文冲突，待游戏核实）[^67] | 车辆安装件，用于车辆安装位（Radio）；适用车型见右列 / 维修配件 | 添加物品 | Base.89fordBronco → Radio；Base.89fordBroncoPD → Radio；Base.89fordBroncoRanger → Radio | 游戏原版[^66] |
| `Base.RadioRed` | 导航仪 / 收音机 (昂科) / 昂科牌收音机（译文冲突，待游戏核实）[^69] | 车辆安装件，用于车辆安装位（Radio）；适用车型见右列 / 维修配件 | 添加物品 | Base.89fordBronco → Radio；Base.89fordBroncoPD → Radio；Base.89fordBroncoRanger → Radio | 游戏原版[^68] |
| `Base.SmallGasTank2` | 油箱 (小型)（翻译文件含非标准语法，待游戏核实）[^71] | 车辆安装件，用于油箱（GasTank）；适用车型见右列 / 维修配件 | 添加物品 | Base.89fordBronco → GasTank；Base.89fordBroncoPD → GasTank；Base.89fordBroncoRanger → GasTank | 游戏原版[^70] |

## 制作配方

| 配方完整 ID（排查用） | 游戏配方名 / 名称状态 | 中文用途 | 菜单 | 来源 |
| --- | --- | --- | --- | --- |
| `Base.80sPickupMakeTire` | 制作80年代皮卡轮胎[^72] | 制作产出：80s Offroad Tire Type A（车辆安装件，用于轮胎（Tire*）、轮胎（DAMNSpareTire）、轮胎（DAMNSpareTireRoof）；适用车型见右列） | 制作界面 | [^73] |
| `Base.89BroncoMakeBedBarrier` | 制作89款福特烈马货箱隔栏[^74] | 制作产出：89 Ford Bronco Bed Barrier（车辆安装件，用于车辆安装位（DAMNBarrier）；适用车型见右列） | 制作界面 | [^75] |
| `Base.89BroncoMakeBedCap` | 制作89款福特烈马后斗硬顶[^76] | 制作产出：89 Ford Bronco Bed Cover（车辆安装件，用于车辆安装位（BR89BedCover）；适用车型见右列） | 制作界面 | [^77] |
| `Base.89BroncoMakeFrontBumper` | 制作89款福特烈马前保险杠[^78] | 制作产出：89 Ford Bronco Front Bumper（车辆安装件，用于保险杠（DAMNBumperFront）；适用车型见右列） | 制作界面 | [^79] |
| `Base.89BroncoMakeRearBumper` | 制作89款福特烈马后保险杠[^80] | 制作产出：89 Ford Bronco Rear Bumper（车辆安装件，用于保险杠（DAMNBumperRear）；适用车型见右列） | 制作界面 | [^81] |
| `Base.89BroncoMakeRearSideWindow` | 制作89款福特烈马后侧窗[^82] | 制作产出：89 Ford Bronco Rear Side Window（车辆安装件，用于车窗（WindowRearLeft）、车窗（WindowRearRight）；适用车型见右列） | 制作界面 | [^83] |
| `Base.89BroncoMakeRearWindshield` | 制作89款福特烈马后挡风玻璃[^84] | 制作产出：89 Ford Bronco Rear Windshield（车辆安装件，用于挡风玻璃（WindshieldRear）；适用车型见右列） | 制作界面 | [^85] |
| `Base.89BroncoMakeReinforcedFrontBumper` | 制作89款福特烈马加固前保险杠[^86] | 制作产出：89 Ford Bronco Front Bullbar（车辆安装件，用于保险杠（DAMNBumperFront）；适用车型见右列） | 制作界面 | [^87] |
| `Base.89BroncoMakeTrunkLid` | 制作89款福特烈马后备箱盖[^88] | 制作产出：89 Ford Bronco Trunk Lid（车辆安装件，用于后备箱（TrunkDoor）；适用车型见右列） | 制作界面 | [^89] |

## 内部定义、历史分支与未解析引用

有效资源层：42.20, common；仅合并 common 与所选版本，Overlay 按相对路径覆盖。
车辆模板 18 个、内部槽位 63 个，均不算整车或背包物品。旧根目录和未选中版本的定义不列入当前可用表。模板中短物品引用若追加机修类型后缀才匹配定义，属于静态映射，安装仍待实测。

内部或过时的 item 定义单列于此，不在上面的背包刷取建议中；它们仍计入各自来源的定义数量。

| 保留定义 ID（不作正常刷取建议） | 脚本显示名 | 中文说明 / 状态 | 来源 |
| --- | --- | --- | --- |
| `damnCraft.Trunk2` | no | 车辆后备箱的内部容量载体，关联车辆槽位与容积状态；不是可携带的旅行箱；显示名 no、图标 na；不作正常刷取建议 | [^90] |

<details><summary>查看内部槽位（不能直接刷取）</summary>

| 槽位 | 名称或说明 | 来源 |
| --- | --- | --- |
| `BR89BedCover` | 后斗硬顶 / 车辆安装位 | [^91] |
| `BR89Rollbar` | 防滚架 / 车辆安装位 | [^92] |
| `BR89Roofrack` | 车顶行李架 / 车顶行李架 | [^93] |
| `BR89Trunk` | 货箱容量 / 后备箱 | [^94] |
| `Battery` | 电池 / 蓄电池 | [^95] |
| `Brake*` | Brake* / 制动器 | [^96] |
| `BrakeFrontLeft` | 左前制动 / 制动器 | [^97] |
| `BrakeFrontRight` | 右前制动 / 制动器 | [^98] |
| `BrakeRearLeft` | 左后制动 / 制动器 | [^99] |
| `BrakeRearRight` | 右后制动 / 制动器 | [^100] |
| `DAMNBarrier` | 驾驶室隔板 / 车辆安装位 | [^101] |
| `DAMNBumperFront` | 前保险杠 / 保险杠 | [^102] |
| `DAMNBumperRear` | 后保险杠 / 保险杠 | [^103] |
| `DAMNFrontLeftArmor` | 左前车窗装甲 / 防护件 | [^104] |
| `DAMNFrontRightArmor` | 右前车窗装甲 / 防护件 | [^105] |
| `DAMNGunrack` | 枪架 / 枪架 | [^106] |
| `DAMNRearLeftArmor` | 左后车窗装甲 / 防护件 | [^107] |
| `DAMNRearRightArmor` | 右后车窗装甲 / 防护件 | [^108] |
| `DAMNSpareTire` | 备胎 / 轮胎 | [^109] |
| `DAMNSpareTireRoof` | 车顶备胎 / 轮胎 | [^110] |
| `DAMNWindshieldArmor` | 挡风玻璃装甲 / 挡风玻璃 | [^111] |
| `Door*` | Door* / 车门 | [^112] |
| `DoorFrontLeft` | 左前门 / 车门 | [^113] |
| `DoorFrontRight` | 右前门 / 车门 | [^114] |
| `Engine` | 引擎 / 发动机 | [^115] |
| `EngineDoor` | 引擎盖 / 引擎盖 | [^116] |
| `GasTank` | 油箱 / 油箱 | [^117] |
| `GloveBox` | 手套箱 / 车辆安装位 | [^118] |
| `Headlight*` | Headlight* / 车灯 | [^119] |
| `HeadlightLeft` | 左大灯 / 车灯 | [^120] |
| `HeadlightRearLeft` | 左尾灯 / 车灯 | [^121] |
| `HeadlightRearRight` | 右尾灯 / 车灯 | [^122] |
| `HeadlightRight` | 右大灯 / 车灯 | [^123] |
| `Heater` | 加热器 / 车辆安装位 | [^124] |
| `Muffler` | 排气消声器 / 消声器 | [^125] |
| `PassengerCompartment` | 乘员舱 / 车辆安装位 | [^126] |
| `Radio` | 电台 / 车辆安装位 | [^127] |
| `SeatFront*` | SeatFront* / 座椅 | [^128] |
| `SeatFrontLeft` | 驾驶座 / 座椅 | [^129] |
| `SeatFrontRight` | 右前座 / 座椅 | [^130] |
| `SeatRear*` | SeatRear* / 座椅 | [^131] |
| `SeatRearLeft` | 左后座 / 座椅 | [^132] |
| `SeatRearRight` | 右后座 / 座椅 | [^133] |
| `Suspension*` | Suspension* / 悬挂 | [^134] |
| `SuspensionFrontLeft` | 左前悬挂 / 悬挂 | [^135] |
| `SuspensionFrontRight` | 右前悬挂 / 悬挂 | [^136] |
| `SuspensionRearLeft` | 左后悬挂 / 悬挂 | [^137] |
| `SuspensionRearRight` | 右后悬挂 / 悬挂 | [^138] |
| `Tire*` | Tire* / 轮胎 | [^139] |
| `TireFrontLeft` | 左前胎 / 轮胎 | [^140] |
| `TireFrontRight` | 右前胎 / 轮胎 | [^141] |
| `TireRearLeft` | 左后胎 / 轮胎 | [^142] |
| `TireRearRight` | 右后胎 / 轮胎 | [^143] |
| `TruckBed` | 补给箱 / 行李箱 / 车辆安装位 | [^144] |
| `TrunkDoor` | 后车盖 / 后备箱 | [^145] |
| `WindowFront*` | WindowFront* / 车窗 | [^146] |
| `WindowFrontLeft` | 左前窗 / 车窗 | [^147] |
| `WindowFrontRight` | 右前窗 / 车窗 | [^148] |
| `WindowRear*` | WindowRear* / 车窗 | [^149] |
| `WindowRearLeft` | 左后窗 / 车窗 | [^150] |
| `WindowRearRight` | 右后窗 / 车窗 | [^151] |
| `Windshield` | 挡风玻璃 / 挡风玻璃 | [^152] |
| `WindshieldRear` | 后挡风玻璃 / 挡风玻璃 | [^153] |

</details>

<details><summary>未定位引用：保留排查线索，不作为可刷 ID</summary>

| 引用（不可直接刷取） | 原因 | 来源 |
| --- | --- | --- |
| Base.BR89SpareTiresPD | 模板未在已启用内容中定位 | [^9] |

</details>


## 概览

| Mod ID / 文件夹 | 分发端 | 版本 | 选择的 mod.info | 原件范围 → 当前范围 |
| --- | --- | --- | --- | --- |
| `89fordBronco` / `89fordBronco` | both（双端） | 未标注 | `42.20/mod.info` | 42.20.0 … - → 42.20.0 … - |

原件体积 11.3 MB；体积按完整目录统计，与当前内容定义数分开。
工作坊：[查看作者页面](https://steamcommunity.com/sharedfiles/filedetails/?id=2886833398)。

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

[^1]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/IG_UI.json:2773`
[^2]: `2886833398/mods/89fordBronco/common/media/lua/shared/Translate/EN/IG_UI.json:3`
[^3]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBronco.txt:24`
[^4]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/IG_UI.json:2774`
[^5]: `2886833398/mods/89fordBronco/common/media/lua/shared/Translate/EN/IG_UI.json:4`
[^6]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBroncoPD.txt:17`
[^7]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/IG_UI.json:2775`
[^8]: `2886833398/mods/89fordBronco/common/media/lua/shared/Translate/EN/IG_UI.json:5`
[^9]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBroncoRanger.txt:3`
[^10]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBronco_vehiclesitems.txt:5`
[^11]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBronco_vehiclesitems.txt:133`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_barrier.txt:13`
[^12]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBronco_vehiclesitems.txt:23`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_trunkdoors.txt:22`
[^13]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBronco_vehiclesitems.txt:87`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_windows.txt:90`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_windows.txt:109`
[^14]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBronco_vehiclesitems.txt:102`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_trunkdoors.txt:146`
[^15]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBronco_vehiclesitems.txt:119`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_bed_cover.txt:12`
[^16]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBronco_vehiclesitems.txt:55`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_frontBumper.txt:26`
[^17]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBronco_vehiclesitems.txt:40`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_frontBumper.txt:26`
[^18]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBronco_vehiclesitems.txt:70`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_rearBumper.txt:19`
[^19]: `3171167894/mods/damnlib/42.20/media/scripts/commonItems/damnCommonTires_vehiclesitems.txt:190`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_tire.txt:302`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_spareTires.txt:6`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_spareTires.txt:57`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBroncoPD.txt:264`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBroncoRanger.txt:245`
[^20]: `3171167894/mods/damnlib/42.20/media/scripts/commonItems/damnCommonTires_vehiclesitems.txt:272`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_tire.txt:302`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_spareTires.txt:6`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_spareTires.txt:57`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBroncoPD.txt:264`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBroncoRanger.txt:245`
[^21]: `3171167894/mods/damnlib/42.20/media/scripts/commonItems/damnCommonTires_vehiclesitems.txt:252`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_tire.txt:302`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_spareTires.txt:6`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_spareTires.txt:57`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBroncoPD.txt:264`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBroncoRanger.txt:245`
[^22]: `3171167894/mods/damnlib/42.20/media/scripts/commonItems/damnCommonTires_vehiclesitems.txt:418`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_tire.txt:302`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_spareTires.txt:6`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_spareTires.txt:57`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBroncoPD.txt:264`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBroncoRanger.txt:245`
[^23]: `3171167894/mods/damnlib/42.20/media/scripts/commonItems/80sPickups_vehiclesitems.txt:69`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_frontBumper.txt:26`
[^24]: `3171167894/mods/damnlib/42.20/media/scripts/commonItems/80sPickups_vehiclesitems.txt:84`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_rearBumper.txt:19`
[^25]: `3171167894/mods/damnlib/42.20/media/scripts/commonItems/80sPickups_vehiclesitems.txt:147`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_rollbar.txt:12`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_rollbarPD.txt:12`
[^26]: `3171167894/mods/damnlib/42.20/media/scripts/commonItems/80sPickups_vehiclesitems.txt:6`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_roofrack.txt:13`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_roofrackPD.txt:13`
[^27]: `3171167894/mods/damnlib/42.20/media/scripts/commonItems/80sPickups_vehiclesitems.txt:101`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_seats.txt:109`
[^28]: `3171167894/mods/damnlib/42.20/media/scripts/commonItems/80sPickups_vehiclesitems.txt:116`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_seats.txt:160`
[^29]: `3171167894/mods/damnlib/42.20/media/scripts/commonItems/80sPickups_vehiclesitems.txt:24`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_armor.txt:105`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_armor.txt:169`
[^30]: `3171167894/mods/damnlib/42.20/media/scripts/commonItems/80sPickups_vehiclesitems.txt:54`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_armor.txt:233`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_armor.txt:296`
[^31]: `3171167894/mods/damnlib/42.20/media/scripts/commonItems/80sPickups_vehiclesitems.txt:39`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_armor.txt:42`
[^32]: `3171167894/mods/damnlib/42.20/media/scripts/commonItems/8thGenFordFseries_vehicleitems.txt:22`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_hood.txt:14`
[^33]: `3171167894/mods/damnlib/42.20/media/scripts/commonItems/8thGenFordFseries_vehicleitems.txt:5`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_doors.txt:24`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_doors.txt:78`
[^34]: `3171167894/mods/damnlib/42.20/media/scripts/commonItems/8thGenFordFseries_vehicleitems.txt:72`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_windows.txt:38`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_windows.txt:64`
[^35]: `3171167894/mods/damnlib/42.20/media/scripts/commonItems/8thGenFordFseries_vehicleitems.txt:57`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_windshield.txt:14`
[^36]: `3171167894/mods/damnlib/42.20/media/scripts/commonItems/damnCommonTires_vehiclesitems.txt:312`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_tire.txt:302`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_spareTires.txt:6`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_spareTires.txt:57`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBroncoPD.txt:264`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBroncoRanger.txt:245`
[^37]: `3171167894/mods/damnlib/42.20/media/scripts/commonItems/damnCommonTires_vehiclesitems.txt:292`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_tire.txt:302`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_spareTires.txt:6`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_spareTires.txt:57`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBroncoPD.txt:264`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBroncoRanger.txt:245`
[^38]: `游戏原版/media/scripts/generated/items/normal.txt:12408`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBronco.txt:333`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBroncoPD.txt:320`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBroncoRanger.txt:301`
[^39]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:448`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:163`
[^40]: `游戏原版/media/scripts/generated/items/drainable.txt:2368`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBronco.txt:348`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBroncoPD.txt:335`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBroncoRanger.txt:316`
[^41]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:970`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:380`
[^42]: `游戏原版/media/scripts/generated/items/normal.txt:13025`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBronco.txt:306`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBroncoPD.txt:286`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBroncoRanger.txt:267`
[^43]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1776`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:687`
[^44]: `游戏原版/media/scripts/generated/items/normal.txt:4661`；`游戏原版/media/scripts/generated/vehicles/template_headlight.txt:25`
[^45]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:6727`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25103`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2563`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:965`
[^46]: `游戏原版/media/scripts/generated/items/normal.txt:12163`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBronco.txt:396`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBroncoPD.txt:383`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBroncoRanger.txt:364`
[^47]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2780`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1050`
[^48]: `游戏原版/media/scripts/generated/items/normal.txt:13166`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBronco.txt:361`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBroncoPD.txt:348`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBroncoRanger.txt:329`
[^49]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2783`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1053`
[^50]: `游戏原版/media/scripts/generated/items/normal.txt:12282`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBronco.txt:413`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBroncoPD.txt:400`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBroncoRanger.txt:381`
[^51]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2786`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1056`
[^52]: `游戏原版/media/scripts/generated/items/normal.txt:12146`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBronco.txt:396`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBroncoPD.txt:383`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBroncoRanger.txt:364`
[^53]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3219`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1135`
[^54]: `游戏原版/media/scripts/generated/items/normal.txt:13151`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBronco.txt:361`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBroncoPD.txt:348`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBroncoRanger.txt:329`
[^55]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3222`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1138`
[^56]: `游戏原版/media/scripts/generated/items/normal.txt:12393`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBronco.txt:333`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBroncoPD.txt:320`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBroncoRanger.txt:301`
[^57]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3228`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1144`
[^58]: `游戏原版/media/scripts/generated/items/normal.txt:12265`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBronco.txt:413`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBroncoPD.txt:400`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBroncoRanger.txt:381`
[^59]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3231`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1147`
[^60]: `游戏原版/media/scripts/generated/items/normal.txt:12129`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBronco.txt:396`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBroncoPD.txt:383`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBroncoRanger.txt:364`
[^61]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3255`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1165`
[^62]: `游戏原版/media/scripts/generated/items/normal.txt:13136`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBronco.txt:361`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBroncoPD.txt:348`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBroncoRanger.txt:329`
[^63]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3258`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1168`
[^64]: `游戏原版/media/scripts/generated/items/radio.txt:308`；`游戏原版/media/scripts/generated/vehicles/template_radio.txt:5`
[^65]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:7374`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25092`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3645`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:5128`
[^66]: `游戏原版/media/scripts/generated/items/radio.txt:335`；`游戏原版/media/scripts/generated/vehicles/template_radio.txt:5`
[^67]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:7375`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25093`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3649`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:5132`
[^68]: `游戏原版/media/scripts/generated/items/radio.txt:361`；`游戏原版/media/scripts/generated/vehicles/template_radio.txt:5`
[^69]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:3001`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25091`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3651`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:5134`
[^70]: `游戏原版/media/scripts/generated/items/normal.txt:12378`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBronco.txt:333`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBroncoPD.txt:320`；`2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBroncoRanger.txt:301`
[^71]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:4152`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1543`
[^72]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:5659`
[^73]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBronco_recipes.txt:3`
[^74]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:649`
[^75]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBronco_recipes.txt:186`
[^76]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:648`
[^77]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBronco_recipes.txt:161`
[^78]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:645`
[^79]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBronco_recipes.txt:94`
[^80]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:646`
[^81]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBronco_recipes.txt:116`
[^82]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:643`
[^83]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBronco_recipes.txt:50`
[^84]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:644`
[^85]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBronco_recipes.txt:72`
[^86]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:647`
[^87]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBronco_recipes.txt:138`
[^88]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:640`
[^89]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBronco_recipes.txt:25`
[^90]: `3171167894/mods/damnlib/42.20/media/scripts/damnCraft/items_damnCraft.txt:572`
[^91]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_bed_cover.txt:12`
[^92]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_rollbar.txt:12`
[^93]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_roofrack.txt:13`
[^94]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_trunk.txt:5`
[^95]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBronco.txt:348`
[^96]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBronco.txt:396`
[^97]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:5`
[^98]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:18`
[^99]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:31`
[^100]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:44`
[^101]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_barrier.txt:13`
[^102]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_frontBumper.txt:26`
[^103]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_rearBumper.txt:19`
[^104]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_armor.txt:105`
[^105]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_armor.txt:169`
[^106]: `3171167894/mods/damnlib/42.20/media/scripts/commonItems/template_DAMN_gunrack.txt:5`
[^107]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_armor.txt:233`
[^108]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_armor.txt:296`
[^109]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_spareTires.txt:6`
[^110]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_spareTires.txt:57`
[^111]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_armor.txt:42`
[^112]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_doors.txt:132`
[^113]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_doors.txt:24`
[^114]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_doors.txt:78`
[^115]: `游戏原版/media/scripts/generated/vehicles/template_engine.txt:5`
[^116]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_hood.txt:14`
[^117]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBronco.txt:333`
[^118]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBronco.txt:306`
[^119]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:25`
[^120]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:5`
[^121]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:15`
[^122]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:20`
[^123]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:10`
[^124]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBronco.txt:374`
[^125]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBronco.txt:361`
[^126]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBronco.txt:384`
[^127]: `游戏原版/media/scripts/generated/vehicles/template_radio.txt:5`
[^128]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_seats.txt:109`
[^129]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_seats.txt:37`
[^130]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_seats.txt:55`
[^131]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_seats.txt:160`
[^132]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_seats.txt:73`
[^133]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_seats.txt:91`
[^134]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/89fordBronco.txt:413`
[^135]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:5`
[^136]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:18`
[^137]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:31`
[^138]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:44`
[^139]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_tire.txt:302`
[^140]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_tire.txt:108`
[^141]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_tire.txt:157`
[^142]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_tire.txt:205`
[^143]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_tire.txt:254`
[^144]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_trunk.txt:24`
[^145]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_trunkdoors.txt:22`
[^146]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_windows.txt:128`
[^147]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_windows.txt:38`
[^148]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_windows.txt:64`
[^149]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_windows.txt:180`
[^150]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_windows.txt:90`
[^151]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_windows.txt:109`
[^152]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_windshield.txt:14`
[^153]: `2886833398/mods/89fordBronco/42.20/media/scripts/vehicles/template_BR89_trunkdoors.txt:146`
