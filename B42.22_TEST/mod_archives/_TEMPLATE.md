# mod 档案 · B42.22_TEST 模板

这个目录按同一副骨架记录当前 **B42.22_TEST** 包的 42 个条目。共同规律写在本文，单个 mod 只填自己的事实；文档由 `tools/mod_archive.py` 生成，人工部分写在 `tools/mod_catalog.json`。

文件名规则：`<steam_id>_<模组原名>_<模组中文介绍>.md`。同一个工作坊 ID 有多个子 mod 时，用文件夹区分，例如 `3640496116_VSGirlBody_S_SFW_...md` 与 `3640496116_VSGirlBody_Fix_...md`。

## 一、这个包的事实

| 项 | 值 |
| --- | --- |
| 游戏版本 | B42.22（profile `gameVersion=42.22.0`） |
| profile | `A004/B42.22_TEST/workspace/defs/b422-batch2/pack.json` |
| 条目 | 42（启用 42，禁用 0） |
| 双端 | Client 42 / Server 38 |
| 仅客户端 | `PzPerformanceFixes`、`VariableSkinSFW`、`VariableSkinFix`、`WhereAmI` |
| 世界名 | `b422batch2` |
| 汉化顺序 | `LaoYuTranslationJava` → `B42ModTrans_CN` → `B42Trans_CN`（末尾） |

三条通用规律：

1. **双端规则**：`distribution=both` 的条目两端都要装；服务端缺条目会因 mod 列表校验连不上。当前 4 条 `client` 只装客户端，进服后会被服务端 `Mods=` 列表丢弃，这是已知行为，不要误判为文件损坏。
2. **依赖顺序**：`ZombieBuddy`、`Viewpoint`、`NeatUI_Framework`、`damnlib`、`YAPZLib` 必须排在依赖它们的条目之前；`Neat_Crafting`、`Project_Cook`、`CleanUI` 都依赖 `NeatUI_Framework`。
3. **物品 id**：脚本物品的完整 id 是 `<module>.<item 名>`，默认模块是 `Base`；查 id 就是查脚本里的 `item` 名。载具脚本与配方单独列出。

## 二、每份文档的固定骨架

```text
# 中文名（英文名）

**一句话简介** · 分类：xx · <steam_id> · 启用 · 加载位次 N

## 它做什么          ← 人工：1-3 句，讲清它解决什么问题
## 概览              ← 自动：工作坊 ID / mod id / 文件夹 / 版本适配 / 作者 / 更新时间 / 分发端 / 体积与文件构成
## 依赖与冲突        ← 自动：require、incompatible、被谁依赖
## 内容清单          ← 自动：脚本物品表（id + 显示名 + 类型）、载具脚本、配方
## 双端与联机        ← 人工 mp 注记 + 当前 profile 的 client/both 状态 + 自动文件构成
## 实测与排查        ← 人工：日志关键字、已知噪声、本机结论 + 两条排查命令
## 作者原话          ← 自动：mod.info 的 description 原文（截断 1000 字符）
## 来源              ← 自动：工作坊链接、测试台本地快照、重新生成命令
```

## 三、自动与人工怎么分工

- **自动**：`tools/mod_archive.py` 扫描 `A004/B42.22_TEST/workspace/mods_library/<workshopId>/mods/<folder>` 和 `A004/B42.22_TEST/workspace/defs/b422-batch2/pack.json`，生成 `mod_archives/*.md`、`INDEX.md` 和根 `README.md`。
- **人工**：`tools/mod_catalog.json` 里每个条目写 `cn` / `brief` / `cat` / `what` / `mp` / `note`。重复工作坊 ID 用 `<id>-<文件夹小写>` 作为键，例如 `3640496116-variableskinsfw`。
- 生成器会删掉 `mod_archives/` 里除 `_TEMPLATE.md` 以外的所有 `.md` 再重写。**不要手工改生成物**，改 catalog 后重跑。

## 四、新增或更新一个 mod 时

1. 在 `A004/B42.22_TEST/workspace/defs/b422-batch2/pack.json` 里加条目，并在 `loadOrder` 里安排位置。
2. 在 `tools/mod_catalog.json` 里补人工字段；如果是重复工作坊 ID，补带文件夹后缀的键。
3. 在 `tools/workshop_times.json` 里补工作坊更新日期；抓不到就留 `-`。
4. 从本目录运行：

```bash
python tools/mod_archive.py --profile b422-batch2
```

5. 到测试台执行 `python lab.py check --profile b422-batch2`，再按 `start-server.bat` / `start-client.bat` 做双端加载验证。生成成功不等于游戏内验收通过。

## 五、已知边界

- 体积、文件数、物品数按本地包**完整目录**统计；同一个 mod 带多个版本目录时，实际加载只取匹配 B42.22 的一档，数字会偏大。
- `Neat_Crafting` 使用 `42.13` 适配目录、`Project_Cook` 使用 `42.15`；两者都只写 `versionMin`，没有 `versionMax`，当前 B42.22_TEST 加载正常。
- `87fordB700` 的 `B700SideStorage` / `B700Mudflaps` 与 `82jeepJ10` 的 `JP82SpareTireRear` 模板缺失，是上游脚本噪声，目前不阻止启动。
- 本目录只记录整合信息，不分发 mod 文件；版权归原作者。
