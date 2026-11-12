# 僵尸伙伴（ZombieBuddy）

**模组框架与3D动画核心** · 分类：框架 / 渲染底层 · `3619862853` · 启用 · 加载位次 1
归属：**日常组合**；档案视图 `b422-compat`。

## 它做什么

给 Java 模组提供植入通道，并提供 3D 视角、骨骼动画与模型替换的底层支持；Viewpoint 全家桶都建立在它之上。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3619862853` |
| mod id | `ZombieBuddy` |
| 文件夹 | `ZombieBuddy` |
| Mod 版本 | `-` |
| 原件适配 | `-` … `-` |
| 当前生效适配 | `-` … `-`（原件） |
| 元数据来源 | `42/mod.info` |
| 作者 | Zed |
| 工作坊更新时间 | 2026-10-03 |
| 分发端 | both（双端） |
| 体积 / 文件 | 13.8 MB · 202 文件（lua 4，client 4，server 0；贴图 12；模型 0；翻译 2；Java 源码 150、jar/class 1） |

## 依赖与冲突

- 需要：无
- 互斥：无
- 被依赖：`Viewpoint`、`AimohPmxPreview`、`PzPerformanceFixes`、`SuPerfCore`、`ViewpointLivingProps`、`aparosa_vpmo_RaccoonCityB42`、`ViewpointDLSS`、`ViewpointVisualFixes`、`PV-modmapbakefix`、`ProjectViewpointShelves`、`ProjectViewpoint-KI5VehiclePartsFix`、`ViewpointVehicleShellFix`、`ViewpointPartPaint`、`LaoYuTranslationJava`、`BasileDoors3D`、`ViewpointKI5Materials`、`ViewpointInteriors`、`GridVansHost`、`GridVans`、`DeadWorksVehicleFramework`、`VariableSkinBoobBounce`、`VariableSkinBoobBounceViewpoint`

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端都要装。原生库 zbNative.dll、ZombieBuddy.jar、.zbs 要落在游戏根目录，客户端用 -agentlib:zbNative 启动。

当前 profile：both（双端）。

本机文件构成：客户端有 lua；服务端无 lua（只挂载）。

## 实测与排查

迁移前 B42.22.2 日志出现 [ZB] activating ZombieBuddy v2.3.4、[ZB] Agent installed.；当前根补丁修复服务端角色判断。AnimSets 目录缺失是已知未阻断启动的警告，不能代替玩法验收。

```
cd A004
python lab.py check --profile b422-compat
grep -a 'ZombieBuddy' runs/<trial>/*console.log
```

## 作者原话

```
Java bytecode manipulation framework for Project Zomboid. Enables runtime patching of game classes and Lua integration for advanced modding.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3619862853`
- 本地原件：`A004/workspace/mods_library/3619862853/mods/ZombieBuddy`
- 档案生成：`python tools/mod_archive.py --profile b422-compat`
