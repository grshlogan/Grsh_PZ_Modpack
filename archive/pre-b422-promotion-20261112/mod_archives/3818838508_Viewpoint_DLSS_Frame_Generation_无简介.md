# Viewpoint DLSS Frame Generation（Viewpoint DLSS Frame Generation）

**** · 分类：- · 3818838508 · 启用 · 加载位次 8

## 它做什么

（待补：这个 mod 的作用）

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3818838508` |
| mod id | `ViewpointDLSS` |
| 文件夹 | `ViewpointDLSS` |
| 版本 / 适配 | `42.21` … `42.21` |
| 作者 | - |
| 工作坊更新时间 | 2026-10-19 |
| 分发端 | both |
| 体积 / 文件 | 4.3 MB · 5 文件（lua 0，client 0，server 0；贴图 1；模型 0；翻译 0；Java 源码 0、jar/class 1） |

## 依赖与冲突

- 需要：`ZombieBuddy, Viewpoint`
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

-

本机实测文件构成：客户端无 lua（纯资源）；服务端无 lua（只挂载）。

## 实测与排查

DLSS 帧生成 2x/4x/6x（RTX 50 可 4x/6x）；客户端 Java 插件，服务端由 ZB 跳过。

```
python lab.py check --profile play
grep -a 'ViewpointDLSS' runs/<trial>/console.log
```

## 作者原话

```
Native NVIDIA DLSS frame generation for Project Viewpoint. Off, 2x, 4x and 6x controls in Delete > Graphics. Windows x64; compatible GPU required. Beta.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3818838508`
- 本地快照：`workspace/mods_library/3818838508/mods/ViewpointDLSS`
- 档案生成：`python tools/mod_archive.py --profile play`

