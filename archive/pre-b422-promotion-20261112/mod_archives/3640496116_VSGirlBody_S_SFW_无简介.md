# VSGirlBody_S_SFW（VSGirlBody_S_SFW）

**** · 分类：- · 3640496116 · 启用 · 加载位次 4

## 它做什么

（待补：这个 mod 的作用）

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3640496116` |
| mod id | `42_VSGirlBodySFW` |
| 文件夹 | `VariableSkinSFW` |
| 版本 / 适配 | `-` … `-` |
| 作者 | - |
| 工作坊更新时间 | - |
| 分发端 | both |
| 体积 / 文件 | 75.2 MB · 2,096 文件（lua 0，client 0，server 0；贴图 91；模型 162；翻译 2） |

## 依赖与冲突

- 需要：无
- 互斥：`42_VSGirlBodyL_M, 42_VSGirlBodyNSFW, VSGirlBodyM, VSGirlBodyL, 42_VSGirlBodySFW, TombBody, TombBodyCustom, TombBodyTex, TombBodyTexDOLL, TombBodyTexNUDE`
- 被依赖：无（叶子节点）

## 内容清单

脚本物品 **18** 条：

| 完整 id | 显示名 | 类型 |
| --- | --- | --- |
| `Base.ANSDhair` | ANSDhair | - |
| `Base.ANShair` | ANShair | - |
| `Base.CZChair` | CZChair | - |
| `Base.CZYhair` | CZYhair | - |
| `Base.CZZFhair` | CZZFhair | - |
| `Base.CZZhair` | CZZhair | - |
| `Base.face5` | face5 | - |
| `Base.1` | - | - |
| `Base.HBShair` | HBShair | - |
| `Base.HSMhair` | HSMhair | - |
| `Base.LJhair` | LJhair | - |
| `Base.MQDhair` | MQDhair | - |
| `Base.Phoebehair` | Phoebehair | - |
| `Base.Phoebehat` | Phoebehat | - |
| `Base.SJFhair` | SJFhair | - |
| `Base.TRChair` | TRChair | - |
| `Base.WKThair` | WKThair | - |
| `Base.ZMWhair` | ZMWhair | - |

配方 1 条：`Phoebehair`

## 双端与联机

-

本机实测文件构成：客户端无 lua（纯资源）；服务端无 lua（只挂载）。

## 实测与排查

VSGirlBody 女性身形替换（SFW / S 体型）；含重制发型与衣物适配。同一时间只能启用一个体型。

```
python lab.py check --profile play
grep -a 'VariableSkinSFW' runs/<trial>/console.log
```

## 作者原话

```
42_VSGirlBodySFW
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3640496116`
- 本地快照：`workspace/mods_library/3640496116/mods/VariableSkinSFW`
- 档案生成：`python tools/mod_archive.py --profile play`

