# 3D 厢式房车（Viewpoint - 3D RV Van）

提供带车内空间的厢式房车，可在后厢放置家具；内饰画在车模型内部，需要 Viewpoint 与模型库。

归属：**日常组合（玩法待验收）**；档案视图 `b422-compat`。
当前版本定义：**整车 1、本地物品定义 0、配方 0**；另引用共享物品 23。本地定义数含内部保留项，见独立列表；整车定义包括覆盖原版的条目，不等于新增车型数。

## 如何查找

- **生成整车**：在生成车辆菜单搜索下表完整 ID；显示译名时搜索中文列。联机管理命令用 `/addvehicle 完整ID`。
- **添加到背包**：普通物品、维修件、改装件都在添加物品菜单使用完整物品 ID；不要拿配方或内部槽位去刷车。
- **制作配方**：在制作界面查译名；配方 ID 用于排查，不是可放进背包的物品。
- 中文解释说明用途；只有翻译文件中找到的文字才称为游戏中文名。缺译保留脚本显示名，冲突列出各译文。

## 整车

| 完整生成车辆 ID | 当前中文名 / 名称状态 | 英文名或脚本名 | 变体说明 | 来源 |
| --- | --- | --- | --- | --- |
| `Base.VansCourierDuo` | Courier Duo 厢式货车[^1] | Courier Duo[^2] | 脚本座位数 4；机修类型 2；具体外观与性能待游戏实刷 | [^3] |

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
| `Base.BigGasTank2` | 油箱 (大型)（翻译文件含非标准语法，待游戏核实）[^5] | 车辆安装件，用于油箱（GasTank）；适用车型见右列 / 维修配件 | 添加物品 | Base.VansCourierDuo → GasTank | 游戏原版[^4] |
| `Base.CarBattery2` | 汽车电池（翻译文件含非标准语法，待游戏核实）[^7] | 车辆安装件，用于蓄电池（Battery）、蓄电池（GRHouseBattery1）、蓄电池（GRHouseBattery2）；适用车型见右列 / 维修配件 | 添加物品 | Base.VansCourierDuo → Battery | 游戏原版[^6] |
| `Base.EngineDoor2` | 引擎罩（翻译文件含非标准语法，待游戏核实）[^9] | 车辆安装件，用于引擎盖（EngineDoor）；适用车型见右列 / 维修配件 | 添加物品 | Base.VansCourierDuo → EngineDoor | 游戏原版[^8] |
| `Base.FrontCarDoor2` | 车前门（翻译文件含非标准语法，待游戏核实）[^11] | 车辆安装件，用于车门（DoorFrontLeft）、车门（DoorFrontRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.VansCourierDuo → DoorFrontLeft；Base.VansCourierDuo → DoorFrontRight | 游戏原版[^10] |
| `Base.GloveBox2` | 手套箱（翻译文件含非标准语法，待游戏核实）[^13] | 车辆安装件，用于车辆安装位（GloveBox）；适用车型见右列 / 维修配件 | 添加物品 | Base.VansCourierDuo → GloveBox | 游戏原版[^12] |
| `Base.LightBulb` | 灯泡-白色 / 灯泡 (白)（译文冲突，待游戏核实）[^15] | 车辆安装件，用于车灯（Headlight*）、车灯（JP82DorothyLights）；适用车型见右列 / 维修配件 | 添加物品 | Base.VansCourierDuo → Headlight* | 游戏原版[^14] |
| `Base.ModernBrake2` | 制动器 (高级)（翻译文件含非标准语法，待游戏核实）[^17] | 车辆安装件，用于制动器（Brake*）；适用车型见右列 / 维修配件 | 添加物品 | Base.VansCourierDuo → Brake* | 游戏原版[^16] |
| `Base.ModernCarMuffler2` | 消声器 (高级)（翻译文件含非标准语法，待游戏核实）[^19] | 车辆安装件，用于消声器（Muffler）；适用车型见右列 / 维修配件 | 添加物品 | Base.VansCourierDuo → Muffler | 游戏原版[^18] |
| `Base.ModernSuspension2` | 悬挂 (高级)（翻译文件含非标准语法，待游戏核实）[^21] | 车辆安装件，用于悬挂（Suspension*）；适用车型见右列 / 维修配件 | 添加物品 | Base.VansCourierDuo → Suspension* | 游戏原版[^20] |
| `Base.ModernTire2` | 轮胎 (高级)（翻译文件含非标准语法，待游戏核实）[^23] | 车辆安装件，用于轮胎（Tire*）；适用车型见右列 / 维修配件 | 添加物品 | Base.VansCourierDuo → Tire* | 游戏原版[^22] |
| `Base.NormalBrake2` | 制动器 (普通)（翻译文件含非标准语法，待游戏核实）[^25] | 车辆安装件，用于制动器（Brake*）；适用车型见右列 / 维修配件 | 添加物品 | Base.VansCourierDuo → Brake* | 游戏原版[^24] |
| `Base.NormalCarMuffler2` | 消声器 (普通)（翻译文件含非标准语法，待游戏核实）[^27] | 车辆安装件，用于消声器（Muffler）；适用车型见右列 / 维修配件 | 添加物品 | Base.VansCourierDuo → Muffler | 游戏原版[^26] |
| `Base.NormalCarSeat2` | 座椅 (标准)（翻译文件含非标准语法，待游戏核实）[^29] | 车辆安装件，用于座椅（Seat*）；适用车型见右列 / 维修配件 | 添加物品 | Base.VansCourierDuo → Seat* | 游戏原版[^28] |
| `Base.NormalGasTank2` | 油箱 (标准)（翻译文件含非标准语法，待游戏核实）[^31] | 车辆安装件，用于油箱（GasTank）；适用车型见右列 / 维修配件 | 添加物品 | Base.VansCourierDuo → GasTank | 游戏原版[^30] |
| `Base.NormalSuspension2` | 悬挂 (普通)（翻译文件含非标准语法，待游戏核实）[^33] | 车辆安装件，用于悬挂（Suspension*）；适用车型见右列 / 维修配件 | 添加物品 | Base.VansCourierDuo → Suspension* | 游戏原版[^32] |
| `Base.NormalTire2` | 轮胎 (普通)（翻译文件含非标准语法，待游戏核实）[^35] | 车辆安装件，用于轮胎（Tire*）；适用车型见右列 / 维修配件 | 添加物品 | Base.VansCourierDuo → Tire* | 游戏原版[^34] |
| `Base.OldBrake2` | 制动器 (老式)（翻译文件含非标准语法，待游戏核实）[^37] | 车辆安装件，用于制动器（Brake*）；适用车型见右列 / 维修配件 | 添加物品 | Base.VansCourierDuo → Brake* | 游戏原版[^36] |
| `Base.OldCarMuffler2` | 消声器 (老式)（翻译文件含非标准语法，待游戏核实）[^39] | 车辆安装件，用于消声器（Muffler）；适用车型见右列 / 维修配件 | 添加物品 | Base.VansCourierDuo → Muffler | 游戏原版[^38] |
| `Base.OldTire2` | 轮胎 (廉价)（翻译文件含非标准语法，待游戏核实）[^41] | 车辆安装件，用于轮胎（TireFrontLeft）、轮胎（TireFrontRight）、轮胎（Tire*）、轮胎（TireRearLeft）、轮胎（TireRearRight）；适用车型见右列 / 维修配件 | 添加物品 | Base.VansCourierDuo → Tire* | 游戏原版[^40] |
| `Base.RadioBlack` | 收音机 (超值科技) / 收音机 (廉科) / 廉科牌收音机（译文冲突，待游戏核实）[^43] | 车辆安装件，用于车辆安装位（Radio）；适用车型见右列 / 维修配件 | 添加物品 | Base.VansCourierDuo → Radio | 游戏原版[^42] |
| `Base.RadioMakeShift` | 收音机 (简易) / 自制收音机（译文冲突，待游戏核实）[^45] | 车辆安装件，用于车辆安装位（Radio）；适用车型见右列 / 维修配件 | 添加物品 | Base.VansCourierDuo → Radio | 游戏原版[^44] |
| `Base.RadioRed` | 导航仪 / 收音机 (昂科) / 昂科牌收音机（译文冲突，待游戏核实）[^47] | 车辆安装件，用于车辆安装位（Radio）；适用车型见右列 / 维修配件 | 添加物品 | Base.VansCourierDuo → Radio | 游戏原版[^46] |
| `Base.SmallGasTank2` | 油箱 (小型)（翻译文件含非标准语法，待游戏核实）[^49] | 车辆安装件，用于油箱（GasTank）；适用车型见右列 / 维修配件 | 添加物品 | Base.VansCourierDuo → GasTank | 游戏原版[^48] |

