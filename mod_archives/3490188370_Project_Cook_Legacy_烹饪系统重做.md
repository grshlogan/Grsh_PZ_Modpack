# 烹饪重制（Project Cook [Legacy]）

**烹饪系统重做** · 分类：玩法 / 制作 · 3490188370 · 启用 · 加载位次 29

## 它做什么

重做烹饪流程：食材组合、菜谱解锁、成品属性都换了一套规则。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3490188370` |
| mod id | `Project_Cook` |
| 文件夹 | `Project_Cook` |
| 版本 / 适配 | `42.10` … `42.12` |
| 作者 | Rocco, Afyrmo |
| 工作坊更新时间 | 2026-10-31 |
| 分发端 | both |
| 体积 / 文件 | 7.6 MB · 582 文件（lua 53，client 48，server 2；贴图 246；模型 0；翻译 252） |

## 依赖与冲突

- 需要：`NeatUI_Framework`
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端；配方与食物属性由服务端裁决，必须两端版本一致。

本机实测文件构成：客户端有 lua；服务端有 lua。

## 实测与排查

require NeatUI_Framework；当前是 Legacy 分支，Lua 驱动、几乎不含脚本物品。

```
python lab.py check --profile play
grep -a 'Project_Cook' runs/<trial>/console.log
```

## 作者原话

```
Adds a cooking recipe browser and helper UI for Project Zomboid. Includes support for older B42 builds and Build 42.15+ through separate internal mod variants, with Build 42.21.0 compatibility checked.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3490188370`
- 本地快照：`workspace/mods_library/3490188370/mods/Project_Cook`
- 档案生成：`python tools/mod_archive.py --profile play`

