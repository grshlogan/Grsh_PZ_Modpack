# B42.22 Mod 档案模板

本目录覆盖日常组合与独立兼容候选。条目数、端别和归属以 [INDEX.md](INDEX.md) 为准；运行验证边界见 [兼容说明](../COMPATIBILITY.md)。生成档案不切换运行组合。

## 每份档案的骨架

1. **它做什么**：作用和用途，来自人工 catalog。
2. **概览**：Workshop/Mod ID、文件夹、Mod 版本、原件范围、Overlay 后范围、元数据路径、作者、更新时间快照、端别和完整目录统计。
3. **依赖与冲突**：当前有效 mod.info 的 require、incompatible 与被依赖关系；工坊 Required items 需另行逐页核对。
4. **内容清单**：脚本物品 ID、载具脚本和配方。物品完整 ID 为 `<module>.<item>`，通常 module 为 `Base`。
5. **双端与联机**：人工注记、profile 的 distribution 以及文件构成；文件存在不证明功能可用。
6. **实测与排查**：区分历史加载、离线检查和待验收；记录补丁路径与静态检查命令。
7. **作者原话**：所选 mod.info 的 description，最多 1000 字符。
8. **来源**：工坊页、A004 原件相对路径和重新生成命令。

## 自动与人工的分工

- `tools/mod_catalog.json` 保存 `cn / brief / cat / what / mp / note`。
- 自动字段从 `A004/workspace/mods_library/<id>/mods/<folder>`、`workspace/patches/mods/<folder>` 及所选 profile 生成。
- 元数据版本目录按部署工具的规则选择：取不高于引擎的最新数字目录，再应用对应 Overlay；不因原件上限旧而偷偷挑另一旧分支。
- 原件范围与补丁后范围必须分列；本地放行不写成作者支持 B42.22。
- 一个 Workshop ID 含多个子 Mod 时，catalog 键用 `<id>-<folder小写>`；档案文件名为 `<id>_<原名>_<中文简介>.md`。
- 不手改生成的单 Mod 文档。生成器会重建输出目录除 `_TEMPLATE.md` 外的 Markdown，README 写在输出目录的父级。

## 离线更新

在 `Grsh_PZ_Modpack` 中执行：

```bash
python tools/mod_archive.py
python tools/test_mod_archive.py
```

默认档案视图 `b422-compat` 覆盖候选全集；实际 `lab.py` 与 BAT 仍默认 `b422-main`。检查指定组合在 A004 根执行 `python lab.py check --profile <组合>`，不会启动游戏。

## 边界

- 体积、文件数、物品/配方/载具统计遍历原件完整目录。多版本目录会重复或放大统计，数字不是引擎实际加载值。
- 四条仅客户端项进服后会按服务端清单重载；不把主菜单加载当作进服仍有效。
- `both` 两端均需挂载；依赖在前，三个汉化包置底。
- 加载日志、SERVER STARTED、无异常都不等于视觉、碰撞、联机一致性或存档验收。
- 所有 Mod 版权归各自作者；本仓库只保存开发说明，不分发 Mod 二进制。
