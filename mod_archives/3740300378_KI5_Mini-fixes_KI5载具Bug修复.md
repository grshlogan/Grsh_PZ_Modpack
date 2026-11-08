# KI5小修（KI5 Mini-fixes）

**KI5载具Bug修复** · 分类：修复 / 载具 · 3740300378 · 启用 · 加载位次 23

## 它做什么

集中修 KI5 系列载具的常见 Bug：零件装不上、引擎盖错位、后备箱容量异常。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3740300378` |
| mod id | `KI5minifixes` |
| 文件夹 | `KI5MiniFixes` |
| 版本 / 适配 | `42.00` … `-` |
| 作者 | Пупсич |
| 工作坊更新时间 | 2026-10-03 |
| 分发端 | both |
| 体积 / 文件 | 521.5 KB · 22 文件（lua 6，client 2，server 1；贴图 2；模型 0；翻译 0） |

## 依赖与冲突

- 需要：`damnlib,YAPZLib`
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端。

本机实测文件构成：客户端有 lua；服务端有 lua。

## 实测与排查

require damnlib 与 YAPZLib，两个库都必须先加载。

```
python lab.py check --profile play
grep -a 'KI5MiniFixes' runs/<trial>/console.log
```

## 作者原话

```
Fixes some minor problems in KI5's mods.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3740300378`
- 本地快照：`workspace/mods_library/3740300378/mods/KI5MiniFixes`
- 档案生成：`python tools/mod_archive.py --profile play`

