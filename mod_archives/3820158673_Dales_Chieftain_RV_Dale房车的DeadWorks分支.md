# DeadWorks Dale 房车（Dale's Chieftain RV）

提供 DeadWorks Dale's Chieftain RV 分支；还依赖同包 DeadWorksNomadRV，不选择旧 Legacy/替代分支。

归属：**日常组合（玩法待验收）**；档案视图 `b422-compat`。
当前版本定义：**整车 1、本地物品定义 0、配方 0**；另引用共享物品 36。本地定义数含内部保留项，见独立列表；整车定义包括覆盖原版的条目，不等于新增车型数。

## 如何查找

- **生成整车**：在生成车辆菜单搜索下表完整 ID；显示译名时搜索中文列。联机管理命令用 `/addvehicle 完整ID`。
- **添加到背包**：普通物品、维修件、改装件都在添加物品菜单使用完整物品 ID；不要拿配方或内部槽位去刷车。
- **制作配方**：在制作界面查译名；配方 ID 用于排查，不是可放进背包的物品。
- 中文解释说明用途；只有翻译文件中找到的文字才称为游戏中文名。缺译保留脚本显示名，冲突列出各译文。

## 整车

| 完整生成车辆 ID | 当前中文名 / 名称状态 | 英文名或脚本名 | 变体说明 | 来源 |
| --- | --- | --- | --- | --- |
| `Base.DaleChieftainRV` | 戴尔的酋长房车 / Dale 的 Chieftain 房车（译文冲突，待游戏核实）[^1] | Dale's Chieftain RV[^2] | 脚本座位数 4；机修类型 2；具体外观与性能待游戏实刷 | [^3] |

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
| `Base.BigGasTank2` | 油箱 (大型)（翻译文件含非标准语法，待游戏核实）[^5] | 车辆安装件，用于油箱（GasTank）；适用车型见右列 / 维修配件 | 添加物品 | Base.DaleChieftainRV → GasTank | 游戏原版[^4] |
| `Base.CarBattery2` | 汽车电池（翻译文件含非标准语法，待游戏核实）[^7] | 车辆安装件，用于蓄电池（Battery）、蓄电池（GRHouseBattery1）、蓄电池（GRHouseBattery2）；适用车型见右列 / 维修配件 | 添加物品 | Base.DaleChieftainRV → Battery；Base.DaleChieftainRV → GRHouseBattery1；Base.DaleChieftainRV → GRHouseBattery2 | 游戏原版[^6] |
| `Base.EngineDoor2` | 引擎罩（翻译文件含非标准语法，待游戏核实）[^9] | 车辆安装件，用于引擎盖（EngineDoor）；适用车型见右列 / 维修配件 | 添加物品 | Base.DaleChieftainRV → EngineDoor | 游戏原版[^8] |
| `Base.FrontCarDoor2` | 车前门（翻译文件含非标准语法，待游戏核实）[^11] | 车辆安装件，用于车门（DoorFrontLeft）、车门（DoorFrontRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.DaleChieftainRV → DoorFrontLeft；Base.DaleChieftainRV → DoorFrontRight | 游戏原版[^10] |
| `Base.FrontWindow2` | 车前窗（翻译文件含非标准语法，待游戏核实）[^13] | 车辆安装件，用于车窗（WindowFrontLeft）、车窗（WindowFrontRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.DaleChieftainRV → WindowFrontLeft；Base.DaleChieftainRV → WindowFrontRight | 游戏原版[^12] |
| `Base.GloveBox2` | 手套箱（翻译文件含非标准语法，待游戏核实）[^15] | 车辆安装件，用于车辆安装位（GloveBox）；适用车型见右列 / 维修配件 | 添加物品 | Base.DaleChieftainRV → GloveBox | 游戏原版[^14] |
| `Base.GridRVArmorDoor` | 房车车门装甲 / 房车入口门装甲（译文冲突，待游戏核实）[^17] | 车辆安装件，用于车门（RVArmorDoor）；适用车型见右列 / 改装配件 | 添加物品 | Base.DaleChieftainRV → RVArmorDoor | DeadWorksNomadRV[^16] |
| `Base.GridRVArmorDoorXmas` | 房车圣诞入口门装甲[^19] | 车辆安装件，用于车门（RVArmorDoor）；适用车型见右列 / 改装配件 | 添加物品 | Base.DaleChieftainRV → RVArmorDoor | DeadWorksNomadRV[^18] |
| `Base.GridRVArmorGrilles` | 房车车窗格栅 / 房车车窗护栏（译文冲突，待游戏核实）[^21] | 车辆安装件，用于防护件（RVArmorGrilles）；适用车型见右列 / 改装配件 | 添加物品 | Base.DaleChieftainRV → RVArmorGrilles | DeadWorksNomadRV[^20] |
| `Base.GridRVArmorGrillesXmas` | 房车圣诞车窗护栏[^23] | 车辆安装件，用于防护件（RVArmorGrilles）；适用车型见右列 / 改装配件 | 添加物品 | Base.DaleChieftainRV → RVArmorGrilles | DeadWorksNomadRV[^22] |
| `Base.GridRVArmorSkirts` | 房车侧面装甲 / 房车侧裙装甲（译文冲突，待游戏核实）[^25] | 车辆安装件，用于防护件（RVArmorSkirts）；适用车型见右列 / 改装配件 | 添加物品 | Base.DaleChieftainRV → RVArmorSkirts | DeadWorksNomadRV[^24] |
| `Base.GridRVArmorSkirtsXmas` | 房车圣诞侧裙装甲[^27] | 车辆安装件，用于防护件（RVArmorSkirts）；适用车型见右列 / 改装配件 | 添加物品 | Base.DaleChieftainRV → RVArmorSkirts | DeadWorksNomadRV[^26] |
| `Base.GridRVBikeCarrier` | 房车摩托车架[^29] | 车辆安装件，用于车辆安装位（RVRack）；适用车型见右列 / 维修配件 | 添加物品 | Base.DaleChieftainRV → RVRack | DeadWorksNomadRV[^28] |
| `Base.GridRVCowCatcher` | 房车排障器[^31] | 车辆安装件，用于防护件（RVArmorCatcher）；适用车型见右列 / 改装配件 | 添加物品 | Base.DaleChieftainRV → RVArmorCatcher | DeadWorksNomadRV[^30] |
| `Base.GridRVCowCatcherXmas` | 房车圣诞排障器[^33] | 车辆安装件，用于防护件（RVArmorCatcher）；适用车型见右列 / 改装配件 | 添加物品 | Base.DaleChieftainRV → RVArmorCatcher | DeadWorksNomadRV[^32] |
| `Base.LightBulb` | 灯泡-白色 / 灯泡 (白)（译文冲突，待游戏核实）[^35] | 车辆安装件，用于车灯（Headlight*）、车灯（JP82DorothyLights）；适用车型见右列 / 维修配件 | 添加物品 | Base.DaleChieftainRV → Headlight* | 游戏原版[^34] |
| `Base.ModernBrake2` | 制动器 (高级)（翻译文件含非标准语法，待游戏核实）[^37] | 车辆安装件，用于制动器（Brake*）；适用车型见右列 / 维修配件 | 添加物品 | Base.DaleChieftainRV → Brake* | 游戏原版[^36] |
| `Base.ModernCarMuffler2` | 消声器 (高级)（翻译文件含非标准语法，待游戏核实）[^39] | 车辆安装件，用于消声器（Muffler）；适用车型见右列 / 维修配件 | 添加物品 | Base.DaleChieftainRV → Muffler | 游戏原版[^38] |
| `Base.ModernSuspension2` | 悬挂 (高级)（翻译文件含非标准语法，待游戏核实）[^41] | 车辆安装件，用于悬挂（Suspension*）；适用车型见右列 / 维修配件 | 添加物品 | Base.DaleChieftainRV → Suspension* | 游戏原版[^40] |
| `Base.ModernTire2` | 轮胎 (高级)（翻译文件含非标准语法，待游戏核实）[^43] | 车辆安装件，用于轮胎（Tire*）；适用车型见右列 / 维修配件 | 添加物品 | Base.DaleChieftainRV → Tire* | 游戏原版[^42] |
| `Base.NormalBrake2` | 制动器 (普通)（翻译文件含非标准语法，待游戏核实）[^45] | 车辆安装件，用于制动器（Brake*）；适用车型见右列 / 维修配件 | 添加物品 | Base.DaleChieftainRV → Brake* | 游戏原版[^44] |
| `Base.NormalCarMuffler2` | 消声器 (普通)（翻译文件含非标准语法，待游戏核实）[^47] | 车辆安装件，用于消声器（Muffler）；适用车型见右列 / 维修配件 | 添加物品 | Base.DaleChieftainRV → Muffler | 游戏原版[^46] |
| `Base.NormalGasTank2` | 油箱 (标准)（翻译文件含非标准语法，待游戏核实）[^49] | 车辆安装件，用于油箱（GasTank）；适用车型见右列 / 维修配件 | 添加物品 | Base.DaleChieftainRV → GasTank | 游戏原版[^48] |
| `Base.NormalSuspension2` | 悬挂 (普通)（翻译文件含非标准语法，待游戏核实）[^51] | 车辆安装件，用于悬挂（Suspension*）；适用车型见右列 / 维修配件 | 添加物品 | Base.DaleChieftainRV → Suspension* | 游戏原版[^50] |
| `Base.NormalTire2` | 轮胎 (普通)（翻译文件含非标准语法，待游戏核实）[^53] | 车辆安装件，用于轮胎（Tire*）；适用车型见右列 / 维修配件 | 添加物品 | Base.DaleChieftainRV → Tire* | 游戏原版[^52] |
| `Base.OldBrake2` | 制动器 (老式)（翻译文件含非标准语法，待游戏核实）[^55] | 车辆安装件，用于制动器（Brake*）；适用车型见右列 / 维修配件 | 添加物品 | Base.DaleChieftainRV → Brake* | 游戏原版[^54] |
| `Base.OldCarMuffler2` | 消声器 (老式)（翻译文件含非标准语法，待游戏核实）[^57] | 车辆安装件，用于消声器（Muffler）；适用车型见右列 / 维修配件 | 添加物品 | Base.DaleChieftainRV → Muffler | 游戏原版[^56] |
| `Base.OldTire2` | 轮胎 (廉价)（翻译文件含非标准语法，待游戏核实）[^59] | 车辆安装件，用于轮胎（TireFrontLeft）、轮胎（TireFrontRight）、轮胎（Tire*）、轮胎（TireRearLeft）、轮胎（TireRearRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.DaleChieftainRV → Tire* | 游戏原版[^58] |
| `Base.RadioBlack` | 收音机 (超值科技) / 收音机 (廉科) / 廉科牌收音机（译文冲突，待游戏核实）[^61] | 车辆安装件，用于车辆安装位（Radio）；适用车型见右列 / 维修配件 | 添加物品 | Base.DaleChieftainRV → Radio | 游戏原版[^60] |
| `Base.RadioMakeShift` | 收音机 (简易) / 自制收音机（译文冲突，待游戏核实）[^63] | 车辆安装件，用于车辆安装位（Radio）；适用车型见右列 / 维修配件 | 添加物品 | Base.DaleChieftainRV → Radio | 游戏原版[^62] |
| `Base.RadioRed` | 导航仪 / 收音机 (昂科) / 昂科牌收音机（译文冲突，待游戏核实）[^65] | 车辆安装件，用于车辆安装位（Radio）；适用车型见右列 / 维修配件 | 添加物品 | Base.DaleChieftainRV → Radio | 游戏原版[^64] |
| `Base.RearWindow2` | 车后窗（翻译文件含非标准语法，待游戏核实）[^67] | 车辆安装件，用于车窗（WindowRearLeft）、车窗（WindowRearRight）、车窗（WindowMiddleLeft）、车窗（WindowMiddleRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.DaleChieftainRV → WindowRearLeft；Base.DaleChieftainRV → WindowRearRight | 游戏原版[^66] |
| `Base.RearWindshield2` | 后挡风玻璃（翻译文件含非标准语法，待游戏核实）[^69] | 车辆安装件，用于挡风玻璃（WindshieldRear）；适用车型见右列 / 维修配件 | 添加物品 | Base.DaleChieftainRV → WindshieldRear | 游戏原版[^68] |
| `Base.SmallGasTank2` | 油箱 (小型)（翻译文件含非标准语法，待游戏核实）[^71] | 车辆安装件，用于油箱（GasTank）；适用车型见右列 / 维修配件 | 添加物品 | Base.DaleChieftainRV → GasTank | 游戏原版[^70] |
| `Base.TrunkDoor2` | 后备箱盖（翻译文件含非标准语法，待游戏核实）[^73] | 车辆安装件，用于车门（RVBayDoorLeftRear）、车门（RVBayDoorLeftFront）、车门（RVBayDoorRightRear）、车门（RVBayDoorRightFront）、车门（RVBayDoorRightWater）、车门（RVBayDoorLeftBattery）、车门（DaleLockerDoorLeftRear）、车门（DaleLockerDoorLeftMidRear）、车门（DaleLockerDoorLeftMidFront）、车门（DaleLockerDoorLeftFront）、车门（DaleLockerDoorRightRear）、车门（DaleLockerDoorRightMid）、车门（DaleLockerDoorRightFront）、车门（DaleRearDoor）、后备箱（TrunkDoor）；适用车型见右列 / 维修配件 | 添加物品 | Base.DaleChieftainRV → DaleLockerDoorLeftRear；Base.DaleChieftainRV → DaleLockerDoorLeftMidRear；Base.DaleChieftainRV → DaleLockerDoorLeftMidFront；Base.DaleChieftainRV → DaleLockerDoorLeftFront；Base.DaleChieftainRV → DaleLockerDoorRightRear；Base.DaleChieftainRV → DaleLockerDoorRightMid；Base.DaleChieftainRV → DaleLockerDoorRightFront；Base.DaleChieftainRV → DaleRearDoor | 游戏原版[^72] |
| `Base.Windshield2` | 挡风玻璃（翻译文件含非标准语法，待游戏核实）[^75] | 车辆安装件，用于挡风玻璃（Windshield）；适用车型见右列 / 维修配件 | 添加物品 | Base.DaleChieftainRV → Windshield | 游戏原版[^74] |

