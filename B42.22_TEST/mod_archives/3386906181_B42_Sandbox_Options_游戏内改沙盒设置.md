# 沙盒选项（[B42] Sandbox Options）

**游戏内改沙盒设置** · 分类：工具 / 管理 · `3386906181` · 启用 · 加载位次 29

## 它做什么

在游戏内直接查看和修改沙盒选项，不用退出到主菜单重开世界。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3386906181` |
| mod id | `SandboxSettings` |
| 文件夹 | `B42SandboxOptions` |
| 版本 / 适配 | `42.20.0` … `-` |
| 作者 | Zky |
| 工作坊更新时间 | 2026-10-03 |
| 分发端 | both（双端） |
| 体积 / 文件 | 8.9 MB · 193 文件（lua 3，client 3，server 0；贴图 21；模型 0；翻译 162） |

## 依赖与冲突

- 需要：无
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端；联机下只有管理员能改。

当前 profile：both（双端）。

本机文件构成：客户端有 lua；服务端无 lua（只挂载）。

## 实测与排查

带 42 / 42.15 / 42.20 三档适配目录；当前 profile 双端加载。

```
cd A004/B42.22_TEST
python lab.py check --profile b422-batch2
grep -a 'B42SandboxOptions' runs/<trial>/console.log
```

## 作者原话

```
Change Sandbox Settings in-game
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3386906181`
- 本地快照（测试台）：`A004/B42.22_TEST/workspace/mods_library/3386906181/mods/B42SandboxOptions`
- 档案生成：`python tools/mod_archive.py --profile b422-batch2`
