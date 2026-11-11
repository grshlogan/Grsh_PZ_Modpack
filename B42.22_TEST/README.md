# B42.22_TEST · 42 Mod 联机测试包

这是 **A004/B42.22_TEST** 的文档副本，记录当前 B42.22 联机测试包的 42 个条目：
它们做什么、依赖谁、加了哪些物品/载具/配方、哪一端加载、以及本机实测注意事项。
这里只放档案，不含 mod 本体；实际运行库在 `A004/B42.22_TEST`。

## 当前包

- 游戏版本：`B42.22`（profile `gameVersion=42.22.0`）
- 条目：**42**（启用 42，禁用 0）
- 双端：**Client 42 / Server 38**；服务端不加载的 4 条是 `PzPerformanceFixes`、`VariableSkinSFW`、`VariableSkinFix`、`WhereAmI`。
- 世界名 / 服务器名：`b422batch2`；入口：`A004/B42.22_TEST/start-client.bat`、`start-server.bat`。
- 体积：2.6 GB；脚本物品：436 条。
- 三个汉化包均为 `both`，服务端 `Mods=` 末尾依次是 `LaoYuTranslationJava`、`B42ModTrans_CN`、`B42Trans_CN`。

## 目录

```
B42.22_TEST/
├── README.md              # 本文件：包说明 + 按类别索引
├── mod_archives/          # 一个 mod 一份档案
│   ├── INDEX.md           # 42 条简表
│   ├── _TEMPLATE.md       # 固定骨架与通用规则
│   └── <steam_id>_<原名>_<中文简介>.md
└── tools/
    ├── mod_archive.py     # 从 A004/B42.22_TEST 生成档案
    ├── mod_catalog.json    # 人工简介、分类、排查注记
    └── workshop_times.json # 工作坊更新日期快照
```

## 模组索引（按类别）

类别只表示用途，不代表加载顺序；实际顺序看 profile 的 `loadOrder`。

### 核心框架与渲染（5 个）

