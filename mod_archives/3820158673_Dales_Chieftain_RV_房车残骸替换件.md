# 废弃酋长房车（Dale's Chieftain RV）

**房车残骸替换件** · 分类：载具 / 可选 · 3820158673 · 禁用 · 加载位次 17

## 它做什么

把酋长房车替换成废弃残骸外观（DeadWorks 系列）。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3820158673` |
| mod id | `DeadWorksDaleRV` |
| 文件夹 | `DeadWorksDaleRV` |
| 版本 / 适配 | `42.21` … `42.21` |
| 作者 | DeadWorks Collective |
| 工作坊更新时间 | 2026-11-04 |
| 分发端 | both |
| 体积 / 文件 | 53.5 MB · 218 文件（lua 3，client 1，server 0；贴图 49；模型 154；翻译 3） |

## 依赖与冲突

- 需要：`DeadWorksVehicleFramework, DeadWorksNomadRV, PZVoxelStudioViewpoint`
- 互斥：`GridRV, GridRVHost, DaleChieftainRV`
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

载具脚本 1 条：`DaleChieftainRV`

## 双端与联机

双端，但当前**禁用**：与在用的酋长房车同源，同时开会出现重复载具。

本机实测文件构成：客户端有 lua；服务端无 lua（只挂载）。

## 实测与排查

pack 里 enabled=false，只作为备选保留。

```
python lab.py check --profile play
grep -a 'DeadWorksDaleRV' runs/<trial>/console.log
```

## 作者原话

```
Dale's Chieftain RV, model and profile for the DeadWorks Vehicle Framework.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3820158673`
- 本地快照：`workspace/mods_library/3820158673/mods/DeadWorksDaleRV`
- 档案生成：`python tools/mod_archive.py --profile play`

