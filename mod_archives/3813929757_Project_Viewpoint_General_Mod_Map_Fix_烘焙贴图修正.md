# 地图烘焙修复（Project Viewpoint: General Mod Map Fix）

**烘焙贴图修正** · 分类：修复 / 地图 · 3813929757 · 启用 · 加载位次 10

## 它做什么

修正 Project Viewpoint 地图的 bake 烘焙贴图错误（黑块、错位）。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3813929757` |
| mod id | `PV-modmapbakefix` |
| 文件夹 | `PV-modmapbakefix` |
| 版本 / 适配 | `42.21` … `42.21` |
| 作者 | PV-modmapbakefix contributors |
| 工作坊更新时间 | 2026-10-11 |
| 分发端 | both |
| 体积 / 文件 | 25.8 KB · 4 文件（lua 0，client 0，server 0；贴图 0；模型 0；翻译 0；Java 源码 0、jar/class 1） |

## 依赖与冲突

- 需要：`Viewpoint, ZombieBuddy`
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端。

本机实测文件构成：客户端无 lua（纯资源）；服务端无 lua（只挂载）。

## 实测与排查

25.8 KB 的纯补丁，versionMin/Max 都锁 42.21。

```
python lab.py check --profile play
grep -a 'PV-modmapbakefix' runs/<trial>/console.log
```

## 作者原话

```
Fixes missing mid/far terrain caused by overlapping mod map cells in Project Viewpoint. Preserves native Viewpoint rendering settings. Requires Viewpoint and ZombieBuddy. Restart the game after enabling or disabling.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3813929757`
- 本地快照：`workspace/mods_library/3813929757/mods/PV-modmapbakefix`
- 档案生成：`python tools/mod_archive.py --profile play`

