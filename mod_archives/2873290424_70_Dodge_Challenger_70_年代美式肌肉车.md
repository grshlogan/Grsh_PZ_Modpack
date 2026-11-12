# 1970 道奇挑战者（'70 Dodge Challenger）

1970 Dodge Challenger，多种涂装与改装件。

归属：**日常组合（玩法待验收）**；档案视图 `b422-compat`。
当前版本定义：**整车 5、本地物品定义 28、配方 25**；另引用共享物品 25。本地定义数含内部保留项，见独立列表；整车定义包括覆盖原版的条目，不等于新增车型数。

## 如何查找

- **生成整车**：在生成车辆菜单搜索下表完整 ID；显示译名时搜索中文列。联机管理命令用 `/addvehicle 完整ID`。
- **添加到背包**：普通物品、维修件、改装件都在添加物品菜单使用完整物品 ID；不要拿配方或内部槽位去刷车。
- **制作配方**：在制作界面查译名；配方 ID 用于排查，不是可放进背包的物品。
- 中文解释说明用途；只有翻译文件中找到的文字才称为游戏中文名。缺译保留脚本显示名，冲突列出各译文。

## 整车

| 完整生成车辆 ID | 当前中文名 / 名称状态 | 英文名或脚本名 | 变体说明 | 来源 |
| --- | --- | --- | --- | --- |
| `Base.70dodgeBG` | 70款道奇挑战者黑幽灵[^1] | '70 Dodge Challenger Black Ghost[^2] | 黑幽灵变体；当前汉化为 70款道奇挑战者黑幽灵，不额外推定性能加成 | [^3] |
| `Base.70dodgeOP` | 70款道奇挑战者O/P[^4] | '70 Dodge Challenger O/P[^5] | O/P 变体；当前汉化为 70款道奇挑战者O/P，不据缩写推定发动机或性能 | [^6] |
| `Base.70dodgePD` | 70款道奇挑战者警车[^7] | '70 Dodge Challenger Police[^8] | 警车变体；当前汉化为 70款道奇挑战者警车 | [^9] |
| `Base.70dodgeRT` | 70款道奇挑战者R/T[^10] | '70 Dodge Challenger R/T[^11] | R/T 变体；使用 RT 引擎盖与专属车顶部件，具体外观和性能待实刷 | [^12] |
| `Base.70dodgeTA` | 70款道奇挑战者T/A[^13] | '70 Dodge Challenger T/A[^14] | T/A 变体；当前模板引用 TA 系引擎盖，具体涂装和性能待实刷 | [^15] |

## 普通物品与书籍

| 完整物品 ID | 游戏显示名 / 名称状态 | 中文用途 / 类别 | 菜单 | 适用车辆与安装位置 | 来源 / 状态 |
| --- | --- | --- | --- | --- | --- |
| `Base.DodgeMagazine` | 70 Dodge Challenger Auto Manual（未找到有效中文译文） | 阅读资料；脚本声明解锁：制作70款道奇挑战者R/T引擎盖（Base.70dodgeRTMakeHood）、制作70款道奇挑战者P/D引擎盖（Base.70dodgePDMakeHood）、制作70款道奇挑战者T/A引擎盖（Base.70dodgeTAMakeHood）、制作70款道奇挑战者前门（Base.70dodgeMakeFrontDoor）、制作70款道奇挑战者后备箱盖（Base.70dodgeMakeTrunkLid）、制作70款道奇挑战者前座（Base.70dodgeMakeFrontSeat）、制作70款道奇挑战者后座（Base.70dodgeMakeRearSeat）、制作70款道奇挑战者挡风玻璃（Base.70dodgeMakeFrontWindshield）、制作70款道奇挑战者前部侧窗（Base.70dodgeMakeFrontSideWindow）、Make 70 Dodge Challenger Rear Side Window（Base.70dodgeMakeRearSideWindow）、制作70款道奇挑战者后挡风玻璃（Base.70dodgeMakeRearWindshield）、制作道奇挑战者小型复古车顶行李架（Base.70dodgeMakeRoofrack） / 普通物品 / 书籍 | 添加物品 | 未定位整车安装关系 | 70dodge[^16] |

## 维修配件

