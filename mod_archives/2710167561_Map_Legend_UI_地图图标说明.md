# 地图图例（Map Legend UI）

**地图图标说明** · 分类：UI / 地图 · 2710167561 · 启用 · 加载位次 32

## 它做什么

给大地图加图例：每种标记代表什么、当前视口比例尺多少。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `2710167561` |
| mod id | `MapLegendUI` |
| 文件夹 | `MapLegendUI` |
| 版本 / 适配 | `41.65` … `-` |
| 作者 | NikGamer |
| 工作坊更新时间 | 2026-03-14 |
| 分发端 | both |
| 体积 / 文件 | 787.8 KB · 94 文件（lua 2，client 2，server 0；贴图 22；模型 0；翻译 68） |

## 依赖与冲突

- 需要：无
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端；纯客户端显示。

本机实测文件构成：客户端有 lua；服务端无 lua（只挂载）。

## 实测与排查

老 mod，B42 仍可用。

```
python lab.py check --profile play
grep -a 'MapLegendUI' runs/<trial>/console.log
```

## 作者原话

```
Adds a legend from town maps to in-game world map.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=2710167561`
- 本地快照：`workspace/mods_library/2710167561/mods/MapLegendUI`
- 档案生成：`python tools/mod_archive.py --profile play`

