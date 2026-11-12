# KK 3D 货架（Project Viewpoint: KK's Shelves in 3D）

**货架按库存显示空/轻/满** · 分类：渲染 / 模型 · 3815931973 · 禁用 · 加载位次 未列

## 它做什么

货架、书柜、展示柜按容器内物品数量显示空、少量、堆满三种 3D 状态，增减物品自动更新。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3815931973` |
| mod id | `ProjectViewpointShelves` |
| 文件夹 | `ProjectViewpointShelves` |
| 版本 / 适配 | `42.21` … `42.21` |
| 作者 | Kauno |
| 工作坊更新时间 | 2026-10-14 |
| 分发端 | both |
| 体积 / 文件 | 176.3 MB · 4,714 文件（lua 1，client 1，server 0；贴图 1；模型 2352；翻译 0；Java 源码 0、jar/class 1） |

## 依赖与冲突

- 需要：`Viewpoint, ZombieBuddy`
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端挂载；带 Java 扩展。

本机实测文件构成：客户端有 lua；服务端无 lua（只挂载）。

## 实测与排查

只替换受支持的容器外观；与 6244/6282 共存，排在 6282 之后。

```
python lab.py check --profile play
grep -a 'ProjectViewpointShelves' runs/<trial>/console.log
```

## 作者原话

```
Adaptive empty, lightly stocked and heavily stocked 3D shelves for Project Viewpoint. Original meshes and textures.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3815931973`
- 本地快照：`workspace/mods_library/3815931973/mods/ProjectViewpointShelves`
- 档案生成：`python tools/mod_archive.py --profile play`

