# 网格房车后端（Grid RV Host backend (Legacy)）

**房车系统后端库** · 分类：框架 / 载具 · 3820158673 · 启用 · 加载位次 14

## 它做什么

GridRV 三件套共用的后端：网格化载具空间、建造与存储逻辑。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3820158673` |
| mod id | `GridRVHost` |
| 文件夹 | `GridRVHost` |
| 版本 / 适配 | `42.21` … `42.21` |
| 作者 | Nomad Grid RV team |
| 工作坊更新时间 | 2026-11-04 |
| 分发端 | both |
| 体积 / 文件 | 106.9 KB · 7 文件（lua 3，client 0，server 3；贴图 0；模型 0；翻译 0；Java 源码 0、jar/class 1） |

## 依赖与冲突

- 需要：`ZombieBuddy`
- 互斥：`DeadWorksNomadRV, DeadWorksDaleRV`
- 被依赖：`GridRV`、`DaleChieftainRV`

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端。单独装没有内容，必须配 GridRV / DaleChieftainRV。

本机实测文件构成：客户端无 lua（纯资源）；服务端有 lua。

## 实测与排查

服务端权威后端。mod.info 声明 javaJarFile=media/java/server/GridRVHost.jar；ZombieBuddy 2.3.4 在无头服务器上会误判成客户端并把 server-only jar 跳过，导致客户端一直提示 Waiting for the Grid RV Host backend——需要把 jar 复制到 media/java/ 并改写 mod.info（A004 的 lab.py sync 自动处理）。

```
python lab.py check --profile play
grep -a 'GridRVHost' runs/<trial>/console.log
```

## 作者原话

```
Server authority and synchronization for the Grid RV multiplayer cabin.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3820158673`
- 本地快照：`workspace/mods_library/3820158673/mods/GridRVHost`
- 档案生成：`python tools/mod_archive.py --profile play`

