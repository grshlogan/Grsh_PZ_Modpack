# 无缝房车：只有 Viewpoint 3D 能做到“走进去”，其它路线都是妥协

> 本文保留 2026-11-09、B42.21 的调研快照；下文“未装”“缺框架”等状态已过期，路线结论也只覆盖当时调查的对象。当前 DeadWorks 房车链已并入日常组合，补丁证据和待实测范围见[兼容说明](COMPATIBILITY.md)，实际目录及完整 ID 见[当前清单](README.md)。

数据时间 2026-11-09，游戏 42.21。问题：社区是否存在「原版视角和 Viewpoint 视角都能无缝」的房车？结论先说：**没有**。真正的无缝（走进车里、镜头跟着人、家具和储物随车移动）必须走 Viewpoint 3D 渲染；另外两条路线分别是「开顶＋等距」和「传送到独立地图格」。

## 1. 三条技术路线

| 路线 | 代表 mod | 视角 | 是否无缝 | 联机 | 代价 |
|---|---|---|---|---|---|
| **Viewpoint 3D 内饰**（内饰长在车模型里） | 3820158673 Viewpoint - 3D RVs；3821174725 Viewpoint - 3D RV Van | 仅第一/第三人称 3D | ✅ 真无缝 | ✅ 作者标 dedicated server | 必须 ZB + Viewpoint + 模型包；只能 3D 看 |
| **开顶＋等距**（进车时隐藏车顶和上半车身） | 3811728541 Real Vehicle Interiors [B42/MP/BETA] | 仅等距；装了 Viewpoint 会**强制切回等距** | ⚠️ 不传送，但视角退回 2.5D | 实验性 | 作者明说“不改渲染方式没法支持第一人称” |
| **独立地图格**（按 V 传送到内饰地图） | 3543229299 [B42]Project RV Interior；3817030886 RV Viewpoint Patch | 等距 | ❌ 传送，不是同一空间 | ✅（作者标注） | 需要 Map= 配置、存档迁移风险；补丁只是把入口塞进 Viewpoint 交互列表 |

### 为什么 3D 无缝必须绑 Viewpoint
反编译两辆车的内饰 jar（本地已下载）：

- `GridVans.jar`：120 个 class，**49 处引用 `viewpoint/core/Frame`**，另有 `render/SceneData`、`render/ModelDraws`、`packs/PackBind`。
- `DeadWorksVehicleFramework.jar`：148 个 class，**32 处引用 `viewpoint/core/Frame`**，同样依赖 `SceneData`/`ModelDraws`/`PackBind`。
- 两者都**没有 `maps` 目录**——内饰不是独立地图格，而是画在车辆模型内部，靠 Viewpoint 的帧渲染管线出图。

所以不存在「关掉 Viewpoint 还能无缝走进去」的版本：关掉它，内饰就没有渲染器。作者页面也直接写 “This vehicle is designed for Viewpoint's 3D view.” / “Walkable 3D RVs for Project Viewpoint”。

Real Vehicle Interiors 走的是完全不同的路子（隐藏车顶 + 自定义渲染），作者在评论里说得很白：*“viewpoint support is very difficult for this mod, because of the way this mod works… it would basically require a full rework”*；最新版虽然“should now be compatible with Project Viewpoint”，但 **“interiors still only work in the isometric view”**，进内饰会把相机切成等距。

## 2. Viewpoint 线的候选

