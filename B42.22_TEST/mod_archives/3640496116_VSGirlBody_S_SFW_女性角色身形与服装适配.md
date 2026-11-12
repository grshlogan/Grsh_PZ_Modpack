# VSGirlBody SFW 身形（VSGirlBody_S_SFW）

**女性角色身形与服装适配** · 分类：角色 / 外观 · `3640496116` · 启用 · 加载位次 47

## 它做什么

VariableSkin 系列的 SFW 女性身形包，提供角色身体与服装的替换资源；不包含成人内容。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3640496116` |
| mod id | `42_VSGirlBodySFW` |
| 文件夹 | `VariableSkinSFW` |
| 版本 / 适配 | `-` … `-` |
| 作者 | - |
| 工作坊更新时间 | - |
| 分发端 | client（仅客户端） |
| 体积 / 文件 | 75.2 MB · 2,096 文件（lua 0，client 0，server 0；贴图 91；模型 162；翻译 2） |

## 依赖与冲突

- 需要：无
- 互斥：`42_VSGirlBodyL_M, 42_VSGirlBodyNSFW, VSGirlBodyM, VSGirlBodyL, 42_VSGirlBodySFW, TombBody, TombBodyCustom, TombBodyTex, TombBodyTexDOLL, TombBodyTexNUDE`
- 被依赖：无（叶子节点）

## 内容清单

脚本物品 **17** 条：

| 完整 id | 显示名 | 类型 |
| --- | --- | --- |
| `Base.ANSDhair` | ANSDhair | base:clothing |
| `Base.ANShair` | ANShair | base:clothing |
| `Base.CZChair` | CZChair | base:clothing |
| `Base.CZYhair` | CZYhair | base:clothing |
| `Base.CZZFhair` | CZZFhair | base:clothing |
| `Base.CZZhair` | CZZhair | base:clothing |
| `Base.face5` | face5 | base:clothing |
| `Base.HBShair` | HBShair | base:clothing |
| `Base.HSMhair` | HSMhair | base:clothing |
| `Base.LJhair` | LJhair | base:clothing |
| `Base.MQDhair` | MQDhair | base:clothing |
| `Base.Phoebehair` | Phoebehair | base:clothing |
| `Base.Phoebehat` | Phoebehat | base:clothing |
| `Base.SJFhair` | SJFhair | base:clothing |
| `Base.TRChair` | TRChair | base:clothing |
| `Base.WKThair` | WKThair | base:clothing |
| `Base.ZMWhair` | ZMWhair | base:clothing |

配方 1 条：`Phoebehair`

## 双端与联机

当前 profile 为 client-only：只装客户端；服务端不加载，进服后会被服务端 Mods= 列表丢弃。

**当前 profile：client-only（仅客户端）。** 服务端 `Mods=` 不含此条；联机进服后客户端会按服务端列表重载，因此该项在服务器内不会保留。

本机文件构成：客户端无 lua（纯资源）；服务端无 lua（只挂载）。

## 实测与排查

工作坊 ID 3640496116 包含多个子 mod；本条目文件夹 VariableSkinSFW、mod id 42_VSGirlBodySFW；18 个脚本物品，75.2 MB。

```
cd A004/B42.22_TEST
python lab.py check --profile b422-batch2
grep -a 'VariableSkinSFW' runs/<trial>/console.log
```

## 作者原话

```
42_VSGirlBodySFW
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3640496116`
- 本地快照（测试台）：`A004/B42.22_TEST/workspace/mods_library/3640496116/mods/VariableSkinSFW`
- 档案生成：`python tools/mod_archive.py --profile b422-batch2`
