# 自动整理（Tidy Up Meister）

**库存自动归位** · 分类：UI / 整理 · 2769706949 · 启用 · 加载位次 28

## 它做什么

一键把背包和容器里的物品按规则排序归位，支持自定义优先级。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `2769706949` |
| mod id | `P4TidyUpMeister` |
| 文件夹 | `P4TidyUpMeister` |
| 版本 / 适配 | `42.0.0` … `-` |
| 作者 | PePePePePeil |
| 工作坊更新时间 | 2026-10-10 |
| 分发端 | both |
| 体积 / 文件 | 1.3 MB · 119 文件（lua 12，client 8，server 0；贴图 9；模型 0；翻译 92） |

## 依赖与冲突

- 需要：无
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端；只改本地排序视图。

本机实测文件构成：客户端有 lua；服务端无 lua（只挂载）。

## 实测与排查

mod id 是 P4TidyUpMeister。

```
python lab.py check --profile play
grep -a 'P4TidyUpMeister' runs/<trial>/console.log
```

## 作者原话

```
Automatically returns to the original equipment when the operation is completed.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=2769706949`
- 本地快照：`workspace/mods_library/2769706949/mods/P4TidyUpMeister`
- 档案生成：`python tools/mod_archive.py --profile play`

