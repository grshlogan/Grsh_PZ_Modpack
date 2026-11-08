# 3D 门与车库（Project Viewpoint - 3D Doors, Gates & Garages）

**276 个门模型替代** · 分类：渲染 / 模型 · 3818859807 · 启用 · 加载位次 5

## 它做什么

把原版门、玻璃店门、安全/监狱门、铁丝网门、木栅门和车库门换成 3D 模型，覆盖 396 个原生门状态，保留开门、锁、血量、碰撞与存档数据。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3818859807` |
| mod id | `BasileDoors3D` |
| 文件夹 | `BasileDoors3D` |
| 版本 / 适配 | `42.21` … `42.21` |
| 作者 | Basile |
| 工作坊更新时间 | 2026-10-23 |
| 分发端 | both |
| 体积 / 文件 | 65.6 MB · 315 文件（lua 2，client 2，server 0；贴图 33；模型 276；翻译 0；Java 源码 0、jar/class 1） |

## 依赖与冲突

- 需要：`ZombieBuddy, Viewpoint`
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端挂载；渲染在客户端完成，服务端只保持 mod 列表一致。

本机实测文件构成：客户端有 lua；服务端无 lua（只挂载）。

## 实测与排查

作者建议装在 ZombieBuddy / Viewpoint / Door Fix 之后；本包已移除 Door Fix，由它接管门类。

```
python lab.py check --profile play
grep -a 'BasileDoors3D' runs/<trial>/console.log
```

## 作者原话

```
Native-style 3D doors, wire-mesh gates, timber and rail farm gates, and sectional or roller garage doors. Distinct native finishes, real garage windows and full-height clear-glass bay doors with slim frames. Client-side visual replacements preserve native gameplay.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3818859807`
- 本地快照：`workspace/mods_library/3818859807/mods/BasileDoors3D`
- 档案生成：`python tools/mod_archive.py --profile play`

