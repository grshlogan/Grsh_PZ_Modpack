# VSGirlBody_Fix（VSGirlBody_Fix）

**** · 分类：- · 3640496116 · 启用 · 加载位次 5

## 它做什么

（待补：这个 mod 的作用）

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3640496116` |
| mod id | `42_VSGirlBody_Fix` |
| 文件夹 | `VariableSkinFix` |
| 版本 / 适配 | `-` … `-` |
| 作者 | - |
| 工作坊更新时间 | - |
| 分发端 | both |
| 体积 / 文件 | 82.7 KB · 6 文件（lua 1，client 1，server 0；贴图 2；模型 0；翻译 2） |

## 依赖与冲突

- 需要：无
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

-

本机实测文件构成：客户端有 lua；服务端无 lua（只挂载）。

## 实测与排查

VSGirlBody 修复补丁。

```
python lab.py check --profile play
grep -a 'VariableSkinFix' runs/<trial>/console.log
```

## 作者原话

```
42_VSGirlBodyFix
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3640496116`
- 本地快照：`workspace/mods_library/3640496116/mods/VariableSkinFix`
- 档案生成：`python tools/mod_archive.py --profile play`

