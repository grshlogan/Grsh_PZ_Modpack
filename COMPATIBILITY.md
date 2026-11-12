# B42.22 主线迁移与兼容候选

记录日期：2026-11-12。当前结论：**日常主线已迁到 B42.22，日常组合现为 100 客户端 / 93 服务端；其余候选只有离线准备，尚不能宣称运行通过。** 迁移收尾阶段 Owner 要求 Agent 不启动游戏；当晚 Owner 六次调整日常：并入 render 3 与 rv 6，移出 DLSS / VisualFixes / Interiors，加回 VisualFixes / Interiors，删除 Interiors 并并入驾驶扩展 6（ImmersiveDriving、ShiftYourGear、ViewpointVanillaSteering、ViewpointDriveByShooting，以及 Drive-By 硬依赖 CarRoofFix、CarEnterExitFix），最后并入 KI5 车队 28 辆与 2 个载具功能件，由 Owner 自行实测。rv 6 首次联机崩在服务端 `NoSuchFieldError: PlayerPacket.id`，已用两份 jar 的字节码补丁修复，等 Owner 复测。

## 日常与候选分开

| 组合 | Client / Server | 世界 / 服务端名 | 内容 |
| --- | --- | --- | --- |
| `b422-main` | 100 / 93 | `b422batch2` | 日常默认；render 3 + rv 6（rv jar 已打字节码补丁）+ 驾驶扩展 6 + KI5 车队 28 辆与 2 个载具功能件，保留原 B42.22 世界名，待 Owner 复测 |
| `b422-compat-render` | 54 / 50 | `b422compatrender` | 日常去掉 rv 6 与驾驶扩展 6；独立世界备选，未启动 |
| `b422-compat-rv` | 60 / 56 | `b422compatrv` | 日常去掉驾驶扩展 6；独立世界备选，未启动 |
| `b422-compat` | 102 / 95 | `b422compat` | 日常 + 两个动态身体子模块；未启动 |

默认入口始终是 `A004/start-server.bat`、`A004/start-client.bat`；参数可选上述组合，但**当前不要启动**。候选不写日常世界；禁止把新引擎写过的存档交回旧 42.21。

[根 README](README.md) 与 [完整档案索引](mod_archives/INDEX.md) 覆盖当前 98 份档案（96 份日常、2 份兼容候选），另保留 1 份已移出档案（ViewpointDLSS）。对应 102 个 Mod 目录；4 组附属子 Mod 沿用合页。整车、物品、配方与共享引用分别统计，档案数量不等于启用 Mod 数，也不代表运行兼容通过。

## 原 12 条候选的当前去向（ViewpointInteriors 已删除，现保留 11 条）

| 组 | 文件夹 / Mod | 原件版本 | 原件上限 | 本地适配 |
| --- | --- | --- | --- | --- |
| render | `PZVoxelStudioViewpoint`（6282） | 1.0 | 42.21.0 | 元数据上限改 42.22 |
| render | `BasileDoors3D` | 0.2.8 | 42.21 | 同上 |
| render | `ViewpointKI5Materials` | 0.1.0 | 42.21.99 | 同上 |
| rv | `GridVansHost` | 0.1.8 | 42.21 | 42 与 common 元数据上限改 42.22 |
| rv | `GridVans` | 0.1.8 | 42.21 | 同上 |
| rv | `DeadWorksVehicleFramework` | 1.0.4 | 42.21 | 同上 |
| rv | `aparosa_DWVFTweaks` | 0.0.7 | 无 | 无需版本补丁；依赖房车框架 |
| rv | `DeadWorksNomadRV` | 0.9.2 | 42.21 | 42 与 common 元数据上限改 42.22 |
| rv | `DeadWorksDaleRV` | 0.2.2 | 42.21 | 同上 |
| full | `VariableSkinBoobBounce` | 0.6.1-test | 42.21 | 元数据上限改 42.22 |
| full | `VariableSkinBoobBounceViewpoint` | 0.6.0-test | 42.21 | 同上；真实 Mod ID 含 `(Requires ZombieBuddy)` |

