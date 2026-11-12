# 地图烘焙修复（Project Viewpoint: General Mod Map Fix）

**修复地图 mod 的烘焙与显示** · 分类：渲染 / 地图 · `3813929757` · 启用 · 加载位次 13
归属：**日常组合**；档案视图 `b422-compat`。

## 它做什么

修复 Project Viewpoint 下地图 mod 的烘焙与显示问题，当前版本支持 42.22；依赖 Viewpoint 和 ZombieBuddy。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3813929757` |
| mod id | `PV-modmapbakefix` |
| 文件夹 | `PV-modmapbakefix` |
| Mod 版本 | `0.1.4` |
| 原件适配 | `42.21` … `42.22` |
| 当前生效适配 | `42.21` … `42.22`（原件） |
| 元数据来源 | `42/mod.info` |
| 作者 | PV-modmapbakefix contributors |
| 工作坊更新时间 | 2026-11-10 |
| 分发端 | both（双端） |
| 体积 / 文件 | 25.8 KB · 4 文件（lua 0，client 0，server 0；贴图 0；模型 0；翻译 0；Java 源码 0、jar/class 1） |

## 依赖与冲突

- 需要：`Viewpoint, ZombieBuddy`
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端挂载；实际修复在客户端。

当前 profile：both（双端）。

本机文件构成：客户端无 lua（纯资源）；服务端无 lua（只挂载）。

## 实测与排查

上游 0.1.4；versionMin=42.21，versionMax=42.22；2026-11-10 更新。

```
cd A004
python lab.py check --profile b422-compat
grep -a 'PV-modmapbakefix' runs/<trial>/*console.log
```

## 作者原话

```
Fixes missing mid/far terrain caused by overlapping mod map cells in Project Viewpoint. Preserves native Viewpoint rendering settings. Requires Viewpoint and ZombieBuddy. Restart the game after enabling or disabling.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3813929757`
- 本地原件：`A004/workspace/mods_library/3813929757/mods/PV-modmapbakefix`
- 档案生成：`python tools/mod_archive.py --profile b422-compat`
