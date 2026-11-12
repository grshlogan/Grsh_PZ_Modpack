# DeadWorks 载具框架（DeadWorks Vehicle Framework）

为 DeadWorks Nomad 与 Dale 房车提供车内行走、门窗踏板、座椅家具、水电与装甲等系统。

归属：**日常组合（玩法待验收）**；档案视图 `b422-compat`。
当前版本定义：**整车 0、本地物品定义 0、配方 0**；另引用共享物品 0。本地定义数含内部保留项，见独立列表；整车定义包括覆盖原版的条目，不等于新增车型数。

## 如何查找

- **生成整车**：在生成车辆菜单搜索下表完整 ID；显示译名时搜索中文列。联机管理命令用 `/addvehicle 完整ID`。
- **添加到背包**：普通物品、维修件、改装件都在添加物品菜单使用完整物品 ID；不要拿配方或内部槽位去刷车。
- **制作配方**：在制作界面查译名；配方 ID 用于排查，不是可放进背包的物品。
- 中文解释说明用途；只有翻译文件中找到的文字才称为游戏中文名。缺译保留脚本显示名，冲突列出各译文。

## 整车

本 Mod 没有当前版本的独立整车定义。

## 普通物品与书籍

无当前有效条目。

## 维修配件

无当前有效条目。

## 改装配件

无当前有效条目。

## 共享配件

无当前有效条目。

## 制作配方

无当前有效的脚本制作配方。Lua 动态添加的内容不在本次静态统计内。

## 内部定义、历史分支与未解析引用

有效资源层：42；仅合并 common 与所选版本，Overlay 按相对路径覆盖。
车辆模板 0 个、内部槽位 0 个，均不算整车或背包物品。旧根目录和未选中版本的定义不列入当前可用表。模板中短物品引用若追加机修类型后缀才匹配定义，属于静态映射，安装仍待实测。


## 概览

| Mod ID / 文件夹 | 分发端 | 版本 | 选择的 mod.info | 原件范围 → 当前范围 |
| --- | --- | --- | --- | --- |
| `DeadWorksVehicleFramework` / `DeadWorksVehicleFramework` | both（双端） | 1.0.4 | `42/mod.info` | 42.21 … 42.21 → 42.21 … 42.22（Overlay） |

原件体积 437.4 KB；体积按完整目录统计，与当前内容定义数分开。
工作坊：[查看作者页面](https://steamcommunity.com/sharedfiles/filedetails/?id=3825724093)。

## 证据与使用边界

**verified：有效源码静态确认。** 每个当前可复制 ID 均来自所选版本的定义；这不保证游戏已成功注册、生成、安装或联机同步。
挑战者 5 个车辆中文名另有 Owner 截图确认；本轮没有启动游戏。译文冲突、动态 Lua 内容和玩法效果仍需 Owner 游戏内核实。
以下人工记录保留原始语境；其中旧组合、旧数量和旧候选状态仅供追溯，当前统计与归属以上表和 profile 为准。

<!-- retained:start -->
## 依赖与冲突

- 需要：`ZombieBuddy, Viewpoint, PZVoxelStudioViewpoint`
- 互斥：无
- 被依赖：`aparosa_DWVFTweaks`、`DeadWorksNomadRV`、`DeadWorksDaleRV`

## 双端与联机

双端候选；依赖 ZombieBuddy、Viewpoint、6282，状态同步与存档兼容必须单独验收。

当前 profile：both（双端）。

本机文件构成：客户端有 lua；服务端有 lua。

## 实测与排查

原件 1.0.4，42.21 上限；Overlay 只放宽元数据，未修改 Java/Lua 行为；不与旧 GridRVHost 分支混装。

**planned：仅完成依赖、版本与补丁指纹静态检查。** 迁移收尾按 Owner 要求不启动游戏；本候选组合未验证加载、联网、存档或视觉。

版本放行补丁：`A004/workspace/patches/mods/DeadWorksVehicleFramework/42/mod.info`。原件更新后须重新核对指纹；撤除此补丁后运行 check 会恢复原件版本限制。

```
cd A004
python lab.py check --profile b422-compat
grep -a 'DeadWorksVehicleFramework' runs/<trial>/*console.log
```
<!-- retained:end -->

## 静态来源

路径相对 `A004/workspace/mods_library/`；`Overlay/<文件夹>/` 指 `A004/workspace/patches/mods/<文件夹>/`，`游戏原版/` 指当前 B42.22 客户端 Game 目录。翻译来源列出所有候选，未按加载顺序擅自消解异文。
