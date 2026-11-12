# DeadWorks 载具框架（DeadWorks Vehicle Framework）

**房车内饰水电家具内核** · 分类：框架 / 房车 · `3825724093` · 启用 · 加载位次 56
归属：**兼容候选（未运行验收）**；档案视图 `b422-compat`。

## 它做什么

为 DeadWorks Nomad 与 Dale 房车提供车内行走、门窗踏板、座椅家具、水电与装甲等系统。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3825724093` |
| mod id | `DeadWorksVehicleFramework` |
| 文件夹 | `DeadWorksVehicleFramework` |
| Mod 版本 | `1.0.4` |
| 原件适配 | `42.21` … `42.21` |
| 当前生效适配 | `42.21` … `42.22`（Overlay 放行，非上游正式支持） |
| 元数据来源 | `42/mod.info` |
| 作者 | DeadWorks Collective |
| 工作坊更新时间 | 2026-11-04 |
| 分发端 | both（双端） |
| 体积 / 文件 | 437.4 KB · 46 文件（lua 31，client 19，server 5；贴图 1；模型 1；翻译 3；Java 源码 0、jar/class 1） |

## 依赖与冲突

- 需要：`ZombieBuddy, Viewpoint, PZVoxelStudioViewpoint`
- 互斥：无
- 被依赖：`aparosa_DWVFTweaks`、`DeadWorksNomadRV`、`DeadWorksDaleRV`

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端候选；依赖 ZombieBuddy、Viewpoint、6282，状态同步与存档兼容必须单独验收。

当前 profile：both（双端）。

本机文件构成：客户端有 lua；服务端有 lua。

## 实测与排查

原件 1.0.4，42.21 上限；Overlay 只放宽元数据，未修改 Java/Lua 行为；不与旧 GridRVHost 分支混装。

**planned：仅完成依赖、版本与补丁指纹静态检查。** 迁移收尾按 Owner 要求不启动游戏；本候选组合未验证加载、联网、存档或视觉。

版本放行补丁：`A004/workspace/patches/mods/DeadWorksVehicleFramework/42/mod.info`。原件更新后须重新核对指纹；撤除此补丁后运行 check 会恢复原件版本限制。

```
cd A004
python lab.py check --profile b422-compat
grep -a 'DeadWorksVehicleFramework' runs/<trial>/*console.log
```

## 作者原话

```
Walkable interiors for DeadWorks vehicle mods. Enable this in your save or server mod list yourself, not only as a requirement.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3825724093`
- 本地原件：`A004/workspace/mods_library/3825724093/mods/DeadWorksVehicleFramework`
- 档案生成：`python tools/mod_archive.py --profile b422-compat`