| 完整物品 ID | 游戏显示名 / 名称状态 | 中文用途 / 类别 | 菜单 | 适用车辆与安装位置 | 来源 / 状态 |
| --- | --- | --- | --- | --- | --- |
| `Base.DG70Door3` | 70 Dodge Challenger Door（未找到有效中文译文） | 挑战者车门维修件；对应前车门安装位 / 维修配件 | 添加物品 | Base.70dodgeBG → DoorFrontLeft；Base.70dodgeBG → DoorFrontRight；Base.70dodgeOP → DoorFrontLeft；Base.70dodgeOP → DoorFrontRight；Base.70dodgePD → DoorFrontLeft；Base.70dodgePD → DoorFrontRight；Base.70dodgeRT → DoorFrontLeft；Base.70dodgeRT → DoorFrontRight；Base.70dodgeTA → DoorFrontLeft；Base.70dodgeTA → DoorFrontRight | 70dodge[^17] |
| `Base.DG70FrontBumper0` | 70 Dodge Challenger Front Bumper（未找到有效中文译文） | 挑战者普通前保险杠；与三种前防撞杠改装件分开 / 维修配件 | 添加物品 | Base.70dodgeBG → DAMNBumperFront；Base.70dodgeOP → DAMNBumperFront；Base.70dodgePD → DAMNBumperFront；Base.70dodgeRT → DAMNBumperFront；Base.70dodgeTA → DAMNBumperFront | 70dodge[^18] |
| `Base.DG70FrontSideWindow3` | 70 Dodge Challenger Front Side Window（未找到有效中文译文） | 挑战者前侧车窗玻璃维修件；与前挡风玻璃分开 / 维修配件 | 添加物品 | Base.70dodgeBG → WindowFrontLeft；Base.70dodgeBG → WindowFrontRight；Base.70dodgeOP → WindowFrontLeft；Base.70dodgeOP → WindowFrontRight；Base.70dodgePD → WindowFrontLeft；Base.70dodgePD → WindowFrontRight；Base.70dodgeRT → WindowFrontLeft；Base.70dodgeRT → WindowFrontRight；Base.70dodgeTA → WindowFrontLeft；Base.70dodgeTA → WindowFrontRight | 70dodge[^19] |
| `Base.DG70PDEngineDoor` | 70 Dodge Challenger PD Hood（未找到有效中文译文） | PD 型引擎盖维修件；当前安装引用覆盖 O/P 与警车，实际适配见右列 / 维修配件 | 添加物品 | Base.70dodgeOP → EngineDoor；Base.70dodgePD → EngineDoor | 70dodge[^20] |
| `Base.DG70RTEngineDoor` | 70 Dodge Challenger RT Hood（未找到有效中文译文） | R/T 引擎盖维修件；EngineDoor 在这里指引擎盖，不是发动机本体 / 维修配件 | 添加物品 | Base.70dodgeRT → EngineDoor | 70dodge[^21] |
| `Base.DG70RearBumper0` | 70 Dodge Challenger Rear Bumper（未找到有效中文译文） | 挑战者普通后保险杠；与三种后防撞杠改装件分开 / 维修配件 | 添加物品 | Base.70dodgeBG → DAMNBumperRear；Base.70dodgeOP → DAMNBumperRear；Base.70dodgePD → DAMNBumperRear；Base.70dodgeRT → DAMNBumperRear；Base.70dodgeTA → DAMNBumperRear | 70dodge[^22] |
| `Base.DG70RearSideWindow3` | 70 Dodge Challenger Rear Side Window（未找到有效中文译文） | 挑战者后侧车窗玻璃维修件；适配位置见右列 / 维修配件 | 添加物品 | Base.70dodgeBG → WindowRear*；Base.70dodgeOP → WindowRear*；Base.70dodgePD → WindowRear*；Base.70dodgeRT → WindowRear*；Base.70dodgeTA → WindowRear* | 70dodge[^23] |
| `Base.DG70TAEngineDoor0` | Not in use（未找到有效中文译文） | TA 系编号 0 引擎盖定义；作者显示名虽为 Not in use，当前 BG / TA 模板仍引用 / 维修配件 | 添加物品 | Base.70dodgeBG → EngineDoor；Base.70dodgeTA → EngineDoor | 70dodge[^24]；作者显示名为 Not in use；当前模板仍引用，不能据名称判为停用 |
| `Base.DG70TAEngineDoor1` | 70 Dodge Challenger TA Black Hood（未找到有效中文译文） | TA 系黑色引擎盖维修件；当前 BG / TA 模板引用 / 维修配件 | 添加物品 | Base.70dodgeBG → EngineDoor；Base.70dodgeTA → EngineDoor | 70dodge[^25] |
| `Base.DG70TrunkDoor3` | 70 Dodge Challenger Trunk Lid（未找到有效中文译文） | 挑战者后备箱盖维修件；不是后备箱容量或可携带箱子 / 维修配件 | 添加物品 | Base.70dodgeBG → TrunkDoor；Base.70dodgeOP → TrunkDoor；Base.70dodgePD → TrunkDoor；Base.70dodgeRT → TrunkDoor；Base.70dodgeTA → TrunkDoor | 70dodge[^26] |
| `Base.DG70Windshield3` | 70 Dodge Challenger Windshield（未找到有效中文译文） | 挑战者前挡风玻璃维修件；不是玻璃装甲 / 维修配件 | 添加物品 | Base.70dodgeBG → Windshield；Base.70dodgeOP → Windshield；Base.70dodgePD → Windshield；Base.70dodgeRT → Windshield；Base.70dodgeTA → Windshield | 70dodge[^27] |
| `Base.DG70WindshieldRear3` | 70 Dodge Challenger Rear Windshield（未找到有效中文译文） | 挑战者后挡风玻璃维修件；不是后侧窗 / 维修配件 | 添加物品 | Base.70dodgeBG → WindshieldRear；Base.70dodgeOP → WindshieldRear；Base.70dodgePD → WindshieldRear；Base.70dodgeRT → WindshieldRear；Base.70dodgeTA → WindshieldRear | 70dodge[^28] |
| `Base.DodgeFrontSeat3` | 70 Dodge Challenger Front Seat（未找到有效中文译文） | 挑战者前排座椅维修件；对应座椅槽位，不能生成整车 / 维修配件 | 添加物品 | Base.70dodgeBG → SeatFrontLeft；Base.70dodgeBG → SeatFrontRight；Base.70dodgeOP → SeatFrontLeft；Base.70dodgeOP → SeatFrontRight；Base.70dodgePD → SeatFrontLeft；Base.70dodgePD → SeatFrontRight；Base.70dodgeRT → SeatFrontLeft；Base.70dodgeRT → SeatFrontRight；Base.70dodgeTA → SeatFrontLeft；Base.70dodgeTA → SeatFrontRight | 70dodge[^29] |
| `Base.DodgeRearSeat3` | 70 Dodge Challenger Rear Seat（未找到有效中文译文） | 挑战者后排座椅维修件；对应后排座椅槽位 / 维修配件 | 添加物品 | Base.70dodgeBG → SeatRearLeft；Base.70dodgeBG → SeatRearRight；Base.70dodgeOP → SeatRearLeft；Base.70dodgeOP → SeatRearRight；Base.70dodgePD → SeatRearLeft；Base.70dodgePD → SeatRearRight；Base.70dodgeRT → SeatRearLeft；Base.70dodgeRT → SeatRearRight；Base.70dodgeTA → SeatRearLeft；Base.70dodgeTA → SeatRearRight | 70dodge[^30] |

## 改装配件

