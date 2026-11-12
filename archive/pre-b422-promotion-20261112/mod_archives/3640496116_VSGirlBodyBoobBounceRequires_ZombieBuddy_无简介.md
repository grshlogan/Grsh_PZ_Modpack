# VSGirlBodyBoobBounce(Requires ZombieBuddy)（VSGirlBodyBoobBounce(Requires ZombieBuddy)）

**** · 分类：- · 3640496116 · 启用 · 加载位次 6

## 它做什么

（待补：这个 mod 的作用）

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3640496116` |
| mod id | `VariableSkinBoobBounce` |
| 文件夹 | `VariableSkinBoobBounce` |
| 版本 / 适配 | `42.21` … `42.21` |
| 作者 | - |
| 工作坊更新时间 | - |
| 分发端 | both |
| 体积 / 文件 | 127.3 KB · 7 文件（lua 1，client 1，server 0；贴图 2；模型 0；翻译 0；Java 源码 0、jar/class 1） |

## 依赖与冲突

- 需要：`ZombieBuddy`
- 互斥：`VSGirlBodyExtension`
- 被依赖：`VariableSkinBoobBounceViewpoint`

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

-

本机实测文件构成：客户端有 lua；服务端无 lua（只挂载）。

## 实测与排查

2D 视角的次级运动（需 ZombieBuddy）；测试版。

```
python lab.py check --profile play
grep -a 'VariableSkinBoobBounce' runs/<trial>/console.log
```

## 作者原话

```
Development test. Runtime secondary motion and nearby soft garment binding for original VS bodies. Requires a supported original VS body. Restart the game. Not game-validated.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3640496116`
- 本地快照：`workspace/mods_library/3640496116/mods/VariableSkinBoobBounce`
- 档案生成：`python tools/mod_archive.py --profile play`

