# Grsh PZ Modpack · B42.22 开发主线

这里记录 A004 当前 Mod 原件、依赖、物品 ID 与兼容候选；不包含游戏或 Mod 二进制。
日常入口在 `A004/start-server.bat`、`A004/start-client.bat`，默认 `b422-main`。
本页是 `b422-compat` 的**档案视图**：64 条中 52 条属于日常组合，其余 12 条为兼容候选。生成档案不会切换运行组合。

## 从这里读

- [完整索引](mod_archives/INDEX.md)：按 Mod 查依赖、物品/载具 ID 和分发端。
- [兼容与迁移说明](COMPATIBILITY.md)：补丁、回退、未覆盖项与 Owner 验收。
- [档案模板](mod_archives/_TEMPLATE.md)：自动字段、人工简介与统计限制。
- [迁移前清单](archive/pre-b422-promotion-20261112/README.md)：历史资料，不是当前启用列表。

## 组合与验证边界

| 组合 | Client / Server | 世界 | 定位 |
| --- | --- | --- | --- |
| `b422-main` | 52 / 48 | `b422batch2` | 日常默认；迁移后联机/存档重进未验收 |
| `b422-compat-render` | 56 / 52 | `b422compatrender` | 兼容候选；仅静态检查，未启动 |
| `b422-compat-rv` | 62 / 58 | `b422compatrv` | 兼容候选；仅静态检查，未启动 |
| `b422-compat` | 64 / 60 | `b422compat` | 兼容候选；仅静态检查，未启动 |

- 档案输入版本：`42.22.2`；当前日常底座为 B42.22.2，git `3d39148846`。
- 迁移前 52/48 已有双端加载证据；新路径仅服务端曾到达就绪，不能代替客户端联网与存档重进。
- Owner 要求迁移收尾不启动游戏，因此新增候选只有离线依赖/版本/指纹证据，**不是兼容通过**。
- Viewpoint 固定官方 0.1.6.2，与 R116 0.3.51 指纹绑定；不混用 nightly，也不加已被内置资源替代的旧 GF2 外置包。
- 四条仅客户端项：`PzPerformanceFixes`、`42_VSGirlBodySFW`、`42_VSGirlBody_Fix`、`BB_WhereAmI`。进服后按服务端清单重载，不把它们仍有效当作已验证。
- 三汉化包必须双端，加载末尾依次是 `LaoYuTranslationJava` → `B42ModTrans_CN` → `B42Trans_CN`。
- 完整包目录统计：3.4 GB；脚本物品 450 条。多个版本目录、资源副本会使统计大于实际加载。

## Mod 索引（按用途）

“归属”区分日常与候选，不是运行验收结论。加载顺序以对应 profile 的 loadOrder 为准。

### 核心框架与渲染（15 个）