工坊 9 个相关条目已逐页核对 Required items 并递归检查依赖，缓存更新时间与查询结果一致，无需重新下载。详细原始记录保存在本地 `A004/runs/promotion-b422-20261112/workshop-dependencies.json`；这是日期快照，不保证日后仍是最新版。

原件放 `A004/workspace/mods_library/`，本地适配只放 `A004/workspace/patches/mods/`。6282 原先在原件上做的实验改动已恢复；版本补丁只改元数据，唯一的**代码级**改动是 rv 两个 jar 的字节码补丁（见下节）。当前 Overlay 为 10 个 Mod 目录、23 条指纹保护记录，见本地 `workspace/patches/overlay-guards.json`。

`lab.py check / sync / export` 会校验选中候选的已登记原件和补丁指纹，发现上游变化就阻断，防止旧补丁静默套到新原件。房车仅选择 DeadWorks 分支，不加同包旧 GridRV/Legacy/替代分支；旧 GF2 外置包已被 R116 内置资源取代，不复活。

## 2026-11-12 组合调整（verified）

Owner 当日多次授权，Agent 只改定义与运行树，未启动游戏：

- 并入日常：`PZVoxelStudioViewpoint`、`BasileDoors3D`、`ViewpointKI5Materials`（render 3）与 rv 6 条房车链；`b422-main` 由 56/52 变为 59/55。
- 移出：`ViewpointDLSS`（3818838508）、`ViewpointVisualFixes`（3821308495）、`ViewpointInteriors`（3826550325）；四个组合定义同步移除，两端运行树的残留空目录已清。
- 加回：`ViewpointVisualFixes`、`ViewpointInteriors` 回到四个组合；`b422-main` 变为 61/57，compat-render 55/51、compat-rv 61/57、compat 63/59。同步记录 `A004/runs/interiors-restore-20261112/`（client 61 / 74,132 文件、Server 57 / 71,875；复制 171；28.56 s）。
- 同步记录（并入 rv 6 那次）：`A004/runs/rv-full-20261112/`（client 59 / 73,962 文件、Server 55 / 71,705；复制 589、删除 175；29.06 s）；回退用同目录 `pack-before.json`。
- 删除与并入（第四、五次调整）：按 Owner 指示删除 `ViewpointInteriors`（3826550325）——四个组合、原件库、Overlay 与档案页一起移除；并入驾驶扩展 4 条 `ImmersiveDriving`（3817413313）、`ShiftYourGear`（3838041847）、`ViewpointVanillaSteering`（3835182791）、`ViewpointDriveByShooting`（3826176290），以及 Drive-By 的硬依赖 `CarRoofFix`（3781616141）、`CarEnterExitFix`（3785695033）。6 条都只写 `versionMin`、没有 `versionMax`，**不需要 Overlay**。`b422-main` 66/62、compat-render 54/50、compat-rv 60/56、compat 68/64。
- 同步记录（驾驶扩展）：`A004/runs/driving-20261112/`（client 66 / 74,656 文件、Server 62 / 72,399；复制 692、删除 167；82.4 MiB；32.09 s）；两端运行树里 `ViewpointInteriors` 的残留空目录已清。回退用 `python lab.py sync --profile b422-main` 重新同步旧定义。
- 并入 KI5 车队（第六次调整，2026-11-12 深夜）：按 Owner 指示把第一批 8 辆（消防泵车 2942793445、99 款警车 2971246021、Campers! 3670064951、Bronco 2886833398、Hilux 3435796523、M923 2811383142、8N 拖拉机 3171176891、高尔夫球车 3330401526）与第二批 20 辆（YJ 3287727378、XJ 3409287192、Trooper 2932549988、F-Series 3073430075、Ranger 3539691958、Beetle 3005903549、Type 2 3041122351、Volvo 200 3292659291、Taurus 3088951320、Caravan 3034636011、Geo Metro 3008795514、GT500 3026723485、Camaro 2991201484、Charger 3631989559、92 Crown Vic 2962175696、LTD 3366300557、Caprice 3413704851、M151A2 2785549133、CUCV 3428008364、Oshkosh M911 2618213077）全部并入，再加 Owner 认可的两件载具功能件 `VisibleVehicleCouplingB42`（3807182783，mod 文件夹名带空格）与 `CarBatteryChargerModel`（3822775022，含 Viewpoint 补丁与客户端 jar `CBCPlacement.jar`）。
- 依赖与分发：28 个车型 / 拖挂工坊条目除 `82oshkoshM911` 外全部 `require damnlib`（已在组合内）；`92jeepYJJP18` 依赖 `92jeepYJ`、两份 `*extra` 贴图依赖各自本体、`CarBatteryChargerModel_Viewpoint` 依赖 ZombieBuddy + Viewpoint + 本体。两份 `*extra` 与 `CarBatteryChargerModel_Viewpoint` 共三条新增项设为 **client-only**，加上原有四条，客户端 100、服务端 93（差值 7）。全部 30 个新工坊条目的 `mod.info` 都**没有 `versionMax`**（`versionMin` 落在 42.14–42.21），**不需要新 Overlay**；`workspace/patches/` 维持 10 个 Mod 目录、23 条指纹。
- 同步记录（KI5 车队）：`A004/runs/ki5-fleet-20261112/`（client 100 / 84,652 文件、Server 93 / 82,375；复制 9,997 / 9,977；删除 0；553.1 / 551.1 MiB；67.03 s）；回退用同目录 `pack-before-b422-main.json` 与 `pack-before-b422-compat.json` 覆盖回定义后重跑 `sync`。
- 风险点（均未验证）：28 辆车会让路网车辆种类大幅增加，刷车密度与原版车比例会变；`CarEnterExitFix` 工坊有个别 KI5 车辆下车卡死反馈，第一批就该测；`Campers!` 与 DeadWorks RV 框架同为拖挂体系，联机拖挂物理需实测；M923/M151A2 的额外贴图只在客户端，服务端不装属于预期。
- 风险点（均未验证）：Drive-By 多人同步作者标 experimental；`CarEnterExitFix` 工坊评论有个别 KI5 车辆下车卡死案例；`ViewpointVanillaSteering` 明确不覆盖 KI5 方向盘。
- Owner 指令中的 `3633421539` 实为 ModernFirearmsSystem 42.21（3.786 GB 枪械大改），不是 Drive-By Shooting；本条按标题采用真实工坊 ID `3826176290`。
- 仍停在 42.21 的候选只剩 `VariableSkinBoobBounce` 与 `VariableSkinBoobBounceViewpoint`（compat 102/95）。

