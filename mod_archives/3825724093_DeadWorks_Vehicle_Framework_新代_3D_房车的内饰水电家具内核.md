# DeadWorks 房车框架（DeadWorks Vehicle Framework）

**新代 3D 房车的内饰/水电/家具内核** · 分类：载具 / 房车 · 3825724093 · 启用 · 加载位次 14

## 它做什么

给 Nomad RV 与 Dale Chieftain RV 提供可行走内饰、门窗踏板、座椅家具、电池/水/家电、遮阳篷、装甲等 profile 系统，联机由客户端-主机同步。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3825724093` |
| mod id | `DeadWorksVehicleFramework` |
| 文件夹 | `DeadWorksVehicleFramework` |
| 版本 / 适配 | `42.21` … `42.21` |
| 作者 | DeadWorks Collective |
| 工作坊更新时间 | 2026-11-04 |
| 分发端 | both |
| 体积 / 文件 | 437.4 KB · 46 文件（lua 31，client 19，server 5；贴图 1；模型 1；翻译 3；Java 源码 0、jar/class 1） |

## 依赖与冲突

- 需要：`ZombieBuddy, Viewpoint, PZVoxelStudioViewpoint`
- 互斥：无
- 被依赖：`DeadWorksDaleRV`、`DeadWorksNomadRV`、`aparosa_DWVFTweaks`

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端都要装；jar 在 `media/java/`，服务端由 ZombieBuddy 加载。

本机实测文件构成：客户端有 lua；服务端有 lua。

## 实测与排查

1.0.4；与 legacy GridRV 的 Java 同时加载会提示「old GridRV java is loaded too」，车厢会出错，所以 legacy 三件已停用。

```
python lab.py check --profile play
grep -a 'DeadWorksVehicleFramework' runs/<trial>/console.log
```

## 作者原话

```
Walkable interiors for DeadWorks vehicle mods. Enable this in your save or server mod list yourself, not only as a requirement.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3825724093`
- 本地快照：`workspace/mods_library/3825724093/mods/DeadWorksVehicleFramework`
- 档案生成：`python tools/mod_archive.py --profile play`

