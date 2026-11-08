# 3D RV Van 服务端后端（3D Vans Host backend）

**厢货车厢与家具的服务端权威** · 分类：载具 / 房车 · 3821174725 · 启用 · 加载位次 18

## 它做什么

server-only jar（`media/java/server/`），负责车厢占位、家具与乘员同步。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3821174725` |
| mod id | `GridVansHost` |
| 文件夹 | `GridVansHost` |
| 版本 / 适配 | `42.21` … `42.21` |
| 作者 | Deadworks Collective |
| 工作坊更新时间 | 2026-10-19 |
| 分发端 | both |
| 体积 / 文件 | 107.6 KB · 6 文件（lua 2，client 0，server 2；贴图 0；模型 0；翻译 0；Java 源码 0、jar/class 1） |

## 依赖与冲突

- 需要：`ZombieBuddy`
- 互斥：无
- 被依赖：`GridVans`

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

只服务端加载；客户端正确跳过。

本机实测文件构成：客户端无 lua（纯资源）；服务端有 lua。

## 实测与排查

0.1.8；依赖 ZombieBuddy 角色判定修复补丁才能被服务端加载。

```
python lab.py check --profile play
grep -a 'GridVansHost' runs/<trial>/console.log
```

## 作者原话

```
Independent server authority and synchronization for 3D Vans interiors.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3821174725`
- 本地快照：`workspace/mods_library/3821174725/mods/GridVansHost`
- 档案生成：`python tools/mod_archive.py --profile play`

