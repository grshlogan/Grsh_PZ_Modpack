# VSGirlBodyBoobBounceViewpoint（VSGirlBodyBoobBounceViewpoint）

**** · 分类：- · 3640496116 · 启用 · 加载位次 7

## 它做什么

（待补：这个 mod 的作用）

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3640496116` |
| mod id | `VariableSkinBoobBounceViewpoint(Requires ZombieBuddy)` |
| 文件夹 | `VariableSkinBoobBounceViewpoint` |
| 版本 / 适配 | `42.21` … `42.21` |
| 作者 | - |
| 工作坊更新时间 | - |
| 分发端 | both |
| 体积 / 文件 | 56.2 KB · 6 文件（lua 0，client 0，server 0；贴图 2；模型 0；翻译 2；Java 源码 0、jar/class 1） |

## 依赖与冲突

- 需要：`ZombieBuddy, VariableSkinBoobBounce, Viewpoint`
- 互斥：`VSGirlBodyExtension`
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

-

本机实测文件构成：客户端无 lua（纯资源）；服务端无 lua（只挂载）。

## 实测与排查

Viewpoint 3D 视角的次级运动；require BoobBounce + Viewpoint + ZombieBuddy。

```
python lab.py check --profile play
grep -a 'VariableSkinBoobBounceViewpoint' runs/<trial>/console.log
```

## 作者原话

```
Development test. Runtime secondary motion and nearby soft garment binding for original VS bodies. Requires a supported original VS body. Restart the game. Not game-validated.
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3640496116`
- 本地快照：`workspace/mods_library/3640496116/mods/VariableSkinBoobBounceViewpoint`
- 档案生成：`python tools/mod_archive.py --profile play`