| 完整物品 ID | 游戏显示名 / 名称状态 | 中文用途 / 类别 | 菜单 | 适用车辆与安装位置 | 来源 / 状态 |
| --- | --- | --- | --- | --- | --- |
| `Base.DG70DoorArmor` | 70 Dodge Challenger Door Armor（未找到有效中文译文） | 挑战者车门防护件；不能代替完整车门维修件 / 改装配件 | 添加物品 | Base.70dodgeBG → DAMNFrontLeftArmor；Base.70dodgeBG → DAMNFrontRightArmor；Base.70dodgeOP → DAMNFrontLeftArmor；Base.70dodgeOP → DAMNFrontRightArmor；Base.70dodgePD → DAMNFrontLeftArmor；Base.70dodgePD → DAMNFrontRightArmor；Base.70dodgeRT → DAMNFrontLeftArmor；Base.70dodgeRT → DAMNFrontRightArmor；Base.70dodgeTA → DAMNFrontLeftArmor；Base.70dodgeTA → DAMNFrontRightArmor | 70dodge[^31] |
| `Base.DG70FrontBumperA` | 70 Dodge Challenger Front Bullbar Type 1（未找到有效中文译文） | 挑战者前防撞杠 1 型；是改装配件，防护效果未游戏验证 / 改装配件 | 添加物品 | Base.70dodgeBG → DAMNBumperFront；Base.70dodgeOP → DAMNBumperFront；Base.70dodgePD → DAMNBumperFront；Base.70dodgeRT → DAMNBumperFront；Base.70dodgeTA → DAMNBumperFront | 70dodge[^32] |
| `Base.DG70FrontBumperB` | 70 Dodge Challenger Front Bullbar Type 2（未找到有效中文译文） | 挑战者前防撞杠 2 型；与 1 / 3 型为不同定义，不据编号推定强弱 / 改装配件 | 添加物品 | Base.70dodgeBG → DAMNBumperFront；Base.70dodgeOP → DAMNBumperFront；Base.70dodgePD → DAMNBumperFront；Base.70dodgeRT → DAMNBumperFront；Base.70dodgeTA → DAMNBumperFront | 70dodge[^33] |
| `Base.DG70FrontBumperC` | 70 Dodge Challenger Front Bullbar Type 3（未找到有效中文译文） | 挑战者前防撞杠 3 型；外观与具体防护差异待实刷 / 改装配件 | 添加物品 | Base.70dodgeBG → DAMNBumperFront；Base.70dodgeOP → DAMNBumperFront；Base.70dodgePD → DAMNBumperFront；Base.70dodgeRT → DAMNBumperFront；Base.70dodgeTA → DAMNBumperFront | 70dodge[^34] |
| `Base.DG70RTRoof0` | 70 Dodge Challenger RT Roof（未找到有效中文译文） | 挑战者 R/T 车顶组件；对应车顶安装位，不是可背负的行李袋 / 改装配件 | 添加物品 | Base.70dodgeBG → DG70RTRoof；Base.70dodgeRT → DG70RTRoof | 70dodge[^35] |
| `Base.DG70RearBumperA` | 70 Dodge Challenger Rear Bullbar Type 1（未找到有效中文译文） | 挑战者后防撞杠 1 型；安装在后部保险杠位置 / 改装配件 | 添加物品 | Base.70dodgeBG → DAMNBumperRear；Base.70dodgeOP → DAMNBumperRear；Base.70dodgePD → DAMNBumperRear；Base.70dodgeRT → DAMNBumperRear；Base.70dodgeTA → DAMNBumperRear | 70dodge[^36] |
| `Base.DG70RearBumperB` | 70 Dodge Challenger Rear Bullbar Type 2（未找到有效中文译文） | 挑战者后防撞杠 2 型；是后部改装件，不是后备箱盖 / 改装配件 | 添加物品 | Base.70dodgeBG → DAMNBumperRear；Base.70dodgeOP → DAMNBumperRear；Base.70dodgePD → DAMNBumperRear；Base.70dodgeRT → DAMNBumperRear；Base.70dodgeTA → DAMNBumperRear | 70dodge[^37] |
| `Base.DG70RearBumperC` | 70 Dodge Challenger Rear Bullbar Type 3（未找到有效中文译文） | 挑战者后防撞杠 3 型；不据编号推定性能加成 / 改装配件 | 添加物品 | Base.70dodgeBG → DAMNBumperRear；Base.70dodgeOP → DAMNBumperRear；Base.70dodgePD → DAMNBumperRear；Base.70dodgeRT → DAMNBumperRear；Base.70dodgeTA → DAMNBumperRear | 70dodge[^38] |
| `Base.DG70Spoiler0` | 70 Dodge Challenger Spoiler Type 1（未找到有效中文译文） | 挑战者扰流板 1 型；外观改装部件，不承诺额外下压力或速度收益 / 改装配件 | 添加物品 | Base.70dodgeOP → DAMNSpoiler；Base.70dodgePD → DAMNSpoiler；Base.70dodgeRT → DAMNSpoiler；Base.70dodgeTA → DAMNSpoiler | 70dodge[^39] |
| `Base.DG70Spoiler1` | 70 Dodge Challenger Spoiler Type 2（未找到有效中文译文） | 挑战者扰流板 2 型；与 1 型为不同物品定义，性能影响未验证 / 改装配件 | 添加物品 | Base.70dodgeOP → DAMNSpoiler；Base.70dodgePD → DAMNSpoiler；Base.70dodgeRT → DAMNSpoiler；Base.70dodgeTA → DAMNSpoiler | 70dodge[^40] |
| `Base.DG70WindshieldArmor` | 70 Dodge Challenger Windshield Armor Type 1（未找到有效中文译文） | 挑战者前挡风玻璃防护件 1 型；与玻璃本身是不同物品 / 改装配件 | 添加物品 | Base.70dodgeBG → DAMNWindshieldArmor；Base.70dodgeOP → DAMNWindshieldArmor；Base.70dodgePD → DAMNWindshieldArmor；Base.70dodgeRT → DAMNWindshieldArmor；Base.70dodgeTA → DAMNWindshieldArmor | 70dodge[^41] |
| `Base.DG70WindshieldArmorB` | 70 Dodge Challenger Windshield Armor Type 2（未找到有效中文译文） | 挑战者前挡风玻璃防护件 2 型；具体防护与视野影响待游戏核实 / 改装配件 | 添加物品 | Base.70dodgeBG → DAMNWindshieldArmor；Base.70dodgeOP → DAMNWindshieldArmor；Base.70dodgePD → DAMNWindshieldArmor；Base.70dodgeRT → DAMNWindshieldArmor；Base.70dodgeTA → DAMNWindshieldArmor | 70dodge[^42] |
| `Base.DG70WindshieldRearArmor` | 70 Dodge Challenger Rear Windshield Armor（未找到有效中文译文） | 挑战者后挡风玻璃防护件；不用于前挡风玻璃 / 改装配件 | 添加物品 | Base.70dodgeBG → DAMNWindshieldRearArmor；Base.70dodgeOP → DAMNWindshieldRearArmor；Base.70dodgePD → DAMNWindshieldRearArmor；Base.70dodgeRT → DAMNWindshieldRearArmor；Base.70dodgeTA → DAMNWindshieldRearArmor | 70dodge[^43] |

## 共享配件

下列物品由已启用依赖或游戏原版提供，不计入本 Mod 的本地物品数。