### rv 字节码补丁（2026-11-12，离线 verified）

- 症状：rv 6 并入后首次联机，服务端在 `fully-connected` 后 1 秒主线程崩：`java.lang.NoSuchFieldError: Class zombie.network.packets.character.PlayerPacket does not have member field 'zombie.network.fields.character.PlayerID id'`（`PlayerPacket.processServer` 的 ZB advice 里）。B42.22 已删除该字段。
- 修法：只改引用，不改逻辑。两份 jar 共 4 个类里 `getfield PlayerPacket.id` + `invokevirtual PlayerID.getPlayer` 改指 `getfield PlayerPacket.player` + `invokevirtual ConnectionPlayer.getPlayer()`；常量池追加新条目，指令操作数换索引，其余字节不动。
- 范围：`DeadWorksVehicleFramework.jar`（`DWVHost`、`Hooks$RiderWorld`）、`GridVansHost.jar`（`VanHostCabin`、`VanHostHooks$RiderWorld`）；`GridVans.jar` 与两个 jar 内其它类无此引用（全量扫描确认）。
- 产物：`workspace/patches/mods/<folder>/…` Overlay，指纹登记在 `workspace/patches/overlay-guards.json`；原件未改。
- 证据与回退：`A004/runs/rv-playerpacket-fix-20261112/NOTE.md`；`javap` 复核四个类均已指向新成员，四组 `check` 0 problem，`sync` 已把补丁写进双端运行树（各复制 2 个文件）。**运行期是否恢复正常仍需 Owner 联机复测。**