## 制作配方

无当前有效的脚本制作配方。Lua 动态添加的内容不在本次静态统计内。

## 内部定义、历史分支与未解析引用

有效资源层：42；仅合并 common 与所选版本，Overlay 按相对路径覆盖。
车辆模板 0 个、内部槽位 234 个，均不算整车或背包物品。旧根目录和未选中版本的定义不列入当前可用表。模板中短物品引用若追加机修类型后缀才匹配定义，属于静态映射，安装仍待实测。

<details><summary>查看内部槽位（不能直接刷取）</summary>

| 槽位 | 名称或说明 | 来源 |
| --- | --- | --- |
| `Battery` | 电池 / 蓄电池 | [^50] |
| `Brake*` | Brake* / 制动器 | [^51] |
| `BrakeFrontLeft` | 左前制动 / 制动器 | [^52] |
| `BrakeFrontRight` | 右前制动 / 制动器 | [^53] |
| `BrakeRearLeft` | 左后制动 / 制动器 | [^54] |
| `BrakeRearRight` | 右后制动 / 制动器 | [^55] |
| `Door*` | Door* / 车门 | [^56] |
| `DoorFrontLeft` | 左前门 / 车门 | [^57] |
| `DoorFrontRight` | 右前门 / 车门 | [^58] |
| `DoorRear*` | DoorRear* / 车门 | [^59] |
| `Engine` | 引擎 / 发动机 | [^60] |
| `EngineDoor` | 引擎盖 / 引擎盖 | [^61] |
| `EngineDoor*` | EngineDoor* / 引擎盖 | [^62] |
| `GRCargoRadio` | GRCargoRadio / 车辆安装位 | [^63] |
| `GRCell0` | GRCell0 / 车辆安装位 | [^64] |
| `GRCell1` | GRCell1 / 车辆安装位 | [^65] |
| `GRCell10` | GRCell10 / 车辆安装位 | [^66] |
| `GRCell11` | GRCell11 / 车辆安装位 | [^67] |
| `GRCell12` | GRCell12 / 车辆安装位 | [^68] |
| `GRCell13` | GRCell13 / 车辆安装位 | [^69] |
| `GRCell14` | GRCell14 / 车辆安装位 | [^70] |
| `GRCell15` | GRCell15 / 车辆安装位 | [^71] |
| `GRCell16` | GRCell16 / 车辆安装位 | [^72] |
| `GRCell17` | GRCell17 / 车辆安装位 | [^73] |
| `GRCell18` | GRCell18 / 车辆安装位 | [^74] |
| `GRCell19` | GRCell19 / 车辆安装位 | [^75] |
| `GRCell2` | GRCell2 / 车辆安装位 | [^76] |
| `GRCell20` | GRCell20 / 车辆安装位 | [^77] |
| `GRCell21` | GRCell21 / 车辆安装位 | [^78] |
| `GRCell22` | GRCell22 / 车辆安装位 | [^79] |
| `GRCell23` | GRCell23 / 车辆安装位 | [^80] |
| `GRCell24` | GRCell24 / 车辆安装位 | [^81] |
| `GRCell25` | GRCell25 / 车辆安装位 | [^82] |
| `GRCell26` | GRCell26 / 车辆安装位 | [^83] |
| `GRCell27` | GRCell27 / 车辆安装位 | [^84] |
| `GRCell28` | GRCell28 / 车辆安装位 | [^85] |
| `GRCell29` | GRCell29 / 车辆安装位 | [^86] |
| `GRCell3` | GRCell3 / 车辆安装位 | [^87] |
| `GRCell30` | GRCell30 / 车辆安装位 | [^88] |
| `GRCell31` | GRCell31 / 车辆安装位 | [^89] |
| `GRCell32` | GRCell32 / 车辆安装位 | [^90] |
| `GRCell33` | GRCell33 / 车辆安装位 | [^91] |
| `GRCell34` | GRCell34 / 车辆安装位 | [^92] |
| `GRCell35` | GRCell35 / 车辆安装位 | [^93] |
| `GRCell36` | GRCell36 / 车辆安装位 | [^94] |
| `GRCell37` | GRCell37 / 车辆安装位 | [^95] |
| `GRCell38` | GRCell38 / 车辆安装位 | [^96] |
| `GRCell39` | GRCell39 / 车辆安装位 | [^97] |
| `GRCell4` | GRCell4 / 车辆安装位 | [^98] |
| `GRCell40` | GRCell40 / 车辆安装位 | [^99] |
| `GRCell41` | GRCell41 / 车辆安装位 | [^100] |
| `GRCell42` | GRCell42 / 车辆安装位 | [^101] |
| `GRCell43` | GRCell43 / 车辆安装位 | [^102] |
| `GRCell44` | GRCell44 / 车辆安装位 | [^103] |
| `GRCell45` | GRCell45 / 车辆安装位 | [^104] |
| `GRCell46` | GRCell46 / 车辆安装位 | [^105] |
| `GRCell47` | GRCell47 / 车辆安装位 | [^106] |
| `GRCell48` | GRCell48 / 车辆安装位 | [^107] |
| `GRCell49` | GRCell49 / 车辆安装位 | [^108] |
| `GRCell5` | GRCell5 / 车辆安装位 | [^109] |
| `GRCell50` | GRCell50 / 车辆安装位 | [^110] |
| `GRCell51` | GRCell51 / 车辆安装位 | [^111] |
| `GRCell52` | GRCell52 / 车辆安装位 | [^112] |
| `GRCell53` | GRCell53 / 车辆安装位 | [^113] |
| `GRCell54` | GRCell54 / 车辆安装位 | [^114] |
| `GRCell55` | GRCell55 / 车辆安装位 | [^115] |
| `GRCell56` | GRCell56 / 车辆安装位 | [^116] |
| `GRCell57` | GRCell57 / 车辆安装位 | [^117] |
| `GRCell58` | GRCell58 / 车辆安装位 | [^118] |
| `GRCell59` | GRCell59 / 车辆安装位 | [^119] |
| `GRCell6` | GRCell6 / 车辆安装位 | [^120] |
| `GRCell60` | GRCell60 / 车辆安装位 | [^121] |
| `GRCell61` | GRCell61 / 车辆安装位 | [^122] |
| `GRCell62` | GRCell62 / 车辆安装位 | [^123] |
| `GRCell63` | GRCell63 / 车辆安装位 | [^124] |
| `GRCell64` | GRCell64 / 车辆安装位 | [^125] |
| `GRCell65` | GRCell65 / 车辆安装位 | [^126] |
| `GRCell66` | GRCell66 / 车辆安装位 | [^127] |
| `GRCell67` | GRCell67 / 车辆安装位 | [^128] |
| `GRCell68` | GRCell68 / 车辆安装位 | [^129] |
| `GRCell69` | GRCell69 / 车辆安装位 | [^130] |
| `GRCell7` | GRCell7 / 车辆安装位 | [^131] |
| `GRCell70` | GRCell70 / 车辆安装位 | [^132] |
| `GRCell71` | GRCell71 / 车辆安装位 | [^133] |
| `GRCell8` | GRCell8 / 车辆安装位 | [^134] |
| `GRCell9` | GRCell9 / 车辆安装位 | [^135] |
| `GRCourierRearRight` | GRCourierRearRight / 车辆安装位 | [^136] |
| `GRFreezer0` | GRFreezer0 / 车辆安装位 | [^137] |
| `GRFreezer1` | GRFreezer1 / 车辆安装位 | [^138] |
| `GRFreezer10` | GRFreezer10 / 车辆安装位 | [^139] |
| `GRFreezer11` | GRFreezer11 / 车辆安装位 | [^140] |
| `GRFreezer12` | GRFreezer12 / 车辆安装位 | [^141] |
| `GRFreezer13` | GRFreezer13 / 车辆安装位 | [^142] |
| `GRFreezer14` | GRFreezer14 / 车辆安装位 | [^143] |
| `GRFreezer15` | GRFreezer15 / 车辆安装位 | [^144] |
| `GRFreezer16` | GRFreezer16 / 车辆安装位 | [^145] |
| `GRFreezer17` | GRFreezer17 / 车辆安装位 | [^146] |
| `GRFreezer18` | GRFreezer18 / 车辆安装位 | [^147] |
| `GRFreezer19` | GRFreezer19 / 车辆安装位 | [^148] |
| `GRFreezer2` | GRFreezer2 / 车辆安装位 | [^149] |
| `GRFreezer20` | GRFreezer20 / 车辆安装位 | [^150] |
| `GRFreezer21` | GRFreezer21 / 车辆安装位 | [^151] |
| `GRFreezer22` | GRFreezer22 / 车辆安装位 | [^152] |
| `GRFreezer23` | GRFreezer23 / 车辆安装位 | [^153] |
| `GRFreezer3` | GRFreezer3 / 车辆安装位 | [^154] |
| `GRFreezer4` | GRFreezer4 / 车辆安装位 | [^155] |
| `GRFreezer5` | GRFreezer5 / 车辆安装位 | [^156] |
| `GRFreezer6` | GRFreezer6 / 车辆安装位 | [^157] |
| `GRFreezer7` | GRFreezer7 / 车辆安装位 | [^158] |
| `GRFreezer8` | GRFreezer8 / 车辆安装位 | [^159] |
| `GRFreezer9` | GRFreezer9 / 车辆安装位 | [^160] |
| `GRLoose0` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^161] |
| `GRLoose1` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^162] |
| `GRLoose10` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^163] |
| `GRLoose11` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^164] |
| `GRLoose12` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^165] |
| `GRLoose13` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^166] |
| `GRLoose14` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^167] |
| `GRLoose15` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^168] |
| `GRLoose16` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^169] |
| `GRLoose17` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^170] |
| `GRLoose18` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^171] |
| `GRLoose19` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^172] |
| `GRLoose2` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^173] |
| `GRLoose20` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^174] |
| `GRLoose21` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^175] |
| `GRLoose22` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^176] |
| `GRLoose23` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^177] |
| `GRLoose3` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^178] |
| `GRLoose4` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^179] |
| `GRLoose5` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^180] |
| `GRLoose6` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^181] |
| `GRLoose7` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^182] |
| `GRLoose8` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^183] |
| `GRLoose9` | 房车地板 / 摆放物品 / 房车地面／放置物品 / 车辆安装位 | [^184] |
| `GRPacked0` | GRPacked0 / 车辆安装位 | [^185] |
| `GRPacked1` | GRPacked1 / 车辆安装位 | [^186] |
| `GRPacked10` | GRPacked10 / 车辆安装位 | [^187] |
| `GRPacked11` | GRPacked11 / 车辆安装位 | [^188] |
| `GRPacked12` | GRPacked12 / 车辆安装位 | [^189] |
| `GRPacked13` | GRPacked13 / 车辆安装位 | [^190] |
| `GRPacked14` | GRPacked14 / 车辆安装位 | [^191] |
| `GRPacked15` | GRPacked15 / 车辆安装位 | [^192] |
| `GRPacked16` | GRPacked16 / 车辆安装位 | [^193] |
| `GRPacked17` | GRPacked17 / 车辆安装位 | [^194] |
| `GRPacked18` | GRPacked18 / 车辆安装位 | [^195] |
| `GRPacked19` | GRPacked19 / 车辆安装位 | [^196] |
| `GRPacked2` | GRPacked2 / 车辆安装位 | [^197] |
| `GRPacked20` | GRPacked20 / 车辆安装位 | [^198] |
| `GRPacked21` | GRPacked21 / 车辆安装位 | [^199] |
| `GRPacked22` | GRPacked22 / 车辆安装位 | [^200] |
| `GRPacked23` | GRPacked23 / 车辆安装位 | [^201] |
| `GRPacked24` | GRPacked24 / 车辆安装位 | [^202] |
| `GRPacked25` | GRPacked25 / 车辆安装位 | [^203] |
| `GRPacked26` | GRPacked26 / 车辆安装位 | [^204] |
| `GRPacked27` | GRPacked27 / 车辆安装位 | [^205] |
| `GRPacked28` | GRPacked28 / 车辆安装位 | [^206] |
| `GRPacked29` | GRPacked29 / 车辆安装位 | [^207] |
| `GRPacked3` | GRPacked3 / 车辆安装位 | [^208] |
| `GRPacked30` | GRPacked30 / 车辆安装位 | [^209] |
| `GRPacked31` | GRPacked31 / 车辆安装位 | [^210] |
| `GRPacked32` | GRPacked32 / 车辆安装位 | [^211] |
| `GRPacked33` | GRPacked33 / 车辆安装位 | [^212] |
| `GRPacked34` | GRPacked34 / 车辆安装位 | [^213] |
| `GRPacked35` | GRPacked35 / 车辆安装位 | [^214] |
| `GRPacked36` | GRPacked36 / 车辆安装位 | [^215] |
| `GRPacked37` | GRPacked37 / 车辆安装位 | [^216] |
| `GRPacked38` | GRPacked38 / 车辆安装位 | [^217] |
| `GRPacked39` | GRPacked39 / 车辆安装位 | [^218] |
| `GRPacked4` | GRPacked4 / 车辆安装位 | [^219] |
| `GRPacked40` | GRPacked40 / 车辆安装位 | [^220] |
| `GRPacked41` | GRPacked41 / 车辆安装位 | [^221] |
| `GRPacked42` | GRPacked42 / 车辆安装位 | [^222] |
| `GRPacked43` | GRPacked43 / 车辆安装位 | [^223] |
| `GRPacked44` | GRPacked44 / 车辆安装位 | [^224] |
| `GRPacked45` | GRPacked45 / 车辆安装位 | [^225] |
| `GRPacked46` | GRPacked46 / 车辆安装位 | [^226] |
| `GRPacked47` | GRPacked47 / 车辆安装位 | [^227] |
| `GRPacked48` | GRPacked48 / 车辆安装位 | [^228] |
| `GRPacked49` | GRPacked49 / 车辆安装位 | [^229] |
| `GRPacked5` | GRPacked5 / 车辆安装位 | [^230] |
| `GRPacked50` | GRPacked50 / 车辆安装位 | [^231] |
| `GRPacked51` | GRPacked51 / 车辆安装位 | [^232] |
| `GRPacked52` | GRPacked52 / 车辆安装位 | [^233] |
| `GRPacked53` | GRPacked53 / 车辆安装位 | [^234] |
| `GRPacked54` | GRPacked54 / 车辆安装位 | [^235] |
| `GRPacked55` | GRPacked55 / 车辆安装位 | [^236] |
| `GRPacked56` | GRPacked56 / 车辆安装位 | [^237] |
| `GRPacked57` | GRPacked57 / 车辆安装位 | [^238] |
| `GRPacked58` | GRPacked58 / 车辆安装位 | [^239] |
| `GRPacked59` | GRPacked59 / 车辆安装位 | [^240] |
| `GRPacked6` | GRPacked6 / 车辆安装位 | [^241] |
| `GRPacked60` | GRPacked60 / 车辆安装位 | [^242] |
| `GRPacked61` | GRPacked61 / 车辆安装位 | [^243] |
| `GRPacked62` | GRPacked62 / 车辆安装位 | [^244] |
| `GRPacked63` | GRPacked63 / 车辆安装位 | [^245] |
| `GRPacked64` | GRPacked64 / 车辆安装位 | [^246] |
| `GRPacked65` | GRPacked65 / 车辆安装位 | [^247] |
| `GRPacked66` | GRPacked66 / 车辆安装位 | [^248] |
| `GRPacked67` | GRPacked67 / 车辆安装位 | [^249] |
| `GRPacked68` | GRPacked68 / 车辆安装位 | [^250] |
| `GRPacked69` | GRPacked69 / 车辆安装位 | [^251] |
| `GRPacked7` | GRPacked7 / 车辆安装位 | [^252] |
| `GRPacked70` | GRPacked70 / 车辆安装位 | [^253] |
| `GRPacked71` | GRPacked71 / 车辆安装位 | [^254] |
| `GRPacked8` | GRPacked8 / 车辆安装位 | [^255] |
| `GRPacked9` | GRPacked9 / 车辆安装位 | [^256] |
| `GRRooms` | GRRooms / 车辆安装位 | [^257] |
| `GVCourierRearLeft` | GVCourierRearLeft / 车辆安装位 | [^258] |
| `GasTank` | 油箱 / 油箱 | [^259] |
| `GloveBox` | 手套箱 / 车辆安装位 | [^260] |
| `Headlight*` | Headlight* / 车灯 | [^261] |
| `HeadlightLeft` | 左大灯 / 车灯 | [^262] |
| `HeadlightRearLeft` | 左尾灯 / 车灯 | [^263] |
| `HeadlightRearRight` | 右尾灯 / 车灯 | [^264] |
| `HeadlightRight` | 右大灯 / 车灯 | [^265] |
| `Heater` | 加热器 / 车辆安装位 | [^266] |
| `Muffler` | 排气消声器 / 消声器 | [^267] |
| `Radio` | 电台 / 车辆安装位 | [^268] |
| `Seat*` | Seat* / 座椅 | [^269] |
| `SeatFrontLeft` | 驾驶座 / 座椅 | [^270] |
| `SeatFrontRight` | 右前座 / 座椅 | [^271] |
| `SeatRearLeft` | 左后座 / 座椅 | [^272] |
| `SeatRearRight` | 右后座 / 座椅 | [^273] |
| `Suspension*` | Suspension* / 悬挂 | [^274] |
| `SuspensionFrontLeft` | 左前悬挂 / 悬挂 | [^275] |
| `SuspensionFrontRight` | 右前悬挂 / 悬挂 | [^276] |
| `SuspensionRearLeft` | 左后悬挂 / 悬挂 | [^277] |
| `SuspensionRearRight` | 右后悬挂 / 悬挂 | [^278] |
| `Tire*` | Tire* / 轮胎 | [^279] |
| `TireFrontLeft` | 左前胎 / 轮胎 | [^280] |
| `TireFrontRight` | 右前胎 / 轮胎 | [^281] |
| `TireRearLeft` | 左后胎 / 轮胎 | [^282] |
| `TireRearRight` | 右后胎 / 轮胎 | [^283] |

