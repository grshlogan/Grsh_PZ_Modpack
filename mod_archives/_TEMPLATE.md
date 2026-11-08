# mod 档案 · 通用模板

这个目录里的每份文档都按同一副骨架写，骨架来自对 `play` 包 31 个条目的遍历：
共性部分一次写好、逐份复用；每个 mod 只填自己那段。

文件名规则：`<steam_id>_<模组原名>_<模组中文介绍>.md`（例：`3619862853_ZombieBuddy_模组框架与3D动画核心.md`）。

## 一、遍历出来的共性（31 个条目）

| 共性 | 数量 | 说明 |
| --- | --- | --- |
| `mod.info` 不在根目录、而在版本子目录（`42/`、`42.0/`、`42.20.4/`…） | 21 / 31 | 引擎按 `versionMin/versionMax` 选目录，所以同一个 mod 会有多份 `mod.info`，内容基本一致 |
| 目录结构是 `<版本目录>/ + common/` | 11 / 31 | `common/` 放跨版本共用资源，版本目录放该版本的脚本与 lua |
| 有 `media/lua/client` | 24 / 31 | 客户端行为；纯资源类（模型包、贴图包）没有 |
| 有 `media/lua/server` | 7 / 31 | 服务端裁决逻辑；大多数 mod 服务端只是“挂载”以保证 mod 列表一致 |
| 有 `Translate/` | 19 / 31 | 翻译是整文件覆盖：`Translate/CN/UI.json` 会顶掉同名的其它 mod 文件（C 组实测） |
| 有贴图 | 29 / 31 | 几乎都带 `.png` / `.dds` |
| 有 3D 模型（`.fbx` / `.x`） | 5 / 31 | Viewpoint 系的模型包 |
| 有 `media/scripts` 脚本 | 7 / 31 | 只有它们会注册物品/载具/配方 |

由此得到三条通用规律：

1. **双端规则**：`distribution` 为 `both` 的 mod 两端都要装；服务端不一定跑逻辑，但缺了会让客户端连不上（mod 列表校验）。
2. **加载顺序规则**：被 `require=` 的库必须在前；汉化必须最后（本包 `order_tail` = 统一模组汉化 → 统一中文汉化）。
3. **物品 id 规则**：脚本物品的完整 id 是 `<module>.<item 名>`，默认模块是 `Base`；所以查 id 就是查脚本里的 `item` 名。

## 二、每份文档的固定骨架

```
# 中文名（英文名）

**一句话简介** · 分类：xx · <steam_id> · 启用/禁用 · 加载位次 N

## 它做什么          ← 人工：1-3 句，讲清它解决什么问题
## 概览              ← 自动：工作坊 ID / mod id / 文件夹 / 版本适配 / 作者 / 更新时间 / 分发端 / 体积与文件构成
## 依赖与冲突        ← 自动：require、incompatible、被谁依赖
## 内容清单          ← 自动：脚本物品表（id + 显示名 + 类型）、载具脚本、配方
## 双端与联机        ← 人工 mp 注记 + 自动（客户端是否有 lua、服务端是否有 lua）
## 实测与排查        ← 人工：日志关键字、已知噪声、我们跑出来的结论 + 两条排查命令
## 作者原话          ← 自动：mod.info 的 description 原文
## 来源              ← 自动：工作坊链接、本地快照路径、重新生成命令
```

分工：

- **自动**部分由 `tools/mod_archive.py` 扫 `workspace/mods_library/` 和 `defs/play/pack.json` 生成，不会手抄出错。
- **人工**部分（它做什么 / 双端与联机 / 实测与排查）写在 `tools/mod_catalog.json`，一个 mod 一段。

## 三、新增或更新一个 mod 时

1. 在 `workspace/defs/play/pack.json` 里加条目（`workshopId` / `folder` / `modId` / `enabled` / `distribution`）。
2. 在 `tools/mod_catalog.json` 里补 `cn` / `brief` / `cat` / `what` / `mp` / `note`（`233` 这样的键：工作坊 ID；同一 ID 多 mod 时用 `<id>-<文件夹小写>`）。
3. 跑 `python tools/mod_archive.py --profile play`，文档、索引一起刷新。

> 生成器会删掉目录里除 `_TEMPLATE.md` 之外的 `.md` 再重写，所以不要手工改生成物 —— 改 catalog。
