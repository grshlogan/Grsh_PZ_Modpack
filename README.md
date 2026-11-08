# Grsh PZ Modpack

Project Zomboid **Build 42.22** 整合包，以 Viewpoint 第一人称 3D 渲染为核心，配齐界面、制作、性能与汉化，
面向联机（双端加载同一份 mod 列表）。这里放的是**模组档案与说明**，不含模组本体——
装包请按下面的清单在 Steam 创意工坊逐一订阅，尊重原作者的版权。

- 游戏版本：B42.22（实测 `42.21.0`）
- 条目：36 个（启用 34，禁用 2）
- 体积：1.9 GB，脚本物品 315 条
- 服务器世界名：`labworld`（同一个世界名 = 同一个存档与角色，换包不丢人）

## 目录

```
Grsh_PZ_Modpack/
├── README.md              # 本文件：整合包介绍 + 全量索引（按实际加载顺序）
└── mod_archives/          # 一个 mod 一份档案
    ├── INDEX.md           # 简表
    ├── _TEMPLATE.md       # 档案的通用骨架与遍历结论
    └── <steam_id>_<模组原名>_<中文简介>.md
```

## 模组索引（按整合包加载顺序）

顺序即游戏里的实际加载顺序：库在前、内容在中、汉化垫底。禁用项保留在表尾，方便换回来。

