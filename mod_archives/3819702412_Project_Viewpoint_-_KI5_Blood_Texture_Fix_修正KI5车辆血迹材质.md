# KI5 血迹材质修复（Project Viewpoint - KI5 Blood Texture Fix）

**修正KI5车辆血迹材质** · 分类：修复 / 载具材质 · `3819702412` · 启用 · 加载位次 52
归属：**兼容候选（未运行验收）**；档案视图 `b422-compat`。

## 它做什么

修正 Viewpoint 下 KI5 车辆沾血后的材质与贴图显示；不能代替载具零件位置或外壳修复。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3819702412` |
| mod id | `ViewpointKI5Materials` |
| 文件夹 | `ViewpointKI5Materials` |
| Mod 版本 | `0.1.0` |
| 原件适配 | `42.21.0` … `42.21.99` |
| 当前生效适配 | `42.21.0` … `42.22`（Overlay 放行，非上游正式支持） |
| 元数据来源 | `42.21/mod.info` |
| 作者 | Motor |
| 工作坊更新时间 | 2026-10-14 |
| 分发端 | both（双端） |
| 体积 / 文件 | 72.1 KB · 10 文件（lua 1，client 1，server 0；贴图 2；模型 0；翻译 0；Java 源码 2、jar/class 1） |

## 依赖与冲突

- 需要：`ZombieBuddy, Viewpoint, damnlib`
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端候选；依赖 ZombieBuddy、Viewpoint 与 damnlib，实际材质功能在客户端。

当前 profile：both（双端）。

本机文件构成：客户端有 lua；服务端无 lua（只挂载）。

## 实测与排查

原件 0.1.0，42.21.0…42.21.99；Overlay 放宽至 42.22，保留 JAR 原件，尚未验证血迹效果。

**planned：仅完成依赖、版本与补丁指纹静态检查。** 迁移收尾按 Owner 要求不启动游戏；本候选组合未验证加载、联网、存档或视觉。

版本放行补丁：`A004/workspace/patches/mods/ViewpointKI5Materials/42.21/mod.info`。原件更新后须重新核对指纹；撤除此补丁后运行 check 会恢复原件版本限制。

```
cd A004
python lab.py check --profile b422-compat
grep -a 'ViewpointKI5Materials' runs/<trial>/*console.log
```

## 作者原话

```
Fixes false blood stains on KI5/DAMN vehicles in Project Viewpoint. Preserves real blood and body damage. Исправляет ложные кровавые пятна на машинах KI5/DAMN, сохраняя настоящую кровь и повреждения.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3819702412`
- 本地原件：`A004/workspace/mods_library/3819702412/mods/ViewpointKI5Materials`
- 档案生成：`python tools/mod_archive.py --profile b422-compat`
