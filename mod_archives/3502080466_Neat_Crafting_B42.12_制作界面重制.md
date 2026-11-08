# Neat制作（Neat Crafting [B42.12]）

**制作界面重制** · 分类：UI / 制作 · 3502080466 · 启用 · 加载位次 30

## 它做什么

把原版制作面板换成可分栏、可搜索、可收藏的新界面。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3502080466` |
| mod id | `Neat_Crafting` |
| 文件夹 | `Neat_Crafting` |
| 版本 / 适配 | `42.9` … `42.12` |
| 作者 | Rocco, Afyrmo |
| 工作坊更新时间 | 2026-11-05 |
| 分发端 | both |
| 体积 / 文件 | 4.1 MB · 347 文件（lua 51，client 50，server 0；贴图 99；模型 0；翻译 172） |

## 依赖与冲突

- 需要：`NeatUI_Framework`
- 互斥：`WhatCanICraft_Addon, WhatCanICraft`
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端；配方数据仍以服务端为准。

本机实测文件构成：客户端有 lua；服务端无 lua（只挂载）。

## 实测与排查

require NeatUI_Framework；附带可选的像素图标包 Project_Cook_Pixel_Icon。

```
python lab.py check --profile play
grep -a 'Neat_Crafting' runs/<trial>/console.log
```

## 作者原话

```
Neat Crafting replaces and enhances the Project Zomboid Build 42 crafting interface. By default, crafting inputs follow vanilla transfer behavior; a sandbox option can restore direct crafting from accessible containers. Avoid removing from existing saves without Neat Crafting - Safe Uninstall Support.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3502080466`
- 本地快照：`workspace/mods_library/3502080466/mods/Neat_Crafting`
- 档案生成：`python tools/mod_archive.py --profile play`

