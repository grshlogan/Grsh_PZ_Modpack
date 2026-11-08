# Viewpoint 渲染管线、施工可见性与 DLSS：社区现状（2026-11-09 核查）

所有 ID、体积、更新日期来自 Steam 官方 `GetPublishedFileDetails`（本机 2026-11-09 拉取）；管线能力来自本地 Viewpoint 0.1.6.1 的 jar 与 `viewpoint-live.properties`。

## 0. 一句话结论

- **两个施工 mod 解决的是同一件事**：3D 视角下重建/摆家具时，原版光标还留在“看不见的等距画面”里，你看不到要放的东西。
- **Viewpoint 本身就是一套自研 PBR 渲染管线**，自带光影包系统（`Zomboid\viewpoint-shaderpacks`），社区有 7 个以上成熟光影包。
- **DLSS 是真的**：Viewpoint 里带的是 NVIDIA 官方 Streamline / DLSS 运行时（`nvngx_dlss.dll` 310.9.1），0.1.6 起把 FSR 3 / XeSS / DLSS 标为实验；帧生成另有独立 mod（2x/4x/6x）。
- **“少前2 渲染管线搬进 PZ”查不到任何证据**。B 站上少前2 的渲染视频都是 Unity / UE5 / Blender 的还原研究；少前2 角色 mod 的移植目标是 **Left 4 Dead 2**，不是僵毁。PZ 这边只有老式的卡通着色替换（PZK Animeboid）和角色贴图/身形，跟 Viewpoint 管线无关。

## 1. 施工可见性：两个 mod 的差别

| | **Construction 1P Viewpoint** | **Project Viewpoint: Visible Construction** |
|---|---|---|
| 工坊 ID | `3812312558` | `3815631078` |
| 作者 | Fatalitiko | DTechno |
| 体积 / 更新 | 0.71 MB / 2026-10-12 | 0.39 MB / 2026-10-14 |
| 订阅（第三方统计） | ≈46,500 | ≈22,700 |
| 实现 | Java jar（要 ZB 批准） | 纯 Lua |
| 依赖 | ZombieBuddy + Viewpoint | Viewpoint |
| 联机 | 作者标 **未验证**（本地玩家 0、键鼠） | 服务端必须启用（Lua mod 的硬规则） |
| 预览方式 | **几何线框**（绿/红），自定义模型形状可能对不上 | **真实物件幽灵** + 地面绿/红板，墙体对齐格边 |
| 额外功能 | F7 拾取 / F8 放置 / F9 旋转 / F10 目标菜单 / N 切换家具；采集发现卡 | 右键物品 Place 预览；Shift+旋转键切换家具；旋转键可单独改键 |
| 备注 | Viewpoint 的 **F10 是 ISOLATE**，与它的目标菜单冲突，需要在选项里改键 | 只改你屏幕上看到的东西，不写存档、不发服务器 |

**为什么房车装修需要它**：RV Van 的货舱是 3D 空间，摆家具时如果预览不可见，你只能盲放。**Visible Construction 更贴合这个场景**（能看到真实家具、服务端一起装就联机可用）；Construction 1P 更适合想要“第一人称拾取/旋转家具”整套操作流的人，但联机没验证。

## 2. Viewpoint 自带的渲染管线

作者原文：从零写的现代 OpenGL 渲染器、完整 PBR 管线，Vanilla / Modern 两套观感，三套内置光影包（Vanilla / Default / Vivid），支持自定义光影包，还实验性兼容 Minecraft IRIS 光影包。

- 光影包目录：`Zomboid\viewpoint-shaderpacks`；游戏内按 **Delete** 打开设置选包。
- 每套包在配置里有自己的 `renderScale` 与 `upscaling` 开关（我们当前是 `renderScale=100`、`upscaling=off`）。
- 管线里能确认的模块：太阳/月亮阴影、逐像素灯光阴影、手电筒投影、体积光、god rays、反弹光、bloom、抗锯齿（MSAA/SSAA/FXAA/TAAU）、云/雨/闪电、地形起伏（Terrain Relief）、模型包 LOD（`lod.packRing`）与显存池（`memory.packMiB`）。
- 升采样后端：jar 内同时带 **NVIDIA Streamline（DLSS/DLAA）**、**AMD FidelityFX（FSR 3）**、**Intel XeSS** 的运行时与许可文件；DLSS DLL 从 NVIDIA 官方仓库拉取（`nvngx_dlss.dll` v310.9.1）。0.1.6 更新日志把三者标为实验性。

## 3. 社区光影包（都要求 Viewpoint + ZombieBuddy）

| ID | 名称 | 体积 | 更新 | 风格 |
|---|---|---:|---|---|
| `3818656834` | Deadwood Shaders | 0.53 MB | 2026-11-01 | Vibrant / Moody 两套电影感；默认 67% + FSR3，可切 DLSS/DLAA |
| `3821721515` | Hollow Light | 4.94 MB | 2026-10-27 | Photon 改的暗色天气驱动包；配 Viewpoint Uplink 才吃真实天气 |
| `3818548144` | Redraw | 0.45 MB | 2026-10-27 | 手绘漫画 / Telltale 风格，墨线+排线 |
| `3819221828` | Mitypoint Shaders | 5.18 MB | 2026-10-15 | TWD 电影感，自动安装/更新 |
| `3820195046` | coldFog Shaders | 0.42 MB | 2026-11-01 | 恐怖雾气，四时段，低配友好 |
| `3820467974` | Wasteland Shaders | 0.13 MB | 2026-10-15 | 四档废土预设（high/balanced/low/potato） |
| `3823573829` | Worn Lens | 0.57 MB | 2026-11-07 | 廉价老镜头：鱼眼、颗粒、眩光、走路晃动 |

