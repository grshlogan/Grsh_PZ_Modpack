# 酋长房车（Dale's Chieftain RV (Legacy)）

**大型房车载具** · 分类：载具 · 3820158673 · 启用 · 加载位次 18

## 它做什么

Dale 的 Chieftain 大型房车，空间比游牧版更大。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3820158673` |
| mod id | `DaleChieftainRV` |
| 文件夹 | `DaleChieftainRV` |
| 版本 / 适配 | `42.21` … `42.21` |
| 作者 | Deadworks Collective |
| 工作坊更新时间 | 2026-11-04 |
| 分发端 | both |
| 体积 / 文件 | 172.8 MB · 117 文件（lua 1，client 0，server 0；贴图 2；模型 104；翻译 2） |

## 依赖与冲突

- 需要：`GridRV, GridRVHost, PZVoxelStudioViewpoint`
- 互斥：`DeadWorksNomadRV, DeadWorksDaleRV`
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

载具脚本 1 条：`DaleChieftainRV`

## 双端与联机

双端。

本机实测文件构成：客户端无 lua（纯资源）；服务端无 lua（只挂载）。

## 实测与排查

刷法：管理员聊天框 `/addvehicle "Base.DaleChieftainRV" "TEST"`，或 -debug 的「生成车辆」窗口选 `Base.DaleChieftainRV`。自然刷新权重与 GridRV 相同（campground 2、rvpark 2、trailerpark 0.75 等），但只在对应区域缺车时补位。172.8 MB，主要体积在模型与贴图。

```
python lab.py check --profile play
grep -a 'DaleChieftainRV' runs/<trial>/console.log
```

## 作者原话

```
Dale's Chieftain RV add-on for Nomad Grid RV. Furnished walkable interior, deployable steps and awning, shared multiplayer cabin systems, and natural vehicle spawns.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3820158673`
- 本地快照：`workspace/mods_library/3820158673/mods/DaleChieftainRV`
- 档案生成：`python tools/mod_archive.py --profile play`

