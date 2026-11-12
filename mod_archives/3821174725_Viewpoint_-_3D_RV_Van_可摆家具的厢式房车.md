# 3D 厢式房车（Viewpoint - 3D RV Van）

**可摆家具的厢式房车** · 分类：玩法 / 房车 · `3821174725` · 启用 · 加载位次 55
归属：**兼容候选（未运行验收）**；档案视图 `b422-compat`。

## 它做什么

提供带车内空间的厢式房车，可在后厢放置家具；内饰画在车模型内部，需要 Viewpoint 与模型库。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3821174725` |
| mod id | `GridVans` |
| 文件夹 | `GridVans` |
| Mod 版本 | `0.1.8` |
| 原件适配 | `42.21` … `42.21` |
| 当前生效适配 | `42.21` … `42.22`（Overlay 放行，非上游正式支持） |
| 元数据来源 | `42/mod.info` |
| 作者 | Deadworks Collective |
| 工作坊更新时间 | 2026-10-19 |
| 分发端 | both（双端） |
| 体积 / 文件 | 54.4 MB · 34 文件（lua 12，client 7，server 0；贴图 2；模型 10；翻译 2；Java 源码 0、jar/class 1） |

## 依赖与冲突

- 需要：`ZombieBuddy, Viewpoint, GridVansHost, PZVoxelStudioViewpoint`
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有独立脚本物品；载具和配方见下。

载具脚本 1 条：`VansCourierDuo`

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

## 作者原话

```
Independent walkable 3D vans with furniture, battery-powered devices and multiplayer interiors.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3821174725`
- 本地原件：`A004/workspace/mods_library/3821174725/mods/GridVans`
- 档案生成：`python tools/mod_archive.py --profile b422-compat`
