# DLSS 帧生成（Viewpoint DLSS Frame Generation）

**给 Viewpoint 加 DLSS 帧生成** · 分类：渲染 / 性能 · `3818838508` · 启用 · 加载位次 11

## 它做什么

为 Viewpoint 增加 DLSS 帧生成支持，在高分辨率下提升帧率；依赖 Viewpoint 和 ZombieBuddy。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3818838508` |
| mod id | `ViewpointDLSS` |
| 文件夹 | `ViewpointDLSS` |
| 版本 / 适配 | `42.21` … `42.22` |
| 作者 | - |
| 工作坊更新时间 | 2026-11-10 |
| 分发端 | both（双端） |
| 体积 / 文件 | 4.3 MB · 5 文件（lua 0，client 0，server 0；贴图 1；模型 0；翻译 0；Java 源码 0、jar/class 1） |

## 依赖与冲突

- 需要：`ZombieBuddy, Viewpoint`
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端挂载；实际图形功能在客户端，服务端只校验 mod 列表；需要支持 DLSS 的显卡和驱动。

当前 profile：both（双端）。

本机文件构成：客户端无 lua（纯资源）；服务端无 lua（只挂载）。

## 实测与排查

上游 0.1.6；versionMin=42.21，versionMax=42.22；2026-11-10 更新；实际帧率和画面需进游戏验收。

```
cd A004/B42.22_TEST
python lab.py check --profile b422-batch2
grep -a 'ViewpointDLSS' runs/<trial>/console.log
```

## 作者原话

```
Native NVIDIA DLSS frame generation for Project Viewpoint. Off, 2x, 4x and 6x controls in Delete > Graphics. Windows x64; compatible GPU required. Beta.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3818838508`
- 本地快照（测试台）：`A004/B42.22_TEST/workspace/mods_library/3818838508/mods/ViewpointDLSS`
- 档案生成：`python tools/mod_archive.py --profile b422-batch2`
