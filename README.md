# Grsh PZ Modpack · B42.22 中文查询手册

档案视图 `b422-compat`：102 个 Mod 中 100 条属于日常组合；合并附属项后 98 份当前档案。

从[完整索引](mod_archives/INDEX.md)找 Mod，再复制该页整车表或物品表的完整 ID。中文解释与实际游戏显示名分列，缺译和冲突均有标记。
日常入口为 `A004/start-server.bat`、`A004/start-client.bat`，默认 `b422-main`。

- [兼容与迁移说明](COMPATIBILITY.md)：补丁证据与待验收项。
- [档案格式与统计规则](mod_archives/_TEMPLATE.md)。
- [迁移前历史清单](archive/pre-b422-promotion-20261112/README.md)。

## 组合与验证边界

| 组合 | Client / Server | 世界 |
| --- | --- | --- |
| `b422-main` | 100 / 93 | `b422batch2` |
| `b422-compat-render` | 54 / 50 | `b422compatrender` |
| `b422-compat-rv` | 60 / 56 | `b422compatrv` |
| `b422-compat` | 102 / 95 | `b422compat` |

仅客户端项 7 条：`PzPerformanceFixes`、`42_VSGirlBodySFW`、`42_VSGirlBody_Fix`、`BB_WhereAmI`、`83amgeneralM923extra`、`74amgeneralM151A2extra`、`CarBatteryChargerModel_Viewpoint`。
当前数值来自有效 common / 版本层和 Overlay 的静态定义；整车包括覆盖原版的定义，物品不混入旧分支、模板或配方产出引用。
完整原件目录体积单独统计。源码、Owner 截图、游戏实刷是不同证据层；本轮没有游戏运行验证。

## 按 Mod 查询

“实际文件夹名”对应 `./Zomboid/mods/` 下的目录原名；合并档案会列出全部子 Mod 文件夹。点击 Steam ID 直达工坊页面，点击“详细文档”查看内容与使用方法。
载具数按当前有效整车定义统计（含覆盖原版）；物品数按本 Mod 定义统计（含在详情中单列的内部保留项），共享物品不重复计入。

### 核心框架与渲染