| 完整物品 ID | 游戏显示名 / 名称状态 | 中文用途 / 类别 | 菜单 | 适用车辆与安装位置 | 来源 / 状态 |
| --- | --- | --- | --- | --- | --- |
| `Base.BigGasTank3` | 油箱 (大型)（翻译文件含非标准语法，待游戏核实）[^45] | 车辆安装件，用于油箱（GasTank）；适用车型见右列 / 维修配件 | 添加物品 | Base.70dodgeBG → GasTank；Base.70dodgeOP → GasTank；Base.70dodgePD → GasTank；Base.70dodgeRT → GasTank；Base.70dodgeTA → GasTank | 游戏原版[^44] |
| `Base.CUDAtire3` | 70 Barracuda Tire（未找到有效中文译文） | 车辆安装件，用于轮胎（Tire*）、轮胎（DAMNSpareTire）；适用车型见右列 / 维修配件 | 添加物品 | Base.70dodgeBG → Tire*；Base.70dodgeBG → DAMNSpareTire；Base.70dodgeOP → Tire*；Base.70dodgeOP → DAMNSpareTire；Base.70dodgePD → Tire*；Base.70dodgePD → DAMNSpareTire；Base.70dodgeRT → Tire*；Base.70dodgeRT → DAMNSpareTire；Base.70dodgeTA → Tire*；Base.70dodgeTA → DAMNSpareTire | damnlib[^46] |
| `Base.CamaroSStire3` | 69 Camaro Tire（未找到有效中文译文） | 车辆安装件，用于轮胎（Tire*）、轮胎（DAMNSpareTire）；适用车型见右列 / 维修配件 | 添加物品 | Base.70dodgeBG → Tire*；Base.70dodgeBG → DAMNSpareTire；Base.70dodgeOP → Tire*；Base.70dodgeOP → DAMNSpareTire；Base.70dodgePD → Tire*；Base.70dodgePD → DAMNSpareTire；Base.70dodgeRT → Tire*；Base.70dodgeRT → DAMNSpareTire；Base.70dodgeTA → Tire*；Base.70dodgeTA → DAMNSpareTire | damnlib[^47] |
| `Base.CarBattery3` | 汽车电池（翻译文件含非标准语法，待游戏核实）[^49] | 车辆安装件，用于蓄电池（Battery）；适用车型见右列 / 维修配件 | 添加物品 | Base.70dodgeBG → Battery；Base.70dodgeOP → Battery；Base.70dodgePD → Battery；Base.70dodgeRT → Battery；Base.70dodgeTA → Battery | 游戏原版[^48] |
| `Base.DodgeRTtire3` | 70 Challenger Tire（未找到有效中文译文） | 车辆安装件，用于轮胎（Tire*）、轮胎（DAMNSpareTire）；适用车型见右列 / 维修配件 | 添加物品 | Base.70dodgeBG → Tire*；Base.70dodgeBG → DAMNSpareTire；Base.70dodgeOP → Tire*；Base.70dodgeOP → DAMNSpareTire；Base.70dodgePD → Tire*；Base.70dodgePD → DAMNSpareTire；Base.70dodgeRT → Tire*；Base.70dodgeRT → DAMNSpareTire；Base.70dodgeTA → Tire*；Base.70dodgeTA → DAMNSpareTire | damnlib[^50] |
| `Base.GloveBox3` | 手套箱（翻译文件含非标准语法，待游戏核实）[^52] | 车辆安装件，用于车辆安装位（GloveBox）；适用车型见右列 / 维修配件 | 添加物品 | Base.70dodgeBG → GloveBox；Base.70dodgeOP → GloveBox；Base.70dodgePD → GloveBox；Base.70dodgeRT → GloveBox；Base.70dodgeTA → GloveBox | 游戏原版[^51] |
| `Base.HamRadio1` | 微型导航仪 / 收音机 (业余电台) / 民用无线电台 (昂科) / 民用无线电台 - 昂科公司（译文冲突，待游戏核实）[^54] | 车辆安装件，用于车辆安装位（Radio）；适用车型见右列 / 维修配件 | 添加物品 | Base.70dodgePD → Radio | 游戏原版[^53] |
| `Base.HamRadio2` | 收音机 (军用) / 军用无线电台（译文冲突，待游戏核实）[^56] | 车辆安装件，用于车辆安装位（Radio）；适用车型见右列 / 维修配件 | 添加物品 | Base.70dodgePD → Radio | 游戏原版[^55] |
| `Base.HamRadioMakeShift` | 收音机 (简易业余无线电) / 收音机 (简易业余电台) / 自制无线电台（译文冲突，待游戏核实）[^58] | 车辆安装件，用于车辆安装位（Radio）；适用车型见右列 / 维修配件 | 添加物品 | Base.70dodgePD → Radio | 游戏原版[^57] |
| `Base.LightBulb` | 灯泡-白色 / 灯泡 (白)（译文冲突，待游戏核实）[^60] | 车辆安装件，用于车灯（Headlight*）、车灯（JP82DorothyLights）；适用车型见右列 / 维修配件 | 添加物品 | Base.70dodgeBG → Headlight*；Base.70dodgeOP → Headlight*；Base.70dodgePD → Headlight*；Base.70dodgeRT → Headlight*；Base.70dodgeTA → Headlight* | 游戏原版[^59] |
| `Base.ModernBrake3` | 制动器 (高级)（翻译文件含非标准语法，待游戏核实）[^62] | 车辆安装件，用于制动器（Brake*）；适用车型见右列 / 维修配件 | 添加物品 | Base.70dodgeBG → Brake*；Base.70dodgeOP → Brake*；Base.70dodgePD → Brake*；Base.70dodgeRT → Brake*；Base.70dodgeTA → Brake* | 游戏原版[^61] |
| `Base.ModernCarMuffler3` | 消声器 (高级)（翻译文件含非标准语法，待游戏核实）[^64] | 车辆安装件，用于消声器（Muffler）；适用车型见右列 / 维修配件 | 添加物品 | Base.70dodgeBG → Muffler；Base.70dodgeOP → Muffler；Base.70dodgePD → Muffler；Base.70dodgeRT → Muffler；Base.70dodgeTA → Muffler | 游戏原版[^63] |
| `Base.ModernSuspension3` | 悬挂 (高级)（翻译文件含非标准语法，待游戏核实）[^66] | 车辆安装件，用于悬挂（Suspension*）；适用车型见右列 / 维修配件 | 添加物品 | Base.70dodgeBG → Suspension*；Base.70dodgeOP → Suspension*；Base.70dodgePD → Suspension*；Base.70dodgeRT → Suspension*；Base.70dodgeTA → Suspension* | 游戏原版[^65] |
| `Base.NormalBrake3` | 制动器 (普通)（翻译文件含非标准语法，待游戏核实）[^68] | 车辆安装件，用于制动器（Brake*）；适用车型见右列 / 维修配件 | 添加物品 | Base.70dodgeBG → Brake*；Base.70dodgeOP → Brake*；Base.70dodgePD → Brake*；Base.70dodgeRT → Brake*；Base.70dodgeTA → Brake* | 游戏原版[^67] |
| `Base.NormalCarMuffler3` | 消声器 (普通)（翻译文件含非标准语法，待游戏核实）[^70] | 车辆安装件，用于消声器（Muffler）；适用车型见右列 / 维修配件 | 添加物品 | Base.70dodgeBG → Muffler；Base.70dodgeOP → Muffler；Base.70dodgePD → Muffler；Base.70dodgeRT → Muffler；Base.70dodgeTA → Muffler | 游戏原版[^69] |
| `Base.NormalGasTank3` | 油箱 (标准)（翻译文件含非标准语法，待游戏核实）[^72] | 车辆安装件，用于油箱（GasTank）；适用车型见右列 / 维修配件 | 添加物品 | Base.70dodgeBG → GasTank；Base.70dodgeOP → GasTank；Base.70dodgePD → GasTank；Base.70dodgeRT → GasTank；Base.70dodgeTA → GasTank | 游戏原版[^71] |
| `Base.NormalSuspension3` | 悬挂 (普通)（翻译文件含非标准语法，待游戏核实）[^74] | 车辆安装件，用于悬挂（Suspension*）；适用车型见右列 / 维修配件 | 添加物品 | Base.70dodgeBG → Suspension*；Base.70dodgeOP → Suspension*；Base.70dodgePD → Suspension*；Base.70dodgeRT → Suspension*；Base.70dodgeTA → Suspension* | 游戏原版[^73] |
| `Base.OldBrake3` | 制动器 (老式)（翻译文件含非标准语法，待游戏核实）[^76] | 车辆安装件，用于制动器（Brake*）；适用车型见右列 / 维修配件 | 添加物品 | Base.70dodgeBG → Brake*；Base.70dodgeOP → Brake*；Base.70dodgePD → Brake*；Base.70dodgeRT → Brake*；Base.70dodgeTA → Brake* | 游戏原版[^75] |
| `Base.OldCarMuffler3` | 消声器 (老式)（翻译文件含非标准语法，待游戏核实）[^78] | 车辆安装件，用于消声器（Muffler）；适用车型见右列 / 维修配件 | 添加物品 | Base.70dodgeBG → Muffler；Base.70dodgeOP → Muffler；Base.70dodgePD → Muffler；Base.70dodgeRT → Muffler；Base.70dodgeTA → Muffler | 游戏原版[^77] |
| `Base.OldSmallRoofrack3` | Small Vintage Roofrack（未找到有效中文译文） | 车辆安装件，用于车顶行李架（DG70Roofrack）、车顶行李架（CAM69Roofrack）、车顶行李架（CHR69Roofrack）；适用车型见右列 / 改装配件 | 添加物品 | Base.70dodgeBG → DG70Roofrack；Base.70dodgeOP → DG70Roofrack；Base.70dodgeTA → DG70Roofrack | damnlib[^79] |
| `Base.RadioBlack` | 收音机 (超值科技) / 收音机 (廉科) / 廉科牌收音机（译文冲突，待游戏核实）[^81] | 车辆安装件，用于车辆安装位（Radio）；适用车型见右列 / 维修配件 | 添加物品 | Base.70dodgeBG → Radio；Base.70dodgeOP → Radio；Base.70dodgeRT → Radio；Base.70dodgeTA → Radio | 游戏原版[^80] |
| `Base.RadioMakeShift` | 收音机 (简易) / 自制收音机（译文冲突，待游戏核实）[^83] | 车辆安装件，用于车辆安装位（Radio）；适用车型见右列 / 维修配件 | 添加物品 | Base.70dodgeBG → Radio；Base.70dodgeOP → Radio；Base.70dodgeRT → Radio；Base.70dodgeTA → Radio | 游戏原版[^82] |
| `Base.RadioRed` | 导航仪 / 收音机 (昂科) / 昂科牌收音机（译文冲突，待游戏核实）[^85] | 车辆安装件，用于车辆安装位（Radio）；适用车型见右列 / 维修配件 | 添加物品 | Base.70dodgeBG → Radio；Base.70dodgeOP → Radio；Base.70dodgeRT → Radio；Base.70dodgeTA → Radio | 游戏原版[^84] |
| `Base.SmallGasTank3` | 油箱 (小型)（翻译文件含非标准语法，待游戏核实）[^87] | 车辆安装件，用于油箱（GasTank）；适用车型见右列 / 维修配件 | 添加物品 | Base.70dodgeBG → GasTank；Base.70dodgeOP → GasTank；Base.70dodgePD → GasTank；Base.70dodgeRT → GasTank；Base.70dodgeTA → GasTank | 游戏原版[^86] |

