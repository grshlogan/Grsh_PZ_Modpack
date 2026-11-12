# 右键修复（Viewpoint - Right Click Fix）

**右键直接打开指向物体菜单** · 分类：操作 / 修复 · 3819018807 · 启用 · 加载位次 16

## 它做什么

第一/第三人称且显示光标时，右键直接打开光标指向物体的交互菜单，不必先左键选中。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3819018807` |
| mod id | `ViewpointRightClick` |
| 文件夹 | `ViewpointRightClick` |
| 版本 / 适配 | `42.21` … `-` |
| 作者 | - |
| 工作坊更新时间 | 2026-10-14 |
| 分发端 | both |
| 体积 / 文件 | 347.1 KB · 12 文件（lua 1，client 1，server 0；贴图 1；模型 0；翻译 2；Java 源码 4、jar/class 1） |

## 依赖与冲突

- 需要：`Viewpoint`
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端挂载；纯客户端输入逻辑。

本机实测文件构成：客户端有 lua；服务端无 lua（只挂载）。

## 实测与排查

Java 模块 ViewpointRightClick.jar，需 ZombieBuddy 批准。

```
python lab.py check --profile play
grep -a 'ViewpointRightClick' runs/<trial>/console.log
```

## 作者原话

```
Addon for Project Viewpoint. In first and third person with the mouse cursor shown, right click anything under the cursor, animals included, to open its menu. Menus open up to 5 tiles from your character (1-30 in Mod Options). Mouse-look and the isometric view keep the game's own right click.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3819018807`
- 本地快照：`workspace/mods_library/3819018807/mods/ViewpointRightClick`
- 档案生成：`python tools/mod_archive.py --profile play`

