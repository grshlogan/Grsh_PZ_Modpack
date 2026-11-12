# VSGirlBody 动态身体（VSGirlBodyBoobBounce(Requires ZombieBuddy)）

**身体模型动态效果** · 分类：角色 / 动画 · `3640496116` · 启用 · 加载位次 60
归属：**兼容候选（未运行验收）**；档案视图 `b422-compat`。

## 它做什么

为 VSGirlBody 身体模型提供动态效果扩展；这是现有工坊包中的子模块，不另外加入其他身体分支。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3640496116` |
| mod id | `VariableSkinBoobBounce` |
| 文件夹 | `VariableSkinBoobBounce` |
| Mod 版本 | `0.6.1-test` |
| 原件适配 | `42.21` … `42.21` |
| 当前生效适配 | `42.21` … `42.22`（Overlay 放行，非上游正式支持） |
| 元数据来源 | `42/mod.info` |
| 作者 | - |
| 工作坊更新时间 | 2026-10-21 |
| 分发端 | both（双端） |
| 体积 / 文件 | 127.3 KB · 7 文件（lua 1，client 1，server 0；贴图 2；模型 0；翻译 0；Java 源码 0、jar/class 1） |

## 依赖与冲突

- 需要：`ZombieBuddy`
- 互斥：`VSGirlBodyExtension`
- 被依赖：`VariableSkinBoobBounceViewpoint`

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

当前双端候选；依赖 ZombieBuddy，与 VSGirlBodyExtension 互斥。

当前 profile：both（双端）。

本机文件构成：客户端有 lua；服务端无 lua（只挂载）。

## 实测与排查

原件 0.6.1-test，42.21 上限；只改版本元数据。身体网格、动作和联机显示未验证。

**planned：仅完成依赖、版本与补丁指纹静态检查。** 迁移收尾按 Owner 要求不启动游戏；本候选组合未验证加载、联网、存档或视觉。

版本放行补丁：`A004/workspace/patches/mods/VariableSkinBoobBounce/42/mod.info`。原件更新后须重新核对指纹；撤除此补丁后运行 check 会恢复原件版本限制。

```
cd A004
python lab.py check --profile b422-compat
grep -a 'VariableSkinBoobBounce' runs/<trial>/*console.log
```

## 作者原话

```
Development test. Runtime secondary motion and nearby soft garment binding for original VS bodies. Requires a supported original VS body. Restart the game. Not game-validated.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3640496116`
- 本地原件：`A004/workspace/mods_library/3640496116/mods/VariableSkinBoobBounce`
- 档案生成：`python tools/mod_archive.py --profile b422-compat`
