# Viewpoint 渲染管线、施工可见性、DLSS 与改模：社区现状（2026-11-09 核查）

所有 ID、体积、订阅数、更新日期来自 Steam 官方 `GetPublishedFileDetails`（本机 2026-11-09 拉取）；管线能力来自本地 Viewpoint 0.1.6.1 的 jar 与 `viewpoint-live.properties`。

## 0. 一句话结论

- **两个施工 mod 解决的是同一件事**：3D 视角下重建/摆家具时，原版光标还留在“看不见的等距画面”里，你看不到要放的东西。
- **Viewpoint 本身就是一套自研 PBR 渲染管线**，自带光影包系统（`Zomboid\viewpoint-shaderpacks`），社区有 7 个以上成熟光影包；另有一套竞争框架 **pz3d**。
- **DLSS 是真的**：Viewpoint 里带的是 NVIDIA 官方 Streamline / DLSS 4.x 运行时（`nvngx_dlss.dll` 310.9.1），0.1.6 起把 FSR 3 / XeSS / DLSS 标为实验；帧生成另有独立 mod（2x/4x/6x）。DLSS 5 只给 RTX 50，但需要游戏逐作集成，僵毁用不上。
- **“少前2 渲染管线搬进 PZ”是真的**：B 站 `BV1Di4A6bEsY`《烧掉近50亿token的 僵毁逆向工程少前2渲染管线》（UP：CRASHCRASHCRASH，2026-11-03，96 秒，3.6 万播放），作者尚未公开、正在小范围内测。它和 Viewpoint 是两条不同的技术路线。

## 1. 施工可见性：两个 mod 的差别

| | **Construction 1P Viewpoint** | **Project Viewpoint: Visible Construction** |
|---|---|---|
| 工坊 ID | `3812312558` | `3815631078` |
| 作者 | Fatalitiko | DTechno |
| 体积 / 更新 | 0.71 MB / 2026-10-12 | 0.39 MB / 2026-10-14 |
| 订阅（2026-11-09） | 47,380 | 45,568 |
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

**另一条管线：pz3d**（`3807334881`，237 MB，74,029 订阅，0.9.16）。目标同样是“把镜头放下来”，但和 Viewpoint 是竞争关系，不能同时开；它自己只带少量示例模型，靠社区补模型包，光影能力不如 Viewpoint 完整。它不是 Viewpoint 适配，而是另一个框架。两者都依赖 ZombieBuddy。
**另一条管线：pz3d**（`3807334881`，237 MB，74,029 订阅，0.9.16）。目标同样是“把镜头放下来”，但两个都是接管相机/渲染的框架，通常二选一；它自己只带少量示例模型，靠社区补模型包，光影主要靠内置雾效，不像 Viewpoint 有完整的光影包体系。它不是 Viewpoint 适配，而是另一个框架。两者都依赖 ZombieBuddy。
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

## 4. DLSS / 帧生成 / DLSS 5

| 能力 | 提供方 | 说明 |
|---|---|---|
| DLSS / DLAA 升采样 | **Viewpoint 内置**（NVIDIA Streamline） | 设置里切 Resolution scaling；DLAA 包通过 Viewpoint 自己的下载按钮装，装完要完全重启 |
| FSR 3 / XeSS 升采样 | **Viewpoint 内置** | 与 DLSS 同一入口，实验性 |
| 帧生成 2x/4x/6x | `3818838508` Viewpoint DLSS Frame Generation [B42] [Beta]，4.31 MB，2026-10-19 | RTX 40 用 2x，4x/6x 要 RTX 50 + 驱动支持；RTX 30 走 FSR 2x；要求 PZ 42.21 + Viewpoint 0.1.6 + ZB 2.3.x、Modern 渲染器、Windows 硬件加速 GPU 计划；只加显示帧，不加快游戏模拟 |
| 通用 FSR 升采样 + 软件帧生成 | `3827724780` FSR-UPSC，5.09 MB，2026-11-06 | 不依赖 Viewpoint；FSR1/2/3 + 2-duplicate/3-interpolated；纯客户端，B42.21/22 白名单 |

### DLSS 5 与 5080

DLSS 5 已于 2026-09-03 上线（首发《NBA 2K27》），是“3D-Guided Neural Rendering”，**目前只支持 RTX 50 系**（含 5080）。它需要游戏逐作集成——读取引擎的法线、几何、材质、光照数据，再跑 NVIDIA 为该作准备的神经渲染模型，**不是换一个 DLL 就能开**。

所以：

- 5080 在支持 DLSS 5 的游戏里（NBA 2K27、霍格沃茨之遗、War Thunder、Where Winds Meet 等）可以开。
- 僵毁/Viewpoint **开不了**：Viewpoint 带的是 DLSS 4.x 运行时（310.9.1），没有 DLSS 5 的集成，PZ 也没有那套输入约定。
- 不存在“DLSS 5 破解版”。拿来源不明的 DLL 替换只会让 NGX 初始化失败（帧生成 mod 的更新日志修过 `NGX 0xBAD00004`）。

## 5. 少前2 管线项目：确认存在，尚未公开

