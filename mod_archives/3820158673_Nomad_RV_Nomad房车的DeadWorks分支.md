# DeadWorks Nomad 房车（Nomad RV）

提供依赖 DeadWorks 新框架的 Nomad 房车分支及配套物品；不与同一工坊包内的旧 GridRV/Legacy 分支混装。

归属：**日常组合（玩法待验收）**；档案视图 `b422-compat`。
当前版本定义：**整车 1、本地物品定义 14、配方 16**；另引用共享物品 27。本地定义数含内部保留项，见独立列表；整车定义包括覆盖原版的条目，不等于新增车型数。

## 如何查找

- **生成整车**：在生成车辆菜单搜索下表完整 ID；显示译名时搜索中文列。联机管理命令用 `/addvehicle 完整ID`。
- **添加到背包**：普通物品、维修件、改装件都在添加物品菜单使用完整物品 ID；不要拿配方或内部槽位去刷车。
- **制作配方**：在制作界面查译名；配方 ID 用于排查，不是可放进背包的物品。
- 中文解释说明用途；只有翻译文件中找到的文字才称为游戏中文名。缺译保留脚本显示名，冲突列出各译文。

## 整车

| 完整生成车辆 ID | 当前中文名 / 名称状态 | 英文名或脚本名 | 变体说明 | 来源 |
| --- | --- | --- | --- | --- |
| `Base.GridRV` | 游牧者房车 / Nomad 房车（译文冲突，待游戏核实）[^1] | Nomad RV[^2] | 脚本座位数 4；机修类型 2；具体外观与性能待游戏实刷 | [^3] |

## 普通物品与书籍

| 完整物品 ID | 游戏显示名 / 名称状态 | 中文用途 / 类别 | 菜单 | 适用车辆与安装位置 | 来源 / 状态 |
| --- | --- | --- | --- | --- | --- |
| `Base.GridRVArmourManual` | 房车装甲手册[^5] | 阅读资料；脚本声明解锁：焊接房车尖刺撞角 (V形楔) / 焊接房车尖刺冲角（V 形楔）（Base.GridRVMakeRamV）、焊接房车侧面装甲 / 焊接房车侧裙装甲（Base.GridRVMakeArmorSkirts）、焊接房车排障器（Base.GridRVMakeCowCatcher） / 普通物品 / 书籍 | 添加物品 | 未定位整车安装关系 | DeadWorksNomadRV[^4] |

## 维修配件

| 完整物品 ID | 游戏显示名 / 名称状态 | 中文用途 / 类别 | 菜单 | 适用车辆与安装位置 | 来源 / 状态 |
| --- | --- | --- | --- | --- | --- |
| `Base.GridRVBikeCarrier` | 房车摩托车架[^7] | 车辆安装件，用于车辆安装位（RVRack）；适用车型见右列 / 维修配件 | 添加物品 | Base.GridRV → RVRack | DeadWorksNomadRV[^6] |
| `Base.GridRVRamFlat` | 房车尖刺撞角 (平头) / 房车尖刺冲角（平头）（译文冲突，待游戏核实）[^9] | 旧平头型尖刺撞角配件；当前 legacy 映射与 U 形旧件一样指向 Base.GridRVRamV，不视作独立新款升级件 / 维修配件 | 添加物品 | 未定位整车安装关系 | DeadWorksNomadRV[^8]；旧物品定义保留用于迁移，替换行为尚未游戏验证 |
| `Base.GridRVRamU` | 房车尖刺撞角 (U形头) / 房车尖刺冲角（U 形车头）（译文冲突，待游戏核实）[^11] | 旧 U 形车头尖刺撞角配件；当前 GridRVProfile 的 legacy 映射将它转向 Base.GridRVRamV，新建车辆优先查现行配件 / 维修配件 | 添加物品 | 未定位整车安装关系 | DeadWorksNomadRV[^10]；旧物品定义保留用于迁移，替换行为尚未游戏验证 |

## 改装配件

| 完整物品 ID | 游戏显示名 / 名称状态 | 中文用途 / 类别 | 菜单 | 适用车辆与安装位置 | 来源 / 状态 |
| --- | --- | --- | --- | --- | --- |
| `Base.GridRVArmorDoor` | 房车车门装甲 / 房车入口门装甲（译文冲突，待游戏核实）[^13] | 车辆安装件，用于车门（RVArmorDoor）；适用车型见右列 / 改装配件 | 添加物品 | Base.GridRV → RVArmorDoor | DeadWorksNomadRV[^12] |
| `Base.GridRVArmorDoorXmas` | 房车圣诞入口门装甲[^15] | 车辆安装件，用于车门（RVArmorDoor）；适用车型见右列 / 改装配件 | 添加物品 | Base.GridRV → RVArmorDoor | DeadWorksNomadRV[^14] |
| `Base.GridRVArmorGrilles` | 房车车窗格栅 / 房车车窗护栏（译文冲突，待游戏核实）[^17] | 车辆安装件，用于防护件（RVArmorGrilles）；适用车型见右列 / 改装配件 | 添加物品 | Base.GridRV → RVArmorGrilles | DeadWorksNomadRV[^16] |
| `Base.GridRVArmorGrillesXmas` | 房车圣诞车窗护栏[^19] | 车辆安装件，用于防护件（RVArmorGrilles）；适用车型见右列 / 改装配件 | 添加物品 | Base.GridRV → RVArmorGrilles | DeadWorksNomadRV[^18] |
| `Base.GridRVArmorSkirts` | 房车侧面装甲 / 房车侧裙装甲（译文冲突，待游戏核实）[^21] | 车辆安装件，用于防护件（RVArmorSkirts）；适用车型见右列 / 改装配件 | 添加物品 | Base.GridRV → RVArmorSkirts | DeadWorksNomadRV[^20] |
| `Base.GridRVArmorSkirtsXmas` | 房车圣诞侧裙装甲[^23] | 车辆安装件，用于防护件（RVArmorSkirts）；适用车型见右列 / 改装配件 | 添加物品 | Base.GridRV → RVArmorSkirts | DeadWorksNomadRV[^22] |
| `Base.GridRVCowCatcher` | 房车排障器[^25] | 车辆安装件，用于防护件（RVArmorCatcher）；适用车型见右列 / 改装配件 | 添加物品 | Base.DaleChieftainRV → RVArmorCatcher | DeadWorksNomadRV[^24] |
| `Base.GridRVCowCatcherXmas` | 房车圣诞排障器[^27] | 车辆安装件，用于防护件（RVArmorCatcher）；适用车型见右列 / 改装配件 | 添加物品 | Base.DaleChieftainRV → RVArmorCatcher | DeadWorksNomadRV[^26] |
| `Base.GridRVRamV` | 房车尖刺撞角 (V形楔) / 房车尖刺冲角（V 形楔）（译文冲突，待游戏核实）[^29] | 车辆安装件，用于防护件（RVArmorRam）；适用车型见右列 / 改装配件 | 添加物品 | Base.GridRV → RVArmorRam | DeadWorksNomadRV[^28] |
| `Base.GridRVRamVXmas` | 房车圣诞尖刺冲角[^31] | 车辆安装件，用于防护件（RVArmorRam）；适用车型见右列 / 改装配件 | 添加物品 | Base.GridRV → RVArmorRam | DeadWorksNomadRV[^30] |

## 共享配件

下列物品由已启用依赖或游戏原版提供，不计入本 Mod 的本地物品数。

