"""Documentation promotion regressions; all generation is confined to temporary fixtures."""
from __future__ import annotations
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

REPO = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('mod_archive', REPO / 'tools/mod_archive.py')
gen = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(gen)


class ArchiveTests(unittest.TestCase):
    def test_live_lab_is_sibling_root(self):
        self.assertEqual(gen.LAB_DEFAULT, REPO.parent)

    def test_overlay_bounds_are_reported_without_changing_base(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            base = root / 'Base/Fixture'
            overlay = root / 'Overlay/Fixture'
            (base / '42').mkdir(parents=True)
            (overlay / '42').mkdir(parents=True)
            original = b'name=Fixture\nid=Fixture\nversionMin=42.21\nversionMax=42.21\n'
            source = base / '42/mod.info'
            source.write_bytes(original)
            (overlay / '42/mod.info').write_bytes(original.replace(b'versionMax=42.21', b'versionMax=42.22'))
            info = gen.read_info(base, overlay)
            self.assertEqual(info['versionmax'], '42.22')
            self.assertEqual(info['_base_versionmax'], '42.21')
            self.assertEqual(source.read_bytes(), original)

    def test_version_directory_matches_deployment_not_metadata_minimum(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            for version, minimum in [('42', '42.21'), ('42.22', '42.0'), ('42.23', '42.0')]:
                folder = base / version
                folder.mkdir()
                (folder / 'mod.info').write_text(
                    f'id=Fixture\nversionMin={minimum}\nmodversion={version}\n', encoding='utf-8')
            info = gen.read_info(base)
            self.assertEqual(info['modversion'], '42.22')
            self.assertEqual(info['_info_path'], '42.22/mod.info')

    def test_effective_scripts_use_full_module_ids_and_only_selected_version(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            for branch, text in {
                '': 'module Base { item Legacy { Type = Normal, } vehicle Old {} }',
                '42.0': 'module Base { item Superseded { Type = Normal, } }',
                '42.13': '''module Base {
                    item Part { DisplayName = "Panel // still a name", Type = Normal, }
                    vehicle Car { template = CarBody, }
                    template vehicle CarBody { part Door { itemType = Base.Part, } }
                    craftRecipe MakePart { outputs { item 1 Base.Part, } }
                }
                module Extra { item Part { Type = Normal, } vehicle Trailer {} }
                // vehicle CommentOnly { }
                ''',
                '42.23': 'module Base { item Future { Type = Normal, } }',
                'common': 'module Shared { item Book { Type = Literature, } }',
            }.items():
                folder = base / branch
                scripts = folder / 'media/scripts'
                scripts.mkdir(parents=True)
                (folder / 'mod.info').write_text('id=Fixture\n', encoding='utf-8')
                (scripts / ('shared.txt' if branch == 'common' else 'fixture.txt')).write_text(text, encoding='utf-8')
            facts = gen.script_facts(base)
            self.assertEqual(set(facts['vehicles']), {'Base.Car', 'Extra.Trailer'})
            self.assertEqual(set(facts['items']), {'Base.Part', 'Extra.Part', 'Shared.Book'})
            self.assertEqual(set(facts['recipes']), {'Base.MakePart'})
            self.assertEqual(facts['items']['Base.Part']['display'], 'Panel // still a name')

    def test_names_support_json_gbk_txt_missing_and_conflicting_translations(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            records = {}
            for relative, text, encoding in [
                ('lua/shared/Translate/CN/IG_UI.json', '{"IGUI_VehicleNameCar": "中文整车"}', 'utf-8'),
                ('lua/shared/Translate/EN/IG_UI.json', '{"IGUI_VehicleNameCar": "English car"}', 'utf-8'),
                ('lua/shared/Translate/CN/ItemName_CN.txt', 'ItemName_CN = { ItemName_Base.Part = "车门", }', 'gb18030'),
                ('lua/shared/Translate/CN/Recipes.json', '{"MakePart": "制作车门"}', 'utf-8'),
            ]:
                path = base / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(text.encode(encoding))
                records[relative] = (path, relative)
            names = gen.load_translations(records, 'Fixture')
            self.assertEqual(gen.name_for(names, 'vehicle', 'Base.Car', 'Car')['text'], '中文整车')
            self.assertEqual(gen.name_for(names, 'item', 'Base.Part', 'Panel')['text'], '车门')
            self.assertEqual(gen.name_for(names, 'recipe', 'Base.MakePart', 'MakePart')['text'], '制作车门')
            missing = gen.name_for(names, 'item', 'Base.Missing', 'English only')
            self.assertEqual(missing['text'], 'English only')
            self.assertIn('未找到', missing['status'])
            names[('EN', 'item', 'Base.EnglishOnly')] = [{'text':'English game label', 'source':'EN:1'}]
            english = gen.name_for(names, 'item', 'Base.EnglishOnly', 'InternalIdentifier')
            self.assertEqual(english['text'], 'English game label')
            self.assertIn('未找到有效中文', english['status'])
            self.assertEqual(english['sources'], ['EN:1'])
            names[('CN', 'vehicle', 'Car')].append({'text':'另一译文', 'source':'Other:1'})
            conflict = gen.name_for(names, 'vehicle', 'Base.Car', 'Car')
            self.assertIn('冲突', conflict['status'])
            self.assertIn('另一译文', conflict['text'])
            self.assertTrue(any('Other:1' == x for x in conflict['sources']))

    def test_comments_overlay_scripts_and_nonstandard_translation_are_visible(self):
        text = 'module Base { /* outer /* nested */ hidden */ item Keep {} /*/ item Hidden {} /*/ }'
        clean = gen.strip_comments(text)
        self.assertIn('item Keep', clean)
        self.assertNotIn('Hidden', clean)
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            base, overlay = root/'mod', root/'patch'
            for path in (base, overlay):
                (path/'42/media/scripts').mkdir(parents=True)
                (path/'42/mod.info').write_text('id=Fixture\n', 'utf-8')
            original = b'module Base { item Old {} }'
            (base/'42/media/scripts/items.txt').write_bytes(original)
            (overlay/'42/media/scripts/items.txt').write_text('module Base { item New {} }', 'utf-8')
            facts = gen.script_facts(base, overlay)
            self.assertEqual(set(facts['items']), {'Base.New'})
            self.assertTrue(facts['items']['Base.New']['source'].startswith('Overlay/'))
            gen.stamp_facts(facts, '1/mods/Fixture')
            self.assertTrue(facts['items']['Base.New']['source'].startswith('Overlay/Fixture/'))
            self.assertEqual((base/'42/media/scripts/items.txt').read_bytes(), original)
            translation = root/'ItemName.json'
            translation.write_text('{"Base.New":"新物品",}', 'utf-8')
            names = gen.load_translations({'lua/shared/Translate/CN/ItemName.json':(translation,'ItemName.json')})
            self.assertIn('非标准', gen.name_for(names,'item','Base.New','New')['status'])

    def test_template_parts_resolve_shared_items_and_do_not_invent_spawn_ids(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rows = []
            for folder, script in {
                'Library': 'module Base { item Roofrack3 { Type = Normal, } }',
                'CarMod': '''module Base {
                    item Manual { ItemType = base:literature, LearnedRecipes = MakeRoofrack, }
                    item Shirt { ItemType = base:clothing, BodyLocation = Torso1, }
                    template vehicle Body {
                        part Roofrack { itemType = Base.Roofrack, }
                        part Empty { itemType = Base.nil, }
                    }
                    vehicle Car { mechanicType = 3, template = Body, }
                    craftRecipe MakeRoofrack { outputs { item 1 Base.Roofrack3, } }
                }''',
            }.items():
                branch = root / folder / '42/media/scripts'
                branch.mkdir(parents=True)
                (branch.parent.parent / 'mod.info').write_text(f'id={folder}\n', encoding='utf-8')
                (branch / 'test.txt').write_text(script, encoding='utf-8')
                rows.append({'folder':folder, 'load':len(rows)+1, 'enabled':True,
                             'cat':{}, 'facts':gen.script_facts(root/folder)})
            rows[0]['cat'] = {'content': {'Base.Roofrack3': {'purpose':'公共库提供的车顶行李架'}}}
            gen.enrich_content(rows, {})
            facts = rows[1]['facts']
            self.assertEqual(set(facts['shared_items']), {'Base.Roofrack3'})
            shared = facts['shared_items']['Base.Roofrack3']
            self.assertEqual(shared['provider'], 'Library')
            self.assertEqual(shared['fitments'][0]['vehicle'], 'Base.Car')
            self.assertEqual(shared['purpose'], '公共库提供的车顶行李架')
            self.assertNotIn('Base.Roofrack', facts['items'])
            self.assertEqual(facts['items']['Base.Manual']['category'], '普通物品 / 书籍')
            self.assertIn('Base.MakeRoofrack', facts['items']['Base.Manual']['purpose'])
            self.assertIn('穿戴', facts['items']['Base.Shirt']['purpose'])
            self.assertFalse(any(x['reference'] == 'Base.nil' for x in facts['unresolved']))

    def test_crlf_manual_sections_exclude_old_generated_inventories(self):
        text = ('# 旧档案\r\n\r\n## 内容清单\r\n\r\n旧物品 30 个。\r\n\r\n'
                '## 实测与排查\r\n\r\nOwner 的真实记录。\r\n\r\n'
                '## 来源\r\n\r\n旧自动路径。\r\n')
        self.assertEqual(gen.manual_sections(text), '## 实测与排查\n\nOwner 的真实记录。')

    def test_readme_lists_real_folders_workshop_links_and_grouped_counts(self):
        base = {'folder':'Visible Vehicle Coupling', 'wid':'3807182783',
                'info':{'id':'DifferentModId', 'name':'Workshop display title'},
                'cat':{'cn':'拖挂连接件', 'file':'3807182783_detail.md'},
                'distribution':'both', 'baseline':True,
                'facts':{'vehicles':{'Base.Car':{}, 'Base.Trailer':{}},
                         'items':{'Base.PartA':{}, 'Base.PartB':{}, 'Base.PartC':{}}}}
        addon = {**base, 'folder':'Actual Addon Folder', 'distribution':'client',
                 'info':{'id':'DifferentAddonId'}}
        page = {**base, 'members':[base, addon]}
        text = gen.render_readme([base, addon], [page], 'fixture', [])
        row = next(line for line in text.splitlines() if line.startswith('| 拖挂连接件 |'))
        self.assertIn('`Visible Vehicle Coupling`<br>`Actual Addon Folder`', row)
        self.assertNotIn('DifferentModId', row)
        self.assertNotIn('Workshop display title', row)
        self.assertIn('[3807182783](https://steamcommunity.com/sharedfiles/filedetails/?id=3807182783)', row)
        self.assertIn('[详细文档](mod_archives/3807182783_detail.md)', row)
        cells = [part.strip() for part in row.strip('|').split('|')]
        self.assertEqual(cells[3:5], ['2', '3'])
        self.assertIn('双端', row)
        self.assertIn('仅客户端', row)

    def test_custom_output_keeps_readme_with_its_archive(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            lab = root / 'lab'
            base = lab / 'workspace/mods_library/1/mods/Fixture/42'
            base.mkdir(parents=True)
            (base / 'mod.info').write_text('name=Fixture\nid=Fixture\nversionMin=42.22\n', encoding='utf-8')
            profile = lab / 'workspace/defs/b422-main/pack.json'
            profile.parent.mkdir(parents=True)
            profile.write_text(json.dumps({'gameVersion':'42.22.2','serverName':'fixture','worldName':'fixture',
                'adminPassword':'do-not-copy-fixture-secret',
                'mods':[{'workshopId':'1','folder':'Fixture','modId':'Fixture','distribution':'both','enabled':True}],
                'loadOrder':['Fixture']}), encoding='utf-8')
            catalog = root / 'catalog.json'
            catalog.write_text(json.dumps({'mods':{'1':{'cn':'Fixture','brief':'Fixture','what':'Fixture'}}}), encoding='utf-8')
            default = root / 'default-docs'
            default.mkdir()
            out = root / 'chosen-docs/mod_archives'
            argv = ['mod_archive.py', '--lab', str(lab), '--profile', 'b422-main', '--out', str(out)]
            with patch.multiple(gen, ROOT=default, CATALOG=catalog, TIMES=root/'no-times.json'), \
                 patch.object(sys, 'argv', argv), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(gen.main(), 0)
            self.assertTrue((out.parent / 'README.md').is_file())
            self.assertFalse((default / 'README.md').exists())
            readme = (out.parent / 'README.md').read_text(encoding='utf-8')
            self.assertIn('1 条属于日常组合', readme)
            page = next(out.glob('1_*.md'))
            page.write_text(page.read_text('utf-8') + '\n## 实测与排查\n\nOwner 实测记录必须保留。\n', 'utf-8')
            removed = out / '9_Removed.md'
            removed_bytes = '# 已移出\r\n保留此页。\r\n'.encode('utf-8')
            removed.write_bytes(removed_bytes)
            with patch.multiple(gen, ROOT=default, CATALOG=catalog, TIMES=root/'no-times.json'), \
                 patch.object(sys, 'argv', argv), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(gen.main(), 0)
                before = page.read_bytes()
                self.assertEqual(gen.main(), 0)
            self.assertEqual(page.read_bytes(), before)
            self.assertIn('Owner 实测记录必须保留。', page.read_text('utf-8'))
            self.assertEqual(removed.read_text('utf-8'), '# 已移出\n保留此页。\n')
            self.assertEqual(removed.read_bytes(), removed_bytes)
            self.assertNotIn('do-not-copy-fixture-secret', readme)


if __name__ == '__main__':
    unittest.main(verbosity=2)
