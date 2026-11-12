# DeadWorks 沙盒调节（DeadWorks Vehicle Framework Tweaks）

**装甲水箱电池车重可调** · 分类：玩法 / 房车设置 · `3826684062` · 启用 · 加载位次 57
归属：**兼容候选（未运行验收）**；档案视图 `b422-compat`。

## 它做什么

为 DeadWorksVehicleFramework 增加装甲、水箱、电池和车重等沙盒选项。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3826684062` |
| mod id | `aparosa_DWVFTweaks` |
| 文件夹 | `aparosa_DWVFTweaks` |
| Mod 版本 | `0.0.7` |
| 原件适配 | `42.21` … `-` |
| 当前生效适配 | `42.21` … `-`（原件） |
| 元数据来源 | `42/mod.info` |
| 作者 | APAROSA |
| 工作坊更新时间 | 2026-11-10 |
| 分发端 | both（双端） |
| 体积 / 文件 | 509.0 KB · 21 文件（lua 3，client 1，server 0；贴图 1；模型 0；翻译 14） |

## 依赖与冲突

- 需要：`DeadWorksVehicleFramework`
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端候选；自身没有 42.21 上限，但必须带 DeadWorksVehicleFramework 及其完整依赖链。

当前 profile：both（双端）。

本机文件构成：客户端有 lua；服务端无 lua（只挂载）。

## 实测与排查

原件 0.0.7，min42.21、无 max；该条不需版本 Overlay，仍受房车框架兼容性限制。

**planned：仅完成依赖、版本与补丁指纹静态检查。** 迁移收尾按 Owner 要求不启动游戏；本候选组合未验证加载、联网、存档或视觉。

```
cd A004
python lab.py check --profile b422-compat
grep -a 'aparosa_DWVFTweaks' runs/<trial>/*console.log
```

## 作者原话

```
Sandbox options for vehicles on DeadWorks Vehicle Framework (Viewpoint - 3D RVs and others): armour kit hit threshold and item weight, part durability against weapons and vehicle weight, plus storage bay doors, Battery Hatch and Water Hatch that follow the exterior door. Changes take effect when you press Apply in the in-game sandbox options.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3826684062`
- 本地原件：`A004/workspace/mods_library/3826684062/mods/aparosa_DWVFTweaks`
- 档案生成：`python tools/mod_archive.py --profile b422-compat`