| 完整物品 ID | 游戏显示名 / 名称状态 | 中文用途 / 类别 | 菜单 | 适用车辆与安装位置 | 来源 / 状态 |
| --- | --- | --- | --- | --- | --- |
| `Base.BigGasTank2` | 油箱 (大型)（翻译文件含非标准语法，待游戏核实）[^33] | 车辆安装件，用于油箱（GasTank）；适用车型见右列 / 维修配件 | 添加物品 | Base.GridRV → GasTank | 游戏原版[^32] |
| `Base.CarBattery2` | 汽车电池（翻译文件含非标准语法，待游戏核实）[^35] | 车辆安装件，用于蓄电池（Battery）、蓄电池（GRHouseBattery1）、蓄电池（GRHouseBattery2）；适用车型见右列 / 维修配件 | 添加物品 | Base.GridRV → Battery；Base.GridRV → GRHouseBattery1；Base.GridRV → GRHouseBattery2 | 游戏原版[^34] |
| `Base.EngineDoor2` | 引擎罩（翻译文件含非标准语法，待游戏核实）[^37] | 车辆安装件，用于引擎盖（EngineDoor）；适用车型见右列 / 维修配件 | 添加物品 | Base.GridRV → EngineDoor | 游戏原版[^36] |
| `Base.FrontCarDoor2` | 车前门（翻译文件含非标准语法，待游戏核实）[^39] | 车辆安装件，用于车门（DoorFrontLeft）、车门（DoorFrontRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.GridRV → DoorFrontLeft；Base.GridRV → DoorFrontRight | 游戏原版[^38] |
| `Base.FrontWindow2` | 车前窗（翻译文件含非标准语法，待游戏核实）[^41] | 车辆安装件，用于车窗（WindowFrontLeft）、车窗（WindowFrontRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.GridRV → WindowFrontLeft；Base.GridRV → WindowFrontRight | 游戏原版[^40] |
| `Base.GloveBox2` | 手套箱（翻译文件含非标准语法，待游戏核实）[^43] | 车辆安装件，用于车辆安装位（GloveBox）；适用车型见右列 / 维修配件 | 添加物品 | Base.GridRV → GloveBox | 游戏原版[^42] |
| `Base.LightBulb` | 灯泡-白色 / 灯泡 (白)（译文冲突，待游戏核实）[^45] | 车辆安装件，用于车灯（Headlight*）、车灯（JP82DorothyLights）；适用车型见右列 / 维修配件 | 添加物品 | Base.GridRV → Headlight* | 游戏原版[^44] |
| `Base.ModernBrake2` | 制动器 (高级)（翻译文件含非标准语法，待游戏核实）[^47] | 车辆安装件，用于制动器（Brake*）；适用车型见右列 / 维修配件 | 添加物品 | Base.GridRV → Brake* | 游戏原版[^46] |
| `Base.ModernCarMuffler2` | 消声器 (高级)（翻译文件含非标准语法，待游戏核实）[^49] | 车辆安装件，用于消声器（Muffler）；适用车型见右列 / 维修配件 | 添加物品 | Base.GridRV → Muffler | 游戏原版[^48] |
| `Base.ModernSuspension2` | 悬挂 (高级)（翻译文件含非标准语法，待游戏核实）[^51] | 车辆安装件，用于悬挂（Suspension*）；适用车型见右列 / 维修配件 | 添加物品 | Base.GridRV → Suspension* | 游戏原版[^50] |
| `Base.ModernTire2` | 轮胎 (高级)（翻译文件含非标准语法，待游戏核实）[^53] | 车辆安装件，用于轮胎（Tire*）；适用车型见右列 / 维修配件 | 添加物品 | Base.GridRV → Tire* | 游戏原版[^52] |
| `Base.NormalBrake2` | 制动器 (普通)（翻译文件含非标准语法，待游戏核实）[^55] | 车辆安装件，用于制动器（Brake*）；适用车型见右列 / 维修配件 | 添加物品 | Base.GridRV → Brake* | 游戏原版[^54] |
| `Base.NormalCarMuffler2` | 消声器 (普通)（翻译文件含非标准语法，待游戏核实）[^57] | 车辆安装件，用于消声器（Muffler）；适用车型见右列 / 维修配件 | 添加物品 | Base.GridRV → Muffler | 游戏原版[^56] |
| `Base.NormalGasTank2` | 油箱 (标准)（翻译文件含非标准语法，待游戏核实）[^59] | 车辆安装件，用于油箱（GasTank）；适用车型见右列 / 维修配件 | 添加物品 | Base.GridRV → GasTank | 游戏原版[^58] |
| `Base.NormalSuspension2` | 悬挂 (普通)（翻译文件含非标准语法，待游戏核实）[^61] | 车辆安装件，用于悬挂（Suspension*）；适用车型见右列 / 维修配件 | 添加物品 | Base.GridRV → Suspension* | 游戏原版[^60] |
| `Base.NormalTire2` | 轮胎 (普通)（翻译文件含非标准语法，待游戏核实）[^63] | 车辆安装件，用于轮胎（Tire*）；适用车型见右列 / 维修配件 | 添加物品 | Base.GridRV → Tire* | 游戏原版[^62] |
| `Base.OldBrake2` | 制动器 (老式)（翻译文件含非标准语法，待游戏核实）[^65] | 车辆安装件，用于制动器（Brake*）；适用车型见右列 / 维修配件 | 添加物品 | Base.GridRV → Brake* | 游戏原版[^64] |
| `Base.OldCarMuffler2` | 消声器 (老式)（翻译文件含非标准语法，待游戏核实）[^67] | 车辆安装件，用于消声器（Muffler）；适用车型见右列 / 维修配件 | 添加物品 | Base.GridRV → Muffler | 游戏原版[^66] |
| `Base.OldTire2` | 轮胎 (廉价)（翻译文件含非标准语法，待游戏核实）[^69] | 车辆安装件，用于轮胎（TireFrontLeft）、轮胎（TireFrontRight）、轮胎（Tire*）、轮胎（TireRearLeft）、轮胎（TireRearRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.GridRV → Tire* | 游戏原版[^68] |
| `Base.RadioBlack` | 收音机 (超值科技) / 收音机 (廉科) / 廉科牌收音机（译文冲突，待游戏核实）[^71] | 车辆安装件，用于车辆安装位（Radio）；适用车型见右列 / 维修配件 | 添加物品 | Base.GridRV → Radio | 游戏原版[^70] |
| `Base.RadioMakeShift` | 收音机 (简易) / 自制收音机（译文冲突，待游戏核实）[^73] | 车辆安装件，用于车辆安装位（Radio）；适用车型见右列 / 维修配件 | 添加物品 | Base.GridRV → Radio | 游戏原版[^72] |
| `Base.RadioRed` | 导航仪 / 收音机 (昂科) / 昂科牌收音机（译文冲突，待游戏核实）[^75] | 车辆安装件，用于车辆安装位（Radio）；适用车型见右列 / 维修配件 | 添加物品 | Base.GridRV → Radio | 游戏原版[^74] |
| `Base.RearWindow2` | 车后窗（翻译文件含非标准语法，待游戏核实）[^77] | 车辆安装件，用于车窗（WindowRearLeft）、车窗（WindowRearRight）、车窗（WindowMiddleLeft）、车窗（WindowMiddleRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.GridRV → WindowRearLeft；Base.GridRV → WindowRearRight | 游戏原版[^76] |
| `Base.RearWindshield2` | 后挡风玻璃（翻译文件含非标准语法，待游戏核实）[^79] | 车辆安装件，用于挡风玻璃（WindshieldRear）；适用车型见右列 / 维修配件 | 添加物品 | Base.GridRV → WindshieldRear | 游戏原版[^78] |
| `Base.SmallGasTank2` | 油箱 (小型)（翻译文件含非标准语法，待游戏核实）[^81] | 车辆安装件，用于油箱（GasTank）；适用车型见右列 / 维修配件 | 添加物品 | Base.GridRV → GasTank | 游戏原版[^80] |
| `Base.TrunkDoor2` | 后备箱盖（翻译文件含非标准语法，待游戏核实）[^83] | 车辆安装件，用于车门（RVBayDoorLeftRear）、车门（RVBayDoorLeftFront）、车门（RVBayDoorRightRear）、车门（RVBayDoorRightFront）、车门（RVBayDoorRightWater）、车门（RVBayDoorLeftBattery）、车门（DaleLockerDoorLeftRear）、车门（DaleLockerDoorLeftMidRear）、车门（DaleLockerDoorLeftMidFront）、车门（DaleLockerDoorLeftFront）、车门（DaleLockerDoorRightRear）、车门（DaleLockerDoorRightMid）、车门（DaleLockerDoorRightFront）、车门（DaleRearDoor）、后备箱（TrunkDoor）；适用车型见右列 / 维修配件 | 添加物品 | Base.GridRV → RVBayDoorLeftRear；Base.GridRV → RVBayDoorLeftFront；Base.GridRV → RVBayDoorRightRear；Base.GridRV → RVBayDoorRightFront；Base.GridRV → RVBayDoorRightWater；Base.GridRV → RVBayDoorLeftBattery | 游戏原版[^82] |
| `Base.Windshield2` | 挡风玻璃（翻译文件含非标准语法，待游戏核实）[^85] | 车辆安装件，用于挡风玻璃（Windshield）；适用车型见右列 / 维修配件 | 添加物品 | Base.GridRV → Windshield | 游戏原版[^84] |

