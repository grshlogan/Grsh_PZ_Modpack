# 模组调度优化（模组统一调度与优化(subieliSuSir)）

**模组加载调度提速** · 分类：性能 · 3825832401 · 启用 · 加载位次 51

## 它做什么

国内作者 subieliSuSir 的模组调度与优化核心，减少模组初始化阶段的重复扫描。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3825832401` |
| mod id | `SuPerfCore` |
| 文件夹 | `SuPerfCore` |
| 版本 / 适配 | `42.21.0` … `-` |
| 作者 | subieliSuSir |
| 工作坊更新时间 | 2026-10-25 |
| 分发端 | both |
| 体积 / 文件 | 217.3 KB · 6 文件（lua 1，client 0，server 0；贴图 3；模型 0；翻译 0；Java 源码 0、jar/class 1） |

## 依赖与冲突

- 需要：`ZombieBuddy`
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端。

本机实测文件构成：客户端无 lua（纯资源）；服务端无 lua（只挂载）。

## 实测与排查

需要 ZombieBuddy；与 PzPerformanceFixes 同装时按 loadOrder 先后加载。

```
python lab.py check --profile play
grep -a 'SuPerfCore' runs/<trial>/console.log
```

## 作者原话

```
作者苏别黎SuSir。本模组是纯调度核心，不添加任何物品与玩法<br>也不修改任何模组的任何文件，仅在运行时对全模组的Lua高频事件做统一调度与优化。<br>【原理】僵尸毁灭工程里所有Lua事件回调都汇集到同一个分发器。启用一两百个模组后，OnPlayerUpdate、OnTick、OnTickEvenPaused、OnZombieUpdate、OnPlayerMove、OnMouseMove、OnKeyKeepPressed、OnClimateTick这些高频事件会堆积几百个回调并逐帧全部执行，这是掉帧与周期性卡顿的主要来源之一。<br>【调度】在事件分发层按两种语义分别处理：全局按帧触发的事件（OnTick等）按触发次数轮转分组，默认每2次触发执行一组；按对象逐个触发的事件（OnPlayerUpdate、OnZombieUpdate、OnPlayerMove、OnKeyKeepPressed等）改为整帧闸门，默认每2帧执行一次，但该帧内每个玩家、每只丧尸、每个按键都会完整执行所有回调，不会出现只更新一半对象的情况。<br>【去重】同一个回调被模组重复注册多次时只保留一份，很多模组每次读档都会重复注册，越玩越卡的问题由此解决。<br>【保护】瞄准、相机、Viewpoint视角、后坐力、缩放类模组默认保持全速（按文件名自动识别），确保3D视角、开火与镜头逻辑不受影响。每条注入逻辑都带异常保护，调度异常时自动把回调搬回原事件并退回全速，绝不导致崩溃或存档损坏。可随时删除本模组，删除后所有模组立即恢复原样、无任何残留。<br>【可调】修改media/lua/shared/SPC_Core.lua里的SPC.policy表可单独调整每个事件的间隔与排除关键字，间隔填1即不调度。<br>【诊断】控制台执行SPC_Report()可打印各事件回调数量、调度模式与来源文件，定位最吃性能的模组。<br>【局限】仅优化Lua事件调度这一层，贴图、渲染、AI、物理、寻路、存档IO不在优化范围内；纯Java层的模组不经过Lua事件分发，不在本模组的调度范围内；降频为总量均摊而非精确锁频；联机时按对象事件是"每N帧完整更新一次"，不会出现只更新一半玩家的情况。<br>【免责声明】不保证100%一定能提升帧数，也不保证100%绝对可以解决卡顿问题。若出现任何奇怪的报错、崩溃或功能异常，请立
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3825832401`
- 本地快照：`workspace/mods_library/3825832401/mods/SuPerfCore`
- 档案生成：`python tools/mod_archive.py --profile play`