## 制作配方

| 配方完整 ID（排查用） | 游戏配方名 / 名称状态 | 中文用途 | 菜单 | 来源 |
| --- | --- | --- | --- | --- |
| `Base.70dodgeBMakeFrontWindshieldArmor` | 制作70款道奇挑战者前挡风玻璃装甲II[^88] | 制作产出：70 Dodge Challenger Windshield Armor Type 2（挑战者前挡风玻璃防护件 2 型；具体防护与视野影响待游戏核实） | 制作界面 | [^89] |
| `Base.70dodgeMakeFrontBullbarA` | 制作70款道奇挑战者前保险杠I[^90] | 制作产出：70 Dodge Challenger Front Bullbar Type 1（挑战者前防撞杠 1 型；是改装配件，防护效果未游戏验证） | 制作界面 | [^91] |
| `Base.70dodgeMakeFrontBullbarB` | 制作70款道奇挑战者前保险杠II[^92] | 制作产出：70 Dodge Challenger Front Bullbar Type 2（挑战者前防撞杠 2 型；与 1 / 3 型为不同定义，不据编号推定强弱） | 制作界面 | [^93] |
| `Base.70dodgeMakeFrontBullbarC` | 制作70款道奇挑战者前保险杠III[^94] | 制作产出：70 Dodge Challenger Front Bullbar Type 3（挑战者前防撞杠 3 型；外观与具体防护差异待实刷） | 制作界面 | [^95] |
| `Base.70dodgeMakeFrontBumper` | 制作70款道奇挑战者前保险杠[^96] | 制作产出：70 Dodge Challenger Front Bumper（挑战者普通前保险杠；与三种前防撞杠改装件分开） | 制作界面 | [^97] |
| `Base.70dodgeMakeFrontDoor` | 制作70款道奇挑战者前门[^98] | 制作产出：70 Dodge Challenger Door（挑战者车门维修件；对应前车门安装位） | 制作界面 | [^99] |
| `Base.70dodgeMakeFrontSeat` | 制作70款道奇挑战者前座[^100] | 制作产出：70 Dodge Challenger Front Seat（挑战者前排座椅维修件；对应座椅槽位，不能生成整车） | 制作界面 | [^101] |
| `Base.70dodgeMakeFrontSideWindow` | 制作70款道奇挑战者前部侧窗[^102] | 制作产出：70 Dodge Challenger Front Side Window（挑战者前侧车窗玻璃维修件；与前挡风玻璃分开） | 制作界面 | [^103] |
| `Base.70dodgeMakeFrontWindowArmor` | 制作70款道奇挑战者车窗装甲[^104] | 制作产出：70 Dodge Challenger Door Armor（挑战者车门防护件；不能代替完整车门维修件） | 制作界面 | [^105] |
| `Base.70dodgeMakeFrontWindshield` | 制作70款道奇挑战者挡风玻璃[^106] | 制作产出：70 Dodge Challenger Windshield（挑战者前挡风玻璃维修件；不是玻璃装甲） | 制作界面 | [^107] |
| `Base.70dodgeMakeFrontWindshieldArmor` | 制作70款道奇挑战者前挡风玻璃装甲I[^108] | 制作产出：70 Dodge Challenger Windshield Armor Type 1（挑战者前挡风玻璃防护件 1 型；与玻璃本身是不同物品） | 制作界面 | [^109] |
| `Base.70dodgeMakeRearBullbarA` | 制作70款道奇挑战者后保险杠I[^110] | 制作产出：70 Dodge Challenger Rear Bullbar Type 1（挑战者后防撞杠 1 型；安装在后部保险杠位置） | 制作界面 | [^111] |
| `Base.70dodgeMakeRearBullbarB` | 制作70款道奇挑战者后保险杠II[^112] | 制作产出：70 Dodge Challenger Rear Bullbar Type 2（挑战者后防撞杠 2 型；是后部改装件，不是后备箱盖） | 制作界面 | [^113] |
| `Base.70dodgeMakeRearBullbarC` | 制作70款道奇挑战者后保险杠III[^114] | 制作产出：70 Dodge Challenger Rear Bullbar Type 3（挑战者后防撞杠 3 型；不据编号推定性能加成） | 制作界面 | [^115] |
| `Base.70dodgeMakeRearBumper` | 制作70款道奇挑战者后保险杠[^116] | 制作产出：70 Dodge Challenger Rear Bumper（挑战者普通后保险杠；与三种后防撞杠改装件分开） | 制作界面 | [^117] |
| `Base.70dodgeMakeRearSeat` | 制作70款道奇挑战者后座[^118] | 制作产出：70 Dodge Challenger Rear Seat（挑战者后排座椅维修件；对应后排座椅槽位） | 制作界面 | [^119] |
| `Base.70dodgeMakeRearSideWindow` | Make 70 Dodge Challenger Rear Side Window（未找到有效中文译文）[^120] | 制作产出：70 Dodge Challenger Rear Side Window（挑战者后侧车窗玻璃维修件；适配位置见右列） | 制作界面 | [^121] |
| `Base.70dodgeMakeRearWindshield` | 制作70款道奇挑战者后挡风玻璃[^122] | 制作产出：70 Dodge Challenger Rear Windshield（挑战者后挡风玻璃维修件；不是后侧窗） | 制作界面 | [^123] |
| `Base.70dodgeMakeRearWindshieldArmor` | 制作70款道奇挑战者后挡风玻璃装甲[^124] | 制作产出：70 Dodge Challenger Rear Windshield Armor（挑战者后挡风玻璃防护件；不用于前挡风玻璃） | 制作界面 | [^125] |
| `Base.70dodgeMakeRoofrack` | 制作道奇挑战者小型复古车顶行李架[^126] | 制作产出：Small Vintage Roofrack（车辆安装件，用于车顶行李架（DG70Roofrack）、车顶行李架（CAM69Roofrack）、车顶行李架（CHR69Roofrack）；适用车型见右列） | 制作界面 | [^127] |
| `Base.70dodgeMakeTire` | 制作70款道奇挑战者轮胎[^128] | 制作产出：70 Challenger Tire（车辆安装件，用于轮胎（Tire*）、轮胎（DAMNSpareTire）；适用车型见右列） | 制作界面 | [^129] |
| `Base.70dodgeMakeTrunkLid` | 制作70款道奇挑战者后备箱盖[^130] | 制作产出：70 Dodge Challenger Trunk Lid（挑战者后备箱盖维修件；不是后备箱容量或可携带箱子） | 制作界面 | [^131] |
| `Base.70dodgePDMakeHood` | 制作70款道奇挑战者P/D引擎盖[^132] | 制作产出：70 Dodge Challenger PD Hood（PD 型引擎盖维修件；当前安装引用覆盖 O/P 与警车，实际适配见右列） | 制作界面 | [^133] |
| `Base.70dodgeRTMakeHood` | 制作70款道奇挑战者R/T引擎盖[^134] | 制作产出：70 Dodge Challenger RT Hood（R/T 引擎盖维修件；EngineDoor 在这里指引擎盖，不是发动机本体） | 制作界面 | [^135] |
| `Base.70dodgeTAMakeHood` | 制作70款道奇挑战者T/A引擎盖[^136] | 制作产出：70 Dodge Challenger TA Black Hood（TA 系黑色引擎盖维修件；当前 BG / TA 模板引用） | 制作界面 | [^137] |

