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
            self.assertNotIn('do-not-copy-fixture-secret', readme)


if __name__ == '__main__':
    unittest.main(verbosity=2)
