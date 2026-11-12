# 6282 模型库（6282 3D models for Viewpoint [sour_kisel]）

**3D模型与贴图素材库** · 分类：渲染 / 模型资源 · `3810302175` · 启用 · 加载位次 50
归属：**兼容候选（未运行验收）**；档案视图 `b422-compat`。

## 它做什么

为 Viewpoint 注册体素与 3D 物件模型包，用立体资源替代部分原版平面物件；也是房车链依赖的模型资源底层。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3810302175` |
| mod id | `PZVoxelStudioViewpoint` |
| 文件夹 | `PZVoxelStudioViewpoint` |
| Mod 版本 | `1.0` |
| 原件适配 | `42.21.0` … `42.21.0` |
| 当前生效适配 | `42.21.0` … `42.22`（Overlay 放行，非上游正式支持） |
| 元数据来源 | `42.20.4/mod.info` |
| 作者 | sour_kisel |
| 工作坊更新时间 | 2026-10-30 |
| 分发端 | both（双端） |
| 体积 / 文件 | 272.7 MB · 26,304 文件（lua 1，client 1，server 0；贴图 8487；模型 9312；翻译 0） |

## 依赖与冲突

- 需要：无
- 互斥：无
- 被依赖：`GridVans`、`DeadWorksVehicleFramework`、`DeadWorksNomadRV`、`DeadWorksDaleRV`

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

当前兼容候选为双端，资源注册在客户端；房车依赖该 Mod ID，不能只复制模型文件。

当前 profile：both（双端）。

本机文件构成：客户端有 lua；服务端无 lua（只挂载）。

## 实测与排查

原件 1.0，42.21.0 上限；仅 Overlay 放宽至 42.22。旧独立实验已证加载和 16 包注册及联网；1109 GPU 模型与 packs116 为所有包合计，不能证明指定 6282 模型视觉正确。

**planned：仅完成依赖、版本与补丁指纹静态检查。** 迁移收尾按 Owner 要求不启动游戏；本候选组合未验证加载、联网、存档或视觉。

版本放行补丁：`A004/workspace/patches/mods/PZVoxelStudioViewpoint/42.20.4/mod.info`。原件更新后须重新核对指纹；撤除此补丁后运行 check 会恢复原件版本限制。

```
cd A004
python lab.py check --profile b422-compat
grep -a 'PZVoxelStudioViewpoint' runs/<trial>/*console.log
```

## 作者原话

```
Voxel Studio 3D models for Project Viewpoint (first-person view). Stairs and corner-laid models re-anchored for Viewpoint.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3810302175`
- 本地原件：`A004/workspace/mods_library/3810302175/mods/PZVoxelStudioViewpoint`
- 档案生成：`python tools/mod_archive.py --profile b422-compat`