## 制作配方

无当前有效的脚本制作配方。Lua 动态添加的内容不在本次静态统计内。

## 内部定义、历史分支与未解析引用

有效资源层：42；仅合并 common 与所选版本，Overlay 按相对路径覆盖。
车辆模板 0 个、内部槽位 262 个，均不算整车或背包物品。旧根目录和未选中版本的定义不列入当前可用表。模板中短物品引用若追加机修类型后缀才匹配定义，属于静态映射，安装仍待实测。

<details><summary>查看内部槽位（不能直接刷取）</summary>

| 槽位 | 名称或说明 | 来源 |
| --- | --- | --- |
| `Battery` | 电池 / 蓄电池 | [^76] |
| `Brake*` | Brake* / 制动器 | [^77] |
| `BrakeFrontLeft` | 左前制动 / 制动器 | [^78] |
| `BrakeFrontRight` | 右前制动 / 制动器 | [^79] |
| `BrakeRearLeft` | 左后制动 / 制动器 | [^80] |
| `BrakeRearRight` | 右后制动 / 制动器 | [^81] |
| `DaleLockerDoorLeftFront` | 左前储物柜门 / 车门 | [^82] |
| `DaleLockerDoorLeftMidFront` | 左中前储物柜门 / 左侧中前部储物柜门 / 车门 | [^83] |
| `DaleLockerDoorLeftMidRear` | 左中后储物柜门 / 左侧中后部储物柜门 / 车门 | [^84] |
| `DaleLockerDoorLeftRear` | 电池舱门 / 车门 | [^85] |
| `DaleLockerDoorRightFront` | 右前储物柜门 / 车门 | [^86] |
| `DaleLockerDoorRightMid` | 右中储物柜门 / 右侧中部储物柜门 / 车门 | [^87] |
| `DaleLockerDoorRightRear` | 加水口 / 水箱舱盖 / 车门 | [^88] |
| `DaleLockerLeftFront` | 左前储物柜 / 车辆安装位 | [^89] |
| `DaleLockerLeftMidFront` | 左中前储物柜 / 左侧中前部储物柜 / 车辆安装位 | [^90] |
| `DaleLockerLeftMidRear` | 左中后储物柜 / 左侧中后部储物柜 / 车辆安装位 | [^91] |
| `DaleLockerRightFront` | 右前储物柜 / 车辆安装位 | [^92] |
| `DaleLockerRightMid` | 右中储物柜 / 右侧中部储物柜 / 车辆安装位 | [^93] |
| `DaleRearDoor` | 后储物柜门 / 后部储物柜门 / 车门 | [^94] |
| `DaleRearLocker` | 后储物柜 / 后部储物柜 / 车辆安装位 | [^95] |
| `Door*` | Door* / 车门 | [^96] |
| `DoorFrontLeft` | 左前门 / 车门 | [^97] |
| `DoorFrontRight` | 右前门 / 车门 | [^98] |
| `DoorRear*` | DoorRear* / 车门 | [^99] |
| `Engine` | 引擎 / 发动机 | [^100] |
| `EngineDoor` | 引擎盖 / 引擎盖 | [^101] |
| `EngineDoor*` | EngineDoor* / 引擎盖 | [^102] |
| `GRAnim0` | GRAnim0 / 车辆安装位 | [^103] |
| `GRAnim1` | GRAnim1 / 车辆安装位 | [^104] |
| `GRAnim3` | GRAnim3 / 车辆安装位 | [^105] |
| `GRCell0` | GRCell0 / 车辆安装位 | [^106] |
| `GRCell1` | GRCell1 / 车辆安装位 | [^107] |
| `GRCell10` | GRCell10 / 车辆安装位 | [^108] |
| `GRCell11` | GRCell11 / 车辆安装位 | [^109] |
| `GRCell12` | GRCell12 / 车辆安装位 | [^110] |
| `GRCell13` | GRCell13 / 车辆安装位 | [^111] |
| `GRCell14` | GRCell14 / 车辆安装位 | [^112] |
| `GRCell15` | GRCell15 / 车辆安装位 | [^113] |
| `GRCell16` | GRCell16 / 车辆安装位 | [^114] |
| `GRCell17` | GRCell17 / 车辆安装位 | [^115] |
| `GRCell18` | GRCell18 / 车辆安装位 | [^116] |
| `GRCell19` | GRCell19 / 车辆安装位 | [^117] |
| `GRCell2` | GRCell2 / 车辆安装位 | [^118] |
| `GRCell20` | GRCell20 / 车辆安装位 | [^119] |
| `GRCell21` | GRCell21 / 车辆安装位 | [^120] |
| `GRCell22` | GRCell22 / 车辆安装位 | [^121] |
| `GRCell23` | GRCell23 / 车辆安装位 | [^122] |
| `GRCell24` | GRCell24 / 车辆安装位 | [^123] |
| `GRCell25` | GRCell25 / 车辆安装位 | [^124] |
| `GRCell26` | GRCell26 / 车辆安装位 | [^125] |
| `GRCell27` | GRCell27 / 车辆安装位 | [^126] |
| `GRCell28` | GRCell28 / 车辆安装位 | [^127] |
| `GRCell29` | GRCell29 / 车辆安装位 | [^128] |
| `GRCell3` | GRCell3 / 车辆安装位 | [^129] |
| `GRCell30` | GRCell30 / 车辆安装位 | [^130] |
| `GRCell31` | GRCell31 / 车辆安装位 | [^131] |
| `GRCell32` | GRCell32 / 车辆安装位 | [^132] |
| `GRCell33` | GRCell33 / 车辆安装位 | [^133] |
| `GRCell34` | GRCell34 / 车辆安装位 | [^134] |
| `GRCell35` | GRCell35 / 车辆安装位 | [^135] |
| `GRCell36` | GRCell36 / 车辆安装位 | [^136] |
| `GRCell37` | GRCell37 / 车辆安装位 | [^137] |
| `GRCell38` | GRCell38 / 车辆安装位 | [^138] |
| `GRCell39` | GRCell39 / 车辆安装位 | [^139] |
| `GRCell4` | GRCell4 / 车辆安装位 | [^140] |
| `GRCell40` | GRCell40 / 车辆安装位 | [^141] |
| `GRCell41` | GRCell41 / 车辆安装位 | [^142] |
| `GRCell42` | GRCell42 / 车辆安装位 | [^143] |
| `GRCell43` | GRCell43 / 车辆安装位 | [^144] |
| `GRCell44` | GRCell44 / 车辆安装位 | [^145] |
| `GRCell45` | GRCell45 / 车辆安装位 | [^146] |
| `GRCell46` | GRCell46 / 车辆安装位 | [^147] |
| `GRCell47` | GRCell47 / 车辆安装位 | [^148] |
| `GRCell48` | GRCell48 / 车辆安装位 | [^149] |
| `GRCell49` | GRCell49 / 车辆安装位 | [^150] |
| `GRCell5` | GRCell5 / 车辆安装位 | [^151] |
| `GRCell50` | GRCell50 / 车辆安装位 | [^152] |
| `GRCell51` | GRCell51 / 车辆安装位 | [^153] |
| `GRCell52` | GRCell52 / 车辆安装位 | [^154] |
| `GRCell53` | GRCell53 / 车辆安装位 | [^155] |
| `GRCell54` | GRCell54 / 车辆安装位 | [^156] |
| `GRCell55` | GRCell55 / 车辆安装位 | [^157] |
| `GRCell56` | GRCell56 / 车辆安装位 | [^158] |
| `GRCell57` | GRCell57 / 车辆安装位 | [^159] |
| `GRCell58` | GRCell58 / 车辆安装位 | [^160] |
| `GRCell59` | GRCell59 / 车辆安装位 | [^161] |
| `GRCell6` | GRCell6 / 车辆安装位 | [^162] |
| `GRCell60` | GRCell60 / 车辆安装位 | [^163] |
| `GRCell61` | GRCell61 / 车辆安装位 | [^164] |
| `GRCell62` | GRCell62 / 车辆安装位 | [^165] |
| `GRCell63` | GRCell63 / 车辆安装位 | [^166] |
| `GRCell64` | GRCell64 / 车辆安装位 | [^167] |
| `GRCell65` | GRCell65 / 车辆安装位 | [^168] |
| `GRCell66` | GRCell66 / 车辆安装位 | [^169] |
| `GRCell67` | GRCell67 / 车辆安装位 | [^170] |
| `GRCell68` | GRCell68 / 车辆安装位 | [^171] |
| `GRCell69` | GRCell69 / 车辆安装位 | [^172] |
| `GRCell7` | GRCell7 / 车辆安装位 | [^173] |
| `GRCell70` | GRCell70 / 车辆安装位 | [^174] |
| `GRCell71` | GRCell71 / 车辆安装位 | [^175] |
| `GRCell8` | GRCell8 / 车辆安装位 | [^176] |
| `GRCell9` | GRCell9 / 车辆安装位 | [^177] |
| `GRDaleAwning` | GRDaleAwning / 车辆安装位 | [^178] |
| `GRFreezer0` | GRFreezer0 / 车辆安装位 | [^179] |
| `GRFreezer1` | GRFreezer1 / 车辆安装位 | [^180] |
| `GRFreezer10` | GRFreezer10 / 车辆安装位 | [^181] |
| `GRFreezer11` | GRFreezer11 / 车辆安装位 | [^182] |
| `GRFreezer12` | GRFreezer12 / 车辆安装位 | [^183] |
| `GRFreezer13` | GRFreezer13 / 车辆安装位 | [^184] |
| `GRFreezer14` | GRFreezer14 / 车辆安装位 | [^185] |
| `GRFreezer15` | GRFreezer15 / 车辆安装位 | [^186] |
| `GRFreezer16` | GRFreezer16 / 车辆安装位 | [^187] |
| `GRFreezer17` | GRFreezer17 / 车辆安装位 | [^188] |
| `GRFreezer18` | GRFreezer18 / 车辆安装位 | [^189] |
| `GRFreezer19` | GRFreezer19 / 车辆安装位 | [^190] |
| `GRFreezer2` | GRFreezer2 / 车辆安装位 | [^191] |
| `GRFreezer20` | GRFreezer20 / 车辆安装位 | [^192] |
| `GRFreezer21` | GRFreezer21 / 车辆安装位 | [^193] |
| `GRFreezer22` | GRFreezer22 / 车辆安装位 | [^194] |
| `GRFreezer23` | GRFreezer23 / 车辆安装位 | [^195] |
| `GRFreezer3` | GRFreezer3 / 车辆安装位 | [^196] |
| `GRFreezer4` | GRFreezer4 / 车辆安装位 | [^197] |
| `GRFreezer5` | GRFreezer5 / 车辆安装位 | [^198] |
| `GRFreezer6` | GRFreezer6 / 车辆安装位 | [^199] |
| `GRFreezer7` | GRFreezer7 / 车辆安装位 | [^200] |
| `GRFreezer8` | GRFreezer8 / 车辆安装位 | [^201] |
| `GRFreezer9` | GRFreezer9 / 车辆安装位 | [^202] |
| `GRHouseBattery1` | 生活电池1 / 生活电池 1 / 蓄电池 | [^203] |
| `GRHouseBattery2` | 生活电池2 / 生活电池 2 / 蓄电池 | [^204] |
| `GRLoose0` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^205] |
| `GRLoose1` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^206] |
| `GRLoose10` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^207] |
| `GRLoose11` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^208] |
| `GRLoose12` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^209] |
| `GRLoose13` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^210] |
| `GRLoose14` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^211] |
| `GRLoose15` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^212] |
| `GRLoose16` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^213] |
| `GRLoose17` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^214] |
| `GRLoose18` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^215] |
| `GRLoose19` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^216] |
| `GRLoose2` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^217] |
| `GRLoose20` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^218] |
| `GRLoose21` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^219] |
| `GRLoose22` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^220] |
| `GRLoose23` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^221] |
| `GRLoose3` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^222] |
| `GRLoose4` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^223] |
| `GRLoose5` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^224] |
| `GRLoose6` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^225] |
| `GRLoose7` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^226] |
| `GRLoose8` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^227] |
| `GRLoose9` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^228] |
| `GRPacked0` | GRPacked0 / 车辆安装位 | [^229] |
| `GRPacked1` | GRPacked1 / 车辆安装位 | [^230] |
| `GRPacked10` | GRPacked10 / 车辆安装位 | [^231] |
| `GRPacked11` | GRPacked11 / 车辆安装位 | [^232] |
| `GRPacked12` | GRPacked12 / 车辆安装位 | [^233] |
| `GRPacked13` | GRPacked13 / 车辆安装位 | [^234] |
| `GRPacked14` | GRPacked14 / 车辆安装位 | [^235] |
| `GRPacked15` | GRPacked15 / 车辆安装位 | [^236] |
| `GRPacked16` | GRPacked16 / 车辆安装位 | [^237] |
| `GRPacked17` | GRPacked17 / 车辆安装位 | [^238] |
| `GRPacked18` | GRPacked18 / 车辆安装位 | [^239] |
| `GRPacked19` | GRPacked19 / 车辆安装位 | [^240] |
| `GRPacked2` | GRPacked2 / 车辆安装位 | [^241] |
| `GRPacked20` | GRPacked20 / 车辆安装位 | [^242] |
| `GRPacked21` | GRPacked21 / 车辆安装位 | [^243] |
| `GRPacked22` | GRPacked22 / 车辆安装位 | [^244] |
| `GRPacked23` | GRPacked23 / 车辆安装位 | [^245] |
| `GRPacked24` | GRPacked24 / 车辆安装位 | [^246] |
| `GRPacked25` | GRPacked25 / 车辆安装位 | [^247] |
| `GRPacked26` | GRPacked26 / 车辆安装位 | [^248] |
| `GRPacked27` | GRPacked27 / 车辆安装位 | [^249] |
| `GRPacked28` | GRPacked28 / 车辆安装位 | [^250] |
| `GRPacked29` | GRPacked29 / 车辆安装位 | [^251] |
| `GRPacked3` | GRPacked3 / 车辆安装位 | [^252] |
| `GRPacked30` | GRPacked30 / 车辆安装位 | [^253] |
| `GRPacked31` | GRPacked31 / 车辆安装位 | [^254] |
| `GRPacked32` | GRPacked32 / 车辆安装位 | [^255] |
| `GRPacked33` | GRPacked33 / 车辆安装位 | [^256] |
| `GRPacked34` | GRPacked34 / 车辆安装位 | [^257] |
| `GRPacked35` | GRPacked35 / 车辆安装位 | [^258] |
| `GRPacked36` | GRPacked36 / 车辆安装位 | [^259] |
| `GRPacked37` | GRPacked37 / 车辆安装位 | [^260] |
| `GRPacked38` | GRPacked38 / 车辆安装位 | [^261] |
| `GRPacked39` | GRPacked39 / 车辆安装位 | [^262] |
| `GRPacked4` | GRPacked4 / 车辆安装位 | [^263] |
| `GRPacked40` | GRPacked40 / 车辆安装位 | [^264] |
| `GRPacked41` | GRPacked41 / 车辆安装位 | [^265] |
| `GRPacked42` | GRPacked42 / 车辆安装位 | [^266] |
| `GRPacked43` | GRPacked43 / 车辆安装位 | [^267] |
| `GRPacked44` | GRPacked44 / 车辆安装位 | [^268] |
| `GRPacked45` | GRPacked45 / 车辆安装位 | [^269] |
| `GRPacked46` | GRPacked46 / 车辆安装位 | [^270] |
| `GRPacked47` | GRPacked47 / 车辆安装位 | [^271] |
| `GRPacked48` | GRPacked48 / 车辆安装位 | [^272] |
| `GRPacked49` | GRPacked49 / 车辆安装位 | [^273] |
| `GRPacked5` | GRPacked5 / 车辆安装位 | [^274] |
| `GRPacked50` | GRPacked50 / 车辆安装位 | [^275] |
| `GRPacked51` | GRPacked51 / 车辆安装位 | [^276] |
| `GRPacked52` | GRPacked52 / 车辆安装位 | [^277] |
| `GRPacked53` | GRPacked53 / 车辆安装位 | [^278] |
| `GRPacked54` | GRPacked54 / 车辆安装位 | [^279] |
| `GRPacked55` | GRPacked55 / 车辆安装位 | [^280] |
| `GRPacked56` | GRPacked56 / 车辆安装位 | [^281] |
| `GRPacked57` | GRPacked57 / 车辆安装位 | [^282] |
| `GRPacked58` | GRPacked58 / 车辆安装位 | [^283] |
| `GRPacked59` | GRPacked59 / 车辆安装位 | [^284] |
| `GRPacked6` | GRPacked6 / 车辆安装位 | [^285] |
| `GRPacked60` | GRPacked60 / 车辆安装位 | [^286] |
| `GRPacked61` | GRPacked61 / 车辆安装位 | [^287] |
| `GRPacked62` | GRPacked62 / 车辆安装位 | [^288] |
| `GRPacked63` | GRPacked63 / 车辆安装位 | [^289] |
| `GRPacked64` | GRPacked64 / 车辆安装位 | [^290] |
| `GRPacked65` | GRPacked65 / 车辆安装位 | [^291] |
| `GRPacked66` | GRPacked66 / 车辆安装位 | [^292] |
| `GRPacked67` | GRPacked67 / 车辆安装位 | [^293] |
| `GRPacked68` | GRPacked68 / 车辆安装位 | [^294] |
| `GRPacked69` | GRPacked69 / 车辆安装位 | [^295] |
| `GRPacked7` | GRPacked7 / 车辆安装位 | [^296] |
| `GRPacked70` | GRPacked70 / 车辆安装位 | [^297] |
| `GRPacked71` | GRPacked71 / 车辆安装位 | [^298] |
| `GRPacked8` | GRPacked8 / 车辆安装位 | [^299] |
| `GRPacked9` | GRPacked9 / 车辆安装位 | [^300] |
| `GRSteps` | GRSteps / 车辆安装位 | [^301] |
| `GasTank` | 油箱 / 油箱 | [^302] |
| `GloveBox` | 手套箱 / 车辆安装位 | [^303] |
| `Headlight*` | Headlight* / 车灯 | [^304] |
| `HeadlightLeft` | 左大灯 / 车灯 | [^305] |
| `HeadlightRearLeft` | 左尾灯 / 车灯 | [^306] |
| `HeadlightRearRight` | 右尾灯 / 车灯 | [^307] |
| `HeadlightRight` | 右大灯 / 车灯 | [^308] |
| `Heater` | 加热器 / 车辆安装位 | [^309] |
| `Muffler` | 排气消声器 / 消声器 | [^310] |
| `PassengerCompartment` | 乘员舱 / 车辆安装位 | [^311] |
| `RVArmorCatcher` | 排障器 / 防护件 | [^312] |
| `RVArmorDoor` | 车门装甲 / 入口门装甲 / 车门 | [^313] |
| `RVArmorGrilles` | 车窗格栅 / 车窗护栏 / 防护件 | [^314] |
| `RVArmorSkirts` | 侧面装甲 / 侧裙装甲 / 防护件 | [^315] |
| `RVRack` | 摩托车架 / 车辆安装位 | [^316] |
| `Radio` | 电台 / 车辆安装位 | [^317] |
| `SeatFrontLeft` | 驾驶座 / 座椅 | [^318] |
| `SeatFrontRight` | 右前座 / 座椅 | [^319] |
| `SeatRearLeft` | 左后座 / 座椅 | [^320] |
| `SeatRearRight` | 右后座 / 座椅 | [^321] |
| `Suspension*` | Suspension* / 悬挂 | [^322] |
| `SuspensionFrontLeft` | 左前悬挂 / 悬挂 | [^323] |
| `SuspensionFrontRight` | 右前悬挂 / 悬挂 | [^324] |
| `SuspensionRearLeft` | 左后悬挂 / 悬挂 | [^325] |
| `SuspensionRearRight` | 右后悬挂 / 悬挂 | [^326] |
| `Tire*` | Tire* / 轮胎 | [^327] |
| `TireFrontLeft` | 左前胎 / 轮胎 | [^328] |
| `TireFrontRight` | 右前胎 / 轮胎 | [^329] |
| `TireRearLeft` | 左后胎 / 轮胎 | [^330] |
| `TireRearRight` | 右后胎 / 轮胎 | [^331] |
| `WindowFrontLeft` | 左前窗 / 车窗 | [^332] |
| `WindowFrontRight` | 右前窗 / 车窗 | [^333] |
| `WindowRearLeft` | 左后窗 / 车窗 | [^334] |
| `WindowRearRight` | 右后窗 / 车窗 | [^335] |
| `Windshield` | 挡风玻璃 / 挡风玻璃 | [^336] |
| `WindshieldRear` | 后挡风玻璃 / 挡风玻璃 | [^337] |

