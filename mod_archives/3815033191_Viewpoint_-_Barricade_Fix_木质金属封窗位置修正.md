# 封窗木条修复（Viewpoint - Barricade Fix）

**木质/金属封窗位置修正** · 分类：渲染 / 修复 · `3815033191` · 启用 · 加载位次 7
归属：**日常组合**；档案视图 `b422-compat`。

## 它做什么

修正 Viewpoint 下木质与金属封窗木条的摆放位置，并把贴图还原成原版，配合 2D 窗户/门更自然。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3815033191` |
| mod id | `ViewpointBarricade` |
| 文件夹 | `ViewpointBarricade` |
| Mod 版本 | `1.0` |
| 原件适配 | `42.21` … `-` |
| 当前生效适配 | `42.21` … `-`（原件） |
| 元数据来源 | `42/mod.info` |
| 作者 | GamerKreep |
| 工作坊更新时间 | 2026-10-11 |
| 分发端 | both（双端） |
| 体积 / 文件 | 278.3 KB · 14 文件（lua 0，client 0，server 0；贴图 2；模型 0；翻译 0；Java 源码 8、jar/class 1） |

## 依赖与冲突

- 需要：`Viewpoint`
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端挂载；Java 补丁。

当前 profile：both（双端）。

本机文件构成：客户端无 lua，但带 Java 源码补丁；服务端无 lua（只挂载）。

## 实测与排查

兼容 Fitted Barricades / Fenced Barricades；jar=ViewpointBarricades.jar；需 Viewpoint。

```
cd A004
python lab.py check --profile b422-compat
grep -a 'ViewpointBarricade' runs/<trial>/*console.log
```

## 作者原话

```
Patch for Project Viewpoint to fix barricade placements and restore their original textures.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3815033191`
- 本地原件：`A004/workspace/mods_library/3815033191/mods/ViewpointBarricade`
- 档案生成：`python tools/mod_archive.py --profile b422-compat`
