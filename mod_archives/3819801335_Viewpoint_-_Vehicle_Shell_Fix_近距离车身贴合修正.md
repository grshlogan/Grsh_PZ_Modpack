# 车身外壳修复（Viewpoint - Vehicle Shell Fix）

**近距离车身贴合修正** · 分类：渲染 / 修复 · 3819801335 · 启用 · 加载位次 23

## 它做什么

修正 Viewpoint 下车辆外壳在近距离的贴合与近裁剪问题。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3819801335` |
| mod id | `ViewpointVehicleShellFix` |
| 文件夹 | `ViewpointVehicleShellFix` |
| 版本 / 适配 | `42.21` … `-` |
| 作者 | Community compatibility patch |
| 工作坊更新时间 | 2026-10-21 |
| 分发端 | both |
| 体积 / 文件 | 40.5 KB · 10 文件（lua 0，client 0，server 0；贴图 2；模型 0；翻译 0；Java 源码 3、jar/class 1） |

## 依赖与冲突

- 需要：`ZombieBuddy, Viewpoint`
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端挂载；Java 模块。

本机实测文件构成：客户端无 lua，但带 Java 源码补丁；服务端无 lua（只挂载）。

## 实测与排查

require ZombieBuddy + Viewpoint；jar=ViewpointVehicleShellFix.jar。

```
python lab.py check --profile play
grep -a 'ViewpointVehicleShellFix' runs/<trial>/console.log
```

## 作者原话

```
Alternative workaround for close/interior vehicle-shell disappearance that persists after trying astan's original KI5 Vehicle Parts Fix. Made with AI tools; future support is not guaranteed.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3819801335`
- 本地快照：`workspace/mods_library/3819801335/mods/ViewpointVehicleShellFix`
- 档案生成：`python tools/mod_archive.py --profile play`

