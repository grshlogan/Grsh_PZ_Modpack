# DeadWorks 框架沙盒页（DeadWorks Vehicle Framework Tweaks）

**装甲/水箱/电池/车重可调** · 分类：载具 / 房车 · 3826684062 · 启用 · 加载位次 22

## 它做什么

给 DeadWorks 框架加一页沙盒选项：装甲耐久、水箱容量、电池、车重等。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3826684062` |
| mod id | `aparosa_DWVFTweaks` |
| 文件夹 | `aparosa_DWVFTweaks` |
| 版本 / 适配 | `42.21` … `-` |
| 作者 | APAROSA |
| 工作坊更新时间 | - |
| 分发端 | both |
| 体积 / 文件 | 510.6 KB · 21 文件（lua 3，client 1，server 0；贴图 1；模型 0；翻译 14） |

## 依赖与冲突

- 需要：`DeadWorksVehicleFramework`
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端都要装（选项由服务端下发）。

本机实测文件构成：客户端有 lua；服务端无 lua（只挂载）。

## 实测与排查

0.0.7；require DeadWorksVehicleFramework。

```
python lab.py check --profile play
grep -a 'aparosa_DWVFTweaks' runs/<trial>/console.log
```

## 作者原话

```
Sandbox options for vehicles on DeadWorks Vehicle Framework (Viewpoint - 3D RVs and others): armour kit hit threshold and item weight, part durability against weapons and vehicle weight, plus storage bay doors, Battery Hatch and Water Hatch that follow the exterior door. Changes take effect when you press Apply in the in-game sandbox options.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3826684062`
- 本地快照：`workspace/mods_library/3826684062/mods/aparosa_DWVFTweaks`
- 档案生成：`python tools/mod_archive.py --profile play`