## 内部定义、历史分支与未解析引用

有效资源层：42.13, common；仅合并 common 与所选版本，Overlay 按相对路径覆盖。
车辆模板 19 个、内部槽位 59 个，均不算整车或背包物品。旧根目录和未选中版本的定义不列入当前可用表。模板中短物品引用若追加机修类型后缀才匹配定义，属于静态映射，安装仍待实测。

内部或过时的 item 定义单列于此，不在上面的背包刷取建议中；它们仍计入各自来源的定义数量。

| 保留定义 ID（不作正常刷取建议） | 脚本显示名 | 中文说明 / 状态 | 来源 |
| --- | --- | --- | --- |
| `damnCraft.Trunk3` | no | 车辆后备箱的内部容量载体，当前挑战者等模板仍引用；不是背包或独立行李箱；显示名 no、图标 na；不作正常刷取建议 | [^138] |

<details><summary>查看内部槽位（不能直接刷取）</summary>

| 槽位 | 名称或说明 | 来源 |
| --- | --- | --- |
| `Battery` | 电池 / 蓄电池 | [^139] |
| `Brake*` | Brake* / 制动器 | [^140] |
| `BrakeFrontLeft` | 左前制动 / 制动器 | [^141] |
| `BrakeFrontRight` | 右前制动 / 制动器 | [^142] |
| `BrakeRearLeft` | 左后制动 / 制动器 | [^143] |
| `BrakeRearRight` | 右后制动 / 制动器 | [^144] |
| `DAMNBumperFront` | 前保险杠 / 保险杠 | [^145] |
| `DAMNBumperRear` | 后保险杠 / 保险杠 | [^146] |
| `DAMNFrontLeftArmor` | 左前车窗装甲 / 防护件 | [^147] |
| `DAMNFrontRightArmor` | 右前车窗装甲 / 防护件 | [^148] |
| `DAMNSpareTire` | 备胎 / 轮胎 | [^149] |
| `DAMNSpoiler` | 尾翼 / 扰流板 | [^150] |
| `DAMNWindshieldArmor` | 挡风玻璃装甲 / 挡风玻璃 | [^151] |
| `DAMNWindshieldRearArmor` | 后挡风玻璃装甲 / 挡风玻璃 | [^152] |
| `DG70RTRoof` | 可拆卸式车顶架 / 车顶 | [^153] |
| `DG70Roofrack` | 车顶行李架容量 / 车顶行李架 | [^154] |
| `DG70Trunk` | 后备箱容量 / 后备箱 | [^155] |
| `Door*` | Door* / 车门 | [^156] |
| `DoorFrontLeft` | 左前门 / 车门 | [^157] |
| `DoorFrontRight` | 右前门 / 车门 | [^158] |
| `Engine` | 引擎 / 发动机 | [^159] |
| `EngineDoor` | 引擎盖 / 引擎盖 | [^160] |
| `GasTank` | 油箱 / 油箱 | [^161] |
| `GloveBox` | 手套箱 / 车辆安装位 | [^162] |
| `Headlight*` | Headlight* / 车灯 | [^163] |
| `HeadlightLeft` | 左大灯 / 车灯 | [^164] |
| `HeadlightRearLeft` | 左尾灯 / 车灯 | [^165] |
| `HeadlightRearRight` | 右尾灯 / 车灯 | [^166] |
| `HeadlightRight` | 右大灯 / 车灯 | [^167] |
| `Heater` | 加热器 / 车辆安装位 | [^168] |
| `Muffler` | 排气消声器 / 消声器 | [^169] |
| `PassengerCompartment` | 乘员舱 / 车辆安装位 | [^170] |
| `Radio` | 电台 / 车辆安装位 | [^171] |
| `Radio*` | Radio* / 车辆安装位 | [^172] |
| `Seat*` | Seat* / 座椅 | [^173] |
| `SeatFrontLeft` | 驾驶座 / 座椅 | [^174] |
| `SeatFrontRight` | 右前座 / 座椅 | [^175] |
| `SeatRearLeft` | 左后座 / 座椅 | [^176] |
| `SeatRearRight` | 右后座 / 座椅 | [^177] |
| `Suspension*` | Suspension* / 悬挂 | [^178] |
| `SuspensionFrontLeft` | 左前悬挂 / 悬挂 | [^179] |
| `SuspensionFrontRight` | 右前悬挂 / 悬挂 | [^180] |
| `SuspensionRearLeft` | 左后悬挂 / 悬挂 | [^181] |
| `SuspensionRearRight` | 右后悬挂 / 悬挂 | [^182] |
| `Tire*` | Tire* / 轮胎 | [^183] |
| `TireFrontLeft` | 左前胎 / 轮胎 | [^184] |
| `TireFrontRight` | 右前胎 / 轮胎 | [^185] |
| `TireRearLeft` | 左后胎 / 轮胎 | [^186] |
| `TireRearRight` | 右后胎 / 轮胎 | [^187] |
| `TruckBed` | 补给箱 / 行李箱 / 车辆安装位 | [^188] |
| `TrunkDoor` | 后车盖 / 后备箱 | [^189] |
| `WindowFront*` | WindowFront* / 车窗 | [^190] |
| `WindowFrontLeft` | 左前窗 / 车窗 | [^191] |
| `WindowFrontRight` | 右前窗 / 车窗 | [^192] |
| `WindowRear*` | WindowRear* / 车窗 | [^193] |
| `WindowRearLeft` | 左后窗 / 车窗 | [^194] |
| `WindowRearRight` | 右后窗 / 车窗 | [^195] |
| `Windshield` | 挡风玻璃 / 挡风玻璃 | [^196] |
| `WindshieldRear` | 后挡风玻璃 / 挡风玻璃 | [^197] |

</details>


**旧统计纠正（verified）**：旧页的 30 / 39 个物品及 33 条配方混用了历史分支；当前 42.13 层为 28 个本地物品定义、5 个整车定义、25 条配方。旧根目录独有的 Base.DG70Trunk3 不列为当前可刷物品；共享行李架与轮胎另标 damnlib 来源。保留区中的旧数量只用于追溯。

## 概览

| Mod ID / 文件夹 | 分发端 | 版本 | 选择的 mod.info | 原件范围 → 当前范围 |
| --- | --- | --- | --- | --- |
| `70dodge` / `70dodge` | both（双端） | 未标注 | `42.13/mod.info` | 42.13.0 … - → 42.13.0 … - |

