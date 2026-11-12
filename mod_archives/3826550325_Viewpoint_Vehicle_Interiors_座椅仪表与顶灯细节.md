# 载具驾驶舱内饰（Viewpoint Vehicle Interiors）

**座椅仪表与顶灯细节** · 分类：渲染 / 载具内饰 · `3826550325` · 启用 · 加载位次 53
归属：**兼容候选（未运行验收）**；档案视图 `b422-compat`。

## 它做什么

给支持的车种补驾驶舱座椅、饰板、仪表与顶灯等细节；它是内饰显示扩展，不等于房车可行走后厢。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3826550325` |
| mod id | `ViewpointInteriors` |
| 文件夹 | `ViewpointInteriors` |
| Mod 版本 | `1.0.1` |
| 原件适配 | `42.21` … `42.21` |
| 当前生效适配 | `42.21` … `42.22`（Overlay 放行，非上游正式支持） |
| 元数据来源 | `42/mod.info` |
| 作者 | gustavobr120 |
| 工作坊更新时间 | 2026-10-31 |
| 分发端 | both（双端） |
| 体积 / 文件 | 96.3 MB · 167 文件（lua 3，client 2，server 1；贴图 24；模型 93；翻译 30；Java 源码 0、jar/class 1） |

## 依赖与冲突

- 需要：`Viewpoint, ZombieBuddy`
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端候选；依赖 Viewpoint 与 ZombieBuddy，需对具体支持车型验收。

当前 profile：both（双端）。

本机文件构成：客户端有 lua；服务端有 lua。

## 实测与排查

原件 1.0.1，42.21 上限；仅元数据 Overlay 放行。仪表、顶灯与乘员显示尚未运行验证。

**planned：仅完成依赖、版本与补丁指纹静态检查。** 迁移收尾按 Owner 要求不启动游戏；本候选组合未验证加载、联网、存档或视觉。

版本放行补丁：`A004/workspace/patches/mods/ViewpointInteriors/42/mod.info`。原件更新后须重新核对指纹；撤除此补丁后运行 check 会恢复原件版本限制。

```
cd A004
python lab.py check --profile b422-compat
grep -a 'ViewpointInteriors' runs/<trial>/*console.log
```

## 作者原话

```
Vehicle cabin details for Project Viewpoint: measured interiors, working instruments, radio LCD and switchable dome lights. Supported vehicle profiles retain native fallback. See README.md for scope and known issues.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3826550325`
- 本地原件：`A004/workspace/mods_library/3826550325/mods/ViewpointInteriors`
- 档案生成：`python tools/mod_archive.py --profile b422-compat`
