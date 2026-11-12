# DeadWorks Dale 房车（Dale's Chieftain RV）

**Dale房车的DeadWorks分支** · 分类：载具 / 房车 · `3820158673` · 启用 · 加载位次 59
归属：**兼容候选（未运行验收）**；档案视图 `b422-compat`。

## 它做什么

提供 DeadWorks Dale's Chieftain RV 分支；还依赖同包 DeadWorksNomadRV，不选择旧 Legacy/替代分支。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3820158673` |
| mod id | `DeadWorksDaleRV` |
| 文件夹 | `DeadWorksDaleRV` |
| Mod 版本 | `0.2.2` |
| 原件适配 | `42.21` … `42.21` |
| 当前生效适配 | `42.21` … `42.22`（Overlay 放行，非上游正式支持） |
| 元数据来源 | `42/mod.info` |
| 作者 | DeadWorks Collective |
| 工作坊更新时间 | 2026-11-04 |
| 分发端 | both（双端） |
| 体积 / 文件 | 53.5 MB · 218 文件（lua 3，client 1，server 0；贴图 49；模型 154；翻译 3） |

## 依赖与冲突

- 需要：`DeadWorksVehicleFramework, DeadWorksNomadRV, PZVoxelStudioViewpoint`
- 互斥：`GridRV, GridRVHost, DaleChieftainRV`
- 被依赖：无（叶子节点）

## 内容清单

没有独立脚本物品；载具和配方见下。

载具脚本 1 条：`DaleChieftainRV`

## 双端与联机

双端候选；依赖 DeadWorksVehicleFramework、DeadWorksNomadRV 与 6282。

当前 profile：both（双端）。

本机文件构成：客户端有 lua；服务端无 lua（只挂载）。

## 实测与排查

原件 0.2.2，42.21 上限；仅元数据 Overlay。外观、车内交互和持久化未验收。

**planned：仅完成依赖、版本与补丁指纹静态检查。** 迁移收尾按 Owner 要求不启动游戏；本候选组合未验证加载、联网、存档或视觉。

版本放行补丁：`A004/workspace/patches/mods/DeadWorksDaleRV/42/mod.info`。原件更新后须重新核对指纹；撤除此补丁后运行 check 会恢复原件版本限制。

```
cd A004
python lab.py check --profile b422-compat
grep -a 'DeadWorksDaleRV' runs/<trial>/*console.log
```

## 作者原话

```
Dale's Chieftain RV, model and profile for the DeadWorks Vehicle Framework.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3820158673`
- 本地原件：`A004/workspace/mods_library/3820158673/mods/DeadWorksDaleRV`
- 档案生成：`python tools/mod_archive.py --profile b422-compat`
