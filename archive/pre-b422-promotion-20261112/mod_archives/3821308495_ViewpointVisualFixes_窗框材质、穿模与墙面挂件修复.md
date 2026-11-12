# Viewpoint 视觉修复（ViewpointVisualFixes）

**窗框材质、穿模与墙面挂件修复** · 分类：渲染 / 修复 · 3821308495 · 启用 · 加载位次 32

## 它做什么

独立修复 Viewpoint 的窗框材质、替换模型穿墙、墙面挂件对齐、天花板与结构面；可在 Delete → Graphics → Viewpoint Visual Fixes 里逐项开关。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3821308495` |
| mod id | `ViewpointVisualFixes` |
| 文件夹 | `ViewpointVisualFixes` |
| 版本 / 适配 | `42.21` … `42.21` |
| 作者 | - |
| 工作坊更新时间 | 2026-10-17 |
| 分发端 | both |
| 体积 / 文件 | 91.5 KB · 3 文件（lua 0，client 0，server 0；贴图 0；模型 0；翻译 0；Java 源码 0、jar/class 1） |

## 依赖与冲突

- 需要：`ZombieBuddy, Viewpoint`
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

纯客户端 Java 视觉模块；按双端装载以保持 mod 列表一致。

本机实测文件构成：客户端无 lua（纯资源）；服务端无 lua（只挂载）。

## 实测与排查

0.10.4；require ZombieBuddy + Viewpoint；nightly 0.1.7-rc3 未验证；jar=ViewpointVisualFixes.jar。

```
python lab.py check --profile play
grep -a 'ViewpointVisualFixes' runs/<trial>/console.log
```

## 作者原话

```
Independent visual repairs for Viewpoint: window materials, replacement-model clipping, wall alignment, ceilings and structural surfaces. Delete > Graphics > Viewpoint Visual Fixes.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3821308495`
- 本地快照：`workspace/mods_library/3821308495/mods/ViewpointVisualFixes`
- 档案生成：`python tools/mod_archive.py --profile play`