</details>


## 概览

| Mod ID / 文件夹 | 分发端 | 版本 | 选择的 mod.info | 原件范围 → 当前范围 |
| --- | --- | --- | --- | --- |
| `DeadWorksDaleRV` / `DeadWorksDaleRV` | both（双端） | 0.2.2 | `42/mod.info` | 42.21 … 42.21 → 42.21 … 42.22（Overlay） |

原件体积 53.5 MB；体积按完整目录统计，与当前内容定义数分开。
工作坊：[查看作者页面](https://steamcommunity.com/sharedfiles/filedetails/?id=3820158673)。

## 证据与使用边界

**verified：有效源码静态确认。** 每个当前可复制 ID 均来自所选版本的定义；这不保证游戏已成功注册、生成、安装或联机同步。
挑战者 5 个车辆中文名另有 Owner 截图确认；本轮没有启动游戏。译文冲突、动态 Lua 内容和玩法效果仍需 Owner 游戏内核实。
以下人工记录保留原始语境；其中旧组合、旧数量和旧候选状态仅供追溯，当前统计与归属以上表和 profile 为准。

<!-- retained:start -->
## 依赖与冲突

- 需要：`DeadWorksVehicleFramework, DeadWorksNomadRV, PZVoxelStudioViewpoint`
- 互斥：`GridRV, GridRVHost, DaleChieftainRV`
- 被依赖：无（叶子节点）

## 双端与联机

双端候选；依赖 DeadWorksVehicleFramework、DeadWorksNomadRV 与 6282。

当前 profile：both（双端）。

本机文件构成：客户端有 lua；服务端无 lua（只挂载）。

## 实测与排查

原件 0.2.2，42.21 上限；仅元数据 Overlay。外观、车内交互和持久化未验收。

**planned：仅完成依赖、版本与补丁指纹静态检查。** 迁移收尾按 Owner 要求不启动游戏；本候选组合未验证加载、联网、存档或视觉。

版本放行补丁：`A004/workspace/patches/mods/DeadWorksDaleRV/42/mod.info`。原件更新后须重新核对指纹；撤除此补丁后运行 check 会恢复原件版本限制。

```
cd A004
python lab.py check --profile b422-compat
grep -a 'DeadWorksDaleRV' runs/<trial>/*console.log
```
<!-- retained:end -->

## 静态来源

路径相对 `A004/workspace/mods_library/`；`Overlay/<文件夹>/` 指 `A004/workspace/patches/mods/<文件夹>/`，`游戏原版/` 指当前 B42.22 客户端 Game 目录。翻译来源列出所有候选，未按加载顺序擅自消解异文。

[^1]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/IG_UI.json:43519`；`3810637496/mods/LaoYuTranslationJava/common/media/lua/shared/Translate/CN/IG_UI.json:187`
[^2]: `3820158673/mods/DeadWorksDaleRV/42/media/lua/shared/Translate/EN/IG_UI.json:2`；`3820158673/mods/DeadWorksDaleRV/42/media/lua/shared/Translate/EN/IG_UI_EN.txt:2`
[^3]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:2`
[^4]: `游戏原版/media/scripts/generated/items/normal.txt:12408`；`3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:85`
[^5]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:448`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:163`
[^6]: `游戏原版/media/scripts/generated/items/drainable.txt:2368`；`游戏原版/media/scripts/generated/vehicles/template_battery.txt:5`；`3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:709`；`3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:715`
[^7]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:970`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:380`
[^8]: `游戏原版/media/scripts/generated/items/normal.txt:12948`；`游戏原版/media/scripts/generated/vehicles/template_engine_door.txt:5`
[^9]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1530`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:598`
[^10]: `游戏原版/media/scripts/generated/items/normal.txt:12857`；`游戏原版/media/scripts/generated/vehicles/template_door.txt:5`；`游戏原版/media/scripts/generated/vehicles/template_door.txt:23`
[^11]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1659`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:649`
[^12]: `游戏原版/media/scripts/generated/items/normal.txt:12734`；`3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:456`；`3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:472`
[^13]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1662`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:652`
[^14]: `游戏原版/media/scripts/generated/items/normal.txt:13025`；`游戏原版/media/scripts/generated/vehicles/template_glovebox.txt:5`
[^15]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1776`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:687`
[^16]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/GridRVArmourItems.txt:84`；`3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:675`
[^17]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:40341`；`3810637496/mods/LaoYuTranslationJava/common/media/lua/shared/Translate/CN/ItemName.json:2`
[^18]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/GridRVXmasItems.txt:158`；`3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:675`
[^19]: `3810637496/mods/LaoYuTranslationJava/common/media/lua/shared/Translate/CN/ItemName.json:3`
[^20]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/GridRVArmourItems.txt:5`；`3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:667`
[^21]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:40336`；`3810637496/mods/LaoYuTranslationJava/common/media/lua/shared/Translate/CN/ItemName.json:4`
[^22]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/GridRVXmasItems.txt:107`；`3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:667`
[^23]: `3810637496/mods/LaoYuTranslationJava/common/media/lua/shared/Translate/CN/ItemName.json:5`
[^24]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/GridRVArmourItems.txt:18`；`3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:658`
[^25]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:40337`；`3810637496/mods/LaoYuTranslationJava/common/media/lua/shared/Translate/CN/ItemName.json:6`
[^26]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/GridRVXmasItems.txt:56`；`3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:658`
[^27]: `3810637496/mods/LaoYuTranslationJava/common/media/lua/shared/Translate/CN/ItemName.json:7`
[^28]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/GridRVArmourItems.txt:232`；`3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:682`
[^29]: `3810637496/mods/LaoYuTranslationJava/common/media/lua/shared/Translate/CN/ItemName.json:9`
[^30]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/GridRVArmourItems.txt:44`；`3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:649`
[^31]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:40991`；`3810637496/mods/LaoYuTranslationJava/common/media/lua/shared/Translate/CN/ItemName.json:10`
[^32]: `3820158673/mods/DeadWorksNomadRV/42/media/scripts/GridRVXmasItems.txt:5`；`3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:649`
[^33]: `3810637496/mods/LaoYuTranslationJava/common/media/lua/shared/Translate/CN/ItemName.json:11`
[^34]: `游戏原版/media/scripts/generated/items/normal.txt:4661`；`游戏原版/media/scripts/generated/vehicles/template_headlight.txt:25`
[^35]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:6727`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25103`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2563`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:965`
[^36]: `游戏原版/media/scripts/generated/items/normal.txt:12163`；`游戏原版/media/scripts/generated/vehicles/template_brake.txt:57`
[^37]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2780`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1050`
[^38]: `游戏原版/media/scripts/generated/items/normal.txt:13166`；`游戏原版/media/scripts/generated/vehicles/template_muffler.txt:5`
[^39]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2783`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1053`
[^40]: `游戏原版/media/scripts/generated/items/normal.txt:12282`；`游戏原版/media/scripts/generated/vehicles/template_suspension.txt:57`
[^41]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2786`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1056`
[^42]: `游戏原版/media/scripts/generated/items/normal.txt:11998`；`3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:81`
[^43]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2789`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1059`
[^44]: `游戏原版/media/scripts/generated/items/normal.txt:12146`；`游戏原版/media/scripts/generated/vehicles/template_brake.txt:57`
[^45]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3219`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1135`
[^46]: `游戏原版/media/scripts/generated/items/normal.txt:13151`；`游戏原版/media/scripts/generated/vehicles/template_muffler.txt:5`
[^47]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3222`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1138`
[^48]: `游戏原版/media/scripts/generated/items/normal.txt:12393`；`3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:85`
[^49]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3228`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1144`
[^50]: `游戏原版/media/scripts/generated/items/normal.txt:12265`；`游戏原版/media/scripts/generated/vehicles/template_suspension.txt:57`
[^51]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3231`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1147`
[^52]: `游戏原版/media/scripts/generated/items/normal.txt:11978`；`3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:81`
[^53]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3234`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1150`
[^54]: `游戏原版/media/scripts/generated/items/normal.txt:12129`；`游戏原版/media/scripts/generated/vehicles/template_brake.txt:57`
[^55]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3255`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1165`
[^56]: `游戏原版/media/scripts/generated/items/normal.txt:13136`；`游戏原版/media/scripts/generated/vehicles/template_muffler.txt:5`
[^57]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3258`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1168`
[^58]: `游戏原版/media/scripts/generated/items/normal.txt:11958`；`3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:81`
[^59]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3262`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1171`
[^60]: `游戏原版/media/scripts/generated/items/radio.txt:308`；`游戏原版/media/scripts/generated/vehicles/template_radio.txt:5`
[^61]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:7374`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25092`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3645`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:5128`
[^62]: `游戏原版/media/scripts/generated/items/radio.txt:335`；`游戏原版/media/scripts/generated/vehicles/template_radio.txt:5`
[^63]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:7375`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25093`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3649`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:5132`
[^64]: `游戏原版/media/scripts/generated/items/radio.txt:361`；`游戏原版/media/scripts/generated/vehicles/template_radio.txt:5`
[^65]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:3001`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25091`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3651`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:5134`
[^66]: `游戏原版/media/scripts/generated/items/normal.txt:12748`；`3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:464`；`3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:480`
[^67]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3674`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1339`
[^68]: `游戏原版/media/scripts/generated/items/normal.txt:12720`；`3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:448`
[^69]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3677`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1342`
[^70]: `游戏原版/media/scripts/generated/items/normal.txt:12378`；`3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:85`
[^71]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:4152`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1543`
[^72]: `游戏原版/media/scripts/generated/items/normal.txt:12987`；`3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:489`；`3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:508`；`3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:528`；`3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:548`；`3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:568`；`3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:587`；`3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:607`；`3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:627`
[^73]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:4626`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1734`
[^74]: `游戏原版/media/scripts/generated/items/normal.txt:12706`；`3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:440`
[^75]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:4892`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1864`
[^76]: `游戏原版/media/scripts/generated/vehicles/template_battery.txt:5`
[^77]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:57`
[^78]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:5`
[^79]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:18`
[^80]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:31`
[^81]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:44`
[^82]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:548`
[^83]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:528`
[^84]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:508`
[^85]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:489`
[^86]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:607`
[^87]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:587`
[^88]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:568`
[^89]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:566`
[^90]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:546`
[^91]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:526`
[^92]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:625`
[^93]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:605`
[^94]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:627`
[^95]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:647`
[^96]: `游戏原版/media/scripts/generated/vehicles/template_sounds_van.txt:14`
[^97]: `游戏原版/media/scripts/generated/vehicles/template_door.txt:5`
[^98]: `游戏原版/media/scripts/generated/vehicles/template_door.txt:23`
[^99]: `游戏原版/media/scripts/generated/vehicles/template_sounds_van.txt:37`
[^100]: `游戏原版/media/scripts/generated/vehicles/template_engine.txt:5`
[^101]: `游戏原版/media/scripts/generated/vehicles/template_engine_door.txt:5`
[^102]: `游戏原版/media/scripts/generated/vehicles/template_sounds_van.txt:56`
[^103]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:725`
[^104]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:739`
[^105]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:750`
[^106]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:93`
[^107]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:97`
[^108]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:133`
[^109]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:137`
[^110]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:141`
[^111]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:145`
[^112]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:149`
[^113]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:153`
[^114]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:157`
[^115]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:161`
[^116]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:165`
[^117]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:169`
[^118]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:101`
[^119]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:173`
[^120]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:177`
[^121]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:181`
[^122]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:185`
[^123]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:189`
[^124]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:193`
[^125]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:197`
[^126]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:201`
[^127]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:205`
[^128]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:209`
[^129]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:105`
[^130]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:213`
[^131]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:217`
[^132]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:221`
[^133]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:225`
[^134]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:229`
[^135]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:233`
[^136]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:237`
[^137]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:241`
[^138]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:245`
[^139]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:249`
[^140]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:109`
[^141]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:253`
[^142]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:257`
[^143]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:261`
[^144]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:265`
[^145]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:269`
[^146]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:273`
[^147]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:277`
[^148]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:281`
[^149]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:285`
[^150]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:289`
[^151]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:113`
[^152]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:293`
[^153]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:297`
[^154]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:301`
[^155]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:305`
[^156]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:309`
[^157]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:313`
[^158]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:317`
[^159]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:321`
[^160]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:325`
[^161]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:329`
[^162]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:117`
[^163]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:333`
[^164]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:337`
[^165]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:341`
[^166]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:345`
[^167]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:349`
[^168]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:353`
[^169]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:357`
[^170]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:361`
[^171]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:365`
[^172]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:369`
[^173]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:121`
[^174]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:373`
[^175]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:377`
[^176]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:125`
[^177]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:129`
[^178]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:760`
[^179]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:405`
[^180]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:406`
[^181]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:415`
[^182]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:416`
[^183]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:417`
[^184]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:418`
[^185]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:419`
[^186]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:420`
[^187]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:421`
[^188]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:422`
[^189]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:423`
[^190]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:424`
[^191]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:407`
[^192]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:425`
[^193]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:426`
[^194]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:427`
[^195]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:428`
[^196]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:408`
[^197]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:409`
[^198]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:410`
[^199]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:411`
[^200]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:412`
[^201]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:413`
[^202]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:414`
[^203]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:709`
[^204]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:715`
[^205]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:381`
[^206]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:382`
[^207]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:391`
[^208]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:392`
[^209]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:393`
[^210]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:394`
[^211]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:395`
[^212]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:396`
[^213]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:397`
[^214]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:398`
[^215]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:399`
[^216]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:400`
[^217]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:383`
[^218]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:401`
[^219]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:402`
[^220]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:403`
[^221]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:404`
[^222]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:384`
[^223]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:385`
[^224]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:386`
[^225]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:387`
[^226]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:388`
[^227]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:389`
[^228]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:390`
[^229]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:96`
[^230]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:100`
[^231]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:136`
[^232]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:140`
[^233]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:144`
[^234]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:148`
[^235]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:152`
[^236]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:156`
[^237]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:160`
[^238]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:164`
[^239]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:168`
[^240]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:172`
[^241]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:104`
[^242]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:176`
[^243]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:180`
[^244]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:184`
[^245]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:188`
[^246]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:192`
[^247]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:196`
[^248]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:200`
[^249]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:204`
[^250]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:208`
[^251]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:212`
[^252]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:108`
[^253]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:216`
[^254]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:220`
[^255]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:224`
[^256]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:228`
[^257]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:232`
[^258]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:236`
[^259]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:240`
[^260]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:244`
[^261]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:248`
[^262]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:252`
[^263]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:112`
[^264]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:256`
[^265]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:260`
[^266]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:264`
[^267]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:268`
[^268]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:272`
[^269]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:276`
[^270]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:280`
[^271]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:284`
[^272]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:288`
[^273]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:292`
[^274]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:116`
[^275]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:296`
[^276]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:300`
[^277]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:304`
[^278]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:308`
[^279]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:312`
[^280]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:316`
[^281]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:320`
[^282]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:324`
[^283]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:328`
[^284]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:332`
[^285]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:120`
[^286]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:336`
[^287]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:340`
[^288]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:344`
[^289]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:348`
[^290]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:352`
[^291]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:356`
[^292]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:360`
[^293]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:364`
[^294]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:368`
[^295]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:372`
[^296]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:124`
[^297]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:376`
[^298]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:380`
[^299]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:128`
[^300]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:132`
[^301]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:759`
[^302]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:85`
[^303]: `游戏原版/media/scripts/generated/vehicles/template_glovebox.txt:5`
[^304]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:25`
[^305]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:721`
[^306]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:723`
[^307]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:724`
[^308]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:722`
[^309]: `游戏原版/media/scripts/generated/vehicles/template_heater.txt:5`
[^310]: `游戏原版/media/scripts/generated/vehicles/template_muffler.txt:5`
[^311]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:761`
[^312]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:649`
[^313]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:675`
[^314]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:667`
[^315]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:658`
[^316]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:682`
[^317]: `游戏原版/media/scripts/generated/vehicles/template_radio.txt:5`
[^318]: `游戏原版/media/scripts/generated/vehicles/template_seat.txt:5`
[^319]: `游戏原版/media/scripts/generated/vehicles/template_seat.txt:14`
[^320]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:66`
[^321]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:67`
[^322]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:57`
[^323]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:5`
[^324]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:18`
[^325]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:31`
[^326]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:44`
[^327]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:81`
[^328]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:82`
[^329]: `游戏原版/media/scripts/generated/vehicles/template_tire.txt:15`
[^330]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:83`
[^331]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:84`
[^332]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:456`
[^333]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:472`
[^334]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:464`
[^335]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:480`
[^336]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:440`
[^337]: `3820158673/mods/DeadWorksDaleRV/42/media/scripts/vehicles/DaleChieftainRV.txt:448`