</details>


## 概览

| Mod ID / 文件夹 | 分发端 | 版本 | 选择的 mod.info | 原件范围 → 当前范围 |
| --- | --- | --- | --- | --- |
| `GridVans` / `GridVans` | both（双端） | 0.1.8 | `42/mod.info` | 42.21 … 42.21 → 42.21 … 42.22（Overlay） |

原件体积 54.4 MB；体积按完整目录统计，与当前内容定义数分开。
工作坊：[查看作者页面](https://steamcommunity.com/sharedfiles/filedetails/?id=3821174725)。

## 证据与使用边界

**verified：有效源码静态确认。** 每个当前可复制 ID 均来自所选版本的定义；这不保证游戏已成功注册、生成、安装或联机同步。
挑战者 5 个车辆中文名另有 Owner 截图确认；本轮没有启动游戏。译文冲突、动态 Lua 内容和玩法效果仍需 Owner 游戏内核实。
以下人工记录保留原始语境；其中旧组合、旧数量和旧候选状态仅供追溯，当前统计与归属以上表和 profile 为准。

<!-- retained:start -->
## 依赖与冲突

- 需要：`ZombieBuddy, Viewpoint, GridVansHost, PZVoxelStudioViewpoint`
- 互斥：无
- 被依赖：无（叶子节点）

## 双端与联机

双端候选；依赖 GridVansHost、PZVoxelStudioViewpoint、Viewpoint 与 ZombieBuddy，不能单独启用。

当前 profile：both（双端）。

本机文件构成：客户端有 lua；服务端无 lua（只挂载）。

## 实测与排查

原件 0.1.8，42.21 上限；仅元数据 Overlay。上下车、行走、家具、水电与保存重进均待验证。

**planned：仅完成依赖、版本与补丁指纹静态检查。** 迁移收尾按 Owner 要求不启动游戏；本候选组合未验证加载、联网、存档或视觉。

版本放行补丁：`A004/workspace/patches/mods/GridVans/42/mod.info`。原件更新后须重新核对指纹；撤除此补丁后运行 check 会恢复原件版本限制。

```
cd A004
python lab.py check --profile b422-compat
grep -a 'GridVans' runs/<trial>/*console.log
```
<!-- retained:end -->

## 静态来源

路径相对 `A004/workspace/mods_library/`；`Overlay/<文件夹>/` 指 `A004/workspace/patches/mods/<文件夹>/`，`游戏原版/` 指当前 B42.22 客户端 Game 目录。翻译来源列出所有候选，未按加载顺序擅自消解异文。

[^1]: `3810637496/mods/LaoYuTranslationJava/common/media/lua/shared/Translate/CN/IG_UI.json:189`
[^2]: `3821174725/mods/GridVans/42/media/lua/shared/Translate/EN/IG_UI.json:2`；`3821174725/mods/GridVans/42/media/lua/shared/Translate/EN/IG_UI_EN.txt:1`
[^3]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:2`
[^4]: `游戏原版/media/scripts/generated/items/normal.txt:12408`；`3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:77`
[^5]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:448`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:163`
[^6]: `游戏原版/media/scripts/generated/items/drainable.txt:2368`；`游戏原版/media/scripts/generated/vehicles/template_battery.txt:5`
[^7]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:970`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:380`
[^8]: `游戏原版/media/scripts/generated/items/normal.txt:12948`；`游戏原版/media/scripts/generated/vehicles/template_engine_door.txt:5`
[^9]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1530`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:598`
[^10]: `游戏原版/media/scripts/generated/items/normal.txt:12857`；`3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:284`；`3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:285`
[^11]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1659`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:649`
[^12]: `游戏原版/media/scripts/generated/items/normal.txt:13025`；`游戏原版/media/scripts/generated/vehicles/template_glovebox.txt:5`
[^13]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1776`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:687`
[^14]: `游戏原版/media/scripts/generated/items/normal.txt:4661`；`游戏原版/media/scripts/generated/vehicles/template_headlight.txt:25`
[^15]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:6727`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25103`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2563`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:965`
[^16]: `游戏原版/media/scripts/generated/items/normal.txt:12163`；`游戏原版/media/scripts/generated/vehicles/template_brake.txt:57`
[^17]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2780`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1050`
[^18]: `游戏原版/media/scripts/generated/items/normal.txt:13166`；`游戏原版/media/scripts/generated/vehicles/template_muffler.txt:5`
[^19]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2783`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1053`
[^20]: `游戏原版/media/scripts/generated/items/normal.txt:12282`；`游戏原版/media/scripts/generated/vehicles/template_suspension.txt:57`
[^21]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2786`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1056`
[^22]: `游戏原版/media/scripts/generated/items/normal.txt:11998`；`游戏原版/media/scripts/generated/vehicles/template_tire.txt:45`
[^23]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2789`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1059`
[^24]: `游戏原版/media/scripts/generated/items/normal.txt:12146`；`游戏原版/media/scripts/generated/vehicles/template_brake.txt:57`
[^25]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3219`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1135`
[^26]: `游戏原版/media/scripts/generated/items/normal.txt:13151`；`游戏原版/media/scripts/generated/vehicles/template_muffler.txt:5`
[^27]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3222`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1138`
[^28]: `游戏原版/media/scripts/generated/items/normal.txt:13063`；`游戏原版/media/scripts/generated/vehicles/template_seat.txt:59`
[^29]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3225`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1141`
[^30]: `游戏原版/media/scripts/generated/items/normal.txt:12393`；`3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:77`
[^31]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3228`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1144`
[^32]: `游戏原版/media/scripts/generated/items/normal.txt:12265`；`游戏原版/media/scripts/generated/vehicles/template_suspension.txt:57`
[^33]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3231`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1147`
[^34]: `游戏原版/media/scripts/generated/items/normal.txt:11978`；`游戏原版/media/scripts/generated/vehicles/template_tire.txt:45`
[^35]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3234`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1150`
[^36]: `游戏原版/media/scripts/generated/items/normal.txt:12129`；`游戏原版/media/scripts/generated/vehicles/template_brake.txt:57`
[^37]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3255`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1165`
[^38]: `游戏原版/media/scripts/generated/items/normal.txt:13136`；`游戏原版/media/scripts/generated/vehicles/template_muffler.txt:5`
[^39]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3258`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1168`
[^40]: `游戏原版/media/scripts/generated/items/normal.txt:11958`；`游戏原版/media/scripts/generated/vehicles/template_tire.txt:45`
[^41]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3262`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1171`
[^42]: `游戏原版/media/scripts/generated/items/radio.txt:308`；`游戏原版/media/scripts/generated/vehicles/template_radio.txt:5`
[^43]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:7374`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25092`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3645`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:5128`
[^44]: `游戏原版/media/scripts/generated/items/radio.txt:335`；`游戏原版/media/scripts/generated/vehicles/template_radio.txt:5`
[^45]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:7375`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25093`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3649`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:5132`
[^46]: `游戏原版/media/scripts/generated/items/radio.txt:361`；`游戏原版/media/scripts/generated/vehicles/template_radio.txt:5`
[^47]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:3001`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25091`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3651`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:5134`
[^48]: `游戏原版/media/scripts/generated/items/normal.txt:12378`；`3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:77`
[^49]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:4152`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1543`
[^50]: `游戏原版/media/scripts/generated/vehicles/template_battery.txt:5`
[^51]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:57`
[^52]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:5`
[^53]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:18`
[^54]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:31`
[^55]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:44`
[^56]: `游戏原版/media/scripts/generated/vehicles/template_sounds_van.txt:14`
[^57]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:284`
[^58]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:285`
[^59]: `游戏原版/media/scripts/generated/vehicles/template_sounds_van.txt:37`
[^60]: `游戏原版/media/scripts/generated/vehicles/template_engine.txt:5`
[^61]: `游戏原版/media/scripts/generated/vehicles/template_engine_door.txt:5`
[^62]: `游戏原版/media/scripts/generated/vehicles/template_sounds_van.txt:56`
[^63]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:89`
[^64]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:90`
[^65]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:92`
[^66]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:110`
[^67]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:112`
[^68]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:114`
[^69]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:116`
[^70]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:118`
[^71]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:120`
[^72]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:122`
[^73]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:124`
[^74]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:126`
[^75]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:128`
[^76]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:94`
[^77]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:130`
[^78]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:132`
[^79]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:134`
[^80]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:136`
[^81]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:138`
[^82]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:140`
[^83]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:142`
[^84]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:144`
[^85]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:146`
[^86]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:148`
[^87]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:96`
[^88]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:150`
[^89]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:152`
[^90]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:154`
[^91]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:156`
[^92]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:158`
[^93]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:160`
[^94]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:162`
[^95]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:164`
[^96]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:166`
[^97]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:168`
[^98]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:98`
[^99]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:170`
[^100]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:172`
[^101]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:174`
[^102]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:176`
[^103]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:178`
[^104]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:180`
[^105]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:182`
[^106]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:184`
[^107]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:186`
[^108]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:188`
[^109]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:100`
[^110]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:190`
[^111]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:192`
[^112]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:194`
[^113]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:196`
[^114]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:198`
[^115]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:200`
[^116]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:202`
[^117]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:204`
[^118]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:206`
[^119]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:208`
[^120]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:102`
[^121]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:210`
[^122]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:212`
[^123]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:214`
[^124]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:216`
[^125]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:218`
[^126]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:220`
[^127]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:222`
[^128]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:224`
[^129]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:226`
[^130]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:228`
[^131]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:104`
[^132]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:230`
[^133]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:232`
[^134]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:106`
[^135]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:108`
[^136]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:283`
[^137]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:258`
[^138]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:259`
[^139]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:268`
[^140]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:269`
[^141]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:270`
[^142]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:271`
[^143]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:272`
[^144]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:273`
[^145]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:274`
[^146]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:275`
[^147]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:276`
[^148]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:277`
[^149]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:260`
[^150]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:278`
[^151]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:279`
[^152]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:280`
[^153]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:281`
[^154]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:261`
[^155]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:262`
[^156]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:263`
[^157]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:264`
[^158]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:265`
[^159]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:266`
[^160]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:267`
[^161]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:234`
[^162]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:235`
[^163]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:244`
[^164]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:245`
[^165]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:246`
[^166]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:247`
[^167]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:248`
[^168]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:249`
[^169]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:250`
[^170]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:251`
[^171]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:252`
[^172]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:253`
[^173]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:236`
[^174]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:254`
[^175]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:255`
[^176]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:256`
[^177]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:257`
[^178]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:237`
[^179]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:238`
[^180]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:239`
[^181]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:240`
[^182]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:241`
[^183]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:242`
[^184]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:243`
[^185]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:91`
[^186]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:93`
[^187]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:111`
[^188]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:113`
[^189]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:115`
[^190]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:117`
[^191]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:119`
[^192]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:121`
[^193]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:123`
[^194]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:125`
[^195]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:127`
[^196]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:129`
[^197]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:95`
[^198]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:131`
[^199]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:133`
[^200]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:135`
[^201]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:137`
[^202]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:139`
[^203]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:141`
[^204]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:143`
[^205]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:145`
[^206]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:147`
[^207]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:149`
[^208]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:97`
[^209]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:151`
[^210]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:153`
[^211]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:155`
[^212]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:157`
[^213]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:159`
[^214]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:161`
[^215]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:163`
[^216]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:165`
[^217]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:167`
[^218]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:169`
[^219]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:99`
[^220]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:171`
[^221]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:173`
[^222]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:175`
[^223]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:177`
[^224]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:179`
[^225]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:181`
[^226]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:183`
[^227]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:185`
[^228]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:187`
[^229]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:189`
[^230]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:101`
[^231]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:191`
[^232]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:193`
[^233]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:195`
[^234]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:197`
[^235]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:199`
[^236]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:201`
[^237]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:203`
[^238]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:205`
[^239]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:207`
[^240]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:209`
[^241]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:103`
[^242]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:211`
[^243]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:213`
[^244]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:215`
[^245]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:217`
[^246]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:219`
[^247]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:221`
[^248]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:223`
[^249]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:225`
[^250]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:227`
[^251]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:229`
[^252]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:105`
[^253]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:231`
[^254]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:233`
[^255]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:107`
[^256]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:109`
[^257]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:88`
[^258]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:282`
[^259]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:77`
[^260]: `游戏原版/media/scripts/generated/vehicles/template_glovebox.txt:5`
[^261]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:25`
[^262]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:80`
[^263]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:82`
[^264]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:83`
[^265]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:81`
[^266]: `游戏原版/media/scripts/generated/vehicles/template_heater.txt:5`
[^267]: `游戏原版/media/scripts/generated/vehicles/template_muffler.txt:5`
[^268]: `游戏原版/media/scripts/generated/vehicles/template_radio.txt:5`
[^269]: `游戏原版/media/scripts/generated/vehicles/template_seat.txt:59`
[^270]: `游戏原版/media/scripts/generated/vehicles/template_seat.txt:5`
[^271]: `游戏原版/media/scripts/generated/vehicles/template_seat.txt:14`
[^272]: `游戏原版/media/scripts/generated/vehicles/template_seat.txt:41`
[^273]: `游戏原版/media/scripts/generated/vehicles/template_seat.txt:50`
[^274]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:57`
[^275]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:5`
[^276]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:18`
[^277]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:31`
[^278]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:44`
[^279]: `游戏原版/media/scripts/generated/vehicles/template_tire.txt:45`
[^280]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:84`
[^281]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:85`
[^282]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:86`
[^283]: `3821174725/mods/GridVans/42/media/scripts/vehicles/VansCourierDuo.txt:87`
