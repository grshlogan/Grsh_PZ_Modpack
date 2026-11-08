# 分类整理（Better Sorting）

**库存分类菜单** · 分类：UI / 整理 · 2313387159 · 启用 · 加载位次 9

## 它做什么

给容器和背包加分类标签页，按类型快速过滤物品。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `2313387159` |
| mod id | `BetterSortCC` |
| 文件夹 | `BetterSorting` |
| 版本 / 适配 | `-` … `-` |
| 作者 | ChthonicKnight |
| 工作坊更新时间 | 2026-09-12 |
| 分发端 | both |
| 体积 / 文件 | 1.7 MB · 149 文件（lua 78，client 63，server 0；贴图 4；模型 0；翻译 59） |

## 依赖与冲突

- 需要：无
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端；纯 UI，不影响物品数据。

本机实测文件构成：客户端有 lua；服务端无 lua（只挂载）。

## 实测与排查

老牌 mod（B41 起就在用），B42 适配正常。

```
python lab.py check --profile play
grep -a 'BetterSorting' runs/<trial>/console.log
```

## 作者原话

```
v2.1.5 - Complete overhaul to item categories and various name tweaks.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=2313387159`
- 本地快照：`workspace/mods_library/2313387159/mods/BetterSorting`
- 档案生成：`python tools/mod_archive.py --profile play`

