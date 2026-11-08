# KI5 血迹贴图修复（Project Viewpoint - KI5 Blood Texture Fix）

**KI5 车血迹材质修正** · 分类：渲染 / 修复 · 3819702412 · 启用 · 加载位次 21

## 它做什么

修正 KI5 车辆被血溅后材质/贴图显示异常。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3819702412` |
| mod id | `ViewpointKI5Materials` |
| 文件夹 | `ViewpointKI5Materials` |
| 版本 / 适配 | `42.21.0` … `42.21.99` |
| 作者 | Motor |
| 工作坊更新时间 | 2026-10-14 |
| 分发端 | both |
| 体积 / 文件 | 72.1 KB · 10 文件（lua 1，client 1，server 0；贴图 2；模型 0；翻译 0；Java 源码 2、jar/class 1） |

## 依赖与冲突

- 需要：`ZombieBuddy, Viewpoint, damnlib`
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端挂载；Java 模块。

本机实测文件构成：客户端有 lua；服务端无 lua（只挂载）。

## 实测与排查

额外 require damnlib，必须排在 damnlib 之后；versionMax=42.21.99。

```
python lab.py check --profile play
grep -a 'ViewpointKI5Materials' runs/<trial>/console.log
```

## 作者原话

```
Fixes false blood stains on KI5/DAMN vehicles in Project Viewpoint. Preserves real blood and body damage. Исправляет ложные кровавые пятна на машинах KI5/DAMN, сохраняя настоящую кровь и повреждения.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3819702412`
- 本地快照：`workspace/mods_library/3819702412/mods/ViewpointKI5Materials`
- 档案生成：`python tools/mod_archive.py --profile play`