原件体积 18.2 MB；体积按完整目录统计，与当前内容定义数分开。
工作坊：[查看作者页面](https://steamcommunity.com/sharedfiles/filedetails/?id=2873290424)。

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

require damnlib；39 个脚本物品、5 个载具脚本、33 条配方。

```
cd A004
python lab.py check --profile b422-compat
grep -a '70dodge' runs/<trial>/*console.log
```
<!-- retained:end -->

## 静态来源

路径相对 `A004/workspace/mods_library/`；`Overlay/<文件夹>/` 指 `A004/workspace/patches/mods/<文件夹>/`，`游戏原版/` 指当前 B42.22 客户端 Game 目录。翻译来源列出所有候选，未按加载顺序擅自消解异文。

[^1]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/IG_UI.json:15865`
[^2]: `2873290424/mods/70dodge/common/media/lua/shared/Translate/EN/IG_UI.json:7`；`2873290424/mods/70dodge/42.13/media/lua/shared/Translate/EN/IG_UI_EN.txt:6`
[^3]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeBG.txt:3`
[^4]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/IG_UI.json:15864`
[^5]: `2873290424/mods/70dodge/common/media/lua/shared/Translate/EN/IG_UI.json:6`；`2873290424/mods/70dodge/42.13/media/lua/shared/Translate/EN/IG_UI_EN.txt:5`
[^6]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeOP.txt:3`
[^7]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/IG_UI.json:15863`
[^8]: `2873290424/mods/70dodge/common/media/lua/shared/Translate/EN/IG_UI.json:5`；`2873290424/mods/70dodge/42.13/media/lua/shared/Translate/EN/IG_UI_EN.txt:4`
[^9]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgePD.txt:24`
[^10]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/IG_UI.json:15861`
[^11]: `2873290424/mods/70dodge/common/media/lua/shared/Translate/EN/IG_UI.json:3`；`2873290424/mods/70dodge/42.13/media/lua/shared/Translate/EN/IG_UI_EN.txt:2`
[^12]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeRT.txt:43`
[^13]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/IG_UI.json:15862`
[^14]: `2873290424/mods/70dodge/common/media/lua/shared/Translate/EN/IG_UI.json:4`；`2873290424/mods/70dodge/42.13/media/lua/shared/Translate/EN/IG_UI_EN.txt:3`
[^15]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeTA.txt:44`
[^16]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_vehiclesitems.txt:5`
[^17]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_vehiclesitems.txt:136`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_doors.txt:23`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_doors.txt:74`
[^18]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_vehiclesitems.txt:215`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_frontBumper.txt:33`
[^19]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_vehiclesitems.txt:153`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_windows.txt:42`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_windows.txt:68`
[^20]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_vehiclesitems.txt:72`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_hoods.txt:153`
[^21]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_vehiclesitems.txt:57`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_hoods.txt:38`
[^22]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_vehiclesitems.txt:230`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_rearBumper.txt:33`
[^23]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_vehiclesitems.txt:168`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_windows.txt:235`
[^24]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_vehiclesitems.txt:87`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeBG.txt:252`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_hoods.txt:268`
[^25]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_vehiclesitems.txt:102`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeBG.txt:252`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_hoods.txt:268`
[^26]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_vehiclesitems.txt:119`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_trunkdoor.txt:14`
[^27]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_vehiclesitems.txt:183`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_windshields.txt:21`
[^28]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_vehiclesitems.txt:198`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_windshields.txt:79`
[^29]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_vehiclesitems.txt:23`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_seats.txt:37`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_seats.txt:52`
[^30]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_vehiclesitems.txt:39`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_seats.txt:67`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_seats.txt:82`
[^31]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_vehiclesitems.txt:387`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_armor.txt:110`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_armor.txt:174`
[^32]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_vehiclesitems.txt:247`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_frontBumper.txt:33`
[^33]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_vehiclesitems.txt:262`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_frontBumper.txt:33`
[^34]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_vehiclesitems.txt:277`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_frontBumper.txt:33`
[^35]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_vehiclesitems.txt:437`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70RT_roof.txt:80`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70RT_roof.txt:14`
[^36]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_vehiclesitems.txt:292`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_rearBumper.txt:33`
[^37]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_vehiclesitems.txt:307`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_rearBumper.txt:33`
[^38]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_vehiclesitems.txt:322`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_rearBumper.txt:33`
[^39]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_vehiclesitems.txt:405`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_spoiler.txt:22`
[^40]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_vehiclesitems.txt:420`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_spoiler.txt:22`
[^41]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_vehiclesitems.txt:339`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_armor.txt:42`
[^42]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_vehiclesitems.txt:355`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_armor.txt:42`
[^43]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_vehiclesitems.txt:371`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_armor.txt:238`
[^44]: `游戏原版/media/scripts/generated/items/normal.txt:12453`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeBG.txt:326`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeOP.txt:317`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgePD.txt:335`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeRT.txt:390`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeTA.txt:412`
[^45]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:449`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:164`
[^46]: `3171167894/mods/damnlib/42.20/media/scripts/commonItems/damnCommonTires_vehiclesitems.txt:128`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeBG.txt:241`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_spareTire.txt:15`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeOP.txt:251`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_tires.txt:111`
[^47]: `3171167894/mods/damnlib/42.20/media/scripts/commonItems/damnCommonTires_vehiclesitems.txt:168`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeBG.txt:241`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_spareTire.txt:15`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeOP.txt:251`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_tires.txt:111`
[^48]: `游戏原版/media/scripts/generated/items/drainable.txt:2387`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeBG.txt:349`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeOP.txt:340`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgePD.txt:358`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeRT.txt:413`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeTA.txt:435`
[^49]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:971`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:381`
[^50]: `3171167894/mods/damnlib/42.20/media/scripts/commonItems/damnCommonTires_vehiclesitems.txt:148`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeBG.txt:241`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_spareTire.txt:15`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeOP.txt:251`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_tires.txt:111`
[^51]: `游戏原版/media/scripts/generated/items/normal.txt:13037`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeBG.txt:274`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeOP.txt:273`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgePD.txt:276`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeRT.txt:346`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeTA.txt:360`
[^52]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1777`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:688`
[^53]: `游戏原版/media/scripts/generated/items/radio.txt:203`；`游戏原版/media/scripts/generated/vehicles/template_radio_HAM.txt:5`
[^54]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:3000`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25094`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1908`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:3486`
[^55]: `游戏原版/media/scripts/generated/items/radio.txt:229`；`游戏原版/media/scripts/generated/vehicles/template_radio_HAM.txt:5`
[^56]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:7376`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25095`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1909`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:3487`
[^57]: `游戏原版/media/scripts/generated/items/radio.txt:255`；`游戏原版/media/scripts/generated/vehicles/template_radio_HAM.txt:5`
[^58]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:7377`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25096`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:1910`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:3488`
[^59]: `游戏原版/media/scripts/generated/items/normal.txt:4661`；`游戏原版/media/scripts/generated/vehicles/template_headlight.txt:25`
[^60]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:6727`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25103`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2563`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:965`
[^61]: `游戏原版/media/scripts/generated/items/normal.txt:12214`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeBG.txt:384`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeOP.txt:375`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgePD.txt:393`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeRT.txt:448`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeTA.txt:470`
[^62]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2781`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1051`
[^63]: `游戏原版/media/scripts/generated/items/normal.txt:13211`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeBG.txt:316`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeOP.txt:309`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgePD.txt:325`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeRT.txt:382`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeTA.txt:402`
[^64]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2784`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1054`
[^65]: `游戏原版/media/scripts/generated/items/normal.txt:12316`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeBG.txt:401`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeOP.txt:392`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgePD.txt:410`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeRT.txt:465`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeTA.txt:487`
[^66]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:2787`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1057`
[^67]: `游戏原版/media/scripts/generated/items/normal.txt:12197`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeBG.txt:384`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeOP.txt:375`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgePD.txt:393`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeRT.txt:448`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeTA.txt:470`
[^68]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3220`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1136`
[^69]: `游戏原版/media/scripts/generated/items/normal.txt:13196`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeBG.txt:316`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeOP.txt:309`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgePD.txt:325`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeRT.txt:382`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeTA.txt:402`
[^70]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3223`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1139`
[^71]: `游戏原版/media/scripts/generated/items/normal.txt:12438`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeBG.txt:326`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeOP.txt:317`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgePD.txt:335`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeRT.txt:390`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeTA.txt:412`
[^72]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3229`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1145`
[^73]: `游戏原版/media/scripts/generated/items/normal.txt:12299`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeBG.txt:401`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeOP.txt:392`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgePD.txt:410`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeRT.txt:465`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeTA.txt:487`
[^74]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3232`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1148`
[^75]: `游戏原版/media/scripts/generated/items/normal.txt:12180`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeBG.txt:384`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeOP.txt:375`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgePD.txt:393`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeRT.txt:448`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeTA.txt:470`
[^76]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3256`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1166`
[^77]: `游戏原版/media/scripts/generated/items/normal.txt:13181`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeBG.txt:316`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeOP.txt:309`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgePD.txt:325`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeRT.txt:382`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeTA.txt:402`
[^78]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3259`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1169`
[^79]: `3171167894/mods/damnlib/42.20/media/scripts/commonItems/damnCommonRoofracks_vehiclesitems.txt:7`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_roofrack.txt:14`
[^80]: `游戏原版/media/scripts/generated/items/radio.txt:308`；`游戏原版/media/scripts/generated/vehicles/template_radio.txt:5`
[^81]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:7374`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25092`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3645`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:5128`
[^82]: `游戏原版/media/scripts/generated/items/radio.txt:335`；`游戏原版/media/scripts/generated/vehicles/template_radio.txt:5`
[^83]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:7375`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25093`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3649`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:5132`
[^84]: `游戏原版/media/scripts/generated/items/radio.txt:361`；`游戏原版/media/scripts/generated/vehicles/template_radio.txt:5`
[^85]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:3001`；`3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/ItemName.json:25091`；`3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:3651`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:5134`
[^86]: `游戏原版/media/scripts/generated/items/normal.txt:12423`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeBG.txt:326`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeOP.txt:317`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgePD.txt:335`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeRT.txt:390`；`2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeTA.txt:412`
[^87]: `3556544454/mods/B42Trans_CN_As1/42.0/media/lua/shared/Translate/CN/ItemName.json:4153`；`游戏原版/media/lua/shared/Translate/CN/ItemName.json:1544`
[^88]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6542`
[^89]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_recipes.txt:332`
[^90]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6546`
[^91]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_recipes.txt:423`
[^92]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6547`
[^93]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_recipes.txt:445`
[^94]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6548`
[^95]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_recipes.txt:467`
[^96]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6544`
[^97]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_recipes.txt:379`
[^98]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6533`
[^99]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_recipes.txt:98`
[^100]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6535`
[^101]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_recipes.txt:149`
[^102]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6538`
[^103]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_recipes.txt:219`
[^104]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6540`
[^105]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_recipes.txt:285`
[^106]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6537`
[^107]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_recipes.txt:197`
[^108]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6541`
[^109]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_recipes.txt:308`
[^110]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6549`
[^111]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_recipes.txt:490`
[^112]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6550`
[^113]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_recipes.txt:512`
[^114]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6551`
[^115]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_recipes.txt:535`
[^116]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6545`
[^117]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_recipes.txt:401`
[^118]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6536`
[^119]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_recipes.txt:173`
[^120]: `2873290424/mods/70dodge/42.13/media/lua/shared/Translate/EN/Recipes_EN.txt:12`
[^121]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_recipes.txt:241`
[^122]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6539`
[^123]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_recipes.txt:263`
[^124]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6543`
[^125]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_recipes.txt:356`
[^126]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6552`
[^127]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_recipes.txt:558`
[^128]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6529`
[^129]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_recipes.txt:4`
[^130]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6534`
[^131]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_recipes.txt:124`
[^132]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6531`
[^133]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_recipes.txt:50`
[^134]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6530`
[^135]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_recipes.txt:26`
[^136]: `3556540080/mods/B42ModTrans_CN_As1/42.22/media/lua/shared/Translate/CN/Recipes.json:6532`
[^137]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodge_recipes.txt:74`
[^138]: `3171167894/mods/damnlib/42.20/media/scripts/damnCraft/items_damnCraft.txt:586`
[^139]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeBG.txt:349`
[^140]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeBG.txt:384`
[^141]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:5`
[^142]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:18`
[^143]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:31`
[^144]: `游戏原版/media/scripts/generated/vehicles/template_brake.txt:44`
[^145]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_frontBumper.txt:33`
[^146]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_rearBumper.txt:33`
[^147]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_armor.txt:110`
[^148]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_armor.txt:174`
[^149]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_spareTire.txt:15`
[^150]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_spoiler.txt:22`
[^151]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_armor.txt:42`
[^152]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_armor.txt:238`
[^153]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70RT_roof.txt:80`
[^154]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_roofrack.txt:14`
[^155]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_trunk.txt:5`
[^156]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_doors.txt:125`
[^157]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_doors.txt:23`
[^158]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_doors.txt:74`
[^159]: `游戏原版/media/scripts/generated/vehicles/template_engine.txt:5`
[^160]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeBG.txt:252`
[^161]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeBG.txt:326`
[^162]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeBG.txt:274`
[^163]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:25`
[^164]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:5`
[^165]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:15`
[^166]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:20`
[^167]: `游戏原版/media/scripts/generated/vehicles/template_headlight.txt:10`
[^168]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeBG.txt:362`
[^169]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeBG.txt:316`
[^170]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeBG.txt:372`
[^171]: `游戏原版/media/scripts/generated/vehicles/template_radio.txt:5`
[^172]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeBG.txt:418`
[^173]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_seats.txt:97`
[^174]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_seats.txt:37`
[^175]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_seats.txt:52`
[^176]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_seats.txt:67`
[^177]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_seats.txt:82`
[^178]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeBG.txt:401`
[^179]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:5`
[^180]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:18`
[^181]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:31`
[^182]: `游戏原版/media/scripts/generated/vehicles/template_suspension.txt:44`
[^183]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/70dodgeBG.txt:241`
[^184]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_tires.txt:22`
[^185]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_tires.txt:46`
[^186]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_tires.txt:68`
[^187]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_tires.txt:87`
[^188]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_trunk.txt:24`
[^189]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_trunkdoor.txt:14`
[^190]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_windows.txt:94`
[^191]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_windows.txt:42`
[^192]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_windows.txt:68`
[^193]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_windows.txt:235`
[^194]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_windows.txt:146`
[^195]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_windows.txt:191`
[^196]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_windshields.txt:21`
[^197]: `2873290424/mods/70dodge/42.13/media/scripts/vehicles/template_DG70_windshields.txt:79`