## 已有证据与尚未覆盖

| 范围 | 已有证据 | 不能据此声称 |
| --- | --- | --- |
| 迁移前日常 52/48 | 双端加载、服务端就绪 | 全部玩法、视觉或模板警告已验收 |
| 迁移前 6282 独立实验 | 原上限被跳过；放行后加载、16 包注册及联网 | 指定 6282 模型已正确绘制；GPU 1109 / packs116 是所有包合计 |
| 迁移后新路径 | 日常离线 check/sync；服务端曾到达就绪，但分离进程被宿主回收 | 客户端已联网、存档已保存重进或后台能长期托管 |
| 三个兼容组合 | 依赖、端别、版本范围及指纹静态检查通过 | Java 接口兼容、可加载、能联机、能保存或视觉正常 |

已知警告保留：B700 的 `B700SideStorage` / `B700Mudflaps`、J10 的 `JP82SpareTireRear` 缺失，以及字体、骨骼和空目录警告。它们尚未逐项游戏内确认，不因“未阻断启动”而判为无害。

## Overlay 更新与回退

1. 上游更新前保全当前原件、补丁及存档，重新查工坊依赖和版本。
2. 将对应 Overlay 移到 `workspace/backup/` 暂停使用；不要修改原件以伪造新指纹。
3. 执行相应组合的 `check`。原件仍卡 42.21 时检查失败是预期保护，不绕过。
4. 新原件正式支持后重新验证；需要本地修补时重新建立补丁和指纹，而非沿用旧适配。
5. 从候选切回日常，执行 `python lab.py sync --profile b422-main --trial <唯一记录名>`。部署台账负责移除受管候选文件，保留存档；此命令不启动游戏。

Viewpoint 固定官方 0.1.6.2：R116 0.3.51 校验 JAR 精确 SHA-256。随意升级 nightly 会破坏组合，不采用“永远拉最新版后直接覆盖”。

## 迁移与历史入口

- 当前本地结构：`A004/lab.py`、`workspace/`、`runs/`、`B42.22_runtime/{client,Server}`。
- 旧运行树曾封存于本地 `A004/archive/pre-b422-20261112/`，该 archive 后来已被移除，当前不存在；不能把它当作可用退路。下方 Git 文档历史只保存文档，不包含游戏运行树或存档备份。
- 旧 B42.22 日志在 `A004/runs/b422-history/`，迁移记录在 `A004/runs/promotion-b422-20261112/`。
- 文档旧根 README 与档案原样保存在 [历史目录](archive/pre-b422-promotion-20261112/README.md)。旧嵌套 52-Mod 文档已在提交 `3fd3c54` 保存；历史不是当前事实。

## 迁移阶段离线记录（2026-11-12 历史）

- 部署工具 7 项、档案生成器 4 项回归均通过；四组 `check` 分别为 100 / 54 / 60 / 102 selected，均为 0 problem（2026-11-12 并入 KI5 车队后重跑；`python -m unittest discover -s tests` 7 项 OK）。
- 当时 99 份档案中，96 份属于日常组合，2 份属于未运行的兼容候选，1 份标为已移出（ViewpointDLSS）；新增 30 份 KI5 页由早期脚本写入。人工目录缺 40 项造成的生成阻塞已在下节手册重建中修复；旧数量和旧生成页不作为当前内容统计。
- 日常第三次同步为双端零复制、零删除、零大小不符；保留现有部署台账，不把未测试候选同步到日常运行树。
- 7 个数据库只读 `quick_check` 均为 `ok`，历史账号表行数未变；这不是游戏内保存、联网或重进验收。
- 两处冗余 TEST 已在当时清理。清理前，嵌套 58 个文件与 `3fd3c54` 内容一致（仅允许 CRLF/LF 差异）；原根 65 份文档与完整本地备份逐字节一致。此处是当时的清理记录；旧 archive 后来已被移除，不再宣称封存退路可用。

当时的完整命令、环境、退出码与清理清单保存在本地 `A004/runs/promotion-b422-20261112/`，不随档案发布游戏或 Mod 二进制。当时记录的游戏进程与端口状态不代表现在；本轮手册工作没有启动客户端或服务端。

