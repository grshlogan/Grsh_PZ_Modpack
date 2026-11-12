# KI5 载具零件修复（Project Viewpoint - KI5 Vehicle Parts Fix）

**修正 KI5 载具零件的显示位置** · 分类：修复 / Viewpoint 扩展 · `3815019204` · 启用 · 加载位次 44
归属：**日常组合**；档案视图 `b422-compat`。

## 它做什么

修正 Project Viewpoint 下 KI5 载具零件的显示与位置，避免零件错位或悬空；依赖 Viewpoint 和 ZombieBuddy。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3815019204` |
| mod id | `ProjectViewpointKI5VehiclePartsFix` |
| 文件夹 | `ProjectViewpoint-KI5VehiclePartsFix` |
| Mod 版本 | `1.3` |
| 原件适配 | `42.21` … `-` |
| 当前生效适配 | `42.21` … `-`（原件） |
| 元数据来源 | `42/mod.info` |
| 作者 | astan |
| 工作坊更新时间 | 2026-10-11 |
| 分发端 | both（双端） |
| 体积 / 文件 | 175.3 KB · 6 文件（lua 2，client 2，server 0；贴图 1；模型 0；翻译 0；Java 源码 0、jar/class 1） |

## 依赖与冲突

- 需要：`ZombieBuddy, Viewpoint`
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端挂载；Java 客户端补丁，服务端只校验 mod 列表；放在 KI5 载具之后加载。

当前 profile：both（双端）。

本机文件构成：客户端有 lua；服务端无 lua（只挂载）。

## 实测与排查

上游 1.3；versionMin=42.21，无 versionMax；2026-10-11 更新；jar=ViewpointVehiclePartsGuard.jar。

```
cd A004
python lab.py check --profile b422-compat
grep -a 'ProjectViewpointKI5VehiclePartsFix' runs/<trial>/*console.log
```

## 作者原话

```
Fix for disappearing KI5 vehicle parts in Project Viewpoint. Keeps vehicle parts visible near the camera and uses expanded frustum checks farther away. Fixed adaptive behaviour, no configuration. Tested with Viewpoint 0.1.5a-hotfix and PZ 42.21; later game versions are not blocked.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3815019204`
- 本地原件：`A004/workspace/mods_library/3815019204/mods/ProjectViewpoint-KI5VehiclePartsFix`
- 档案生成：`python tools/mod_archive.py --profile b422-compat`
