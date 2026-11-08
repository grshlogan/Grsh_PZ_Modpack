# 性能修复（PzPerformanceFixes）

**帧率与卡顿优化** · 分类：性能 · 3826630779 · 启用 · 加载位次 30

## 它做什么

针对 B42 的性能补丁：物品扫描从 12 秒降到 2 秒、Lua 列表 9 秒到 2 秒、开车最差帧从 400-600ms 降到 250ms。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3826630779` |
| mod id | `PzPerformanceFixes` |
| 文件夹 | `PzPerformanceFixes` |
| 版本 / 适配 | `42.0.0` … `-` |
| 作者 | Alex |
| 工作坊更新时间 | 2026-11-03 |
| 分发端 | both |
| 体积 / 文件 | 1.1 MB · 89 文件（lua 0，client 0，server 0；贴图 2；模型 0；翻译 0；Java 源码 76、jar/class 1） |

## 依赖与冲突

- 需要：`ZombieBuddy`
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端。

本机实测文件构成：客户端无 lua，但带 Java 源码补丁；服务端无 lua（只挂载）。

## 实测与排查

需要 ZombieBuddy ≥ 2.3.0。

```
python lab.py check --profile play
grep -a 'PzPerformanceFixes' runs/<trial>/console.log
```

## 作者原话

```
Faster loading, fewer hitches and fewer vanilla errors for Build 42. Needs ZombieBuddy. Each player enables it for themselves; a host can also add it to the server's mod list for the server patches, and then every player needs it. No gameplay changes. Every patch has an off switch.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3826630779`
- 本地快照：`workspace/mods_library/3826630779/mods/PzPerformanceFixes`
- 档案生成：`python tools/mod_archive.py --profile play`

