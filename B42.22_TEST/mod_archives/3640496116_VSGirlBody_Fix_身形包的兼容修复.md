# VSGirlBody 修复（VSGirlBody_Fix）

**身形包的兼容修复** · 分类：角色 / 外观 · `3640496116` · 启用 · 加载位次 48

## 它做什么

VSGirlBody 的配套修复补丁，修正身形/服装的兼容问题；需与对应身形包一起使用。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3640496116` |
| mod id | `42_VSGirlBody_Fix` |
| 文件夹 | `VariableSkinFix` |
| 版本 / 适配 | `-` … `-` |
| 作者 | - |
| 工作坊更新时间 | - |
| 分发端 | client（仅客户端） |
| 体积 / 文件 | 82.7 KB · 6 文件（lua 1，client 1，server 0；贴图 2；模型 0；翻译 2） |

## 依赖与冲突

- 需要：无
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

当前 profile 为 client-only；服务端不加载，进服后会被服务端列表丢弃。

**当前 profile：client-only（仅客户端）。** 服务端 `Mods=` 不含此条；联机进服后客户端会按服务端列表重载，因此该项在服务器内不会保留。

本机文件构成：客户端有 lua；服务端无 lua（只挂载）。

## 实测与排查

文件夹 VariableSkinFix、mod id 42_VSGirlBody_Fix；6 个文件 / 84 KB，1 个 lua。

```
cd A004/B42.22_TEST
python lab.py check --profile b422-batch2
grep -a 'VariableSkinFix' runs/<trial>/console.log
```

## 作者原话

```
42_VSGirlBodyFix
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3640496116`
- 本地快照（测试台）：`A004/B42.22_TEST/workspace/mods_library/3640496116/mods/VariableSkinFix`
- 档案生成：`python tools/mod_archive.py --profile b422-batch2`
