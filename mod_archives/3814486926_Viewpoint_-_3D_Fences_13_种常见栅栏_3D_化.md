# 3D 栅栏（Viewpoint - 3D Fences）

**13 种常见栅栏 3D 化** · 分类：渲染 / 模型 · 3814486926 · 启用 · 加载位次 8

## 它做什么

把最常见 13 种栅栏从「贴图铺在盒子上」换成尖桩、木板、横杆、立柱模型。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3814486926` |
| mod id | `ViewpointFences3D` |
| 文件夹 | `ViewpointFences3D` |
| 版本 / 适配 | `42.21` … `-` |
| 作者 | - |
| 工作坊更新时间 | 2026-10-06 |
| 分发端 | both |
| 体积 / 文件 | 2.9 MB · 190 文件（lua 1，client 1，server 0；贴图 49；模型 69；翻译 0） |

## 依赖与冲突

- 需要：`Viewpoint`
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

纯客户端，可安全增删。

本机实测文件构成：客户端有 lua；服务端无 lua（只挂载）。

## 实测与排查

与 6282 模型包有 fencing 图块重叠，本包排在 6282 之后以取得优先。

```
python lab.py check --profile play
grep -a 'ViewpointFences3D' runs/<trial>/console.log
```

## 作者原话

```
3D models for the fences you see most often, for Viewpoint's first-person view.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3814486926`
- 本地快照：`workspace/mods_library/3814486926/mods/ViewpointFences3D`
- 档案生成：`python tools/mod_archive.py --profile play`

