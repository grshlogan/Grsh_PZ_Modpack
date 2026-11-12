# 方向盘模型（Project Viewpoint - Vanilla Steering）

把原版车辆简陋的方向盘换成细节更多的模型，并加转向动画；兼容 `Vanilla Vehicles Animated`。**作者在描述首行限定"原版车辆"，评论区作者明确回了"Doesn't work with KI5"**——KI5 方向盘不会被替换，KI5 车辆维持原样。

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
| `ViewpointVanillaSteering` / `ViewpointVanillaSteering` | both（双端） | 0.3.2 | `42/mod.info` | 42.21 … - → 42.21 … - |

原件体积 10.3 MB；体积按完整目录统计，与当前内容定义数分开。
工作坊：[查看作者页面](https://steamcommunity.com/sharedfiles/filedetails/?id=3835182791)。

## 证据与使用边界

**verified：有效源码静态确认。** 每个当前可复制 ID 均来自所选版本的定义；这不保证游戏已成功注册、生成、安装或联机同步。
挑战者 5 个车辆中文名另有 Owner 截图确认；本轮没有启动游戏。译文冲突、动态 Lua 内容和玩法效果仍需 Owner 游戏内核实。
以下人工记录保留原始语境；其中旧组合、旧数量和旧候选状态仅供追溯，当前统计与归属以上表和 profile 为准。

<!-- retained:start -->
## 依赖与冲突

- 需要：`Viewpoint`、`ZombieBuddy`（`zbVersionMin=2.3.4`）、`ImmersiveDriving`（转向动画来源）
- `loadModAfter=VanillaVehiclesAnimated,TrueVanillaVehicleEnhancer,ImmersiveDriving`
- 本包未装 `VanillaVehiclesAnimated` / `TrueVanillaVehicleEnhancer`，对应兼容分支不生效，属于正常降级

## 双端与联机

`distribution: both`。模型与动画走 Viewpoint 的渲染路径，联机前提同 ImmersiveDriving：双端同版本、ZombieBuddy 已批准 Java 组件。

## 实测与排查

**planned：仅完成依赖、版本与加载顺序静态检查（`check` 0 problem）与同步落盘。** 未启动游戏；方向盘模型是否出现在原版车上、转向动画是否正常都待 Owner 实测。KI5 车辆按作者说明不会变化，不要把它当作 KI5 内饰增强。
<!-- retained:end -->

## 静态来源

路径相对 `A004/workspace/mods_library/`；`Overlay/<文件夹>/` 指 `A004/workspace/patches/mods/<文件夹>/`，`游戏原版/` 指当前 B42.22 客户端 Game 目录。翻译来源列出所有候选，未按加载顺序擅自消解异文。
