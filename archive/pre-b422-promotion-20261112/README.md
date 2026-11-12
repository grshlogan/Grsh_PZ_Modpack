# Grsh PZ Modpack

Project Zomboid **Build 42.22** 整合包，以 Viewpoint 第一人称 3D 渲染为核心，配齐界面、制作、性能与汉化，
面向联机（双端加载同一份 mod 列表）。这里放的是**模组档案与说明**，不含模组本体——
装包请按下面的清单在 Steam 创意工坊逐一订阅，尊重原作者的版权。

- 游戏版本：B42.22（实测 `42.21.0`）
- 索引：62 个（启用 61，保留停用 1）
- 体积：3.6 GB，脚本物品 875 条
- 服务器世界名：`labworld`（同一个世界名 = 同一个存档与角色，换包不丢人）

## 目录

```
Grsh_PZ_Modpack/
├── README.md              # 本文件：整合包介绍 + 按类别索引
└── mod_archives/          # 一个 mod 一份档案
    ├── INDEX.md           # 简表
    ├── _TEMPLATE.md       # 档案的通用骨架与遍历结论
    └── <steam_id>_<模组原名>_<中文简介>.md
```

## 模组索引（按类别）

类别只表示用途，不代表加载顺序；实际顺序由 `workspace/defs/play/pack.json` 的 `loadOrder` 决定。组内按中文名排序。

### 核心框架与渲染（4 个）