| 工坊 ID | 名称 | 体积 | 状态 | 说明 |
|---|---|---:|---|---|
| **3820158673** | Viewpoint - 3D RVs | 375.1 MB | 已装（legacy 三件启用） | Nomad RV + Dale Chieftain RV。作者已把 **legacy `GridRV/GridRVHost/DaleChieftainRV` 冻结**，新路线是 `DeadWorksVehicleFramework` + `DeadWorksNomadRV` + `DeadWorksDaleRV` |
| **3825724093** | DeadWorks Vehicle Framework | 0.4 MB | ❗未装 | 新 RV 的必需框架；可行走内饰、水电、家具、门槛/舱门、MP 同步；jar 在 `media/java/`，两端都加载 |
| **3821174725** | Viewpoint - 3D RV Van | 54.5 MB | ❗未装 | Courier Duo 厢货，2×5 空货舱自己装修；`GridVans`（客户端 jar）+ `GridVansHost`（服务端 jar）；MP 标 dedicated server |
| 3826684062 | DeadWorks Framework Tweaks | 0.1 MB | 可选 | 给框架加沙盒页（装甲耐久、水箱、电池、车重） |
| 3826550325 | Viewpoint Vehicle Interiors | 96.3 MB | 已删除 | 只是**座舱细节**（座椅/仪表/顶灯），不是可行走内饰；2026-11-12 按 Owner 指示从组合与文档中删除 |
| 3826175971 | Motorious Zone 车辆内饰 | 27.0 MB | 已评估 | 同上，外观内饰件 |

本地 `3820158673` 里已经带了 `DeadWorksNomadRV 0.9.2`、`DeadWorksDaleRV 0.2.2`，版本与商店一致；只是缺框架，所以在 pack 里保持禁用（备注也这么写的）。

## 3. 推荐动作

**A. 把现有房车升级到新框架（推荐先做）**

1. 下载 `3825724093` 框架到库。
2. pack 里停用 `GridRV` / `GridRVHost` / `DaleChieftainRV`，启用 `DeadWorksNomadRV` / `DeadWorksDaleRV`。
3. 存档转换是**单向**的：作者说明首次加载会把旧 RV 转成新 RV，转完不能回退，动手前备份 `runtime/Server/Zomboid/Saves/labworld`。
4. 收益：作者列表里的新东西（后梯上车顶、自行车架、Nomad 新仪表、装甲套装、V 轮盘操作、沙盒页），并且官方明确 legacy 即将移除。

**B. 加一辆可以自己装修的厢货**

`3821174725` Viewpoint - 3D RV Van，54.5 MB，两个模块都要开（`GridVans` + `GridVansHost`）。家具摆放需要 `Construction 1P Viewpoint` 或 `Project Viewpoint: Visible Construction` 其中一个。

**C. 服务端注意**

`GridVansHost` 和当年的 `GridRVHost` 一样是 `media/java/server/` 的 server-only jar；我们已经修过 ZombieBuddy 的角色判定补丁（`workspace/patches/root/ZombieBuddy.jar`），服务器现在会正确加载这类 jar，不需要再写路径 Overlay。

## 4. 不推荐混用的组合

- **Real Vehicle Interiors + Viewpoint 3D 视角**：能用，但进内饰会强制切等距，等于你每进一次车就丢一次 3D，体验割裂。
- **Project RV Interior + 3D RVs 同一辆车上**：两套“进入”入口会打架，且前者要求 `Map=` 里加 `map_distanciado`，会改世界地图列表。
- **legacy 与 DeadWorks 版同时开**：作者明确“use one not both”。

## 5. 证据

- `GridVans.jar` / `DeadWorksVehicleFramework.jar` 的 class 常量池引用统计（本地反编译，脚本可复现）。
- `mod.info`：`GridVans` require `ZombieBuddy,Viewpoint,GridVansHost,PZVoxelStudioViewpoint`，`javaJarFile=media/java/client/GridVans.jar`；`GridVansHost` require `ZombieBuddy`，jar 在 `media/java/server/`；框架 require `ZombieBuddy,Viewpoint,PZVoxelStudioViewpoint`，jar 在 `media/java/`。
- Workshop 原文：3D RVs「Walkable 3D RVs for Project Viewpoint」「Legacy is going away soon」；RV Van「This vehicle is designed for Viewpoint's 3D view」；Real Vehicle Interiors「interiors still only work in the isometric view」；Project RV Interior「Map Folder: map_distanciado」。