| 中文名 | 原名 | 工作坊 ID | 分发 | 归属 | 物品 | 档案 |
| --- | --- | --- | --- | --- | --- | --- |
| 3D 栅栏 | Viewpoint - 3D Fences | [`3814486926`](https://steamcommunity.com/sharedfiles/filedetails/?id=3814486926) | both | 日常 | 0 | [查看](mod_archives/3814486926_Viewpoint_-_3D_Fences_把栅栏变成有厚度的_3D_模型.md) |
| 3D 生活道具 | Viewpoint: Living Props | [`3816442251`](https://steamcommunity.com/sharedfiles/filedetails/?id=3816442251) | both | 日常 | 0 | [查看](mod_archives/3816442251_Viewpoint_Living_Props_把室内外小物件变成_3D_模型.md) |
| 3D 货架 | Project Viewpoint: KK's Shelves in 3D | [`3815931973`](https://steamcommunity.com/sharedfiles/filedetails/?id=3815931973) | both | 日常 | 0 | [查看](mod_archives/3815931973_Project_Viewpoint_KKs_Shelves_in_3D_把货架变成有状态的_3D_模型.md) |
| 3D 门与车库门 | Project Viewpoint - 3D Doors, Gates & Garages | [`3818859807`](https://steamcommunity.com/sharedfiles/filedetails/?id=3818859807) | both | 兼容候选 | 0 | [查看](mod_archives/3818859807_Project_Viewpoint_-_3D_Doors_Gates_and_Garages_门与栅门的立体模型替换.md) |
| 6282 模型库 | 6282 3D models for Viewpoint [sour_kisel] | [`3810302175`](https://steamcommunity.com/sharedfiles/filedetails/?id=3810302175) | both | 兼容候选 | 0 | [查看](mod_archives/3810302175_6282_3D_models_for_Viewpoint_sour_kisel_3D模型与贴图素材库.md) |
| DLSS 帧生成 | Viewpoint DLSS Frame Generation | [`3818838508`](https://steamcommunity.com/sharedfiles/filedetails/?id=3818838508) | both | 日常 | 0 | [查看](mod_archives/3818838508_Viewpoint_DLSS_Frame_Generation_给_Viewpoint_加_DLSS_帧生成.md) |
| Raccoon City 地图家具 | Project Viewpoint Map Mod Furniture - Sprite Edition | [`3816419379`](https://steamcommunity.com/sharedfiles/filedetails/?id=3816419379) | both | 日常 | 0 | [查看](mod_archives/3816419379_Project_Viewpoint_Map_Mod_Furniture_-_Sprite_Edition_给地图_mod_补_3D_家具.md) |
| Viewpoint 视觉修复 | ViewpointVisualFixes | [`3821308495`](https://steamcommunity.com/sharedfiles/filedetails/?id=3821308495) | both | 日常 | 0 | [查看](mod_archives/3821308495_ViewpointVisualFixes_修正_Viewpoint_的视觉细节.md) |
| 僵尸伙伴 | ZombieBuddy | [`3619862853`](https://steamcommunity.com/sharedfiles/filedetails/?id=3619862853) | both | 日常 | 0 | [查看](mod_archives/3619862853_ZombieBuddy_模组框架与3D动画核心.md) |
| 右键修复 | Viewpoint - Right Click Fix | [`3819018807`](https://steamcommunity.com/sharedfiles/filedetails/?id=3819018807) | both | 日常 | 0 | [查看](mod_archives/3819018807_Viewpoint_-_Right_Click_Fix_右键直接打开指向物体菜单.md) |
| 地图烘焙修复 | Project Viewpoint: General Mod Map Fix | [`3813929757`](https://steamcommunity.com/sharedfiles/filedetails/?id=3813929757) | both | 日常 | 0 | [查看](mod_archives/3813929757_Project_Viewpoint_General_Mod_Map_Fix_修复地图_mod_的烘焙与显示.md) |
| 封窗木条修复 | Viewpoint - Barricade Fix | [`3815033191`](https://steamcommunity.com/sharedfiles/filedetails/?id=3815033191) | both | 日常 | 0 | [查看](mod_archives/3815033191_Viewpoint_-_Barricade_Fix_木质金属封窗位置修正.md) |
| 视角屋顶 | Viewpoint - Roofs (WIP) | [`3817294484`](https://steamcommunity.com/sharedfiles/filedetails/?id=3817294484) | both | 日常 | 0 | [查看](mod_archives/3817294484_Viewpoint_-_Roofs_WIP_屋顶遮挡与显示.md) |
| 视角重构 | Viewpoint | [`3809306528`](https://steamcommunity.com/sharedfiles/filedetails/?id=3809306528) | both | 日常 | 0 | [查看](mod_archives/3809306528_Viewpoint_第一人称3D渲染核心.md) |
| 载具驾驶舱内饰 | Viewpoint Vehicle Interiors | [`3826550325`](https://steamcommunity.com/sharedfiles/filedetails/?id=3826550325) | both | 兼容候选 | 0 | [查看](mod_archives/3826550325_Viewpoint_Vehicle_Interiors_座椅仪表与顶灯细节.md) |

### 角色与外观（5 个）

| 中文名 | 原名 | 工作坊 ID | 分发 | 归属 | 物品 | 档案 |
| --- | --- | --- | --- | --- | --- | --- |
| VSGirlBody SFW 身形 | VSGirlBody_S_SFW | [`3640496116`](https://steamcommunity.com/sharedfiles/filedetails/?id=3640496116) | client | 日常 | 17 | [查看](mod_archives/3640496116_VSGirlBody_S_SFW_女性角色身形与服装适配.md) |
| VSGirlBody 修复 | VSGirlBody_Fix | [`3640496116`](https://steamcommunity.com/sharedfiles/filedetails/?id=3640496116) | client | 日常 | 0 | [查看](mod_archives/3640496116_VSGirlBody_Fix_身形包的兼容修复.md) |
| VSGirlBody 动态视角桥接 | VSGirlBodyBoobBounceViewpoint | [`3640496116`](https://steamcommunity.com/sharedfiles/filedetails/?id=3640496116) | both | 兼容候选 | 0 | [查看](mod_archives/3640496116_VSGirlBodyBoobBounceViewpoint_动态身体的Viewpoint桥接.md) |
| VSGirlBody 动态身体 | VSGirlBodyBoobBounce(Requires ZombieBuddy) | [`3640496116`](https://steamcommunity.com/sharedfiles/filedetails/?id=3640496116) | both | 兼容候选 | 0 | [查看](mod_archives/3640496116_VSGirlBodyBoobBounceRequires_ZombieBuddy_身体模型动态效果.md) |
| 少前2 整备室（PMX 预览） | R116 | [`3834454638`](https://steamcommunity.com/sharedfiles/filedetails/?id=3834454638) | both | 日常 | 0 | [查看](mod_archives/3834454638_R116_把少前2角色模型搬进僵毁.md) |

### 界面、库存与制作（10 个）

| 中文名 | 原名 | 工作坊 ID | 分发 | 归属 | 物品 | 档案 |
| --- | --- | --- | --- | --- | --- | --- |
| CleanHotBar 清爽快捷栏 | CleanHotBar | [`3461263912`](https://steamcommunity.com/sharedfiles/filedetails/?id=3461263912) | both | 日常 | 0 | [查看](mod_archives/3461263912_CleanHotBar_更清晰的可配置快捷栏.md) |
| CleanUI 清爽界面 | CleanUI | [`3437629766`](https://steamcommunity.com/sharedfiles/filedetails/?id=3437629766) | both | 日常 | 0 | [查看](mod_archives/3437629766_CleanUI_更紧凑可配置的库存与拾取界面.md) |
| Neat制作 | Neat Crafting | [`3502080466`](https://steamcommunity.com/sharedfiles/filedetails/?id=3502080466) | both | 日常 | 0 | [查看](mod_archives/3502080466_Neat_Crafting_制作界面重制.md) |
| Neat界面框架 | NeatUI_Framework | [`3508537032`](https://steamcommunity.com/sharedfiles/filedetails/?id=3508537032) | both | 日常 | 0 | [查看](mod_archives/3508537032_NeatUI_Framework_制作界面框架.md) |
| 分类整理 | Better Sorting | [`2313387159`](https://steamcommunity.com/sharedfiles/filedetails/?id=2313387159) | both | 日常 | 0 | [查看](mod_archives/2313387159_Better_Sorting_库存分类菜单.md) |
| 地图图例 | Map Legend UI | [`2710167561`](https://steamcommunity.com/sharedfiles/filedetails/?id=2710167561) | both | 日常 | 0 | [查看](mod_archives/2710167561_Map_Legend_UI_地图图标说明.md) |
| 就近存取 | Proximity Inventory B42 | [`2847184718`](https://steamcommunity.com/sharedfiles/filedetails/?id=2847184718) | both | 日常 | 0 | [查看](mod_archives/2847184718_Proximity_Inventory_B42_周边容器一键取放.md) |
| 沙盒选项 | [B42] Sandbox Options | [`3386906181`](https://steamcommunity.com/sharedfiles/filedetails/?id=3386906181) | both | 日常 | 0 | [查看](mod_archives/3386906181_B42_Sandbox_Options_游戏内改沙盒设置.md) |
| 烹饪重制 | Project Cook | [`3490188370`](https://steamcommunity.com/sharedfiles/filedetails/?id=3490188370) | both | 日常 | 0 | [查看](mod_archives/3490188370_Project_Cook_烹饪系统重做.md) |
| 自动整理 | Tidy Up Meister | [`2769706949`](https://steamcommunity.com/sharedfiles/filedetails/?id=2769706949) | both | 日常 | 0 | [查看](mod_archives/2769706949_Tidy_Up_Meister_库存自动归位.md) |

### 工具与调试（2 个）

| 中文名 | 原名 | 工作坊 ID | 分发 | 归属 | 物品 | 档案 |
| --- | --- | --- | --- | --- | --- | --- |
| 坐标显示 | Where Am I? | [`3097650043`](https://steamcommunity.com/sharedfiles/filedetails/?id=3097650043) | client | 日常 | 0 | [查看](mod_archives/3097650043_Where_Am_I_显示所在位置.md) |
| 调试菜单社区版 | B42/41调试菜单社区版 (DebugMenu_Community) | [`3735377688`](https://steamcommunity.com/sharedfiles/filedetails/?id=3735377688) | both | 日常 | 0 | [查看](mod_archives/3735377688_B4241调试菜单社区版_DebugMenu_Community_右键多级调试与管理员菜单.md) |

### 性能优化（2 个）

| 中文名 | 原名 | 工作坊 ID | 分发 | 归属 | 物品 | 档案 |
| --- | --- | --- | --- | --- | --- | --- |
| 性能修复 | PzPerformanceFixes | [`3826630779`](https://steamcommunity.com/sharedfiles/filedetails/?id=3826630779) | client | 日常 | 0 | [查看](mod_archives/3826630779_PzPerformanceFixes_帧率与卡顿优化.md) |
| 模组调度优化 | 模组统一调度与优化(subieliSuSir) | [`3825832401`](https://steamcommunity.com/sharedfiles/filedetails/?id=3825832401) | both | 日常 | 0 | [查看](mod_archives/3825832401_模组统一调度与优化subieliSuSir_模组加载调度提速.md) |

### KI5 载具系列（15 个）

| 中文名 | 原名 | 工作坊 ID | 分发 | 归属 | 物品 | 档案 |
| --- | --- | --- | --- | --- | --- | --- |
| '70 Dodge Challenger | '70 Dodge Challenger | [`2873290424`](https://steamcommunity.com/sharedfiles/filedetails/?id=2873290424) | both | 日常 | 30 | [查看](mod_archives/2873290424_70_Dodge_Challenger_70_年代美式肌肉车.md) |
| '78 AM General M35 军卡 | '78 AM General M35 Series Trucks | [`2799152995`](https://steamcommunity.com/sharedfiles/filedetails/?id=2799152995) | both | 日常 | 34 | [查看](mod_archives/2799152995_78_AM_General_M35_Series_Trucks_军用六驱卡车.md) |
| '82 Jeep J10 | '82 Jeep J10 | [`2886832257`](https://steamcommunity.com/sharedfiles/filedetails/?id=2886832257) | both | 日常 | 0 | [查看](mod_archives/2886832257_82_Jeep_J10_全尺寸皮卡.md) |
| '84 Mercedes W460 | '84 Mercedes Benz W460 | [`2805630347`](https://steamcommunity.com/sharedfiles/filedetails/?id=2805630347) | both | 日常 | 57 | [查看](mod_archives/2805630347_84_Mercedes_Benz_W460_方盒子越野车.md) |
| '86 Ford Econoline E-150 | '86 Ford Econoline E150 | [`2870394916`](https://steamcommunity.com/sharedfiles/filedetails/?id=2870394916) | both | 日常 | 55 | [查看](mod_archives/2870394916_86_Ford_Econoline_E150_厢式货车面包车.md) |
| '87 Ford B700/F700 | '87 Ford B700/F700 Trucks | [`3110911330`](https://steamcommunity.com/sharedfiles/filedetails/?id=3110911330) | both | 日常 | 0 | [查看](mod_archives/3110911330_87_Ford_B700F700_Trucks_中型卡车底盘.md) |
| '88 Chevrolet S10 | '88 Chevrolet S10 | [`2886832936`](https://steamcommunity.com/sharedfiles/filedetails/?id=2886832936) | both | 日常 | 0 | [查看](mod_archives/2886832936_88_Chevrolet_S10_紧凑型工作皮卡.md) |
| '90 Ford F350 救护车 | '90 Ford F350 Ambulance Type 1 | [`2952802178`](https://steamcommunity.com/sharedfiles/filedetails/?id=2952802178) | both | 日常 | 0 | [查看](mod_archives/2952802178_90_Ford_F350_Ambulance_Type_1_可当移动医疗点的救护车.md) |
| '91 Range Rover Classic | '91 RANGE ROVER Classic | [`2409333430`](https://steamcommunity.com/sharedfiles/filedetails/?id=2409333430) | both | 日常 | 0 | [查看](mod_archives/2409333430_91_RANGE_ROVER_Classic_经典英式越野_SUV.md) |
| '92 Nissan Skyline GT-R R32 | '92 NISSAN Skyline GT-R (R32) | [`2846036306`](https://steamcommunity.com/sharedfiles/filedetails/?id=2846036306) | both | 日常 | 39 | [查看](mod_archives/2846036306_92_NISSAN_Skyline_GT-R_R32_日系性能跑车.md) |
| Containers! 集装箱 | Containers! | [`2625625421`](https://steamcommunity.com/sharedfiles/filedetails/?id=2625625421) | both | 日常 | 6 | [查看](mod_archives/2625625421_Containers!_可堆叠、可搬运的集装箱.md) |
| M998 悍马 + M101A3 拖车 | '92 AM General M998 + M101A3 Trailer | [`2642541073`](https://steamcommunity.com/sharedfiles/filedetails/?id=2642541073) | both | 日常 | 30 | [查看](mod_archives/2642541073_92_AM_General_M998_+_M101A3_Trailer_军版悍马与货运拖车.md) |
| Trailers! 拖车合集 | Trailers! | [`3330403100`](https://steamcommunity.com/sharedfiles/filedetails/?id=3330403100) | both | 日常 | 12 | [查看](mod_archives/3330403100_Trailers!_多用途拖车与货运挂车.md) |
| 载具资源库 | that DAMN Library | [`3171167894`](https://steamcommunity.com/sharedfiles/filedetails/?id=3171167894) | both | 日常 | 150 | [查看](mod_archives/3171167894_that_DAMN_Library_KI5载具公共资源.md) |
| 通用函数库 | Yet Another PZ Library | [`3624971238`](https://steamcommunity.com/sharedfiles/filedetails/?id=3624971238) | both | 日常 | 0 | [查看](mod_archives/3624971238_Yet_Another_PZ_Library_KI5脚本依赖库.md) |

### 玩法与移动（1 个）

| 中文名 | 原名 | 工作坊 ID | 分发 | 归属 | 物品 | 档案 |
| --- | --- | --- | --- | --- | --- | --- |
| 折叠梯 | Ladders?! B42.22+ (Craftable & movable ladder) | [`3629835761`](https://steamcommunity.com/sharedfiles/filedetails/?id=3629835761) | both | 日常 | 6 | [查看](mod_archives/3629835761_Ladders!_B42.22+_Craftable_and_movable_ladder_B42.22_可制作、可移动的折叠梯.md) |

### 修复与兼容（5 个）

| 中文名 | 原名 | 工作坊 ID | 分发 | 归属 | 物品 | 档案 |
| --- | --- | --- | --- | --- | --- | --- |
| KI5 血迹材质修复 | Project Viewpoint - KI5 Blood Texture Fix | [`3819702412`](https://steamcommunity.com/sharedfiles/filedetails/?id=3819702412) | both | 兼容候选 | 0 | [查看](mod_archives/3819702412_Project_Viewpoint_-_KI5_Blood_Texture_Fix_修正KI5车辆血迹材质.md) |
| KI5 载具零件修复 | Project Viewpoint - KI5 Vehicle Parts Fix | [`3815019204`](https://steamcommunity.com/sharedfiles/filedetails/?id=3815019204) | both | 日常 | 0 | [查看](mod_archives/3815019204_Project_Viewpoint_-_KI5_Vehicle_Parts_Fix_修正_KI5_载具零件的显示位置.md) |
| 数值修复 | Fix NaN Stats [B42.13-42.22] | [`3627071412`](https://steamcommunity.com/sharedfiles/filedetails/?id=3627071412) | both | 日常 | 0 | [查看](mod_archives/3627071412_Fix_NaN_Stats_B42.13-42.22_NaN属性修正.md) |
| 载具外壳修复 | Viewpoint - Vehicle Shell Fix | [`3819801335`](https://steamcommunity.com/sharedfiles/filedetails/?id=3819801335) | both | 日常 | 0 | [查看](mod_archives/3819801335_Viewpoint_-_Vehicle_Shell_Fix_修正_Viewpoint_载具_3D_外壳.md) |
| 载具零件喷漆 | Viewpoint - Part Paint | [`3834561718`](https://steamcommunity.com/sharedfiles/filedetails/?id=3834561718) | both | 日常 | 0 | [查看](mod_archives/3834561718_Viewpoint_-_Part_Paint_给_3D_载具零件上色.md) |

### 房车兼容候选（6 个）

| 中文名 | 原名 | 工作坊 ID | 分发 | 归属 | 物品 | 档案 |
| --- | --- | --- | --- | --- | --- | --- |
| 3D 厢式房车 | Viewpoint - 3D RV Van | [`3821174725`](https://steamcommunity.com/sharedfiles/filedetails/?id=3821174725) | both | 兼容候选 | 0 | [查看](mod_archives/3821174725_Viewpoint_-_3D_RV_Van_可摆家具的厢式房车.md) |
| DeadWorks Dale 房车 | Dale's Chieftain RV | [`3820158673`](https://steamcommunity.com/sharedfiles/filedetails/?id=3820158673) | both | 兼容候选 | 0 | [查看](mod_archives/3820158673_Dales_Chieftain_RV_Dale房车的DeadWorks分支.md) |
| DeadWorks Nomad 房车 | Nomad RV | [`3820158673`](https://steamcommunity.com/sharedfiles/filedetails/?id=3820158673) | both | 兼容候选 | 14 | [查看](mod_archives/3820158673_Nomad_RV_Nomad房车的DeadWorks分支.md) |
| DeadWorks 沙盒调节 | DeadWorks Vehicle Framework Tweaks | [`3826684062`](https://steamcommunity.com/sharedfiles/filedetails/?id=3826684062) | both | 兼容候选 | 0 | [查看](mod_archives/3826684062_DeadWorks_Vehicle_Framework_Tweaks_装甲水箱电池车重可调.md) |
| DeadWorks 载具框架 | DeadWorks Vehicle Framework | [`3825724093`](https://steamcommunity.com/sharedfiles/filedetails/?id=3825724093) | both | 兼容候选 | 0 | [查看](mod_archives/3825724093_DeadWorks_Vehicle_Framework_房车内饰水电家具内核.md) |
| 厢式房车后端 | 3D Vans Host backend | [`3821174725`](https://steamcommunity.com/sharedfiles/filedetails/?id=3821174725) | both | 兼容候选 | 0 | [查看](mod_archives/3821174725_3D_Vans_Host_backend_车厢家具与乘员同步后端.md) |

### 汉化（3 个）

| 中文名 | 原名 | 工作坊 ID | 分发 | 归属 | 物品 | 档案 |
| --- | --- | --- | --- | --- | --- | --- |
| 统一中文汉化 | [B42]统一中文汉化 (排序置底) | [`3556544454`](https://steamcommunity.com/sharedfiles/filedetails/?id=3556544454) | both | 日常 | 0 | [查看](mod_archives/3556544454_B42统一中文汉化_排序置底_游戏本体文本汉化.md) |
| 统一模组汉化 | [B42]统一模组汉化 | [`3556540080`](https://steamcommunity.com/sharedfiles/filedetails/?id=3556540080) | both | 日常 | 0 | [查看](mod_archives/3556540080_B42统一模组汉化_模组文本汉化.md) |
| 老余汉化JAVA版 | 老余汉化JAVA版 | [`3810637496`](https://steamcommunity.com/sharedfiles/filedetails/?id=3810637496) | both | 日常 | 0 | [查看](mod_archives/3810637496_老余汉化JAVA版_Java_界面简中汉化.md) |

## 更新档案（不会启动游戏）

```bash
# 从 Grsh_PZ_Modpack 目录运行；默认扫描同级 A004
python tools/mod_archive.py
python tools/test_mod_archive.py
# 从 A004 根执行静态检查
python lab.py check --profile b422-main
```

生成器读取 `A004/workspace/mods_library`、`workspace/patches/mods` 和所选定义；只写 Markdown，不改 Mod。
修改人工简介用 `tools/mod_catalog.json`；更新日期保存在 `tools/workshop_times.json`。
`--out` 会重建指定档案目录，并把 README 写在其父目录；不要指向未保全的历史资料。

## 权属与范围

所有 Mod 版权归各自作者。这里是本地开发资料，不是正式发布、独立 Review 或 Owner 玩法验收。
