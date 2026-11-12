# 视角屋顶（Viewpoint - Roofs (WIP)）

**屋顶遮挡与显示** · 分类：渲染 · `3817294484` · 启用 · 加载位次 6
归属：**日常组合**；档案视图 `b422-compat`。

## 它做什么

处理屋顶在第一人称下的遮挡关系：进屋自动隐藏、抬头可见完整屋面。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3817294484` |
| mod id | `ViewpointRoofs` |
| 文件夹 | `ViewpointRoofs` |
| Mod 版本 | `0.9.3` |
| 原件适配 | `-` … `-` |
| 当前生效适配 | `-` … `-`（原件） |
| 元数据来源 | `42/mod.info` |
| 作者 | Timidis1 |
| 工作坊更新时间 | 2026-11-06 |
| 分发端 | both（双端） |
| 体积 / 文件 | 84.5 MB · 24,690 文件（lua 3，client 2，server 0；贴图 5927；模型 9003；翻译 0；Java 源码 0、jar/class 1） |

## 依赖与冲突

- 需要：无
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端挂载。

当前 profile：both（双端）。

本机文件构成：客户端有 lua；服务端无 lua（只挂载）。

## 实测与排查

工作坊日期快照 2026-11-06；迁移前 B42.22.2 已加载，屋顶遮挡实际效果未验收。

```
cd A004
python lab.py check --profile b422-compat
grep -a 'ViewpointRoofs' runs/<trial>/*console.log
```

## 作者原话

```
Work in progress. An alternative set of 3D roofs for Viewpoint's first-person view on the vanilla map: 3D roof tiles made from the game's own roof art, plus the back slopes and gable walls the map leaves out. Works on saves you already have. Requires Viewpoint.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3817294484`
- 本地原件：`A004/workspace/mods_library/3817294484/mods/ViewpointRoofs`
- 档案生成：`python tools/mod_archive.py --profile b422-compat`