- 视频：`BV1Di4A6bEsY`，标题《烧掉近50亿token的 僵毁逆向工程少前2渲染管线》，UP 主 **CRASHCRASHCRASH**，2026-11-03 00:24 发布，96 秒，36,368 播放 / 1,155 赞 / 157 评论（2026-11-09 通过 bilibili API 读取）。
- 这是**僵毁**项目，不是 L4D2 移植，也不是 Unity / UE5 还原。此前我说“查不到证据”是错的，撤回。
- 公开信息只有这段 96 秒演示和标题：没有工坊条目、没有下载、没有开源。你已经在申请内测，等作者回复是唯一路径。
- 和 Viewpoint 的关系目前无法确定：可能是在 Viewpoint 之上替换角色/材质着色，也可能是独立渲染后端；从标题看，做的是“少前2 那套角色/材质/光照”的逆向，不是场景光影包。
- 风险：这类项目通常要改 jar、注入原生库或替换着色器，联机一致性和稳定性都要另测；在内测放出来之前，不要把它当成可依赖的方案。

## 5.5 改模 / 换装：Viewpoint 里角色是怎么画的

- Viewpoint 不是把角色当纸片：它调用游戏自己的 `ModelManager` / `ModelSlot` / `ModelInstanceTextureCreator`，把身体网格和衣物贴图合成后绘制（`viewpoint/models/Characters.class`、`viewpoint/render/CharacterTextures.class`、`viewpoint/models/CharacterLooks.class`）。
- 因此**走原版衣物/发型贴图系统的换装 mod，通常不需要专门适配**，3D 里会直接显示；只改物品图标、纯 2D 精灵替换的 mod 不会变成 3D。这一条是代码层推断，我们还没在游戏里逐件验过。
- 需要专门适配的是**改模**（换身体网格、骨骼、物理）。社区目前明确带 Viewpoint 支持的不多：
  - `3640496116` **VSGirlBody(Integrated)**，443.7 MB，205,094 订阅，内含 `VariableSkinBoobBounceViewpoint`（3D 物理，要 ZombieBuddy）。
  - `3827516230` **Sunflower's Ultimate Character Overhaul (VIEWPOINT SUPPORT)**，0.52 MB，1,967 订阅，改身高/腿/腰/胸/臀 + Clothing Studio + 3D 衣物刷子，要求 ZB 2.3.4、42.21/22。
  - `3813230118` Viewpoint - Equipment Overlays 是**第一人称装备遮挡**（头盔面罩、护目镜），不是换装模型。

你手上的量：

- 旧 B42.13 整合包：7 个服装/角色类条目（二维衣橱、Ash and Mae's Hair Salon、Even More Hair Colors、内衣护甲、VSGirlBody、Clothing Does Not Display Patches、Clothing Holes Not Display），**0 个 Viewpoint 适配**——B42.13 时代还没有 Viewpoint。
- Steam 订阅：14 个服装/角色类工坊条目（Fluffy Hair、Spongie's Hair、Ash and Mae's、内衣护甲、Fashionoid、不在服装店 2/3、Dark Weapon Slings、二维衣橱 + 平衡拓展 + 兼容补丁、影狸战术、VSGirlBody、Character Outfit Preset Fix），其中 **1 个带 Viewpoint 子模块**（VSGirlBody）。

## 6. 给我们的建议

**房车装修**：先装 `3815631078` Visible Construction（两端都开，Lua，联机安全），它解决“看不见要放什么”。要更完整的拾取/旋转操作再评估 `3812312558`，注意 F10 与 Viewpoint 的 ISOLATE 冲突。

**画面**：先试一套光影包，不要一次装三个。想要电影感选 Deadwood（0.53 MB，最轻），想要暗色天气驱动选 Hollow Light（4.94 MB，最好配 Viewpoint Uplink），想要漫画风选 Redraw（手动拷贝）。我们的配置当前 `upscaling=off`，装了包之后再决定是否开 DLSS/FSR。

**帧生成**：`3818838508` 对 5080 是合适的——4x/6x 就是给 RTX 50 的；先确认 Windows 硬件加速 GPU 计划已开，再在同一个场景记录开启前后的帧数与手感。它不是“提升模拟速度”，延迟可能变差。

**换装**：常规服装/发型 mod 可以直接装；要改身体或加物理，只有 VSGirlBody / Sunflower 这类带 Viewpoint 支持的才稳。

## 7. 来源

- Steam 创意工坊条目页与官方 `GetPublishedFileDetails`（各 mod 描述、订阅数、更新日志），ID 见上表。
- B 站 `BV1Di4A6bEsY`（`api.bilibili.com/x/web-interface/view`，标题/UP/发布时间/播放数）。
- 本地 `workspace/mods_library/3809306528/mods/Viewpoint/42/media/java/client/Viewpoint.jar` 的类名与字符串（`ModelManager`、`CharacterTextures`、Streamline / FidelityFX / XeSS、`nvngx_dlss.dll` 310.9.1）。
- 本地 `runtime/client/Zomboid/viewpoint-live.properties`（`pack.*.renderScale` / `upscaling`）。
- DLSS 5 上线与 RTX 50 独占：Engadget（2026-09-01）、TechPowerUp（2026-11-04）等公开报道。