## 中文查询手册重建（2026-11-13，静态 verified）

- 生成器按当前 profile 选择 `common`、最高有效版本层与 Overlay；分别解析模块、整车、item、制作配方和模板。完整 ID 保留模块与大小写，不再混入根目录旧版本、模板或配方产出引用。
- 人工目录已补齐原先缺少的 40 个 Mod 条目。当前 98 份有效档案另保留 1 份已移出页，现有文件名与链接保留。按完整 ID 去重为 223 个整车定义、1,249 个本地物品定义、1,067 个配方定义；包含覆盖原版的定义及单列的内部保留 item，不等于新增车型数或推荐刷取物品数。
- 页面依次分列整车、普通物品 / 书籍、维修件、改装件、共享来源、配方与内部定义。每个物品有中文用途和菜单说明；有安装关系时列出车型与槽位，不能确认的具体行为明确标待核实。`Not in use` 与仍被模板引用的事实同时保留。
- 汉化读取当前启用客户端 Mod 及游戏原版的有效 JSON / TXT，支持 UTF-8 与 GB18030。缺中文时回退英文译文或脚本名；同一名称出现异文时列出全部来源。已核对 profile 末尾三汉化的顺序，但不据此假定 JSON、TXT、Java / Lua 运行时改写的最终优先级。含尾逗号等非标准语法的原件翻译保留警示，不声称游戏一定加载成功。
- 挑战者 42.13 分支确认 5 个整车、28 个本地物品、25 条配方；5 个完整车辆 ID 与 Owner 截图的中文名一致。实际示例见[挑战者档案](mod_archives/2873290424_70_Dodge_Challenger_70_年代美式肌肉车.md)。
- 验证命令（cwd：`Grsh_PZ_Modpack`，Windows / 本地 Python，exit code 均为 0）：`python -B tools/test_mod_archive.py`（9 项通过）；`python -B tools/mod_archive.py --profile b422-compat`（先临时预览，再更新正式页面）。
- 全量静态核验覆盖 8,769 个来源位置、98 份人工记录和正文 ID / 中文用途 / 共享提供者；本地链接 0 断链。再次生成后，103 个文件（档案、索引、模板、README、catalog）字节一致。已移出页及两份无关研究文件逐字节保留。
- 已知输入差异单列为线索：R32 模板文件顶层有多余闭括号；未定位的配件或模板引用不进入可刷清单。占位、过时和内部容量载体放在内部定义区；Lua 动态内容不假定已完整提取。
- 写入范围仅限文档及其工具；本轮没有改动原件、组合、运行树或存档，没有执行部署、游戏启动或 Git 写操作。有效定义、翻译文件、Owner 截图与游戏实刷属于不同证据；实际生成、安装、联机及存读仍由 Owner 在游戏内验证。

## Owner 验收表（全部待执行）

本次只交付离线候选。Owner 另行允许启动后，再按组依次验证；未通过不升级默认组合。

- [ ] 日常组合：新路径双端启动、连接到 `b422batch2`，确认原角色/存档，保存退出后重进。
- [ ] render：记录一个指定 6282 对象；确认门开合 / 碰撞 / 锁、KI5 血迹与材质（已并入日常，可直接测）。`ViewpointInteriors` 已删除，不再作为当前组合验收项。
- [ ] rv：并入日常的 6 条房车链（GridVansHost / GridVans / DeadWorksVehicleFramework / aparosa_DWVFTweaks / DeadWorksNomadRV / DeadWorksDaleRV）：生成明确车型，检查踏板/门/上下车/行走/家具/水电，两端状态一致；保存后重启读取。
- [ ] full：确认身体子模块在动作、视角切换和联网时不出错，不影响既有角色。
- [ ] 通用：汉化进服后保留；DebugMenu 管理权限、车辆名称/ID 搜索和模板警告逐项确认。

没有独立 Review verdict，也没有正式发布或签名授权；Owner 玩法验收由 Owner 单独记录。