| 中文名 | 原名 | 工作坊 ID | 分发 | 体积 | 物品 | 档案 |
| --- | --- | --- | --- | --- | --- | --- |
| 僵尸伙伴 | ZombieBuddy | [`3619862853`](https://steamcommunity.com/sharedfiles/filedetails/?id=3619862853) | both | 13.8 MB | 0 | [查看](mod_archives/3619862853_ZombieBuddy_模组框架与3D动画核心.md) |
| 右键修复 | Viewpoint - Right Click Fix | [`3819018807`](https://steamcommunity.com/sharedfiles/filedetails/?id=3819018807) | both | 677.1 KB | 0 | [查看](mod_archives/3819018807_Viewpoint_-_Right_Click_Fix_右键直接打开指向物体菜单.md) |
| 封窗木条修复 | Viewpoint - Barricade Fix | [`3815033191`](https://steamcommunity.com/sharedfiles/filedetails/?id=3815033191) | both | 278.3 KB | 0 | [查看](mod_archives/3815033191_Viewpoint_-_Barricade_Fix_木质金属封窗位置修正.md) |
| 视角屋顶 | Viewpoint - Roofs (WIP) | [`3817294484`](https://steamcommunity.com/sharedfiles/filedetails/?id=3817294484) | both | 84.5 MB | 0 | [查看](mod_archives/3817294484_Viewpoint_-_Roofs_WIP_屋顶遮挡与显示.md) |
| 视角重构 | Viewpoint | [`3809306528`](https://steamcommunity.com/sharedfiles/filedetails/?id=3809306528) | both | 32.6 MB | 0 | [查看](mod_archives/3809306528_Viewpoint_第一人称3D渲染核心.md) |

### 角色与外观（3 个）

| 中文名 | 原名 | 工作坊 ID | 分发 | 体积 | 物品 | 档案 |
| --- | --- | --- | --- | --- | --- | --- |
| VSGirlBody SFW 身形 | VSGirlBody_S_SFW | [`3640496116`](https://steamcommunity.com/sharedfiles/filedetails/?id=3640496116) | client | 75.2 MB | 17 | [查看](mod_archives/3640496116_VSGirlBody_S_SFW_女性角色身形与服装适配.md) |
| VSGirlBody 修复 | VSGirlBody_Fix | [`3640496116`](https://steamcommunity.com/sharedfiles/filedetails/?id=3640496116) | client | 82.7 KB | 0 | [查看](mod_archives/3640496116_VSGirlBody_Fix_身形包的兼容修复.md) |
| 少前2 整备室（PMX 预览） | R116 | [`3834454638`](https://steamcommunity.com/sharedfiles/filedetails/?id=3834454638) | both | 1.3 GB | 0 | [查看](mod_archives/3834454638_R116_把少前2角色模型搬进僵毁.md) |

### 界面、库存与制作（10 个）

| 中文名 | 原名 | 工作坊 ID | 分发 | 体积 | 物品 | 档案 |
| --- | --- | --- | --- | --- | --- | --- |
| CleanHotBar 清爽快捷栏 | CleanHotBar | [`3461263912`](https://steamcommunity.com/sharedfiles/filedetails/?id=3461263912) | both | 810.9 KB | 0 | [查看](mod_archives/3461263912_CleanHotBar_更清晰的可配置快捷栏.md) |
| CleanUI 清爽界面 | CleanUI | [`3437629766`](https://steamcommunity.com/sharedfiles/filedetails/?id=3437629766) | both | 15.5 MB | 0 | [查看](mod_archives/3437629766_CleanUI_更紧凑可配置的库存与拾取界面.md) |
| Neat制作 | Neat Crafting | [`3502080466`](https://steamcommunity.com/sharedfiles/filedetails/?id=3502080466) | both | 4.1 MB | 0 | [查看](mod_archives/3502080466_Neat_Crafting_制作界面重制.md) |
| Neat界面框架 | NeatUI_Framework | [`3508537032`](https://steamcommunity.com/sharedfiles/filedetails/?id=3508537032) | both | 2.2 MB | 0 | [查看](mod_archives/3508537032_NeatUI_Framework_制作界面框架.md) |
| 分类整理 | Better Sorting | [`2313387159`](https://steamcommunity.com/sharedfiles/filedetails/?id=2313387159) | both | 1.7 MB | 0 | [查看](mod_archives/2313387159_Better_Sorting_库存分类菜单.md) |
| 地图图例 | Map Legend UI | [`2710167561`](https://steamcommunity.com/sharedfiles/filedetails/?id=2710167561) | both | 787.8 KB | 0 | [查看](mod_archives/2710167561_Map_Legend_UI_地图图标说明.md) |
| 就近存取 | Proximity Inventory B42 | [`2847184718`](https://steamcommunity.com/sharedfiles/filedetails/?id=2847184718) | both | 685.9 KB | 0 | [查看](mod_archives/2847184718_Proximity_Inventory_B42_周边容器一键取放.md) |
| 沙盒选项 | [B42] Sandbox Options | [`3386906181`](https://steamcommunity.com/sharedfiles/filedetails/?id=3386906181) | both | 8.9 MB | 0 | [查看](mod_archives/3386906181_B42_Sandbox_Options_游戏内改沙盒设置.md) |
| 烹饪重制 | Project Cook | [`3490188370`](https://steamcommunity.com/sharedfiles/filedetails/?id=3490188370) | both | 7.6 MB | 0 | [查看](mod_archives/3490188370_Project_Cook_烹饪系统重做.md) |
| 自动整理 | Tidy Up Meister | [`2769706949`](https://steamcommunity.com/sharedfiles/filedetails/?id=2769706949) | both | 1.3 MB | 0 | [查看](mod_archives/2769706949_Tidy_Up_Meister_库存自动归位.md) |

### 工具与调试（2 个）

| 中文名 | 原名 | 工作坊 ID | 分发 | 体积 | 物品 | 档案 |
| --- | --- | --- | --- | --- | --- | --- |
| 坐标显示 | Where Am I? | [`3097650043`](https://steamcommunity.com/sharedfiles/filedetails/?id=3097650043) | client | 2.2 MB | 0 | [查看](mod_archives/3097650043_Where_Am_I_显示所在位置.md) |
| 调试菜单社区版 | B42/41调试菜单社区版 (DebugMenu_Community) | [`3735377688`](https://steamcommunity.com/sharedfiles/filedetails/?id=3735377688) | both | 1.1 MB | 0 | [查看](mod_archives/3735377688_B4241调试菜单社区版_DebugMenu_Community_右键多级调试与管理员菜单.md) |

### 性能优化（2 个）

| 中文名 | 原名 | 工作坊 ID | 分发 | 体积 | 物品 | 档案 |
| --- | --- | --- | --- | --- | --- | --- |
| 性能修复 | PzPerformanceFixes | [`3826630779`](https://steamcommunity.com/sharedfiles/filedetails/?id=3826630779) | client | 1.1 MB | 0 | [查看](mod_archives/3826630779_PzPerformanceFixes_帧率与卡顿优化.md) |
| 模组调度优化 | 模组统一调度与优化(subieliSuSir) | [`3825832401`](https://steamcommunity.com/sharedfiles/filedetails/?id=3825832401) | both | 217.3 KB | 0 | [查看](mod_archives/3825832401_模组统一调度与优化subieliSuSir_模组加载调度提速.md) |

### KI5 载具系列（15 个）

| 中文名 | 原名 | 工作坊 ID | 分发 | 体积 | 物品 | 档案 |
| --- | --- | --- | --- | --- | --- | --- |
| '70 Dodge Challenger | '70 Dodge Challenger | [`2873290424`](https://steamcommunity.com/sharedfiles/filedetails/?id=2873290424) | both | 18.2 MB | 30 | [查看](mod_archives/2873290424_70_Dodge_Challenger_70_年代美式肌肉车.md) |
| '78 AM General M35 军卡 | '78 AM General M35 Series Trucks | [`2799152995`](https://steamcommunity.com/sharedfiles/filedetails/?id=2799152995) | both | 28.6 MB | 34 | [查看](mod_archives/2799152995_78_AM_General_M35_Series_Trucks_军用六驱卡车.md) |
| '82 Jeep J10 | '82 Jeep J10 | [`2886832257`](https://steamcommunity.com/sharedfiles/filedetails/?id=2886832257) | both | 12.5 MB | 0 | [查看](mod_archives/2886832257_82_Jeep_J10_全尺寸皮卡.md) |
| '84 Mercedes W460 | '84 Mercedes Benz W460 | [`2805630347`](https://steamcommunity.com/sharedfiles/filedetails/?id=2805630347) | both | 26.8 MB | 57 | [查看](mod_archives/2805630347_84_Mercedes_Benz_W460_方盒子越野车.md) |
| '86 Ford Econoline E-150 | '86 Ford Econoline E150 | [`2870394916`](https://steamcommunity.com/sharedfiles/filedetails/?id=2870394916) | both | 27.4 MB | 55 | [查看](mod_archives/2870394916_86_Ford_Econoline_E150_厢式货车面包车.md) |
| '87 Ford B700/F700 | '87 Ford B700/F700 Trucks | [`3110911330`](https://steamcommunity.com/sharedfiles/filedetails/?id=3110911330) | both | 30.0 MB | 0 | [查看](mod_archives/3110911330_87_Ford_B700F700_Trucks_中型卡车底盘.md) |
| '88 Chevrolet S10 | '88 Chevrolet S10 | [`2886832936`](https://steamcommunity.com/sharedfiles/filedetails/?id=2886832936) | both | 9.5 MB | 0 | [查看](mod_archives/2886832936_88_Chevrolet_S10_紧凑型工作皮卡.md) |
| '90 Ford F350 救护车 | '90 Ford F350 Ambulance Type 1 | [`2952802178`](https://steamcommunity.com/sharedfiles/filedetails/?id=2952802178) | both | 10.0 MB | 0 | [查看](mod_archives/2952802178_90_Ford_F350_Ambulance_Type_1_可当移动医疗点的救护车.md) |
| '91 Range Rover Classic | '91 RANGE ROVER Classic | [`2409333430`](https://steamcommunity.com/sharedfiles/filedetails/?id=2409333430) | both | 18.1 MB | 0 | [查看](mod_archives/2409333430_91_RANGE_ROVER_Classic_经典英式越野_SUV.md) |
| '92 Nissan Skyline GT-R R32 | '92 NISSAN Skyline GT-R (R32) | [`2846036306`](https://steamcommunity.com/sharedfiles/filedetails/?id=2846036306) | both | 18.1 MB | 39 | [查看](mod_archives/2846036306_92_NISSAN_Skyline_GT-R_R32_日系性能跑车.md) |
| Containers! 集装箱 | Containers! | [`2625625421`](https://steamcommunity.com/sharedfiles/filedetails/?id=2625625421) | both | 10.4 MB | 6 | [查看](mod_archives/2625625421_Containers!_可堆叠、可搬运的集装箱.md) |
| M998 悍马 + M101A3 拖车 | '92 AM General M998 + M101A3 Trailer | [`2642541073`](https://steamcommunity.com/sharedfiles/filedetails/?id=2642541073) | both | 21.8 MB | 30 | [查看](mod_archives/2642541073_92_AM_General_M998_+_M101A3_Trailer_军版悍马与货运拖车.md) |
| Trailers! 拖车合集 | Trailers! | [`3330403100`](https://steamcommunity.com/sharedfiles/filedetails/?id=3330403100) | both | 11.2 MB | 12 | [查看](mod_archives/3330403100_Trailers!_多用途拖车与货运挂车.md) |
| 载具资源库 | that DAMN Library | [`3171167894`](https://steamcommunity.com/sharedfiles/filedetails/?id=3171167894) | both | 40.3 MB | 150 | [查看](mod_archives/3171167894_that_DAMN_Library_KI5载具公共资源.md) |
| 通用函数库 | Yet Another PZ Library | [`3624971238`](https://steamcommunity.com/sharedfiles/filedetails/?id=3624971238) | both | 90.2 KB | 0 | [查看](mod_archives/3624971238_Yet_Another_PZ_Library_KI5脚本依赖库.md) |

### 玩法与移动（1 个）

| 中文名 | 原名 | 工作坊 ID | 分发 | 体积 | 物品 | 档案 |
| --- | --- | --- | --- | --- | --- | --- |
| 折叠梯 | Ladders?! B42.22+ (Craftable & movable ladder) | [`3629835761`](https://steamcommunity.com/sharedfiles/filedetails/?id=3629835761) | both | 358.0 KB | 6 | [查看](mod_archives/3629835761_Ladders!_B42.22+_Craftable_and_movable_ladder_B42.22_可制作、可移动的折叠梯.md) |

### 修复与兼容（1 个）

| 中文名 | 原名 | 工作坊 ID | 分发 | 体积 | 物品 | 档案 |
| --- | --- | --- | --- | --- | --- | --- |
| 数值修复 | Fix NaN Stats [B42.13-42.22] | [`3627071412`](https://steamcommunity.com/sharedfiles/filedetails/?id=3627071412) | both | 253.7 KB | 0 | [查看](mod_archives/3627071412_Fix_NaN_Stats_B42.13-42.22_NaN属性修正.md) |

### 汉化（3 个）

| 中文名 | 原名 | 工作坊 ID | 分发 | 体积 | 物品 | 档案 |
| --- | --- | --- | --- | --- | --- | --- |
| 统一中文汉化 | [B42]统一中文汉化 (排序置底) | [`3556544454`](https://steamcommunity.com/sharedfiles/filedetails/?id=3556544454) | both | 765.1 MB | 0 | [查看](mod_archives/3556544454_B42统一中文汉化_排序置底_游戏本体文本汉化.md) |
| 统一模组汉化 | [B42]统一模组汉化 | [`3556540080`](https://steamcommunity.com/sharedfiles/filedetails/?id=3556540080) | both | 42.4 MB | 0 | [查看](mod_archives/3556540080_B42统一模组汉化_模组文本汉化.md) |
| 老余汉化JAVA版 | 老余汉化JAVA版 | [`3810637496`](https://steamcommunity.com/sharedfiles/filedetails/?id=3810637496) | both | 3.1 MB | 0 | [查看](mod_archives/3810637496_老余汉化JAVA版_Java_界面简中汉化.md) |

## 三条通用规则

1. **双端一致**：标记 `both` 的模组客户端和服务端都要装；少一边会因 mod 列表校验失败而连不上。当前 4 条 `client` 只装客户端，进服后会被服务端 `Mods=` 列表丢弃，这是已知行为。
2. **依赖在前**：`ZombieBuddy`、`NeatUI_Framework`、`damnlib`、`YAPZLib`、`Viewpoint` 必须排在依赖它的内容之前；汉化包放最后。
3. **汉化垫底**：`LaoYuTranslationJava` → `B42ModTrans_CN` → `B42Trans_CN`，否则翻译文件会被后加载的模组覆盖。

## 怎么读单个档案

每份档案固定为：它做什么 → 概览（版本/作者/体积/更新时间）→ 依赖与冲突 → 内容清单（物品 id / 载具 / 配方）→ 双端与联机 → 实测与排查 → 作者原话 → 来源。
骨架和遍历结论见 [`mod_archives/_TEMPLATE.md`](mod_archives/_TEMPLATE.md)。

## 重新生成与校验

```
cd Grsh_PZ_Modpack/B42.22_TEST
python tools/mod_archive.py --profile b422-batch2
cd ../../../B42.22_TEST
python lab.py check --profile b422-batch2
```

生成器只扫描 `A004/B42.22_TEST/workspace/mods_library` 和 profile，不会复制、修改或上传任何 mod 文件。

## 免责声明

所有模组版权归各自作者所有；本目录只记录整合信息、版本与兼容性结论，不分发模组文件。遇到问题先看对应档案的「实测与排查」，再回创意工坊页面确认版本。
