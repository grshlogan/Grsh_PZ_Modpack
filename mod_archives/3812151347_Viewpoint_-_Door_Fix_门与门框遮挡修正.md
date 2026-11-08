# 视角门修复（Viewpoint - Door Fix）

**门与门框遮挡修正** · 分类：渲染 / 修复 · 3812151347 · 启用 · 加载位次 4

## 它做什么

修正第一人称视角下门、门框、栅栏的模型错位与穿模。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3812151347` |
| mod id | `ViewpointDoor` |
| 文件夹 | `ViewpointDoor` |
| 版本 / 适配 | `42.21` … `-` |
| 作者 | GamerKreep |
| 工作坊更新时间 | 2026-10-12 |
| 分发端 | both |
| 体积 / 文件 | 244.7 KB · 20 文件（lua 0，client 0，server 0；贴图 2；模型 0；翻译 0；Java 源码 15、jar/class 1） |

## 依赖与冲突

- 需要：`Viewpoint`
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端挂载（纯渲染修正，服务端加载只为保持 mod 列表一致）。

本机实测文件构成：客户端无 lua，但带 Java 源码补丁；服务端无 lua（只挂载）。

## 实测与排查

versionMin=42.21，低于该版本的客户端会拒绝加载。

```
python lab.py check --profile play
grep -a 'ViewpointDoor' runs/<trial>/console.log
```

## 作者原话

```
Addon for Project Viewpoint to fix door lighting and textures while in 3D perspective.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3812151347`
- 本地快照：`workspace/mods_library/3812151347/mods/ViewpointDoor`
- 档案生成：`python tools/mod_archive.py --profile play`

