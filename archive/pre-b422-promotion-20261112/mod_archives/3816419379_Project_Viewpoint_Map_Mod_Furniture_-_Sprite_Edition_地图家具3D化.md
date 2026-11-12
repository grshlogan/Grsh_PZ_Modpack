# 浣熊市家具贴图（Project Viewpoint Map Mod Furniture - Sprite Edition）

**地图家具3D化** · 分类：素材 / 地图 · 3816419379 · 启用 · 加载位次 17

## 它做什么

给浣熊市地图家具补 3D 贴图版，配合 Viewpoint 显示成立体家具。

## 概览

| 项 | 值 |
| --- | --- |
| 工作坊 ID | `3816419379` |
| mod id | `aparosa_vpmo_RaccoonCityB42` |
| 文件夹 | `aparosa_vpmo_RaccoonCityB42` |
| 版本 / 适配 | `42.0.0` … `-` |
| 作者 | - |
| 工作坊更新时间 | 2026-10-29 |
| 分发端 | both |
| 体积 / 文件 | 9.4 MB · 23 文件（lua 3，client 2，server 0；贴图 3；模型 0；翻译 14；Java 源码 0、jar/class 1） |

## 依赖与冲突

- 需要：`ZombieBuddy, Viewpoint`
- 互斥：无
- 被依赖：无（叶子节点）

## 内容清单

没有脚本物品（Lua / 模型 / 补丁类 mod）。

## 双端与联机

双端。

本机实测文件构成：客户端有 lua；服务端无 lua（只挂载）。

## 实测与排查

只影响显示，不改地图逻辑。

```
python lab.py check --profile play
grep -a 'aparosa_vpmo_RaccoonCityB42' runs/<trial>/console.log
```

## 作者原话

```
Shapes for map mod furniture and props so Project Viewpoint can show them in 3D. Contains no textures. Also lets this furniture go inside Viewpoint - 3D RVs. Maps: 42Grapeseed, AnruisiTown, AsianStyleTilesOnly, Atlanta, Atlas Underground, Bunker, Burunduk, Cathaya Valley 2.0 B42 version, Clover Lake, Constown42, Daegutest, Daisy County B42 version, Erikas_Tiles, Estate 39, Fort JadeLake, Grapeseed, Greenleaf B42 version, HavenFall, IrisEyot, LiuDing_Tiles, MBSB, Mockingbird, Nekomata Ridge, NellisAFB, Nettle Township B42 version, OujinjinTiles, PertsPartyTiles, Project Gurashi, Quella's Castle, RaccoonCityB42, RavenCreekB42, Roccos_Tiles, SMP_AquaFarmResources, SMP_CustomMapBridge, SafeWayHamlet, Secretz42, ThermoNewburbs, TryhonestyTiles, UnofficialMappersCommunityTilePack, Willowbrook Bastion! 2, Xixi's Serene Cottage, Yanghu Town, bigbearlake42, melos_tiles_for_miles_pack, newhartburg, simonMDsTiles, tikitown_tiles
```

## 来源

- 工作坊：`https://steamcommunity.com/sharedfiles/filedetails/?id=3816419379`
- 本地快照：`workspace/mods_library/3816419379/mods/aparosa_vpmo_RaccoonCityB42`
- 档案生成：`python tools/mod_archive.py --profile play`

