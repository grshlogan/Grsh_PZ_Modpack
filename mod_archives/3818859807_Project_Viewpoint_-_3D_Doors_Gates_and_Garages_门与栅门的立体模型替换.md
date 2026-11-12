# 3D 门与车库门（Project Viewpoint - 3D Doors, Gates & Garages）

**门与栅门的立体模型替换** · 分类：渲染 / 世界物件 · `3818859807` · 启用 · 加载位次 51
归属：**兼容候选（未运行验收）**；档案视图 `b422-compat`。

## 它做什么

为 Viewpoint 提供门、栅门和车库门的 3D 模型与显示逻辑；开合、碰撞和锁定是否与 B42.22 一致仍需游戏内验证。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3818859807` |
| mod id | `BasileDoors3D` |
| 文件夹 | `BasileDoors3D` |
| Mod 版本 | `0.2.8` |
| 原件适配 | `42.21` … `42.21` |
| 当前生效适配 | `42.21` … `42.22`（Overlay 放行，非上游正式支持） |
| 元数据来源 | `42/mod.info` |
| 作者 | Basile |
| 工作坊更新时间 | 2026-10-23 |
| 分发端 | both（双端） |
| 体积 / 文件 | 65.6 MB · 315 文件（lua 2，client 2，server 0；贴图 33；模型 276；翻译 0；Java 源码 0、jar/class 1） |

## 依赖与冲突

- 需要：`ZombieBuddy, Viewpoint`
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端候选；渲染 Java 插件在客户端，服务端清单需一致。

当前 profile：both（双端）。

本机文件构成：客户端有 lua；服务端无 lua（只挂载）。

## 实测与排查

原件 0.2.8，42.21 上限；Overlay 只改版本上限，不改 BasileDoors3D.jar。静态通过不能排除 Java 接口变化。

**planned：仅完成依赖、版本与补丁指纹静态检查。** 迁移收尾按 Owner 要求不启动游戏；本候选组合未验证加载、联网、存档或视觉。

版本放行补丁：`A004/workspace/patches/mods/BasileDoors3D/42/mod.info`。原件更新后须重新核对指纹；撤除此补丁后运行 check 会恢复原件版本限制。

```
cd A004
python lab.py check --profile b422-compat
grep -a 'BasileDoors3D' runs/<trial>/*console.log
```

## 作者原话

```
Native-style 3D doors, wire-mesh gates, timber and rail farm gates, and sectional or roller garage doors. Distinct native finishes, real garage windows and full-height clear-glass bay doors with slim frames. Client-side visual replacements preserve native gameplay.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3818859807`
- 本地原件：`A004/workspace/mods_library/3818859807/mods/BasileDoors3D`
- 档案生成：`python tools/mod_archive.py --profile b422-compat`