安装方式分两类：**自动**（Deadwood / Hollow Light / coldFog / Mitypoint：ZB 批准后把包拷进 `viewpoint-shaderpacks`）和**手动**（Redraw：自己把 `redraw_beta` 文件夹拷进去，`pack.properties` 必须在第一层）。装完要重启一次，再在 Delete → Graphics → Shaders 里选。

## 4. DLSS / 帧生成

| 能力 | 提供方 | 说明 |
|---|---|---|
| DLSS / DLAA 升采样 | **Viewpoint 内置**（NVIDIA Streamline） | 设置里切 Resolution scaling；DLAA 包通过 Viewpoint 自己的下载按钮装，装完要完全重启 |
| FSR 3 / XeSS 升采样 | **Viewpoint 内置** | 与 DLSS 同一入口，实验性 |
| 帧生成 2x/4x/6x | `3818838508` Viewpoint DLSS Frame Generation [B42] [Beta]，4.31 MB，2026-10-19 | RTX 40 用 2x，4x/6x 要 RTX 50 + 驱动支持；RTX 30 走 FSR 2x；要求 Modern 渲染器 + Windows 硬件加速 GPU 计划；只加显示帧，不加快游戏模拟 |
| 通用 FSR 升采样 + 软件帧生成 | `3827724780` FSR-UPSC，5.09 MB，2026-11-06 | 不依赖 Viewpoint；FSR1/2/3 + 2-duplicate/3-interpolated；纯客户端，B42.21/22 白名单 |

**关于“DLSS 5 破解版”**：不需要，也不建议。Viewpoint 已经在用 NVIDIA 官方运行时（带签名与哈希清单），自己去换来源不明的 `nvngx_dlss.dll` 只会让 NGX 初始化失败（帧生成 mod 的更新日志就修过 `NGX 0xBAD00004` 这种冲突）。真要开，走 Viewpoint 设置里的开关，或装上面的帧生成 mod。

## 5. “少前2 渲染管线搬进 PZ”核查

查了 B 站、Steam 创意工坊、GitHub 与网页搜索，结论：

- 少前2 的渲染还原视频（Vepley、闪电姐、春田等）全部是 **Unity / UE5 / Blender** 的材质与光照研究，不是 PZ mod。
- 少前2 角色模型的实际移植目标是 **Left 4 Dead 2**（NekoShaders & L4N 平台，几十个角色），与 PZ 无关。
- PZ 这边的二次元渲染只有两类：**原版着色器替换**（`3457364806` PZK Animeboid，卡通着色+动漫水面，2025-08 后停更）和**角色贴图/身形**（Anime Style、Hotsco's New Body 等）。它们都不走 Viewpoint 的 PBR 管线，也不会得到“高质量角色渲染”。
- 目前没有任何 Viewpoint 专用的角色着色/描边/NPR 光影包。Viewpoint 的着色器接口是给**场景光影**用的，角色仍然走游戏自己的模型与材质。

如果你确实看到过那条视频，最可能是：① L4D2 的少前2 角色 mod 演示；② 用 Viewpoint + IRIS 光影包让画面“看起来像”二次元游戏；③ 纯渲染研究，不是可玩的 PZ mod。三者都不是“把少前2 管线搬进僵毁”。

## 6. 给我们的建议

**房车装修**：先装 `3815631078` Visible Construction（两端都开，Lua，联机安全），它解决“看不见要放什么”。要更完整的拾取/旋转操作再评估 `3812312558`，注意 F10 与 Viewpoint 的 ISOLATE 冲突。

**画面**：先试一套光影包，不要一次装三个。想要电影感选 Deadwood（0.53 MB，最轻），想要暗色天气驱动选 Hollow Light（4.94 MB，最好配 Viewpoint Uplink），想要漫画风选 Redraw（手动拷贝）。我们的配置当前 `upscaling=off`，装了包之后再决定是否开 DLSS/FSR。

**帧生成**：只有 RTX 40/50 才值得试 `3818838508`；先在同一个场景记录开启前后的帧数与手感，再决定留不留。它不是“提升模拟速度”，延迟可能变差。

## 7. 来源

- Steam 创意工坊条目页（各 mod 描述与更新日志），ID 见上表。
- 本地 `workspace/mods_library/3809306528/mods/Viewpoint/42/media/java/client/Viewpoint.jar` 的字符串与许可文件（Streamline / FidelityFX / XeSS、`nvngx_dlss.dll` 310.9.1）。
- 本地 `runtime/client/Zomboid/viewpoint-live.properties`（`pack.*.renderScale` / `upscaling`）。
- Zomboid3D、PZ Manual 的第三方安装说明（仅作旁证，未实机验证）。
