# 3D 栅栏（Viewpoint - 3D Fences）

**把栅栏变成有厚度的 3D 模型** · 分类：渲染 / Viewpoint 扩展 · `3814486926` · 启用 · 加载位次 8

## 它做什么

为 Viewpoint 补充 3D 栅栏模型，让第一/第三人称下的木栅栏、金属栅栏有立体轮廓，不再只是平面贴图。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3814486926` |
| mod id | `ViewpointFences3D` |
| 文件夹 | `ViewpointFences3D` |
| 版本 / 适配 | `42.21` … `-` |
| 作者 | - |
| 工作坊更新时间 | 2026-10-06 |
| 分发端 | both（双端） |
| 体积 / 文件 | 2.9 MB · 190 文件（lua 1，client 1，server 0；贴图 49；模型 69；翻译 0） |

## 依赖与冲突

- 需要：`Viewpoint`
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端挂载；模型与渲染逻辑在客户端，服务端只校验 mod 列表一致。

当前 profile：both（双端）。

本机文件构成：客户端有 lua；服务端无 lua（只挂载）。

## 实测与排查

上游 1.0.0；versionMin=42.21，无 versionMax；require Viewpoint；2026-10-06 更新。

```
cd A004/B42.22_TEST
python lab.py check --profile b422-batch2
grep -a 'ViewpointFences3D' runs/<trial>/console.log
```

## 作者原话

```
3D models for the fences you see most often, for Viewpoint's first-person view.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3814486926`
- 本地快照（测试台）：`A004/B42.22_TEST/workspace/mods_library/3814486926/mods/ViewpointFences3D`
- 档案生成：`python tools/mod_archive.py --profile b422-batch2`
