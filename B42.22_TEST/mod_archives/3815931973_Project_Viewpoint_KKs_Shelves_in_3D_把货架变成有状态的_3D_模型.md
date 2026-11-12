# 3D 货架（Project Viewpoint: KK's Shelves in 3D）

**把货架变成有状态的 3D 模型** · 分类：渲染 / Viewpoint 扩展 · `3815931973` · 启用 · 加载位次 14

## 它做什么

为 Viewpoint 添加 3D 货架/展示柜模型和容器状态支持，依赖 Viewpoint 和 ZombieBuddy；Grsh 旧档案曾禁用，当前 0.4.8 已写 42.22。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3815931973` |
| mod id | `ProjectViewpointShelves` |
| 文件夹 | `ProjectViewpointShelves` |
| 版本 / 适配 | `42.22` … `42.22` |
| 作者 | Kauno |
| 工作坊更新时间 | 2026-11-10 |
| 分发端 | both（双端） |
| 体积 / 文件 | 176.3 MB · 4,714 文件（lua 1，client 1，server 0；贴图 1；模型 2352；翻译 0；Java 源码 0、jar/class 1） |

## 依赖与冲突

- 需要：`Viewpoint, ZombieBuddy`
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端挂载；模型与容器状态在客户端加载，服务端需要 mod 列表一致。

当前 profile：both（双端）。

本机文件构成：客户端有 lua；服务端无 lua（只挂载）。

## 实测与排查

上游 0.4.8；versionMin=42.22，versionMax=42.22；2026-11-10 更新；原 Grsh 档案为禁用，已按新版重新启用。

```
cd A004/B42.22_TEST
python lab.py check --profile b422-batch2
grep -a 'ProjectViewpointShelves' runs/<trial>/console.log
```

## 作者原话

```
Adaptive empty, lightly stocked and heavily stocked 3D shelves for Project Viewpoint. Original meshes and textures.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3815931973`
- 本地快照（测试台）：`A004/B42.22_TEST/workspace/mods_library/3815931973/mods/ProjectViewpointShelves`
- 档案生成：`python tools/mod_archive.py --profile b422-batch2`
