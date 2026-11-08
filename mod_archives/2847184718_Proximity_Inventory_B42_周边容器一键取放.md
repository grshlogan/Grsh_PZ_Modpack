# 就近存取（Proximity Inventory B42）

**周边容器一键取放** · 分类：UI / 便利 · 2847184718 · 启用 · 加载位次 15

## 它做什么

把附近容器（箱子、柜子、后备箱）里的物品汇总到一个面板里直接取放，不用逐个打开。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `2847184718` |
| mod id | `ProximityInventory` |
| 文件夹 | `ProximityInventory` |
| 版本 / 适配 | `-` … `-` |
| 作者 | - |
| 工作坊更新时间 | 2026-08-30 |
| 分发端 | both |
| 体积 / 文件 | 685.9 KB · 57 文件（lua 6，client 6，server 0；贴图 6；模型 0；翻译 41） |

## 依赖与冲突

- 需要：无
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端；服务端负责校验距离，属于服务端授权型便利 mod。

本机实测文件构成：客户端有 lua；服务端无 lua（只挂载）。

## 实测与排查

B42 重制版；物品移动走的是原版容器接口，不复制物品。

```
python lab.py check --profile play
grep -a 'ProximityInventory' runs/<trial>/console.log
```

## 作者原话

```
This is the description of Proximity Inventory.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=2847184718`
- 本地快照：`workspace/mods_library/2847184718/mods/ProximityInventory`
- 档案生成：`python tools/mod_archive.py --profile play`