| # | 中文名 | 原名 | 工作坊 ID | 分类 | 体积 | 状态 | 档案 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 僵尸伙伴 | ZombieBuddy | [`3619862853`](https://steamcommunity.com/sharedfiles/filedetails/?id=3619862853) | 框架 / 渲染底层 | 13.8 MB | ✅ 启用 | [查看](mod_archives/3619862853_ZombieBuddy_模组框架与3D动画核心.md) |
| 2 | 视角重构 | Viewpoint | [`3809306528`](https://steamcommunity.com/sharedfiles/filedetails/?id=3809306528) | 渲染 / 视角 | 32.6 MB | ✅ 启用 | [查看](mod_archives/3809306528_Viewpoint_第一人称3D渲染核心.md) |
| 3 | 6282体素模型包 | 6282 3D models for Viewpoint [sour_kisel] | [`3810302175`](https://steamcommunity.com/sharedfiles/filedetails/?id=3810302175) | 素材 / 模型 | 272.7 MB | ✅ 启用 | [查看](mod_archives/3810302175_6282_3D_models_for_Viewpoint_sour_kisel_3D模型与贴图素材库.md) |
| 4 | 视角表面修复 | Viewpoint - Surface Fix | [`3814398576`](https://steamcommunity.com/sharedfiles/filedetails/?id=3814398576) | 渲染 / 修复 | 536.0 KB | ✅ 启用 | [查看](mod_archives/3814398576_Viewpoint_-_Surface_Fix_墙面地面渲染修正.md) |
| 5 | 3D 门与车库 | Project Viewpoint - 3D Doors, Gates & Garages | [`3818859807`](https://steamcommunity.com/sharedfiles/filedetails/?id=3818859807) | 渲染 / 模型 | 65.6 MB | ✅ 启用 | [查看](mod_archives/3818859807_Project_Viewpoint_-_3D_Doors_Gates_and_Garages_276_个门模型替代.md) |
| 6 | 封窗木条修复 | Viewpoint - Barricade Fix | [`3815033191`](https://steamcommunity.com/sharedfiles/filedetails/?id=3815033191) | 渲染 / 修复 | 278.3 KB | ✅ 启用 | [查看](mod_archives/3815033191_Viewpoint_-_Barricade_Fix_木质金属封窗位置修正.md) |
| 7 | 视角屋顶 | Viewpoint - Roofs (WIP) | [`3817294484`](https://steamcommunity.com/sharedfiles/filedetails/?id=3817294484) | 渲染 | 84.5 MB | ✅ 启用 | [查看](mod_archives/3817294484_Viewpoint_-_Roofs_WIP_屋顶遮挡与显示.md) |
| 8 | 3D 栅栏 | Viewpoint - 3D Fences | [`3814486926`](https://steamcommunity.com/sharedfiles/filedetails/?id=3814486926) | 渲染 / 模型 | 2.9 MB | ✅ 启用 | [查看](mod_archives/3814486926_Viewpoint_-_3D_Fences_13_种常见栅栏_3D_化.md) |
| 9 | 生活道具 | Viewpoint: Living Props | [`3816442251`](https://steamcommunity.com/sharedfiles/filedetails/?id=3816442251) | 渲染 / 模型 | 78.0 MB | ✅ 启用 | [查看](mod_archives/3816442251_Viewpoint_Living_Props_会变状态的家具_3D_化.md) |
| 10 | 右键修复 | Viewpoint - Right Click Fix | [`3819018807`](https://steamcommunity.com/sharedfiles/filedetails/?id=3819018807) | 操作 / 修复 | 347.1 KB | ✅ 启用 | [查看](mod_archives/3819018807_Viewpoint_-_Right_Click_Fix_右键直接打开指向物体菜单.md) |
| 11 | KK 3D 货架 | Project Viewpoint: KK's Shelves in 3D | [`3815931973`](https://steamcommunity.com/sharedfiles/filedetails/?id=3815931973) | 渲染 / 模型 | 176.3 MB | ✅ 启用 | [查看](mod_archives/3815931973_Project_Viewpoint_KKs_Shelves_in_3D_货架按库存显示空轻满.md) |
| 12 | 浣熊市家具贴图 | Project Viewpoint Map Mod Furniture - Sprite Edition | [`3816419379`](https://steamcommunity.com/sharedfiles/filedetails/?id=3816419379) | 素材 / 地图 | 9.4 MB | ✅ 启用 | [查看](mod_archives/3816419379_Project_Viewpoint_Map_Mod_Furniture_-_Sprite_Edition_地图家具3D化.md) |
| 13 | 地图烘焙修复 | Project Viewpoint: General Mod Map Fix | [`3813929757`](https://steamcommunity.com/sharedfiles/filedetails/?id=3813929757) | 修复 / 地图 | 25.8 KB | ✅ 启用 | [查看](mod_archives/3813929757_Project_Viewpoint_General_Mod_Map_Fix_烘焙贴图修正.md) |
| 14 | 网格房车后端 | Grid RV Host backend (Legacy) | [`3820158673`](https://steamcommunity.com/sharedfiles/filedetails/?id=3820158673) | 框架 / 载具 | 106.9 KB | ✅ 启用 | [查看](mod_archives/3820158673_Grid_RV_Host_backend_Legacy_房车系统后端库.md) |
| 15 | 游牧网格房车 | Nomad Grid RV (Legacy) | [`3820158673`](https://steamcommunity.com/sharedfiles/filedetails/?id=3820158673) | 载具 / 建造 | 92.1 MB | ✅ 启用 | [查看](mod_archives/3820158673_Nomad_Grid_RV_Legacy_可建造移动房车.md) |
| 16 | 酋长房车 | Dale's Chieftain RV (Legacy) | [`3820158673`](https://steamcommunity.com/sharedfiles/filedetails/?id=3820158673) | 载具 | 172.8 MB | ✅ 启用 | [查看](mod_archives/3820158673_Dales_Chieftain_RV_Legacy_大型房车载具.md) |
| 17 | 废弃酋长房车 | Dale's Chieftain RV | [`3820158673`](https://steamcommunity.com/sharedfiles/filedetails/?id=3820158673) | 载具 / 可选 | 53.5 MB | ⏸ 禁用 | [查看](mod_archives/3820158673_Dales_Chieftain_RV_房车残骸替换件.md) |
| 18 | 废弃游牧房车 | Nomad RV | [`3820158673`](https://steamcommunity.com/sharedfiles/filedetails/?id=3820158673) | 载具 / 可选 | 56.6 MB | ⏸ 禁用 | [查看](mod_archives/3820158673_Nomad_RV_房车残骸替换件.md) |
| 19 | 载具资源库 | that DAMN Library | [`3171167894`](https://steamcommunity.com/sharedfiles/filedetails/?id=3171167894) | 框架 / 素材 | 40.3 MB | ✅ 启用 | [查看](mod_archives/3171167894_that_DAMN_Library_KI5载具公共资源.md) |
| 20 | 通用函数库 | Yet Another PZ Library | [`3624971238`](https://steamcommunity.com/sharedfiles/filedetails/?id=3624971238) | 框架 | 90.2 KB | ✅ 启用 | [查看](mod_archives/3624971238_Yet_Another_PZ_Library_KI5脚本依赖库.md) |
| 21 | Neat界面框架 | NeatUI_Framework | [`3508537032`](https://steamcommunity.com/sharedfiles/filedetails/?id=3508537032) | 框架 / UI | 2.2 MB | ✅ 启用 | [查看](mod_archives/3508537032_NeatUI_Framework_制作界面框架.md) |
| 22 | 分类整理 | Better Sorting | [`2313387159`](https://steamcommunity.com/sharedfiles/filedetails/?id=2313387159) | UI / 整理 | 1.7 MB | ✅ 启用 | [查看](mod_archives/2313387159_Better_Sorting_库存分类菜单.md) |
| 23 | KI5小修 | KI5 Mini-fixes | [`3740300378`](https://steamcommunity.com/sharedfiles/filedetails/?id=3740300378) | 修复 / 载具 | 521.5 KB | ✅ 启用 | [查看](mod_archives/3740300378_KI5_Mini-fixes_KI5载具Bug修复.md) |
| 24 | 就近存取 | Proximity Inventory B42 | [`2847184718`](https://steamcommunity.com/sharedfiles/filedetails/?id=2847184718) | UI / 便利 | 685.9 KB | ✅ 启用 | [查看](mod_archives/2847184718_Proximity_Inventory_B42_周边容器一键取放.md) |
| 25 | 沙盒选项 | [B42] Sandbox Options | [`3386906181`](https://steamcommunity.com/sharedfiles/filedetails/?id=3386906181) | 工具 / 管理 | 8.9 MB | ✅ 启用 | [查看](mod_archives/3386906181_B42_Sandbox_Options_游戏内改沙盒设置.md) |
| 26 | 烹饪重制 | Project Cook [Legacy] | [`3490188370`](https://steamcommunity.com/sharedfiles/filedetails/?id=3490188370) | 玩法 / 制作 | 7.6 MB | ✅ 启用 | [查看](mod_archives/3490188370_Project_Cook_Legacy_烹饪系统重做.md) |
| 27 | Neat制作 | Neat Crafting [B42.12] | [`3502080466`](https://steamcommunity.com/sharedfiles/filedetails/?id=3502080466) | UI / 制作 | 4.1 MB | ✅ 启用 | [查看](mod_archives/3502080466_Neat_Crafting_B42.12_制作界面重制.md) |
| 28 | 自动整理 | Tidy Up Meister | [`2769706949`](https://steamcommunity.com/sharedfiles/filedetails/?id=2769706949) | UI / 整理 | 1.3 MB | ✅ 启用 | [查看](mod_archives/2769706949_Tidy_Up_Meister_库存自动归位.md) |
| 29 | 地图图例 | Map Legend UI | [`2710167561`](https://steamcommunity.com/sharedfiles/filedetails/?id=2710167561) | UI / 地图 | 787.8 KB | ✅ 启用 | [查看](mod_archives/2710167561_Map_Legend_UI_地图图标说明.md) |
| 30 | 性能修复 | PzPerformanceFixes | [`3826630779`](https://steamcommunity.com/sharedfiles/filedetails/?id=3826630779) | 性能 | 1.1 MB | ✅ 启用 | [查看](mod_archives/3826630779_PzPerformanceFixes_帧率与卡顿优化.md) |
| 31 | 模组调度优化 | 模组统一调度与优化(subieliSuSir) | [`3825832401`](https://steamcommunity.com/sharedfiles/filedetails/?id=3825832401) | 性能 | 217.3 KB | ✅ 启用 | [查看](mod_archives/3825832401_模组统一调度与优化subieliSuSir_模组加载调度提速.md) |
| 32 | 数值修复 | Fix NaN Stats [B42.13-42.22] | [`3627071412`](https://steamcommunity.com/sharedfiles/filedetails/?id=3627071412) | 修复 | 253.7 KB | ✅ 启用 | [查看](mod_archives/3627071412_Fix_NaN_Stats_B42.13-42.22_NaN属性修正.md) |
| 33 | 坐标显示 | Where Am I? | [`3097650043`](https://steamcommunity.com/sharedfiles/filedetails/?id=3097650043) | UI / 工具 | 2.2 MB | ✅ 启用 | [查看](mod_archives/3097650043_Where_Am_I_显示所在位置.md) |
| 34 | 老余汉化JAVA版 | 老余汉化JAVA版 | [`3810637496`](https://steamcommunity.com/sharedfiles/filedetails/?id=3810637496) | 语言 / 汉化 | 2.9 MB | ✅ 启用 | [查看](mod_archives/3810637496_老余汉化JAVA版_Java_界面简中汉化.md) |
| 35 | 统一模组汉化 | [B42]统一模组汉化 | [`3556540080`](https://steamcommunity.com/sharedfiles/filedetails/?id=3556540080) | 汉化 | 39.1 MB | ✅ 启用 | [查看](mod_archives/3556540080_B42统一模组汉化_模组文本汉化.md) |
| 36 | 统一中文汉化 | [B42]统一中文汉化 (排序置底) | [`3556544454`](https://steamcommunity.com/sharedfiles/filedetails/?id=3556544454) | 汉化 | 765.1 MB | ✅ 启用 | [查看](mod_archives/3556544454_B42统一中文汉化_排序置底_游戏本体文本汉化.md) |

## 三条通用规则

1. **双端一致**：标记 `both` 的模组客户端和服务端都要装，少一边会因 mod 列表校验失败而连不上。
2. **依赖在前**：`require=` 指向的库（ZombieBuddy / NeatUI / damnlib / YAPZLib / GridRVHost）必须排在依赖它的内容之前。
3. **汉化垫底**：`统一模组汉化` → `统一中文汉化` 永远放最后，否则翻译文件会被后加载的模组覆盖。

## 怎么读单个模组的档案

每份档案都是同一副骨架：它做什么 → 概览（版本/作者/体积/更新时间）→ 依赖与冲突 →
内容清单（物品 id / 载具 / 配方）→ 双端与联机 → 实测与排查 → 作者原话 → 来源。
骨架与遍历结论见 [`mod_archives/_TEMPLATE.md`](mod_archives/_TEMPLATE.md)。

## 免责声明

所有模组版权归各自作者所有；本仓库只记录整合信息、版本与兼容性结论，不分发模组文件。
遇到问题先看对应档案的「实测与排查」，再回创意工坊页面确认版本。

