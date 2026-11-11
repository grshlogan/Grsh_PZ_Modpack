# 调试菜单社区版（B42/41调试菜单社区版 (DebugMenu_Community)）

**右键多级调试与管理员菜单** · 分类：调试 / 工具 · `3735377688` · 启用 · 加载位次 23

## 它做什么

右键多级菜单：生成物品/车辆、传送、世界与建造调试、笔刷等；管理员判定后出现，部分子功能另需 -debug。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3735377688` |
| mod id | `PZ_Debug` |
| 文件夹 | `DebugMenu` |
| 版本 / 适配 | `-` … `-` |
| 作者 | [千年纹][耄耋][凌社千白] |
| 工作坊更新时间 | 2026-10-21 |
| 分发端 | both（双端） |
| 体积 / 文件 | 1.1 MB · 135 文件（lua 115，client 106，server 3；贴图 2；模型 0；翻译 16） |

## 依赖与冲突

- 需要：无
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端挂载；菜单是客户端 UI，服务端只需 mod 列表一致。

当前 profile：both（双端）。

本机文件构成：客户端有 lua；服务端有 lua。

## 实测与排查

当前本地包 1.1 MB / 135 文件；mod id=PZ_Debug；与 CheatMenuRebuild 不共存。

```
cd A004/B42.22_TEST
python lab.py check --profile b422-batch2
grep -a 'DebugMenu' runs/<trial>/console.log
```

## 作者原话

```
正常版
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3735377688`
- 本地快照（测试台）：`A004/B42.22_TEST/workspace/mods_library/3735377688/mods/DebugMenu`
- 档案生成：`python tools/mod_archive.py --profile b422-batch2`