## 制作配方

| 配方完整 ID（排查用） | 游戏配方名 / 名称状态 | 中文用途 | 菜单 | 来源 |
| --- | --- | --- | --- | --- |
| `Base.GridRVDecorateArmorDoor` | 为房车入口门装甲做圣诞装饰[^86] | 制作产出：房车圣诞入口门装甲（车辆安装件，用于车门（RVArmorDoor）；适用车型见右列） | 制作界面 | [^87] |
| `Base.GridRVDecorateArmorGrilles` | 为房车车窗护栏做圣诞装饰[^88] | 制作产出：房车圣诞车窗护栏（车辆安装件，用于防护件（RVArmorGrilles）；适用车型见右列） | 制作界面 | [^89] |
| `Base.GridRVDecorateArmorSkirts` | 为房车侧裙装甲做圣诞装饰[^90] | 制作产出：房车圣诞侧裙装甲（车辆安装件，用于防护件（RVArmorSkirts）；适用车型见右列） | 制作界面 | [^91] |
| `Base.GridRVDecorateCowCatcher` | 为房车排障器做圣诞装饰[^92] | 制作产出：房车圣诞排障器（车辆安装件，用于防护件（RVArmorCatcher）；适用车型见右列） | 制作界面 | [^93] |
| `Base.GridRVDecorateRamV` | 为房车尖刺冲角做圣诞装饰[^94] | 制作产出：房车圣诞尖刺冲角（车辆安装件，用于防护件（RVArmorRam）；适用车型见右列） | 制作界面 | [^95] |
| `Base.GridRVMakeArmorDoor` | 焊接房车车门装甲 / 焊接房车入口门装甲（译文冲突，待游戏核实）[^96] | 制作产出：房车车门装甲 / 房车入口门装甲（车辆安装件，用于车门（RVArmorDoor）；适用车型见右列） | 制作界面 | [^97] |
| `Base.GridRVMakeArmorGrilles` | 焊接房车车窗格栅 / 焊接房车车窗护栏（译文冲突，待游戏核实）[^98] | 制作产出：房车车窗格栅 / 房车车窗护栏（车辆安装件，用于防护件（RVArmorGrilles）；适用车型见右列） | 制作界面 | [^99] |
| `Base.GridRVMakeArmorSkirts` | 焊接房车侧面装甲 / 焊接房车侧裙装甲（译文冲突，待游戏核实）[^100] | 制作产出：房车侧面装甲 / 房车侧裙装甲（车辆安装件，用于防护件（RVArmorSkirts）；适用车型见右列） | 制作界面 | [^101] |
| `Base.GridRVMakeBikeCarrier` | 焊接房车摩托车架[^102] | 制作产出：房车摩托车架（车辆安装件，用于车辆安装位（RVRack）；适用车型见右列） | 制作界面 | [^103] |
| `Base.GridRVMakeCowCatcher` | 焊接房车排障器[^104] | 制作产出：房车排障器（车辆安装件，用于防护件（RVArmorCatcher）；适用车型见右列） | 制作界面 | [^105] |
| `Base.GridRVMakeRamV` | 焊接房车尖刺撞角 (V形楔) / 焊接房车尖刺冲角（V 形楔）（译文冲突，待游戏核实）[^106] | 制作产出：房车尖刺撞角 (V形楔) / 房车尖刺冲角（V 形楔）（车辆安装件，用于防护件（RVArmorRam）；适用车型见右列） | 制作界面 | [^107] |
| `Base.GridRVStripArmorDoor` | 把房车圣诞入口门装甲涂回原样[^108] | 制作产出：房车车门装甲 / 房车入口门装甲（车辆安装件，用于车门（RVArmorDoor）；适用车型见右列） | 制作界面 | [^109] |
| `Base.GridRVStripArmorGrilles` | 把房车圣诞车窗护栏涂回原样[^110] | 制作产出：房车车窗格栅 / 房车车窗护栏（车辆安装件，用于防护件（RVArmorGrilles）；适用车型见右列） | 制作界面 | [^111] |
| `Base.GridRVStripArmorSkirts` | 把房车圣诞侧裙装甲涂回原样[^112] | 制作产出：房车侧面装甲 / 房车侧裙装甲（车辆安装件，用于防护件（RVArmorSkirts）；适用车型见右列） | 制作界面 | [^113] |
| `Base.GridRVStripCowCatcher` | 把房车圣诞排障器涂回原样[^114] | 制作产出：房车排障器（车辆安装件，用于防护件（RVArmorCatcher）；适用车型见右列） | 制作界面 | [^115] |
| `Base.GridRVStripRamV` | 把房车圣诞尖刺冲角涂回原样[^116] | 制作产出：房车尖刺撞角 (V形楔) / 房车尖刺冲角（V 形楔）（车辆安装件，用于防护件（RVArmorRam）；适用车型见右列） | 制作界面 | [^117] |

## 内部定义、历史分支与未解析引用

有效资源层：42；仅合并 common 与所选版本，Overlay 按相对路径覆盖。
车辆模板 0 个、内部槽位 258 个，均不算整车或背包物品。旧根目录和未选中版本的定义不列入当前可用表。模板中短物品引用若追加机修类型后缀才匹配定义，属于静态映射，安装仍待实测。

<details><summary>查看内部槽位（不能直接刷取）</summary>

