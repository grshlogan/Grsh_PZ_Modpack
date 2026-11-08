# KI5 车辆部件修复（Project Viewpoint - KI5 Vehicle Parts Fix）

**KI5 车部件渲染与装配修正** · 分类：渲染 / 修复 · 3815019204 · 启用 · 加载位次 22

## 它做什么

修正 Viewpoint 第一人称下 KI5 车辆部件的渲染与装配位置，避免部件错位或消失。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3815019204` |
| mod id | `ProjectViewpointKI5VehiclePartsFix` |
| 文件夹 | `ProjectViewpoint-KI5VehiclePartsFix` |
| 版本 / 适配 | `42.21` … `-` |
| 作者 | astan |
| 工作坊更新时间 | 2026-10-12 |
| 分发端 | both |
| 体积 / 文件 | 175.3 KB · 6 文件（lua 2，client 2，server 0；贴图 1；模型 0；翻译 0；Java 源码 0、jar/class 1） |

## 依赖与冲突

- 需要：`ZombieBuddy, Viewpoint`
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端挂载；Java 客户端模块。

本机实测文件构成：客户端有 lua；服务端无 lua（只挂载）。

## 实测与排查

require ZombieBuddy + Viewpoint；jar=ViewpointVehiclePartsGuard.jar。

```
python lab.py check --profile play
grep -a 'ProjectViewpoint-KI5VehiclePartsFix' runs/<trial>/console.log
```

## 作者原话

```
Fix for disappearing KI5 vehicle parts in Project Viewpoint. Keeps vehicle parts visible near the camera and uses expanded frustum checks farther away. Fixed adaptive behaviour, no configuration. Tested with Viewpoint 0.1.5a-hotfix and PZ 42.21; later game versions are not blocked.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3815019204`
- 本地快照：`workspace/mods_library/3815019204/mods/ProjectViewpoint-KI5VehiclePartsFix`
- 档案生成：`python tools/mod_archive.py --profile play`

