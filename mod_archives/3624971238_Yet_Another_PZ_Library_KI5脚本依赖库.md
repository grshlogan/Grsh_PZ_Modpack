# 通用函数库（Yet Another PZ Library）

**KI5脚本依赖库** · 分类：框架 · `3624971238` · 启用 · 加载位次 5
归属：**日常组合**；档案视图 `b422-compat`。

## 它做什么

KI5 模组共用的 Lua 工具函数集合，本身不添加任何内容。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3624971238` |
| mod id | `YAPZLib` |
| 文件夹 | `YetAnotherPZLib` |
| Mod 版本 | `-` |
| 原件适配 | `42.00` … `-` |
| 当前生效适配 | `42.00` … `-`（原件） |
| 元数据来源 | `42/mod.info` |
| 作者 | Пупсич |
| 工作坊更新时间 | 2026-10-03 |
| 分发端 | both（双端） |
| 体积 / 文件 | 90.2 KB · 15 文件（lua 12，client 1，server 3；贴图 2；模型 0；翻译 0） |

## 依赖与冲突

- 需要：无
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端。

当前 profile：both（双端）。

本机文件构成：客户端有 lua；服务端有 lua。

## 实测与排查

mod id=YAPZLib，文件夹 YetAnotherPZLib；本身无内容。

```
cd A004
python lab.py check --profile b422-compat
grep -a 'YAPZLib' runs/<trial>/*console.log
```

## 作者原话

```
Just a library mod.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3624971238`
- 本地原件：`A004/workspace/mods_library/3624971238/mods/YetAnotherPZLib`
- 档案生成：`python tools/mod_archive.py --profile b422-compat`