| 槽位 | 名称或说明 | 来源 |
| --- | --- | --- |
| `Battery` | 电池 / 蓄电池 | [^118] |
| `Brake*` | Brake* / 制动器 | [^119] |
| `BrakeFrontLeft` | 左前制动 / 制动器 | [^120] |
| `BrakeFrontRight` | 右前制动 / 制动器 | [^121] |
| `BrakeRearLeft` | 左后制动 / 制动器 | [^122] |
| `BrakeRearRight` | 右后制动 / 制动器 | [^123] |
| `Door*` | Door* / 车门 | [^124] |
| `DoorFrontLeft` | 左前门 / 车门 | [^125] |
| `DoorFrontRight` | 右前门 / 车门 | [^126] |
| `DoorRear*` | DoorRear* / 车门 | [^127] |
| `Engine` | 引擎 / 发动机 | [^128] |
| `EngineDoor` | 引擎盖 / 引擎盖 | [^129] |
| `EngineDoor*` | EngineDoor* / 引擎盖 | [^130] |
| `GRAnim0` | GRAnim0 / 车辆安装位 | [^131] |
| `GRAnim1` | GRAnim1 / 车辆安装位 | [^132] |
| `GRAnim2` | GRAnim2 / 车辆安装位 | [^133] |
| `GRAnim3` | GRAnim3 / 车辆安装位 | [^134] |
| `GRCell0` | GRCell0 / 车辆安装位 | [^135] |
| `GRCell1` | GRCell1 / 车辆安装位 | [^136] |
| `GRCell10` | GRCell10 / 车辆安装位 | [^137] |
| `GRCell11` | GRCell11 / 车辆安装位 | [^138] |
| `GRCell12` | GRCell12 / 车辆安装位 | [^139] |
| `GRCell13` | GRCell13 / 车辆安装位 | [^140] |
| `GRCell14` | GRCell14 / 车辆安装位 | [^141] |
| `GRCell15` | GRCell15 / 车辆安装位 | [^142] |
| `GRCell16` | GRCell16 / 车辆安装位 | [^143] |
| `GRCell17` | GRCell17 / 车辆安装位 | [^144] |
| `GRCell18` | GRCell18 / 车辆安装位 | [^145] |
| `GRCell19` | GRCell19 / 车辆安装位 | [^146] |
| `GRCell2` | GRCell2 / 车辆安装位 | [^147] |
| `GRCell20` | GRCell20 / 车辆安装位 | [^148] |
| `GRCell21` | GRCell21 / 车辆安装位 | [^149] |
| `GRCell22` | GRCell22 / 车辆安装位 | [^150] |
| `GRCell23` | GRCell23 / 车辆安装位 | [^151] |
| `GRCell24` | GRCell24 / 车辆安装位 | [^152] |
| `GRCell25` | GRCell25 / 车辆安装位 | [^153] |
| `GRCell26` | GRCell26 / 车辆安装位 | [^154] |
| `GRCell27` | GRCell27 / 车辆安装位 | [^155] |
| `GRCell28` | GRCell28 / 车辆安装位 | [^156] |
| `GRCell29` | GRCell29 / 车辆安装位 | [^157] |
| `GRCell3` | GRCell3 / 车辆安装位 | [^158] |
| `GRCell30` | GRCell30 / 车辆安装位 | [^159] |
| `GRCell31` | GRCell31 / 车辆安装位 | [^160] |
| `GRCell32` | GRCell32 / 车辆安装位 | [^161] |
| `GRCell33` | GRCell33 / 车辆安装位 | [^162] |
| `GRCell34` | GRCell34 / 车辆安装位 | [^163] |
| `GRCell35` | GRCell35 / 车辆安装位 | [^164] |
| `GRCell36` | GRCell36 / 车辆安装位 | [^165] |
| `GRCell37` | GRCell37 / 车辆安装位 | [^166] |
| `GRCell38` | GRCell38 / 车辆安装位 | [^167] |
| `GRCell39` | GRCell39 / 车辆安装位 | [^168] |
| `GRCell4` | GRCell4 / 车辆安装位 | [^169] |
| `GRCell40` | GRCell40 / 车辆安装位 | [^170] |
| `GRCell41` | GRCell41 / 车辆安装位 | [^171] |
| `GRCell42` | GRCell42 / 车辆安装位 | [^172] |
| `GRCell43` | GRCell43 / 车辆安装位 | [^173] |
| `GRCell44` | GRCell44 / 车辆安装位 | [^174] |
| `GRCell45` | GRCell45 / 车辆安装位 | [^175] |
| `GRCell46` | GRCell46 / 车辆安装位 | [^176] |
| `GRCell47` | GRCell47 / 车辆安装位 | [^177] |
| `GRCell48` | GRCell48 / 车辆安装位 | [^178] |
| `GRCell49` | GRCell49 / 车辆安装位 | [^179] |
| `GRCell5` | GRCell5 / 车辆安装位 | [^180] |
| `GRCell50` | GRCell50 / 车辆安装位 | [^181] |
| `GRCell51` | GRCell51 / 车辆安装位 | [^182] |
| `GRCell52` | GRCell52 / 车辆安装位 | [^183] |
| `GRCell53` | GRCell53 / 车辆安装位 | [^184] |
| `GRCell54` | GRCell54 / 车辆安装位 | [^185] |
| `GRCell55` | GRCell55 / 车辆安装位 | [^186] |
| `GRCell56` | GRCell56 / 车辆安装位 | [^187] |
| `GRCell57` | GRCell57 / 车辆安装位 | [^188] |
| `GRCell58` | GRCell58 / 车辆安装位 | [^189] |
| `GRCell59` | GRCell59 / 车辆安装位 | [^190] |
| `GRCell6` | GRCell6 / 车辆安装位 | [^191] |
| `GRCell60` | GRCell60 / 车辆安装位 | [^192] |
| `GRCell61` | GRCell61 / 车辆安装位 | [^193] |
| `GRCell62` | GRCell62 / 车辆安装位 | [^194] |
| `GRCell63` | GRCell63 / 车辆安装位 | [^195] |
| `GRCell64` | GRCell64 / 车辆安装位 | [^196] |
| `GRCell65` | GRCell65 / 车辆安装位 | [^197] |
| `GRCell66` | GRCell66 / 车辆安装位 | [^198] |
| `GRCell67` | GRCell67 / 车辆安装位 | [^199] |
| `GRCell68` | GRCell68 / 车辆安装位 | [^200] |
| `GRCell69` | GRCell69 / 车辆安装位 | [^201] |
| `GRCell7` | GRCell7 / 车辆安装位 | [^202] |
| `GRCell70` | GRCell70 / 车辆安装位 | [^203] |
| `GRCell71` | GRCell71 / 车辆安装位 | [^204] |
| `GRCell8` | GRCell8 / 车辆安装位 | [^205] |
| `GRCell9` | GRCell9 / 车辆安装位 | [^206] |
| `GRFreezer0` | GRFreezer0 / 车辆安装位 | [^207] |
| `GRFreezer1` | GRFreezer1 / 车辆安装位 | [^208] |
| `GRFreezer10` | GRFreezer10 / 车辆安装位 | [^209] |
| `GRFreezer11` | GRFreezer11 / 车辆安装位 | [^210] |
| `GRFreezer12` | GRFreezer12 / 车辆安装位 | [^211] |
| `GRFreezer13` | GRFreezer13 / 车辆安装位 | [^212] |
| `GRFreezer14` | GRFreezer14 / 车辆安装位 | [^213] |
| `GRFreezer15` | GRFreezer15 / 车辆安装位 | [^214] |
| `GRFreezer16` | GRFreezer16 / 车辆安装位 | [^215] |
| `GRFreezer17` | GRFreezer17 / 车辆安装位 | [^216] |
| `GRFreezer18` | GRFreezer18 / 车辆安装位 | [^217] |
| `GRFreezer19` | GRFreezer19 / 车辆安装位 | [^218] |
| `GRFreezer2` | GRFreezer2 / 车辆安装位 | [^219] |
| `GRFreezer20` | GRFreezer20 / 车辆安装位 | [^220] |
| `GRFreezer21` | GRFreezer21 / 车辆安装位 | [^221] |
| `GRFreezer22` | GRFreezer22 / 车辆安装位 | [^222] |
| `GRFreezer23` | GRFreezer23 / 车辆安装位 | [^223] |
| `GRFreezer3` | GRFreezer3 / 车辆安装位 | [^224] |
| `GRFreezer4` | GRFreezer4 / 车辆安装位 | [^225] |
| `GRFreezer5` | GRFreezer5 / 车辆安装位 | [^226] |
| `GRFreezer6` | GRFreezer6 / 车辆安装位 | [^227] |
| `GRFreezer7` | GRFreezer7 / 车辆安装位 | [^228] |
| `GRFreezer8` | GRFreezer8 / 车辆安装位 | [^229] |
| `GRFreezer9` | GRFreezer9 / 车辆安装位 | [^230] |
| `GRHouseBattery1` | 生活电池1 / 生活电池 1 / 蓄电池 | [^231] |
| `GRHouseBattery2` | 生活电池2 / 生活电池 2 / 蓄电池 | [^232] |
| `GRLoose0` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^233] |
| `GRLoose1` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^234] |
| `GRLoose10` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^235] |
| `GRLoose11` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^236] |
| `GRLoose12` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^237] |
| `GRLoose13` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^238] |
| `GRLoose14` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^239] |
| `GRLoose15` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^240] |
| `GRLoose16` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^241] |
| `GRLoose17` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^242] |
| `GRLoose18` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^243] |
| `GRLoose19` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^244] |
| `GRLoose2` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^245] |
| `GRLoose20` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^246] |
| `GRLoose21` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^247] |
| `GRLoose22` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^248] |
| `GRLoose23` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^249] |
| `GRLoose3` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^250] |
| `GRLoose4` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^251] |
| `GRLoose5` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^252] |
| `GRLoose6` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^253] |
| `GRLoose7` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^254] |
| `GRLoose8` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^255] |
| `GRLoose9` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^256] |
| `GRPacked0` | GRPacked0 / 车辆安装位 | [^257] |
| `GRPacked1` | GRPacked1 / 车辆安装位 | [^258] |
| `GRPacked10` | GRPacked10 / 车辆安装位 | [^259] |
| `GRPacked11` | GRPacked11 / 车辆安装位 | [^260] |
| `GRPacked12` | GRPacked12 / 车辆安装位 | [^261] |
| `GRPacked13` | GRPacked13 / 车辆安装位 | [^262] |
| `GRPacked14` | GRPacked14 / 车辆安装位 | [^263] |
| `GRPacked15` | GRPacked15 / 车辆安装位 | [^264] |
| `GRPacked16` | GRPacked16 / 车辆安装位 | [^265] |
| `GRPacked17` | GRPacked17 / 车辆安装位 | [^266] |
| `GRPacked18` | GRPacked18 / 车辆安装位 | [^267] |
| `GRPacked19` | GRPacked19 / 车辆安装位 | [^268] |
| `GRPacked2` | GRPacked2 / 车辆安装位 | [^269] |
| `GRPacked20` | GRPacked20 / 车辆安装位 | [^270] |
| `GRPacked21` | GRPacked21 / 车辆安装位 | [^271] |
| `GRPacked22` | GRPacked22 / 车辆安装位 | [^272] |
| `GRPacked23` | GRPacked23 / 车辆安装位 | [^273] |
| `GRPacked24` | GRPacked24 / 车辆安装位 | [^274] |
| `GRPacked25` | GRPacked25 / 车辆安装位 | [^275] |
| `GRPacked26` | GRPacked26 / 车辆安装位 | [^276] |
| `GRPacked27` | GRPacked27 / 车辆安装位 | [^277] |
| `GRPacked28` | GRPacked28 / 车辆安装位 | [^278] |
| `GRPacked29` | GRPacked29 / 车辆安装位 | [^279] |
| `GRPacked3` | GRPacked3 / 车辆安装位 | [^280] |
| `GRPacked30` | GRPacked30 / 车辆安装位 | [^281] |
| `GRPacked31` | GRPacked31 / 车辆安装位 | [^282] |
| `GRPacked32` | GRPacked32 / 车辆安装位 | [^283] |
| `GRPacked33` | GRPacked33 / 车辆安装位 | [^284] |
| `GRPacked34` | GRPacked34 / 车辆安装位 | [^285] |
| `GRPacked35` | GRPacked35 / 车辆安装位 | [^286] |
| `GRPacked36` | GRPacked36 / 车辆安装位 | [^287] |
| `GRPacked37` | GRPacked37 / 车辆安装位 | [^288] |
| `GRPacked38` | GRPacked38 / 车辆安装位 | [^289] |
| `GRPacked39` | GRPacked39 / 车辆安装位 | [^290] |
| `GRPacked4` | GRPacked4 / 车辆安装位 | [^291] |
| `GRPacked40` | GRPacked40 / 车辆安装位 | [^292] |
| `GRPacked41` | GRPacked41 / 车辆安装位 | [^293] |
| `GRPacked42` | GRPacked42 / 车辆安装位 | [^294] |
| `GRPacked43` | GRPacked43 / 车辆安装位 | [^295] |
| `GRPacked44` | GRPacked44 / 车辆安装位 | [^296] |
| `GRPacked45` | GRPacked45 / 车辆安装位 | [^297] |
| `GRPacked46` | GRPacked46 / 车辆安装位 | [^298] |
| `GRPacked47` | GRPacked47 / 车辆安装位 | [^299] |
| `GRPacked48` | GRPacked48 / 车辆安装位 | [^300] |
| `GRPacked49` | GRPacked49 / 车辆安装位 | [^301] |
| `GRPacked5` | GRPacked5 / 车辆安装位 | [^302] |
| `GRPacked50` | GRPacked50 / 车辆安装位 | [^303] |
| `GRPacked51` | GRPacked51 / 车辆安装位 | [^304] |
| `GRPacked52` | GRPacked52 / 车辆安装位 | [^305] |
| `GRPacked53` | GRPacked53 / 车辆安装位 | [^306] |
| `GRPacked54` | GRPacked54 / 车辆安装位 | [^307] |
| `GRPacked55` | GRPacked55 / 车辆安装位 | [^308] |
| `GRPacked56` | GRPacked56 / 车辆安装位 | [^309] |
| `GRPacked57` | GRPacked57 / 车辆安装位 | [^310] |
| `GRPacked58` | GRPacked58 / 车辆安装位 | [^311] |
| `GRPacked59` | GRPacked59 / 车辆安装位 | [^312] |
| `GRPacked6` | GRPacked6 / 车辆安装位 | [^313] |
| `GRPacked60` | GRPacked60 / 车辆安装位 | [^314] |
| `GRPacked61` | GRPacked61 / 车辆安装位 | [^315] |
| `GRPacked62` | GRPacked62 / 车辆安装位 | [^316] |
| `GRPacked63` | GRPacked63 / 车辆安装位 | [^317] |
| `GRPacked64` | GRPacked64 / 车辆安装位 | [^318] |
| `GRPacked65` | GRPacked65 / 车辆安装位 | [^319] |
| `GRPacked66` | GRPacked66 / 车辆安装位 | [^320] |
| `GRPacked67` | GRPacked67 / 车辆安装位 | [^321] |
| `GRPacked68` | GRPacked68 / 车辆安装位 | [^322] |
| `GRPacked69` | GRPacked69 / 车辆安装位 | [^323] |
| `GRPacked7` | GRPacked7 / 车辆安装位 | [^324] |
| `GRPacked70` | GRPacked70 / 车辆安装位 | [^325] |
| `GRPacked71` | GRPacked71 / 车辆安装位 | [^326] |
| `GRPacked8` | GRPacked8 / 车辆安装位 | [^327] |
| `GRPacked9` | GRPacked9 / 车辆安装位 | [^328] |
| `GRSteps` | GRSteps / 车辆安装位 | [^329] |
| `GasTank` | 油箱 / 油箱 | [^330] |
| `GloveBox` | 手套箱 / 车辆安装位 | [^331] |
| `Headlight*` | Headlight* / 车灯 | [^332] |
| `HeadlightLeft` | 左大灯 / 车灯 | [^333] |
| `HeadlightRearLeft` | 左尾灯 / 车灯 | [^334] |
| `HeadlightRearRight` | 右尾灯 / 车灯 | [^335] |
| `HeadlightRight` | 右大灯 / 车灯 | [^336] |
| `Heater` | 加热器 / 车辆安装位 | [^337] |
| `Muffler` | 排气消声器 / 消声器 | [^338] |
| `PassengerCompartment` | 乘员舱 / 车辆安装位 | [^339] |
| `RVArmorDoor` | 车门装甲 / 入口门装甲 / 车门 | [^340] |
| `RVArmorGrilles` | 车窗格栅 / 车窗护栏 / 防护件 | [^341] |
| `RVArmorRam` | 尖刺撞角 / 尖刺冲角 / 防护件 | [^342] |
| `RVArmorSkirts` | 侧面装甲 / 侧裙装甲 / 防护件 | [^343] |
| `RVBayDoorLeftBattery` | 电池仓 / 电池舱盖 / 车门 | [^344] |
| `RVBayDoorLeftFront` | 左前舱门 / 左前货舱门 / 车门 | [^345] |
| `RVBayDoorLeftRear` | 左后舱门 / 左后货舱门 / 车门 | [^346] |
| `RVBayDoorRightFront` | 右前舱门 / 右前货舱门 / 车门 | [^347] |
| `RVBayDoorRightRear` | 右后舱门 / 右后货舱门 / 车门 | [^348] |
| `RVBayDoorRightWater` | 加水口 / 水箱舱盖 / 车门 | [^349] |
| `RVBayLeftFront` | 左前行李舱 / 车辆安装位 | [^350] |
| `RVBayLeftRear` | 左后行李舱 / 车辆安装位 | [^351] |
| `RVBayRightFront` | 右前行李舱 / 车辆安装位 | [^352] |
| `RVBayRightRear` | 右后行李舱 / 车辆安装位 | [^353] |
| `RVRack` | 摩托车架 / 车辆安装位 | [^354] |
| `Radio` | 电台 / 车辆安装位 | [^355] |
| `SeatFrontLeft` | 驾驶座 / 座椅 | [^356] |
| `SeatFrontRight` | 右前座 / 座椅 | [^357] |
| `SeatRearLeft` | 左后座 / 座椅 | [^358] |
| `SeatRearRight` | 右后座 / 座椅 | [^359] |
| `Suspension*` | Suspension* / 悬挂 | [^360] |
| `SuspensionFrontLeft` | 左前悬挂 / 悬挂 | [^361] |
| `SuspensionFrontRight` | 右前悬挂 / 悬挂 | [^362] |
| `SuspensionRearLeft` | 左后悬挂 / 悬挂 | [^363] |
| `SuspensionRearRight` | 右后悬挂 / 悬挂 | [^364] |
| `Tire*` | Tire* / 轮胎 | [^365] |
| `TireFrontLeft` | 左前胎 / 轮胎 | [^366] |
| `TireFrontRight` | 右前胎 / 轮胎 | [^367] |
| `TireRearLeft` | 左后胎 / 轮胎 | [^368] |
| `TireRearRight` | 右后胎 / 轮胎 | [^369] |
| `WindowFrontLeft` | 左前窗 / 车窗 | [^370] |
| `WindowFrontRight` | 右前窗 / 车窗 | [^371] |
| `WindowRearLeft` | 左后窗 / 车窗 | [^372] |
| `WindowRearRight` | 右后窗 / 车窗 | [^373] |
| `Windshield` | 挡风玻璃 / 挡风玻璃 | [^374] |
| `WindshieldRear` | 后挡风玻璃 / 挡风玻璃 | [^375] |

