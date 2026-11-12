# Viewpoint 车辆内饰（Viewpoint Vehicle Interiors）

**驾驶舱座椅、仪表与顶灯细节** · 分类：渲染 / 载具 · 3826550325 · 启用 · 加载位次 31

## 它做什么

给支持的车种补驾驶舱细节：座椅与饰板、随车型变化的材质、工作仪表、收音机 LCD、可在 V 菜单切换的顶灯；不改变后厢可行走逻辑。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3826550325` |
| mod id | `ViewpointInteriors` |
| 文件夹 | `ViewpointInteriors` |
| 版本 / 适配 | `42.21` … `42.21` |
| 作者 | gustavobr120 |
| 工作坊更新时间 | 2026-11-01 |
| 分发端 | both |
| 体积 / 文件 | 96.3 MB · 167 文件（lua 3，client 2，server 1；贴图 24；模型 93；翻译 30；Java 源码 0、jar/class 1） |

## 依赖与冲突

- 需要：`Viewpoint, ZombieBuddy`
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

客户端视觉为主，但含 server Lua 车灯同步，按双端装载。

本机实测文件构成：客户端有 lua；服务端有 lua。

## 实测与排查

1.0.1；作者页面写适配 Viewpoint 0.1.6.1 + ZombieBuddy 2.3.0+，nightly 0.1.7-rc3 未验证；jar=ViewpointInteriors.jar。

```
python lab.py check --profile play
grep -a 'ViewpointInteriors' runs/<trial>/console.log
```

## 作者原话

```
Vehicle cabin details for Project Viewpoint: measured interiors, working instruments, radio LCD and switchable dome lights. Supported vehicle profiles retain native fallback. See README.md for scope and known issues.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3826550325`
- 本地快照：`workspace/mods_library/3826550325/mods/ViewpointInteriors`
- 档案生成：`python tools/mod_archive.py --profile play`

