# 视角表面修复（Viewpoint - Surface Fix）

**墙面地面渲染修正** · 分类：渲染 / 修复 · 3814398576 · 启用 · 加载位次 5

## 它做什么

修复第一人称视角下墙面、地板、天花板的贴图与几何缝隙。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3814398576` |
| mod id | `ViewpointSurface` |
| 文件夹 | `ViewpointSurface` |
| 版本 / 适配 | `42.21` … `-` |
| 作者 | GamerKreep |
| 工作坊更新时间 | 2026-10-15 |
| 分发端 | both |
| 体积 / 文件 | 536.0 KB · 49 文件（lua 0，client 0，server 0；贴图 6；模型 0；翻译 0；Java 源码 40、jar/class 1） |

## 依赖与冲突

- 需要：`Viewpoint, ZombieBuddy`
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端挂载。

本机实测文件构成：客户端无 lua，但带 Java 源码补丁；服务端无 lua（只挂载）。

## 实测与排查

同上，绑定 42.21。

```
python lab.py check --profile play
grep -a 'ViewpointSurface' runs/<trial>/console.log
```

## 作者原话

```
Patch for Project Viewpoint to fix various wall and roof textures while in 3D perspective.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3814398576`
- 本地快照：`workspace/mods_library/3814398576/mods/ViewpointSurface`
- 档案生成：`python tools/mod_archive.py --profile play`