</details>


## 概览

| Mod ID / 文件夹 | 分发端 | 版本 | 选择的 mod.info | 原件范围 → 当前范围 |
| --- | --- | --- | --- | --- |
| `DeadWorksNomadRV` / `DeadWorksNomadRV` | both（双端） | 0.9.2 | `42/mod.info` | 42.21 … 42.21 → 42.21 … 42.22（Overlay） |

原件体积 56.6 MB；体积按完整目录统计，与当前内容定义数分开。
工作坊：[查看作者页面](https://steamcommunity.com/sharedfiles/filedetails/?id=3820158673)。

## 证据与使用边界

**verified：有效源码静态确认。** 每个当前可复制 ID 均来自所选版本的定义；这不保证游戏已成功注册、生成、安装或联机同步。
挑战者 5 个车辆中文名另有 Owner 截图确认；本轮没有启动游戏。译文冲突、动态 Lua 内容和玩法效果仍需 Owner 游戏内核实。
以下人工记录保留原始语境；其中旧组合、旧数量和旧候选状态仅供追溯，当前统计与归属以上表和 profile 为准。

<!-- retained:start -->
## 依赖与冲突

- 需要：`DeadWorksVehicleFramework, PZVoxelStudioViewpoint`
- 互斥：`GridRV, GridRVHost, DaleChieftainRV`
- 被依赖：`DeadWorksDaleRV`

## 双端与联机

双端候选；依赖 DeadWorksVehicleFramework 与 6282，车内状态和保存读取仍待测试。

当前 profile：both（双端）。

本机文件构成：客户端有 lua；服务端有 lua。

## 实测与排查

原件 0.9.2，42.21 上限；仅元数据 Overlay。未因静态依赖齐全而宣称房车运行正常。

**planned：仅完成依赖、版本与补丁指纹静态检查。** 迁移收尾按 Owner 要求不启动游戏；本候选组合未验证加载、联网、存档或视觉。

版本放行补丁：`A004/workspace/patches/mods/DeadWorksNomadRV/42/mod.info`。原件更新后须重新核对指纹；撤除此补丁后运行 check 会恢复原件版本限制。

```
cd A004
python lab.py check --profile b422-compat
grep -a 'DeadWorksNomadRV' runs/<trial>/*console.log
```
<!-- retained:end -->

## 静态来源

路径相对 `A004/workspace/mods_library/`；`Overlay/<文件夹>/` 指 `A004/workspace/patches/mods/<文件夹>/`，`游戏原版/` 指当前 B42.22 客户端 Game 目录。翻译来源列出所有候选，未按加载顺序擅自消解异文。

[^1]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/IG_UI.json:43476`；`3810637496/mods/LaoYuTranslationJava/common/media/lua/shared/Translate/CN/IG_UI.json:188`
[^2]: `3820158673/mods/DeadWorksNomadRV/42/media/lua/shared/Translate/EN/IG_UI.json:6`；`3820158673/mods/DeadWorksNomadRV/42/media/lua/shared/Translate/EN/IG_UI_EN.txt:6`
[^3]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:2`
[^4]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/GridRVArmourItems.txt:98`
[^5]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:40342`；`3810637496/mods/LaoYuTranslationJava/common/media/lua/shared/Translate/CN/ItemName.json:8`
[^6]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/GridRVArmourItems.txt:232`；`3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:278`
[^7]: `3810637496/mods/LaoYuTranslationJava/common/media/lua/shared/Translate/CN/ItemName.json:9`
[^8]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/GridRVArmourItems.txt:71`；`3820158673/mods/DeadWorksNomadRV/42/media/lua/shared/GridRVProfile.lua:87`
[^9]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:40340`；`3810637496/mods/LaoYuTranslationJava/common/media/lua/shared/Translate/CN/ItemName.json:12`
[^10]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/GridRVArmourItems.txt:58`；`3820158673/mods/DeadWorksNomadRV/42/media/lua/shared/GridRVProfile.lua:87`
[^11]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:40339`；`3810637496/mods/LaoYuTranslationJava/common/media/lua/shared/Translate/CN/ItemName.json:13`
[^12]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/GridRVArmourItems.txt:84`；`3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:349`
[^13]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:40341`；`3810637496/mods/LaoYuTranslationJava/common/media/lua/shared/Translate/CN/ItemName.json:2`
[^14]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/GridRVXmasItems.txt:158`；`3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:349`
[^15]: `3810637496/mods/LaoYuTranslationJava/common/media/lua/shared/Translate/CN/ItemName.json:3`
[^16]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/GridRVArmourItems.txt:5`；`3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:322`
[^17]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:40336`；`3810637496/mods/LaoYuTranslationJava/common/media/lua/shared/Translate/CN/ItemName.json:4`
[^18]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/GridRVXmasItems.txt:107`；`3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:322`
[^19]: `3810637496/mods/LaoYuTranslationJava/common/media/lua/shared/Translate/CN/ItemName.json:5`
[^20]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/GridRVArmourItems.txt:18`；`3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:331`
[^21]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:40337`；`3810637496/mods/LaoYuTranslationJava/common/media/lua/shared/Translate/CN/ItemName.json:6`
[^22]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/GridRVXmasItems.txt:56`；`3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:331`
[^23]: `3810637496/mods/LaoYuTranslationJava/common/media/lua/shared/Translate/CN/ItemName.json:7`
[^24]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/GridRVArmourItems.txt:44`；`3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:649`
[^25]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:40991`；`3810637496/mods/LaoYuTranslationJava/common/media/lua/shared/Translate/CN/ItemName.json:10`
[^26]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/GridRVXmasItems.txt:5`；`3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:649`
[^27]: `3810637496/mods/LaoYuTranslationJava/common/media/lua/shared/Translate/CN/ItemName.json:11`
[^28]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/GridRVArmourItems.txt:31`；`3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:340`
[^29]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:40338`；`3810637496/mods/LaoYuTranslationJava/common/media/lua/shared/Translate/CN/ItemName.json:14`
[^30]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/GridRVXmasItems.txt:209`；`3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:340`
[^31]: `3810637496/mods/LaoYuTranslationJava/common/media/lua/shared/Translate/CN/ItemName.json:15`
[^32]: `游戏原版/media/scripts/generated/items/normal.txt:12408`；`3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:83`
[^33]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:448`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:163`
[^34]: `游戏原版/media/scripts/generated/items/drainable.txt:2368`；`游戏原版/media/scripts/generated/vehicles/template_battery.txt:5`；`3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:306`；`3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:312`
[^35]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:970`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:380`
[^36]: `游戏原版/media/scripts/generated/items/normal.txt:12948`；`游戏原版/media/scripts/generated/vehicles/template_engine_door.txt:5`
[^37]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1530`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:598`
[^38]: `游戏原版/media/scripts/generated/items/normal.txt:12857`；`3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:151`；`游戏原版/media/scripts/generated/vehicles/template_door.txt:23`
[^39]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1659`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:649`
[^40]: `游戏原版/media/scripts/generated/items/normal.txt:12734`；`3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:119`；`3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:135`
[^41]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1662`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:652`
[^42]: `游戏原版/media/scripts/generated/items/normal.txt:13025`；`游戏原版/media/scripts/generated/vehicles/template_glovebox.txt:5`
[^43]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1776`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:687`
[^44]: `游戏原版/media/scripts/generated/items/normal.txt:4661`；`游戏原版/media/scripts/generated/vehicles/template_headlight.txt:25`
[^45]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:6727`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25103`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2563`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:965`
[^46]: `游戏原版/media/scripts/generated/items/normal.txt:12163`；`游戏原版/media/scripts/generated/vehicles/template_brake.txt:57`
[^47]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2780`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1050`
[^48]: `游戏原版/media/scripts/generated/items/normal.txt:13166`；`游戏原版/media/scripts/generated/vehicles/template_muffler.txt:5`
[^49]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2783`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1053`
[^50]: `游戏原版/media/scripts/generated/items/normal.txt:12282`；`游戏原版/media/scripts/generated/vehicles/template_suspension.txt:57`
[^51]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2786`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1056`
[^52]: `游戏原版/media/scripts/generated/items/normal.txt:11998`；`3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:80`
[^53]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2789`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1059`
[^54]: `游戏原版/media/scripts/generated/items/normal.txt:12146`；`游戏原版/media/scripts/generated/vehicles/template_brake.txt:57`
[^55]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3219`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1135`
[^56]: `游戏原版/media/scripts/generated/items/normal.txt:13151`；`游戏原版/media/scripts/generated/vehicles/template_muffler.txt:5`
[^57]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3222`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1138`
[^58]: `游戏原版/media/scripts/generated/items/normal.txt:12393`；`3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:83`
[^59]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3228`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1144`
[^60]: `游戏原版/media/scripts/generated/items/normal.txt:12265`；`游戏原版/media/scripts/generated/vehicles/template_suspension.txt:57`
[^61]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3231`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1147`
[^62]: `游戏原版/media/scripts/generated/items/normal.txt:11978`；`3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:80`
[^63]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3234`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1150`
[^64]: `游戏原版/media/scripts/generated/items/normal.txt:12129`；`游戏原版/media/scripts/generated/vehicles/template_brake.txt:57`
[^65]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3255`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1165`
[^66]: `游戏原版/media/scripts/generated/items/normal.txt:13136`；`游戏原版/media/scripts/generated/vehicles/template_muffler.txt:5`
[^67]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3258`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1168`
[^68]: `游戏原版/media/scripts/generated/items/normal.txt:11958`；`3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:80`
[^69]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3262`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1171`
[^70]: `游戏原版/media/scripts/generated/items/radio.txt:308`；`3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:86`
[^71]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:7374`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25092`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3645`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:5128`
[^72]: `游戏原版/media/scripts/generated/items/radio.txt:335`；`3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:86`
[^73]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:7375`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25093`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3649`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:5132`
[^74]: `游戏原版/media/scripts/generated/items/radio.txt:361`；`3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:86`
[^75]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:3001`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25091`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3651`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:5134`
[^76]: `游戏原版/media/scripts/generated/items/normal.txt:12748`；`3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:127`；`3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:143`
[^77]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3674`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1339`
[^78]: `游戏原版/media/scripts/generated/items/normal.txt:12720`；`3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:111`
[^79]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3677`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1342`
[^80]: `游戏原版/media/scripts/generated/items/normal.txt:12378`；`3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:83`
[^81]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:4152`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1543`
[^82]: `游戏原版/media/scripts/generated/items/normal.txt:12987`；`3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:160`；`3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:180`；`3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:200`；`3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:220`；`3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:240`；`3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:259`
[^83]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:4626`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1734`
[^84]: `游戏原版/media/scripts/generated/items/normal.txt:12706`；`3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:103`
[^85]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:4892`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1864`
[^86]: `3810637496/mods/LaoYuTranslationJava/common/media/lua/shared/Translate/CN/Recipes.json:2`
[^87]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/GridRVXmasItems.txt:171`
[^88]: `3810637496/mods/LaoYuTranslationJava/common/media/lua/shared/Translate/CN/Recipes.json:3`
[^89]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/GridRVXmasItems.txt:120`
[^90]: `3810637496/mods/LaoYuTranslationJava/common/media/lua/shared/Translate/CN/Recipes.json:4`
[^91]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/GridRVXmasItems.txt:69`
[^92]: `3810637496/mods/LaoYuTranslationJava/common/media/lua/shared/Translate/CN/Recipes.json:5`
[^93]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/GridRVXmasItems.txt:18`
[^94]: `3810637496/mods/LaoYuTranslationJava/common/media/lua/shared/Translate/CN/Recipes.json:6`
[^95]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/GridRVXmasItems.txt:222`
[^96]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:11935`；`3810637496/mods/LaoYuTranslationJava/common/media/lua/shared/Translate/CN/Recipes.json:7`
[^97]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/GridRVArmourItems.txt:211`
[^98]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:11932`；`3810637496/mods/LaoYuTranslationJava/common/media/lua/shared/Translate/CN/Recipes.json:8`
[^99]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/GridRVArmourItems.txt:121`
[^100]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:11933`；`3810637496/mods/LaoYuTranslationJava/common/media/lua/shared/Translate/CN/Recipes.json:9`
[^101]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/GridRVArmourItems.txt:141`
[^102]: `3810637496/mods/LaoYuTranslationJava/common/media/lua/shared/Translate/CN/Recipes.json:10`
[^103]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/GridRVArmourItems.txt:245`
[^104]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:12211`；`3810637496/mods/LaoYuTranslationJava/common/media/lua/shared/Translate/CN/Recipes.json:11`
[^105]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/GridRVArmourItems.txt:186`
[^106]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:11934`；`3810637496/mods/LaoYuTranslationJava/common/media/lua/shared/Translate/CN/Recipes.json:12`
[^107]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/GridRVArmourItems.txt:163`
[^108]: `3810637496/mods/LaoYuTranslationJava/common/media/lua/shared/Translate/CN/Recipes.json:13`
[^109]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/GridRVXmasItems.txt:191`
[^110]: `3810637496/mods/LaoYuTranslationJava/common/media/lua/shared/Translate/CN/Recipes.json:14`
[^111]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/GridRVXmasItems.txt:140`
[^112]: `3810637496/mods/LaoYuTranslationJava/common/media/lua/shared/Translate/CN/Recipes.json:15`
[^113]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/GridRVXmasItems.txt:89`
[^114]: `3810637496/mods/LaoYuTranslationJava/common/media/lua/shared/Translate/CN/Recipes.json:16`
[^115]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/GridRVXmasItems.txt:38`
[^116]: `3810637496/mods/LaoYuTranslationJava/common/media/lua/shared/Translate/CN/Recipes.json:17`
[^117]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/GridRVXmasItems.txt:242`
[^118]: `游戏原版/media/scripts/generated/vehicles/template_battery.txt:5`
[^119]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:57`
[^120]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:5`
[^121]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:18`
[^122]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:31`
[^123]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:44`
[^124]: `游戏原版/media/scripts/generated/vehicles/template_sounds_van.txt:14`
[^125]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:151`
[^126]: `游戏原版/media/scripts/generated/vehicles/template_door.txt:23`
[^127]: `游戏原版/media/scripts/generated/vehicles/template_sounds_van.txt:37`
[^128]: `游戏原版/media/scripts/generated/vehicles/template_engine.txt:5`
[^129]: `游戏原版/media/scripts/generated/vehicles/template_engine_door.txt:5`
[^130]: `游戏原版/media/scripts/generated/vehicles/template_sounds_van.txt:56`
[^131]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:694`
[^132]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:708`
[^133]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:719`
[^134]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:730`
[^135]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:358`
[^136]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:362`
[^137]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:398`
[^138]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:402`
[^139]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:406`
[^140]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:410`
[^141]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:414`
[^142]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:418`
[^143]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:422`
[^144]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:426`
[^145]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:430`
[^146]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:434`
[^147]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:366`
[^148]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:438`
[^149]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:442`
[^150]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:446`
[^151]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:450`
[^152]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:454`
[^153]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:458`
[^154]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:462`
[^155]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:466`
[^156]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:470`
[^157]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:474`
[^158]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:370`
[^159]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:478`
[^160]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:482`
[^161]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:486`
[^162]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:490`
[^163]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:494`
[^164]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:498`
[^165]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:502`
[^166]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:506`
[^167]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:510`
[^168]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:514`
[^169]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:374`
[^170]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:518`
[^171]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:522`
[^172]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:526`
[^173]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:530`
[^174]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:534`
[^175]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:538`
[^176]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:542`
[^177]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:546`
[^178]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:550`
[^179]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:554`
[^180]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:378`
[^181]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:558`
[^182]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:562`
[^183]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:566`
[^184]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:570`
[^185]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:574`
[^186]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:578`
[^187]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:582`
[^188]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:586`
[^189]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:590`
[^190]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:594`
[^191]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:382`
[^192]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:598`
[^193]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:602`
[^194]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:606`
[^195]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:610`
[^196]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:614`
[^197]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:618`
[^198]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:622`
[^199]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:626`
[^200]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:630`
[^201]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:634`
[^202]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:386`
[^203]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:638`
[^204]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:642`
[^205]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:390`
[^206]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:394`
[^207]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:670`
[^208]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:671`
[^209]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:680`
[^210]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:681`
[^211]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:682`
[^212]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:683`
[^213]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:684`
[^214]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:685`
[^215]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:686`
[^216]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:687`
[^217]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:688`
[^218]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:689`
[^219]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:672`
[^220]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:690`
[^221]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:691`
[^222]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:692`
[^223]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:693`
[^224]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:673`
[^225]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:674`
[^226]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:675`
[^227]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:676`
[^228]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:677`
[^229]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:678`
[^230]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:679`
[^231]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:306`
[^232]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:312`
[^233]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:646`
[^234]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:647`
[^235]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:656`
[^236]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:657`
[^237]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:658`
[^238]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:659`
[^239]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:660`
[^240]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:661`
[^241]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:662`
[^242]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:663`
[^243]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:664`
[^244]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:665`
[^245]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:648`
[^246]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:666`
[^247]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:667`
[^248]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:668`
[^249]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:669`
[^250]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:649`
[^251]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:650`
[^252]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:651`
[^253]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:652`
[^254]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:653`
[^255]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:654`
[^256]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:655`
[^257]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:361`
[^258]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:365`
[^259]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:401`
[^260]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:405`
[^261]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:409`
[^262]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:413`
[^263]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:417`
[^264]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:421`
[^265]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:425`
[^266]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:429`
[^267]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:433`
[^268]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:437`
[^269]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:369`
[^270]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:441`
[^271]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:445`
[^272]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:449`
[^273]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:453`
[^274]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:457`
[^275]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:461`
[^276]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:465`
[^277]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:469`
[^278]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:473`
[^279]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:477`
[^280]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:373`
[^281]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:481`
[^282]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:485`
[^283]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:489`
[^284]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:493`
[^285]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:497`
[^286]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:501`
[^287]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:505`
[^288]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:509`
[^289]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:513`
[^290]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:517`
[^291]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:377`
[^292]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:521`
[^293]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:525`
[^294]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:529`
[^295]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:533`
[^296]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:537`
[^297]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:541`
[^298]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:545`
[^299]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:549`
[^300]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:553`
[^301]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:557`
[^302]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:381`
[^303]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:561`
[^304]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:565`
[^305]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:569`
[^306]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:573`
[^307]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:577`
[^308]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:581`
[^309]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:585`
[^310]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:589`
[^311]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:593`
[^312]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:597`
[^313]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:385`
[^314]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:601`
[^315]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:605`
[^316]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:609`
[^317]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:613`
[^318]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:617`
[^319]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:621`
[^320]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:625`
[^321]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:629`
[^322]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:633`
[^323]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:637`
[^324]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:389`
[^325]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:641`
[^326]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:645`
[^327]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:393`
[^328]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:397`
[^329]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:739`
[^330]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:83`
[^331]: `游戏原版/media/scripts/generated/vehicles/template_glovebox.txt:5`
[^332]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:25`
[^333]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:318`
[^334]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:320`
[^335]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:321`
[^336]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:319`
[^337]: `游戏原版/media/scripts/generated/vehicles/template_heater.txt:5`
[^338]: `游戏原版/media/scripts/generated/vehicles/template_muffler.txt:5`
[^339]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:357`
[^340]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:349`
[^341]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:322`
[^342]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:340`
[^343]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:331`
[^344]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:259`
[^345]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:180`
[^346]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:160`
[^347]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:220`
[^348]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:200`
[^349]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:240`
[^350]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:198`
[^351]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:178`
[^352]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:238`
[^353]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:218`
[^354]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:278`
[^355]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:86`
[^356]: `游戏原版/media/scripts/generated/vehicles/template_seat.txt:5`
[^357]: `游戏原版/media/scripts/generated/vehicles/template_seat.txt:14`
[^358]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:65`
[^359]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:66`
[^360]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:57`
[^361]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:5`
[^362]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:18`
[^363]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:31`
[^364]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:44`
[^365]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:80`
[^366]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:81`
[^367]: `游戏原版/media/scripts/generated/vehicles/template_tire.txt:15`
[^368]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:82`
[^369]: `游戏原版/media/scripts/generated/vehicles/template_tire.txt:35`
[^370]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:119`
[^371]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:135`
[^372]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:127`
[^373]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:143`
[^374]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:103`
[^375]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/vehicles/GridRV.txt:111`
