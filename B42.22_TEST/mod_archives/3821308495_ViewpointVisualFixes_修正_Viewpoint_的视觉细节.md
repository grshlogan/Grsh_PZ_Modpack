# Viewpoint 视觉修复（ViewpointVisualFixes）

**修正 Viewpoint 的视觉细节** · 分类：渲染 / 修复 · `3821308495` · 启用 · 加载位次 12

## 它做什么

修正 Viewpoint 的材质、光照和渲染细节问题，当前版本专门适配 42.22；依赖 Viewpoint 和 ZombieBuddy。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3821308495` |
| mod id | `ViewpointVisualFixes` |
| 文件夹 | `ViewpointVisualFixes` |
| 版本 / 适配 | `42.22` … `42.22` |
| 作者 | - |
| 工作坊更新时间 | 2026-11-10 |
| 分发端 | both（双端） |
| 体积 / 文件 | 91.5 KB · 3 文件（lua 0，client 0，server 0；贴图 0；模型 0；翻译 0；Java 源码 0、jar/class 1） |

## 依赖与冲突

- 需要：`ZombieBuddy, Viewpoint`
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端挂载；渲染逻辑在客户端。

当前 profile：both（双端）。

本机文件构成：客户端无 lua（纯资源）；服务端无 lua（只挂载）。

## 实测与排查

上游 0.10.5；versionMin=42.22，versionMax=42.22；2026-11-10 更新。

```
cd A004/B42.22_TEST
python lab.py check --profile b422-batch2
grep -a 'ViewpointVisualFixes' runs/<trial>/console.log
```

## 作者原话

```
Independent visual repairs for Viewpoint: window materials, replacement-model clipping, wall alignment, ceilings and structural surfaces. Delete > Graphics > Viewpoint Visual Fixes.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3821308495`
- 本地快照（测试台）：`A004/B42.22_TEST/workspace/mods_library/3821308495/mods/ViewpointVisualFixes`
- 档案生成：`python tools/mod_archive.py --profile b422-batch2`