| 中文名 | 原名 | 工作坊 ID | 体积 | 状态 | 档案 |
| --- | --- | --- | --- | --- | --- |
| 6282体素模型包 | 6282 3D models for Viewpoint [sour_kisel] | [`3810302175`](https://steamcommunity.com/sharedfiles/filedetails/?id=3810302175) | 272.7 MB | ✅ 启用 | [查看](mod_archives/3810302175_6282_3D_models_for_Viewpoint_sour_kisel_3D模型与贴图素材库.md) |
| ViewpointDLSS | Viewpoint DLSS Frame Generation | [`3818838508`](https://steamcommunity.com/sharedfiles/filedetails/?id=3818838508) | 4.3 MB | ✅ 启用 | [查看](mod_archives/3818838508_Viewpoint_DLSS_Frame_Generation_无简介.md) |
| 僵尸伙伴 | ZombieBuddy | [`3619862853`](https://steamcommunity.com/sharedfiles/filedetails/?id=3619862853) | 13.8 MB | ✅ 启用 | [查看](mod_archives/3619862853_ZombieBuddy_模组框架与3D动画核心.md) |
| 视角重构 | Viewpoint | [`3809306528`](https://steamcommunity.com/sharedfiles/filedetails/?id=3809306528) | 35.6 MB | ✅ 启用 | [查看](mod_archives/3809306528_Viewpoint_第一人称3D渲染核心.md) |

### Viewpoint 3D 世界与建筑（6 个）

| 中文名 | 原名 | 工作坊 ID | 体积 | 状态 | 档案 |
| --- | --- | --- | --- | --- | --- |
| 3D 栅栏 | Viewpoint - 3D Fences | [`3814486926`](https://steamcommunity.com/sharedfiles/filedetails/?id=3814486926) | 2.9 MB | ✅ 启用 | [查看](mod_archives/3814486926_Viewpoint_-_3D_Fences_13_种常见栅栏_3D_化.md) |
| 3D 门与车库 | Project Viewpoint - 3D Doors, Gates & Garages | [`3818859807`](https://steamcommunity.com/sharedfiles/filedetails/?id=3818859807) | 65.6 MB | ✅ 启用 | [查看](mod_archives/3818859807_Project_Viewpoint_-_3D_Doors_Gates_and_Garages_276_个门模型替代.md) |
| KK 3D 货架 | Project Viewpoint: KK's Shelves in 3D | [`3815931973`](https://steamcommunity.com/sharedfiles/filedetails/?id=3815931973) | 176.3 MB | ⏸ 禁用 | [查看](mod_archives/3815931973_Project_Viewpoint_KKs_Shelves_in_3D_货架按库存显示空轻满.md) |
| 浣熊市家具贴图 | Project Viewpoint Map Mod Furniture - Sprite Edition | [`3816419379`](https://steamcommunity.com/sharedfiles/filedetails/?id=3816419379) | 9.4 MB | ✅ 启用 | [查看](mod_archives/3816419379_Project_Viewpoint_Map_Mod_Furniture_-_Sprite_Edition_地图家具3D化.md) |
| 生活道具 | Viewpoint: Living Props | [`3816442251`](https://steamcommunity.com/sharedfiles/filedetails/?id=3816442251) | 78.0 MB | ✅ 启用 | [查看](mod_archives/3816442251_Viewpoint_Living_Props_会变状态的家具_3D_化.md) |
| 视角屋顶 | Viewpoint - Roofs (WIP) | [`3817294484`](https://steamcommunity.com/sharedfiles/filedetails/?id=3817294484) | 84.5 MB | ✅ 启用 | [查看](mod_archives/3817294484_Viewpoint_-_Roofs_WIP_屋顶遮挡与显示.md) |

### 角色与外观（6 个）

| 中文名 | 原名 | 工作坊 ID | 体积 | 状态 | 档案 |
| --- | --- | --- | --- | --- | --- |
| AimohGF2Eclipse | R116 渲染支持 光影分发 | [`3834707439`](https://steamcommunity.com/sharedfiles/filedetails/?id=3834707439) | 45.0 MB | ✅ 启用 | [查看](mod_archives/3834707439_R116_渲染支持_光影分发_无简介.md) |
| VariableSkinBoobBounce | VSGirlBodyBoobBounce(Requires ZombieBuddy) | [`3640496116`](https://steamcommunity.com/sharedfiles/filedetails/?id=3640496116) | 127.3 KB | ✅ 启用 | [查看](mod_archives/3640496116_VSGirlBodyBoobBounceRequires_ZombieBuddy_无简介.md) |
| VariableSkinBoobBounceViewpoint | VSGirlBodyBoobBounceViewpoint | [`3640496116`](https://steamcommunity.com/sharedfiles/filedetails/?id=3640496116) | 56.2 KB | ✅ 启用 | [查看](mod_archives/3640496116_VSGirlBodyBoobBounceViewpoint_无简介.md) |
| VariableSkinFix | VSGirlBody_Fix | [`3640496116`](https://steamcommunity.com/sharedfiles/filedetails/?id=3640496116) | 82.7 KB | ✅ 启用 | [查看](mod_archives/3640496116_VSGirlBody_Fix_无简介.md) |
| VariableSkinSFW | VSGirlBody_S_SFW | [`3640496116`](https://steamcommunity.com/sharedfiles/filedetails/?id=3640496116) | 75.2 MB | ✅ 启用 | [查看](mod_archives/3640496116_VSGirlBody_S_SFW_无简介.md) |
| 少前2 整备室（PMX 预览） | R116 | [`3834454638`](https://steamcommunity.com/sharedfiles/filedetails/?id=3834454638) | 1.4 GB | ✅ 启用 | [查看](mod_archives/3834454638_R116_把少前2角色模型搬进僵毁.md) |

### KI5 载具系列（19 个）

| 中文名 | 原名 | 工作坊 ID | 体积 | 状态 | 档案 |
| --- | --- | --- | --- | --- | --- |
| '70 Dodge Challenger | '70 Dodge Challenger | [`2873290424`](https://steamcommunity.com/sharedfiles/filedetails/?id=2873290424) | 18.2 MB | ✅ 启用 | [查看](mod_archives/2873290424_70_Dodge_Challenger_70_年代美式肌肉车.md) |
| '78 AM General M35 军卡 | '78 AM General M35 Series Trucks | [`2799152995`](https://steamcommunity.com/sharedfiles/filedetails/?id=2799152995) | 28.6 MB | ✅ 启用 | [查看](mod_archives/2799152995_78_AM_General_M35_Series_Trucks_军用六驱卡车.md) |
| '82 Jeep J10 | '82 Jeep J10 | [`2886832257`](https://steamcommunity.com/sharedfiles/filedetails/?id=2886832257) | 12.5 MB | ✅ 启用 | [查看](mod_archives/2886832257_82_Jeep_J10_全尺寸皮卡.md) |
| '84 Mercedes W460 | '84 Mercedes Benz W460 | [`2805630347`](https://steamcommunity.com/sharedfiles/filedetails/?id=2805630347) | 26.8 MB | ✅ 启用 | [查看](mod_archives/2805630347_84_Mercedes_Benz_W460_方盒子越野车.md) |
| '86 Ford Econoline E-150 | '86 Ford Econoline E150 | [`2870394916`](https://steamcommunity.com/sharedfiles/filedetails/?id=2870394916) | 27.4 MB | ✅ 启用 | [查看](mod_archives/2870394916_86_Ford_Econoline_E150_厢式货车面包车.md) |
| '87 Ford B700/F700 | '87 Ford B700/F700 Trucks | [`3110911330`](https://steamcommunity.com/sharedfiles/filedetails/?id=3110911330) | 30.0 MB | ✅ 启用 | [查看](mod_archives/3110911330_87_Ford_B700F700_Trucks_中型卡车底盘.md) |
| '88 Chevrolet S10 | '88 Chevrolet S10 | [`2886832936`](https://steamcommunity.com/sharedfiles/filedetails/?id=2886832936) | 9.5 MB | ✅ 启用 | [查看](mod_archives/2886832936_88_Chevrolet_S10_紧凑型工作皮卡.md) |
| '90 Ford F350 救护车 | '90 Ford F350 Ambulance Type 1 | [`2952802178`](https://steamcommunity.com/sharedfiles/filedetails/?id=2952802178) | 10.0 MB | ✅ 启用 | [查看](mod_archives/2952802178_90_Ford_F350_Ambulance_Type_1_可当移动医疗点的救护车.md) |
| '91 Range Rover Classic | '91 RANGE ROVER Classic | [`2409333430`](https://steamcommunity.com/sharedfiles/filedetails/?id=2409333430) | 18.1 MB | ✅ 启用 | [查看](mod_archives/2409333430_91_RANGE_ROVER_Classic_经典英式越野_SUV.md) |
| '92 Nissan Skyline GT-R R32 | '92 NISSAN Skyline GT-R (R32) | [`2846036306`](https://steamcommunity.com/sharedfiles/filedetails/?id=2846036306) | 18.1 MB | ✅ 启用 | [查看](mod_archives/2846036306_92_NISSAN_Skyline_GT-R_R32_日系性能跑车.md) |
| Containers! 集装箱 | Containers! | [`2625625421`](https://steamcommunity.com/sharedfiles/filedetails/?id=2625625421) | 10.4 MB | ✅ 启用 | [查看](mod_archives/2625625421_Containers!_可堆叠、可搬运的集装箱.md) |
| KI5 血迹贴图修复 | Project Viewpoint - KI5 Blood Texture Fix | [`3819702412`](https://steamcommunity.com/sharedfiles/filedetails/?id=3819702412) | 72.1 KB | ✅ 启用 | [查看](mod_archives/3819702412_Project_Viewpoint_-_KI5_Blood_Texture_Fix_KI5_车血迹材质修正.md) |
| KI5 车辆部件修复 | Project Viewpoint - KI5 Vehicle Parts Fix | [`3815019204`](https://steamcommunity.com/sharedfiles/filedetails/?id=3815019204) | 175.3 KB | ✅ 启用 | [查看](mod_archives/3815019204_Project_Viewpoint_-_KI5_Vehicle_Parts_Fix_KI5_车部件渲染与装配修正.md) |
| M998 悍马 + M101A3 拖车 | '92 AM General M998 + M101A3 Trailer | [`2642541073`](https://steamcommunity.com/sharedfiles/filedetails/?id=2642541073) | 21.8 MB | ✅ 启用 | [查看](mod_archives/2642541073_92_AM_General_M998_+_M101A3_Trailer_军版悍马与货运拖车.md) |
| Trailers! 拖车合集 | Trailers! | [`3330403100`](https://steamcommunity.com/sharedfiles/filedetails/?id=3330403100) | 11.2 MB | ✅ 启用 | [查看](mod_archives/3330403100_Trailers!_多用途拖车与货运挂车.md) |
| 车身分件喷漆 | Viewpoint - Part Paint | [`3834561718`](https://steamcommunity.com/sharedfiles/filedetails/?id=3834561718) | 700.4 KB | ✅ 启用 | [查看](mod_archives/3834561718_Viewpoint_-_Part_Paint_支持改装车的分件喷漆.md) |
| 车身外壳修复 | Viewpoint - Vehicle Shell Fix | [`3819801335`](https://steamcommunity.com/sharedfiles/filedetails/?id=3819801335) | 40.5 KB | ✅ 启用 | [查看](mod_archives/3819801335_Viewpoint_-_Vehicle_Shell_Fix_近距离车身贴合修正.md) |
| 载具资源库 | that DAMN Library | [`3171167894`](https://steamcommunity.com/sharedfiles/filedetails/?id=3171167894) | 40.3 MB | ✅ 启用 | [查看](mod_archives/3171167894_that_DAMN_Library_KI5载具公共资源.md) |
| 通用函数库 | Yet Another PZ Library | [`3624971238`](https://steamcommunity.com/sharedfiles/filedetails/?id=3624971238) | 90.2 KB | ✅ 启用 | [查看](mod_archives/3624971238_Yet_Another_PZ_Library_KI5脚本依赖库.md) |

### 无缝房车与车辆内饰（7 个）

| 中文名 | 原名 | 工作坊 ID | 体积 | 状态 | 档案 |
| --- | --- | --- | --- | --- | --- |
| 3D RV Van 厢货 | Viewpoint - 3D RV Van | [`3821174725`](https://steamcommunity.com/sharedfiles/filedetails/?id=3821174725) | 54.4 MB | ✅ 启用 | [查看](mod_archives/3821174725_Viewpoint_-_3D_RV_Van_可自行装修的_3D_厢式房车.md) |
| 3D RV Van 服务端后端 | 3D Vans Host backend | [`3821174725`](https://steamcommunity.com/sharedfiles/filedetails/?id=3821174725) | 107.6 KB | ✅ 启用 | [查看](mod_archives/3821174725_3D_Vans_Host_backend_厢货车厢与家具的服务端权威.md) |
| DeadWorks 房车框架 | DeadWorks Vehicle Framework | [`3825724093`](https://steamcommunity.com/sharedfiles/filedetails/?id=3825724093) | 437.4 KB | ✅ 启用 | [查看](mod_archives/3825724093_DeadWorks_Vehicle_Framework_新代_3D_房车的内饰水电家具内核.md) |
| DeadWorks 框架沙盒页 | DeadWorks Vehicle Framework Tweaks | [`3826684062`](https://steamcommunity.com/sharedfiles/filedetails/?id=3826684062) | 510.6 KB | ✅ 启用 | [查看](mod_archives/3826684062_DeadWorks_Vehicle_Framework_Tweaks_装甲水箱电池车重可调.md) |
| Viewpoint 车辆内饰 | Viewpoint Vehicle Interiors | [`3826550325`](https://steamcommunity.com/sharedfiles/filedetails/?id=3826550325) | 96.3 MB | ✅ 启用 | [查看](mod_archives/3826550325_Viewpoint_Vehicle_Interiors_驾驶舱座椅、仪表与顶灯细节.md) |
| 废弃游牧房车 | Nomad RV | [`3820158673`](https://steamcommunity.com/sharedfiles/filedetails/?id=3820158673) | 56.6 MB | ✅ 启用 | [查看](mod_archives/3820158673_Nomad_RV_房车残骸替换件.md) |
| 废弃酋长房车 | Dale's Chieftain RV | [`3820158673`](https://steamcommunity.com/sharedfiles/filedetails/?id=3820158673) | 53.5 MB | ✅ 启用 | [查看](mod_archives/3820158673_Dales_Chieftain_RV_房车残骸替换件.md) |

### 界面、库存与制作（8 个）

| 中文名 | 原名 | 工作坊 ID | 体积 | 状态 | 档案 |
| --- | --- | --- | --- | --- | --- |
| Neat制作 | Neat Crafting [B42.12] | [`3502080466`](https://steamcommunity.com/sharedfiles/filedetails/?id=3502080466) | 4.1 MB | ✅ 启用 | [查看](mod_archives/3502080466_Neat_Crafting_B42.12_制作界面重制.md) |
| Neat界面框架 | NeatUI_Framework | [`3508537032`](https://steamcommunity.com/sharedfiles/filedetails/?id=3508537032) | 2.2 MB | ✅ 启用 | [查看](mod_archives/3508537032_NeatUI_Framework_制作界面框架.md) |
| 分类整理 | Better Sorting | [`2313387159`](https://steamcommunity.com/sharedfiles/filedetails/?id=2313387159) | 1.7 MB | ✅ 启用 | [查看](mod_archives/2313387159_Better_Sorting_库存分类菜单.md) |
| 地图图例 | Map Legend UI | [`2710167561`](https://steamcommunity.com/sharedfiles/filedetails/?id=2710167561) | 787.8 KB | ✅ 启用 | [查看](mod_archives/2710167561_Map_Legend_UI_地图图标说明.md) |
| 就近存取 | Proximity Inventory B42 | [`2847184718`](https://steamcommunity.com/sharedfiles/filedetails/?id=2847184718) | 685.9 KB | ✅ 启用 | [查看](mod_archives/2847184718_Proximity_Inventory_B42_周边容器一键取放.md) |
| 沙盒选项 | [B42] Sandbox Options | [`3386906181`](https://steamcommunity.com/sharedfiles/filedetails/?id=3386906181) | 8.9 MB | ✅ 启用 | [查看](mod_archives/3386906181_B42_Sandbox_Options_游戏内改沙盒设置.md) |
| 烹饪重制 | Project Cook [Legacy] | [`3490188370`](https://steamcommunity.com/sharedfiles/filedetails/?id=3490188370) | 7.6 MB | ✅ 启用 | [查看](mod_archives/3490188370_Project_Cook_Legacy_烹饪系统重做.md) |
| 自动整理 | Tidy Up Meister | [`2769706949`](https://steamcommunity.com/sharedfiles/filedetails/?id=2769706949) | 1.3 MB | ✅ 启用 | [查看](mod_archives/2769706949_Tidy_Up_Meister_库存自动归位.md) |

### 工具与调试（2 个）

| 中文名 | 原名 | 工作坊 ID | 体积 | 状态 | 档案 |
| --- | --- | --- | --- | --- | --- |
| 坐标显示 | Where Am I? | [`3097650043`](https://steamcommunity.com/sharedfiles/filedetails/?id=3097650043) | 2.2 MB | ✅ 启用 | [查看](mod_archives/3097650043_Where_Am_I_显示所在位置.md) |
| 调试菜单社区版 | B42/41调试菜单社区版 (DebugMenu_Community) | [`3735377688`](https://steamcommunity.com/sharedfiles/filedetails/?id=3735377688) | 1.1 MB | ✅ 启用 | [查看](mod_archives/3735377688_B4241调试菜单社区版_DebugMenu_Community_右键多级调试与管理员菜单.md) |

### 性能优化（2 个）

| 中文名 | 原名 | 工作坊 ID | 体积 | 状态 | 档案 |
| --- | --- | --- | --- | --- | --- |
| 性能修复 | PzPerformanceFixes | [`3826630779`](https://steamcommunity.com/sharedfiles/filedetails/?id=3826630779) | 1.1 MB | ✅ 启用 | [查看](mod_archives/3826630779_PzPerformanceFixes_帧率与卡顿优化.md) |
| 模组调度优化 | 模组统一调度与优化(subieliSuSir) | [`3825832401`](https://steamcommunity.com/sharedfiles/filedetails/?id=3825832401) | 217.3 KB | ✅ 启用 | [查看](mod_archives/3825832401_模组统一调度与优化subieliSuSir_模组加载调度提速.md) |

### 修复与兼容（5 个）

| 中文名 | 原名 | 工作坊 ID | 体积 | 状态 | 档案 |
| --- | --- | --- | --- | --- | --- |
| Viewpoint 视觉修复 | ViewpointVisualFixes | [`3821308495`](https://steamcommunity.com/sharedfiles/filedetails/?id=3821308495) | 91.5 KB | ✅ 启用 | [查看](mod_archives/3821308495_ViewpointVisualFixes_窗框材质、穿模与墙面挂件修复.md) |
| 右键修复 | Viewpoint - Right Click Fix | [`3819018807`](https://steamcommunity.com/sharedfiles/filedetails/?id=3819018807) | 347.1 KB | ✅ 启用 | [查看](mod_archives/3819018807_Viewpoint_-_Right_Click_Fix_右键直接打开指向物体菜单.md) |
| 地图烘焙修复 | Project Viewpoint: General Mod Map Fix | [`3813929757`](https://steamcommunity.com/sharedfiles/filedetails/?id=3813929757) | 25.8 KB | ✅ 启用 | [查看](mod_archives/3813929757_Project_Viewpoint_General_Mod_Map_Fix_烘焙贴图修正.md) |
| 封窗木条修复 | Viewpoint - Barricade Fix | [`3815033191`](https://steamcommunity.com/sharedfiles/filedetails/?id=3815033191) | 278.3 KB | ✅ 启用 | [查看](mod_archives/3815033191_Viewpoint_-_Barricade_Fix_木质金属封窗位置修正.md) |
| 数值修复 | Fix NaN Stats [B42.13-42.22] | [`3627071412`](https://steamcommunity.com/sharedfiles/filedetails/?id=3627071412) | 253.7 KB | ✅ 启用 | [查看](mod_archives/3627071412_Fix_NaN_Stats_B42.13-42.22_NaN属性修正.md) |

### 汉化（3 个）

| 中文名 | 原名 | 工作坊 ID | 体积 | 状态 | 档案 |
| --- | --- | --- | --- | --- | --- |
| 统一中文汉化 | [B42]统一中文汉化 (排序置底) | [`3556544454`](https://steamcommunity.com/sharedfiles/filedetails/?id=3556544454) | 765.1 MB | ✅ 启用 | [查看](mod_archives/3556544454_B42统一中文汉化_排序置底_游戏本体文本汉化.md) |
| 统一模组汉化 | [B42]统一模组汉化 | [`3556540080`](https://steamcommunity.com/sharedfiles/filedetails/?id=3556540080) | 39.1 MB | ✅ 启用 | [查看](mod_archives/3556540080_B42统一模组汉化_模组文本汉化.md) |
| 老余汉化JAVA版 | 老余汉化JAVA版 | [`3810637496`](https://steamcommunity.com/sharedfiles/filedetails/?id=3810637496) | 2.9 MB | ✅ 启用 | [查看](mod_archives/3810637496_老余汉化JAVA版_Java_界面简中汉化.md) |

> **关于 ⏸ 禁用**：只保留 `Project Viewpoint: KK's Shelves in 3D`（`3815931973`）一个停用项；
> 它在 nightly 0.1.7-rc3 上调用旧 `PackData` 构造器会抛 `NoSuchMethodError`，启用后会把 6282 模型队列一起卡住。
> 等上游适配新的 `PackData` 构造器后再启用。

## 三条通用规则

1. **双端一致**：标记 `both` 的模组客户端和服务端都要装，少一边会因 mod 列表校验失败而连不上。
2. **依赖在前**：`require=` 指向的库（ZombieBuddy / NeatUI / damnlib / YAPZLib / DeadWorksVehicleFramework / GridVansHost）必须排在依赖它的内容之前。
3. **汉化垫底**：`统一模组汉化` → `统一中文汉化` 永远放最后，否则翻译文件会被后加载的模组覆盖。

## 怎么读单个模组的档案

每份档案都是同一副骨架：它做什么 → 概览（版本/作者/体积/更新时间）→ 依赖与冲突 →
内容清单（物品 id / 载具 / 配方）→ 双端与联机 → 实测与排查 → 作者原话 → 来源。
骨架与遍历结论见 [`mod_archives/_TEMPLATE.md`](mod_archives/_TEMPLATE.md)。

## 免责声明

所有模组版权归各自作者所有；本仓库只记录整合信息、版本与兼容性结论，不分发模组文件。
遇到问题先看对应档案的「实测与排查」，再回创意工坊页面确认版本。