| 中文名 | 实际文件夹名 | Steam ID | 载具数 | 物品数 | 分发端 | 归属 | 详细文档 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 僵尸伙伴 | `ZombieBuddy` | [3619862853](https://steamcommunity.com/sharedfiles/filedetails/?id=3619862853) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/3619862853_ZombieBuddy_模组框架与3D动画核心.md) |
| 视角重构 | `Viewpoint` | [3809306528](https://steamcommunity.com/sharedfiles/filedetails/?id=3809306528) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/3809306528_Viewpoint_第一人称3D渲染核心.md) |
| 右键修复 | `ViewpointRightClick` | [3819018807](https://steamcommunity.com/sharedfiles/filedetails/?id=3819018807) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/3819018807_Viewpoint_-_Right_Click_Fix_右键直接打开指向物体菜单.md) |
| 视角屋顶 | `ViewpointRoofs` | [3817294484](https://steamcommunity.com/sharedfiles/filedetails/?id=3817294484) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/3817294484_Viewpoint_-_Roofs_WIP_屋顶遮挡与显示.md) |
| 封窗木条修复 | `ViewpointBarricade` | [3815033191](https://steamcommunity.com/sharedfiles/filedetails/?id=3815033191) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/3815033191_Viewpoint_-_Barricade_Fix_木质金属封窗位置修正.md) |
| 3D 栅栏 | `ViewpointFences3D` | [3814486926](https://steamcommunity.com/sharedfiles/filedetails/?id=3814486926) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/3814486926_Viewpoint_-_3D_Fences_把栅栏变成有厚度的_3D_模型.md) |
| 3D 生活道具 | `ViewpointLivingProps` | [3816442251](https://steamcommunity.com/sharedfiles/filedetails/?id=3816442251) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/3816442251_Viewpoint_Living_Props_把室内外小物件变成_3D_模型.md) |
| Raccoon City 地图家具 | `aparosa_vpmo_RaccoonCityB42` | [3816419379](https://steamcommunity.com/sharedfiles/filedetails/?id=3816419379) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/3816419379_Project_Viewpoint_Map_Mod_Furniture_-_Sprite_Edition_给地图_mod_补_3D_家具.md) |
| 地图烘焙修复 | `PV-modmapbakefix` | [3813929757](https://steamcommunity.com/sharedfiles/filedetails/?id=3813929757) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/3813929757_Project_Viewpoint_General_Mod_Map_Fix_修复地图_mod_的烘焙与显示.md) |
| 3D 货架 | `ProjectViewpointShelves` | [3815931973](https://steamcommunity.com/sharedfiles/filedetails/?id=3815931973) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/3815931973_Project_Viewpoint_KKs_Shelves_in_3D_把货架变成有状态的_3D_模型.md) |
| 6282 模型库 | `PZVoxelStudioViewpoint` | [3810302175](https://steamcommunity.com/sharedfiles/filedetails/?id=3810302175) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/3810302175_6282_3D_models_for_Viewpoint_sour_kisel_3D模型与贴图素材库.md) |
| 3D 门与车库门 | `BasileDoors3D` | [3818859807](https://steamcommunity.com/sharedfiles/filedetails/?id=3818859807) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/3818859807_Project_Viewpoint_-_3D_Doors_Gates_and_Garages_门与栅门的立体模型替换.md) |
| Viewpoint 视觉修复 | `ViewpointVisualFixes` | [3821308495](https://steamcommunity.com/sharedfiles/filedetails/?id=3821308495) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/3821308495_ViewpointVisualFixes_修正_Viewpoint_的视觉细节.md) |

### 角色与外观

| 中文名 | 实际文件夹名 | Steam ID | 载具数 | 物品数 | 分发端 | 归属 | 详细文档 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 少前2 整备室（PMX 预览） | `AimohPmxPreview` | [3834454638](https://steamcommunity.com/sharedfiles/filedetails/?id=3834454638) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/3834454638_R116_把少前2角色模型搬进僵毁.md) |
| VSGirlBody SFW 身形 | `VariableSkinSFW` | [3640496116](https://steamcommunity.com/sharedfiles/filedetails/?id=3640496116) | 0 | 17 | 仅客户端 | 日常 | [详细文档](mod_archives/3640496116_VSGirlBody_S_SFW_女性角色身形与服装适配.md) |
| VSGirlBody 修复 | `VariableSkinFix` | [3640496116](https://steamcommunity.com/sharedfiles/filedetails/?id=3640496116) | 0 | 0 | 仅客户端 | 日常 | [详细文档](mod_archives/3640496116_VSGirlBody_Fix_身形包的兼容修复.md) |
| VSGirlBody 动态身体 | `VariableSkinBoobBounce` | [3640496116](https://steamcommunity.com/sharedfiles/filedetails/?id=3640496116) | 0 | 0 | 双端 | 兼容候选 | [详细文档](mod_archives/3640496116_VSGirlBodyBoobBounceRequires_ZombieBuddy_身体模型动态效果.md) |
| VSGirlBody 动态视角桥接 | `VariableSkinBoobBounceViewpoint` | [3640496116](https://steamcommunity.com/sharedfiles/filedetails/?id=3640496116) | 0 | 0 | 双端 | 兼容候选 | [详细文档](mod_archives/3640496116_VSGirlBodyBoobBounceViewpoint_动态身体的Viewpoint桥接.md) |

### 修复与兼容

| 中文名 | 实际文件夹名 | Steam ID | 载具数 | 物品数 | 分发端 | 归属 | 详细文档 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 数值修复 | `FixNaNStats` | [3627071412](https://steamcommunity.com/sharedfiles/filedetails/?id=3627071412) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/3627071412_Fix_NaN_Stats_B42.13-42.22_NaN属性修正.md) |
| KI5 载具零件修复 | `ProjectViewpoint-KI5VehiclePartsFix` | [3815019204](https://steamcommunity.com/sharedfiles/filedetails/?id=3815019204) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/3815019204_Project_Viewpoint_-_KI5_Vehicle_Parts_Fix_修正_KI5_载具零件的显示位置.md) |
| 载具外壳修复 | `ViewpointVehicleShellFix` | [3819801335](https://steamcommunity.com/sharedfiles/filedetails/?id=3819801335) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/3819801335_Viewpoint_-_Vehicle_Shell_Fix_修正_Viewpoint_载具_3D_外壳.md) |
| 载具零件喷漆 | `ViewpointPartPaint` | [3834561718](https://steamcommunity.com/sharedfiles/filedetails/?id=3834561718) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/3834561718_Viewpoint_-_Part_Paint_给_3D_载具零件上色.md) |
| KI5 血迹材质修复 | `ViewpointKI5Materials` | [3819702412](https://steamcommunity.com/sharedfiles/filedetails/?id=3819702412) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/3819702412_Project_Viewpoint_-_KI5_Blood_Texture_Fix_修正KI5车辆血迹材质.md) |

### 性能优化

| 中文名 | 实际文件夹名 | Steam ID | 载具数 | 物品数 | 分发端 | 归属 | 详细文档 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 性能修复 | `PzPerformanceFixes` | [3826630779](https://steamcommunity.com/sharedfiles/filedetails/?id=3826630779) | 0 | 0 | 仅客户端 | 日常 | [详细文档](mod_archives/3826630779_PzPerformanceFixes_帧率与卡顿优化.md) |
| 模组调度优化 | `SuPerfCore` | [3825832401](https://steamcommunity.com/sharedfiles/filedetails/?id=3825832401) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/3825832401_模组统一调度与优化subieliSuSir_模组加载调度提速.md) |

### 界面、库存与制作

| 中文名 | 实际文件夹名 | Steam ID | 载具数 | 物品数 | 分发端 | 归属 | 详细文档 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Neat界面框架 | `NeatUI_Framework` | [3508537032](https://steamcommunity.com/sharedfiles/filedetails/?id=3508537032) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/3508537032_NeatUI_Framework_制作界面框架.md) |
| Neat制作 | `Neat_Crafting` | [3502080466](https://steamcommunity.com/sharedfiles/filedetails/?id=3502080466) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/3502080466_Neat_Crafting_制作界面重制.md) |
| 烹饪重制 | `Project_Cook` | [3490188370](https://steamcommunity.com/sharedfiles/filedetails/?id=3490188370) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/3490188370_Project_Cook_烹饪系统重做.md) |
| 分类整理 | `BetterSorting` | [2313387159](https://steamcommunity.com/sharedfiles/filedetails/?id=2313387159) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/2313387159_Better_Sorting_库存分类菜单.md) |
| 就近存取 | `ProximityInventory` | [2847184718](https://steamcommunity.com/sharedfiles/filedetails/?id=2847184718) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/2847184718_Proximity_Inventory_B42_周边容器一键取放.md) |
| 地图图例 | `MapLegendUI` | [2710167561](https://steamcommunity.com/sharedfiles/filedetails/?id=2710167561) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/2710167561_Map_Legend_UI_地图图标说明.md) |
| CleanUI 清爽界面 | `CleanUI` | [3437629766](https://steamcommunity.com/sharedfiles/filedetails/?id=3437629766) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/3437629766_CleanUI_更紧凑可配置的库存与拾取界面.md) |
| CleanHotBar 清爽快捷栏 | `CleanHotBar` | [3461263912](https://steamcommunity.com/sharedfiles/filedetails/?id=3461263912) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/3461263912_CleanHotBar_更清晰的可配置快捷栏.md) |
| 自动整理 | `P4TidyUpMeister` | [2769706949](https://steamcommunity.com/sharedfiles/filedetails/?id=2769706949) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/2769706949_Tidy_Up_Meister_库存自动归位.md) |
| 沙盒选项 | `B42SandboxOptions` | [3386906181](https://steamcommunity.com/sharedfiles/filedetails/?id=3386906181) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/3386906181_B42_Sandbox_Options_游戏内改沙盒设置.md) |

### 汉化

| 中文名 | 实际文件夹名 | Steam ID | 载具数 | 物品数 | 分发端 | 归属 | 详细文档 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 统一模组汉化 | `B42ModTrans_CN_As1` | [3556540080](https://steamcommunity.com/sharedfiles/filedetails/?id=3556540080) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/3556540080_B42统一模组汉化_模组文本汉化.md) |
| 统一中文汉化 | `B42Trans_CN_As1` | [3556544454](https://steamcommunity.com/sharedfiles/filedetails/?id=3556544454) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/3556544454_B42统一中文汉化_排序置底_游戏本体文本汉化.md) |
| 老余汉化JAVA版 | `LaoYuTranslationJava` | [3810637496](https://steamcommunity.com/sharedfiles/filedetails/?id=3810637496) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/3810637496_老余汉化JAVA版_Java_界面简中汉化.md) |

### 玩法与移动

| 中文名 | 实际文件夹名 | Steam ID | 载具数 | 物品数 | 分发端 | 归属 | 详细文档 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 折叠梯 | `Ladders Collapsible` | [3629835761](https://steamcommunity.com/sharedfiles/filedetails/?id=3629835761) | 0 | 6 | 双端 | 日常 | [详细文档](mod_archives/3629835761_Ladders!_B42.22+_Craftable_and_movable_ladder_B42.22_可制作、可移动的折叠梯.md) |

### 工具与调试

| 中文名 | 实际文件夹名 | Steam ID | 载具数 | 物品数 | 分发端 | 归属 | 详细文档 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 调试菜单社区版 | `DebugMenu` | [3735377688](https://steamcommunity.com/sharedfiles/filedetails/?id=3735377688) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/3735377688_B4241调试菜单社区版_DebugMenu_Community_右键多级调试与管理员菜单.md) |
| 坐标显示 | `WhereAmI` | [3097650043](https://steamcommunity.com/sharedfiles/filedetails/?id=3097650043) | 0 | 0 | 仅客户端 | 日常 | [详细文档](mod_archives/3097650043_Where_Am_I_显示所在位置.md) |

### KI5 载具系列

| 中文名 | 实际文件夹名 | Steam ID | 载具数 | 物品数 | 分发端 | 归属 | 详细文档 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 载具资源库 | `damnlib` | [3171167894](https://steamcommunity.com/sharedfiles/filedetails/?id=3171167894) | 0 | 229 | 双端 | 日常 | [详细文档](mod_archives/3171167894_that_DAMN_Library_KI5载具公共资源.md) |
| 通用函数库 | `YetAnotherPZLib` | [3624971238](https://steamcommunity.com/sharedfiles/filedetails/?id=3624971238) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/3624971238_Yet_Another_PZ_Library_KI5脚本依赖库.md) |
| Trailers! 拖车合集 | `KI5trailers` | [3330403100](https://steamcommunity.com/sharedfiles/filedetails/?id=3330403100) | 7 | 11 | 双端 | 日常 | [详细文档](mod_archives/3330403100_Trailers!_多用途拖车与货运挂车.md) |
| Containers! 集装箱 | `isoContainers` | [2625625421](https://steamcommunity.com/sharedfiles/filedetails/?id=2625625421) | 9 | 5 | 双端 | 日常 | [详细文档](mod_archives/2625625421_Containers!_可堆叠、可搬运的集装箱.md) |
| M998 悍马 + M101A3 拖车 | `92amgeneralM998` | [2642541073](https://steamcommunity.com/sharedfiles/filedetails/?id=2642541073) | 3 | 22 | 双端 | 日常 | [详细文档](mod_archives/2642541073_92_AM_General_M998_+_M101A3_Trailer_军版悍马与货运拖车.md) |
| 1970 道奇挑战者 | `70dodge` | [2873290424](https://steamcommunity.com/sharedfiles/filedetails/?id=2873290424) | 5 | 28 | 双端 | 日常 | [详细文档](mod_archives/2873290424_70_Dodge_Challenger_70_年代美式肌肉车.md) |
| '91 Range Rover Classic | `91range` | [2409333430](https://steamcommunity.com/sharedfiles/filedetails/?id=2409333430) | 2 | 26 | 双端 | 日常 | [详细文档](mod_archives/2409333430_91_RANGE_ROVER_Classic_经典英式越野_SUV.md) |
| '88 Chevrolet S10 | `88chevyS10` | [2886832936](https://steamcommunity.com/sharedfiles/filedetails/?id=2886832936) | 1 | 12 | 双端 | 日常 | [详细文档](mod_archives/2886832936_88_Chevrolet_S10_紧凑型工作皮卡.md) |
| '92 Nissan Skyline GT-R R32 | `92nissanGTR` | [2846036306](https://steamcommunity.com/sharedfiles/filedetails/?id=2846036306) | 2 | 38 | 双端 | 日常 | [详细文档](mod_archives/2846036306_92_NISSAN_Skyline_GT-R_R32_日系性能跑车.md) |
| '84 Mercedes W460 | `84mercW460` | [2805630347](https://steamcommunity.com/sharedfiles/filedetails/?id=2805630347) | 4 | 34 | 双端 | 日常 | [详细文档](mod_archives/2805630347_84_Mercedes_Benz_W460_方盒子越野车.md) |
| '87 Ford B700/F700 | `87fordB700` | [3110911330](https://steamcommunity.com/sharedfiles/filedetails/?id=3110911330) | 6 | 52 | 双端 | 日常 | [详细文档](mod_archives/3110911330_87_Ford_B700F700_Trucks_中型卡车底盘.md) |
| '90 Ford F350 救护车 | `90fordF350ambulance` | [2952802178](https://steamcommunity.com/sharedfiles/filedetails/?id=2952802178) | 2 | 20 | 双端 | 日常 | [详细文档](mod_archives/2952802178_90_Ford_F350_Ambulance_Type_1_可当移动医疗点的救护车.md) |
| '86 Ford Econoline E-150 | `86fordE150` | [2870394916](https://steamcommunity.com/sharedfiles/filedetails/?id=2870394916) | 12 | 51 | 双端 | 日常 | [详细文档](mod_archives/2870394916_86_Ford_Econoline_E150_厢式货车面包车.md) |
| '78 AM General M35 军卡 | `78amgeneralM35A2` | [2799152995](https://steamcommunity.com/sharedfiles/filedetails/?id=2799152995) | 4 | 19 | 双端 | 日常 | [详细文档](mod_archives/2799152995_78_AM_General_M35_Series_Trucks_军用六驱卡车.md) |
| '82 Jeep J10 | `82jeepJ10` | [2886832257](https://steamcommunity.com/sharedfiles/filedetails/?id=2886832257) | 4 | 14 | 双端 | 日常 | [详细文档](mod_archives/2886832257_82_Jeep_J10_全尺寸皮卡.md) |

### 房车

| 中文名 | 实际文件夹名 | Steam ID | 载具数 | 物品数 | 分发端 | 归属 | 详细文档 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 厢式房车后端 | `GridVansHost` | [3821174725](https://steamcommunity.com/sharedfiles/filedetails/?id=3821174725) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/3821174725_3D_Vans_Host_backend_车厢家具与乘员同步后端.md) |
| 3D 厢式房车 | `GridVans` | [3821174725](https://steamcommunity.com/sharedfiles/filedetails/?id=3821174725) | 1 | 0 | 双端 | 日常 | [详细文档](mod_archives/3821174725_Viewpoint_-_3D_RV_Van_可摆家具的厢式房车.md) |
| DeadWorks 载具框架 | `DeadWorksVehicleFramework` | [3825724093](https://steamcommunity.com/sharedfiles/filedetails/?id=3825724093) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/3825724093_DeadWorks_Vehicle_Framework_房车内饰水电家具内核.md) |
| DeadWorks 沙盒调节 | `aparosa_DWVFTweaks` | [3826684062](https://steamcommunity.com/sharedfiles/filedetails/?id=3826684062) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/3826684062_DeadWorks_Vehicle_Framework_Tweaks_装甲水箱电池车重可调.md) |
| DeadWorks Nomad 房车 | `DeadWorksNomadRV` | [3820158673](https://steamcommunity.com/sharedfiles/filedetails/?id=3820158673) | 1 | 14 | 双端 | 日常 | [详细文档](mod_archives/3820158673_Nomad_RV_Nomad房车的DeadWorks分支.md) |
| DeadWorks Dale 房车 | `DeadWorksDaleRV` | [3820158673](https://steamcommunity.com/sharedfiles/filedetails/?id=3820158673) | 1 | 0 | 双端 | 日常 | [详细文档](mod_archives/3820158673_Dales_Chieftain_RV_Dale房车的DeadWorks分支.md) |

### 驾驶与载具交互

| 中文名 | 实际文件夹名 | Steam ID | 载具数 | 物品数 | 分发端 | 归属 | 详细文档 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 驾驶动态 | `ImmersiveDriving` | [3817413313](https://steamcommunity.com/sharedfiles/filedetails/?id=3817413313) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/3817413313_Project_Viewpoint_-_Immersive_Driving_驾驶镜头与乘员动画.md) |
| 换挡动画 | `ShiftYourGear` | [3838041847](https://steamcommunity.com/sharedfiles/filedetails/?id=3838041847) | 26 | 0 | 双端 | 日常 | [详细文档](mod_archives/3838041847_Shift_Your_Gear_FIXED_换挡手部与挡杆动画.md) |
| 方向盘模型 | `ViewpointVanillaSteering` | [3835182791](https://steamcommunity.com/sharedfiles/filedetails/?id=3835182791) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/3835182791_Project_Viewpoint_-_Vanilla_Steering_原版方向盘模型与转向动画.md) |
| 车内开火 | `ViewpointDriveByShooting` | [3826176290](https://steamcommunity.com/sharedfiles/filedetails/?id=3826176290) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/3826176290_Project_Viewpoint_-_Drive-By_Shooting_车内开火与坐姿动作.md) |
| 车内瞄准姿态修复 | `CarRoofFix` | [3781616141](https://steamcommunity.com/sharedfiles/filedetails/?id=3781616141) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/3781616141_Vehicle_Aim_Roof_Fix_车内瞄准不再站起.md) |
| 上下车姿态修复 | `CarEnterExitFix` | [3785695033](https://steamcommunity.com/sharedfiles/filedetails/?id=3785695033) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/3785695033_Vehicle_EnterExit_Fix_上下车姿态修复.md) |

### KI5 载具与载具功能件

| 中文名 | 实际文件夹名 | Steam ID | 载具数 | 物品数 | 分发端 | 归属 | 详细文档 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 消防泵车 + 云梯 | `90pierceArrow` | [2942793445](https://steamcommunity.com/sharedfiles/filedetails/?id=2942793445) | 2 | 23 | 双端 | 日常 | [详细文档](mod_archives/2942793445_90pierceArrow_消防泵车+云梯.md) |
| 警用拦截者 | `99fordCVPI` | [2971246021](https://steamcommunity.com/sharedfiles/filedetails/?id=2971246021) | 2 | 15 | 双端 | 日常 | [详细文档](mod_archives/2971246021_99fordCVPI_警用拦截者.md) |
| 90 年代警车 | `92fordCVPI` | [2962175696](https://steamcommunity.com/sharedfiles/filedetails/?id=2962175696) | 11 | 17 | 双端 | 日常 | [详细文档](mod_archives/2962175696_92fordCVPI_90年代警车.md) |
| 警车底盘的旅行车 | `91fordLTD` | [3366300557](https://steamcommunity.com/sharedfiles/filedetails/?id=3366300557) | 8 | 23 | 双端 | 日常 | [详细文档](mod_archives/3366300557_91fordLTD_警车底盘的旅行车.md) |
| 80 年代全尺寸轿车 | `85chevyCaprice` | [3413704851](https://steamcommunity.com/sharedfiles/filedetails/?id=3413704851) | 18 | 11 | 双端 | 日常 | [详细文档](mod_archives/3413704851_85chevyCaprice_80年代全尺寸轿车.md) |
| 美国乡村 SUV | `89fordBronco` | [2886833398](https://steamcommunity.com/sharedfiles/filedetails/?id=2886833398) | 3 | 9 | 双端 | 日常 | [详细文档](mod_archives/2886833398_89fordBronco_美国乡村SUV.md) |
| 越野吉普 | `92jeepYJ`<br>`92jeepYJJP18` | [3287727378](https://steamcommunity.com/sharedfiles/filedetails/?id=3287727378) | 4 | 41 | 双端 | 日常 | [详细文档](mod_archives/3287727378_92jeepYJ_越野吉普（含JP18变体）.md) |
| 早期切诺基 | `84jeepXJ` | [3409287192](https://steamcommunity.com/sharedfiles/filedetails/?id=3409287192) | 5 | 22 | 双端 | 日常 | [详细文档](mod_archives/3409287192_84jeepXJ_早期切诺基.md) |
| 日系硬派 SUV | `89trooper` | [2932549988](https://steamcommunity.com/sharedfiles/filedetails/?id=2932549988) | 3 | 23 | 双端 | 日常 | [详细文档](mod_archives/2932549988_89trooper_日系硬派SUV.md) |
| 日系小皮卡 | `88toyotaHilux` | [3435796523](https://steamcommunity.com/sharedfiles/filedetails/?id=3435796523) | 3 | 24 | 双端 | 日常 | [详细文档](mod_archives/3435796523_88toyotaHilux_日系小皮卡.md) |
| 紧凑皮卡 | `91fordRanger` | [3539691958](https://steamcommunity.com/sharedfiles/filedetails/?id=3539691958) | 6 | 21 | 双端 | 日常 | [详细文档](mod_archives/3539691958_91fordRanger_紧凑皮卡.md) |
| F 系全尺寸皮卡 | `93fordF350` | [3073430075](https://steamcommunity.com/sharedfiles/filedetails/?id=3073430075) | 11 | 33 | 双端 | 日常 | [详细文档](mod_archives/3073430075_93fordF350_F系全尺寸皮卡.md) |
| 甲壳虫 | `63beetle` | [3005903549](https://steamcommunity.com/sharedfiles/filedetails/?id=3005903549) | 3 | 27 | 双端 | 日常 | [详细文档](mod_archives/3005903549_63beetle_甲壳虫.md) |
| T2 面包车 | `63Type2Van` | [3041122351](https://steamcommunity.com/sharedfiles/filedetails/?id=3041122351) | 4 | 35 | 双端 | 日常 | [详细文档](mod_archives/3041122351_63Type2Van_T2面包车.md) |
| 沃尔沃 240 系 | `89volvo200` | [3292659291](https://steamcommunity.com/sharedfiles/filedetails/?id=3292659291) | 3 | 48 | 双端 | 日常 | [详细文档](mod_archives/3292659291_89volvo200_沃尔沃240系.md) |
| 90 年代家用轿车 | `93fordTaurus` | [3088951320](https://steamcommunity.com/sharedfiles/filedetails/?id=3088951320) | 3 | 33 | 双端 | 日常 | [详细文档](mod_archives/3088951320_93fordTaurus_90年代家用轿车.md) |
| 小型 MPV | `89dodgeCaravan` | [3034636011](https://steamcommunity.com/sharedfiles/filedetails/?id=3034636011) | 3 | 24 | 双端 | 日常 | [详细文档](mod_archives/3034636011_89dodgeCaravan_小型MPV.md) |
| 省油小车 | `91geoMetro` | [3008795514](https://steamcommunity.com/sharedfiles/filedetails/?id=3008795514) | 1 | 20 | 双端 | 日常 | [详细文档](mod_archives/3008795514_91geoMetro_省油小车.md) |
| 肌肉车 | `67gt500` | [3026723485](https://steamcommunity.com/sharedfiles/filedetails/?id=3026723485) | 2 | 24 | 双端 | 日常 | [详细文档](mod_archives/3026723485_67gt500_肌肉车（含Eleanor涂装）.md) |
| 肌肉车 | `69camaro` | [2991201484](https://steamcommunity.com/sharedfiles/filedetails/?id=2991201484) | 2 | 22 | 双端 | 日常 | [详细文档](mod_archives/2991201484_69camaro_肌肉车.md) |
| 肌肉车 | `69charger` | [3631989559](https://steamcommunity.com/sharedfiles/filedetails/?id=3631989559) | 5 | 29 | 双端 | 日常 | [详细文档](mod_archives/3631989559_69charger_肌肉车.md) |
| 军用重卡 | `83amgeneralM923`<br>`83amgeneralM923extra` | [2811383142](https://steamcommunity.com/sharedfiles/filedetails/?id=2811383142) | 1 | 18 | `83amgeneralM923`：双端<br>`83amgeneralM923extra`：仅客户端 | 日常 | [详细文档](mod_archives/2811383142_83amgeneralM923_军用重卡（含额外贴图）.md) |
| 军用吉普 | `74amgeneralM151A2`<br>`74amgeneralM151A2extra` | [2785549133](https://steamcommunity.com/sharedfiles/filedetails/?id=2785549133) | 3 | 14 | `74amgeneralM151A2`：双端<br>`74amgeneralM151A2extra`：仅客户端 | 日常 | [详细文档](mod_archives/2785549133_74amgeneralM151A2_军用吉普（含额外贴图）.md) |
| 军用皮卡 + 拖车 | `86chevyCUCV` | [3428008364](https://steamcommunity.com/sharedfiles/filedetails/?id=3428008364) | 10 | 25 | 双端 | 日常 | [详细文档](mod_archives/3428008364_86chevyCUCV_军用皮卡+拖车.md) |
| 军用重型牵引车 | `82oshkoshM911` | [2618213077](https://steamcommunity.com/sharedfiles/filedetails/?id=2618213077) | 8 | 26 | 双端 | 日常 | [详细文档](mod_archives/2618213077_82oshkoshM911_军用重型牵引车.md) |
| 农用拖拉机 | `49ford8N` | [3171176891](https://steamcommunity.com/sharedfiles/filedetails/?id=3171176891) | 1 | 5 | 双端 | 日常 | [详细文档](mod_archives/3171176891_49ford8N_农用拖拉机.md) |
| 高尔夫球车 | `85clubMan` | [3330401526](https://steamcommunity.com/sharedfiles/filedetails/?id=3330401526) | 2 | 7 | 双端 | 日常 | [详细文档](mod_archives/3330401526_85clubMan_高尔夫球车.md) |
| 露营拖挂三件套 | `KI5campers` | [3670064951](https://steamcommunity.com/sharedfiles/filedetails/?id=3670064951) | 6 | 36 | 双端 | 日常 | [详细文档](mod_archives/3670064951_KI5campers_露营拖挂三件套.md) |
| 拖挂可见连接件 | `Visible Vehicle Coupling` | [3807182783](https://steamcommunity.com/sharedfiles/filedetails/?id=3807182783) | 0 | 0 | 双端 | 日常 | [详细文档](mod_archives/3807182783_Visible_Vehicle_Coupling_拖挂可见连接件.md) |
| 电瓶充电器 3D 模型 | `CarBatteryChargerModel`<br>`CarBatteryChargerModel_Viewpoint` | [3822775022](https://steamcommunity.com/sharedfiles/filedetails/?id=3822775022) | 0 | 0 | `CarBatteryChargerModel`：双端<br>`CarBatteryChargerModel_Viewpoint`：仅客户端 | 日常 | [详细文档](mod_archives/3822775022_CarBatteryChargerModel_电瓶充电器3D模型.md) |

## 更新档案

```bash
python -B tools/mod_archive.py --profile b422-compat
python -B tools/test_mod_archive.py
```

人工用途、稳定文件名和保留记录存于 `tools/mod_catalog.json`；再次生成保留视图外页面及人工记录。
`--out` 可先写预览目录；README 位于其父目录。新原件需要先补人工目录。生成过程不修改游戏、原件、运行树或存档。

<details><summary>保留的部署与验证说明（旧语境）</summary>

| 组合 | Client / Server | 世界 | 定位 |
| --- | --- | --- | --- |
| `b422-main` | 100 / 93 | `b422batch2` | 日常默认；render 3 + rv 6（rv jar 已打字节码补丁，待 Owner 复测）+ 驾驶扩展 6 + KI5 车队 28 辆与 2 个载具功能件 |
| `b422-compat-render` | 54 / 50 | `b422compatrender` | 日常去掉 rv 6 与驾驶扩展 6；独立世界备选，未启动 |
| `b422-compat-rv` | 60 / 56 | `b422compatrv` | 日常去掉驾驶扩展 6；独立世界备选，未启动 |
| `b422-compat` | 102 / 95 | `b422compat` | 日常加 2 条身体子模块候选；未启动 |

- 档案输入版本：`42.22.2`；当前日常底座为 B42.22.2，git `3d39148846`。
- 迁移前 52/48 已有双端加载证据；新路径仅服务端曾到达就绪，不能代替客户端联网与存档重进。
- 2026-11-12 Owner 授权五次调整日常：并入 render 4，并入 rv 6 并移出 DLSS、VisualFixes、Interiors，随后加回 VisualFixes 与 Interiors，再删除 Interiors 并并入驾驶扩展 6，最后并入 KI5 车队 28 辆与 2 个载具功能件；剩下 2 条身体子模块候选只有离线证据，**不是兼容通过**。
- Viewpoint 固定官方 0.1.6.2，与 R116 0.3.51 指纹绑定；不混用 nightly，也不加已被内置资源替代的旧 GF2 外置包。
- 七条仅客户端项：`PzPerformanceFixes`、`42_VSGirlBodySFW`、`42_VSGirlBody_Fix`、`BB_WhereAmI`，以及 KI5 三条贴图/补丁（`83amgeneralM923extra`、`74amgeneralM151A2extra`、`CarBatteryChargerModel_Viewpoint`）。进服后按服务端清单重载，不把它们仍有效当作已验证。
- 三汉化包必须双端，加载末尾依次是 `LaoYuTranslationJava` → `B42ModTrans_CN` → `B42Trans_CN`。
- rv 链（`GridVansHost`、`DeadWorksVehicleFramework`）原始 jar 引用 B42.21 才有的 `PlayerPacket.id`；日常用 `workspace/patches/mods/` 下的字节码 Overlay 改指 `PlayerPacket.player` + `ConnectionPlayer.getPlayer()`，原件不动。指纹在 `workspace/patches/overlay-guards.json`（23 条）。

</details>

所有 Mod 版权归各自作者。本手册不是独立 Review 或 Owner 玩法验收。
