# 生活道具（Viewpoint: Living Props）

**会变状态的家具 3D 化** · 分类：渲染 / 模型 · 3816442251 · 启用 · 加载位次 9

## 它做什么

壁炉（柴火、火焰、壁炉架）、书柜、货架、垃圾桶等会随状态变化的家具补上对应 3D 模型。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3816442251` |
| mod id | `ViewpointLivingProps` |
| 文件夹 | `ViewpointLivingProps` |
| 版本 / 适配 | `42.21` … `-` |
| 作者 | - |
| 工作坊更新时间 | 2026-10-14 |
| 分发端 | both |
| 体积 / 文件 | 78.0 MB · 1,480 文件（lua 9，client 9，server 0；贴图 183；模型 1095；翻译 0；Java 源码 10、jar/class 1） |

## 依赖与冲突

- 需要：`Viewpoint, ZombieBuddy`
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端挂载；带 Java helper。

本机实测文件构成：客户端有 lua；服务端无 lua（只挂载）。

## 实测与排查

需在 ZombieBuddy 批准它的 Java 助手；排在 6282 之后覆盖同名图块。

```
python lab.py check --profile play
grep -a 'ViewpointLivingProps' runs/<trial>/console.log
```

## 作者原话

```
Fan-made add-on for Project Viewpoint (not by Hiro.uou). Objects whose sprite changes with their state now change in 3D too: road cones, drums, stop signs and mailboxes (with dented versions after a vehicle hits them), fireplaces (firebox, logs, flickering fire, wall panels, mantels and chimneys), stoves, ovens and microwaves (glowing burners, flames, spinning plate, and a little light from stoves that are on), televisions (the screen follows the game's channel), wall light switches (lever up/down and a little glowing light in the dark) and door curtains (open or closed; a closed curtain darkens the room). Everything runs on your own computer, so it also works on servers that do not have the mod. Needs Viewpoint and ZombieBuddy. Load this mod after Viewpoint, ZombieBuddy and your other model packs.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3816442251`
- 本地快照：`workspace/mods_library/3816442251/mods/ViewpointLivingProps`
- 档案生成：`python tools/mod_archive.py --profile play`

