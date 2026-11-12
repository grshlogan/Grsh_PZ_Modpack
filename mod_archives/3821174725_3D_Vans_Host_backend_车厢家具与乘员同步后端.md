# 厢式房车后端（3D Vans Host backend）

**车厢家具与乘员同步后端** · 分类：框架 / 房车 · `3821174725` · 启用 · 加载位次 54
归属：**兼容候选（未运行验收）**；档案视图 `b422-compat`。

## 它做什么

为 GridVans 处理车厢占位、家具与乘员状态同步；Java 实现位于 server 目录，不把它搬到客户端加载来绕过角色判断。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3821174725` |
| mod id | `GridVansHost` |
| 文件夹 | `GridVansHost` |
| Mod 版本 | `0.1.8` |
| 原件适配 | `42.21` … `42.21` |
| 当前生效适配 | `42.21` … `42.22`（Overlay 放行，非上游正式支持） |
| 元数据来源 | `42/mod.info` |
| 作者 | Deadworks Collective |
| 工作坊更新时间 | 2026-10-19 |
| 分发端 | both（双端） |
| 体积 / 文件 | 107.6 KB · 6 文件（lua 2，client 0，server 2；贴图 0；模型 0；翻译 0；Java 源码 0、jar/class 1） |

## 依赖与冲突

- 需要：`ZombieBuddy`
- 互斥：无
- 被依赖：`GridVans`

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

当前为双端候选挂载，服务端执行后端 JAR；需实际双客户端测试权威状态和同步。

当前 profile：both（双端）。

本机文件构成：客户端无 lua（纯资源）；服务端有 lua。

## 实测与排查

原件 0.1.8，42.21 上限；42 与 common 元数据一并 Overlay 放行，JAR 未改。ZombieBuddy 根角色补丁保留。

**planned：仅完成依赖、版本与补丁指纹静态检查。** 迁移收尾按 Owner 要求不启动游戏；本候选组合未验证加载、联网、存档或视觉。

版本放行补丁：`A004/workspace/patches/mods/GridVansHost/42/mod.info`。原件更新后须重新核对指纹；撤除此补丁后运行 check 会恢复原件版本限制。

```
cd A004
python lab.py check --profile b422-compat
grep -a 'GridVansHost' runs/<trial>/*console.log
```

## 作者原话

```
Independent server authority and synchronization for 3D Vans interiors.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3821174725`
- 本地原件：`A004/workspace/mods_library/3821174725/mods/GridVansHost`
- 档案生成：`python tools/mod_archive.py --profile b422-compat`
