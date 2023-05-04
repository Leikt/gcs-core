import os
import unittest
from pathlib import Path

from gcscore.mod import compact_script


class TestScriptCompaction(unittest.TestCase):
    def do_test(self, path: Path):
        raw = path.read_text()

        expected_path = path.with_stem('oneliner_' + path.stem)
        expected = expected_path.read_text()

        language = 'shell' if path.suffix == '.sh' else 'powershell'
        actual = compact_script(language, raw)
        self.assertEqual(expected, actual)

    def test_all(self):
        parent = Path('data')
        for file in os.listdir(parent):
            if file.startswith('oneliner'):
                continue

            print(f'>>> {file}')
            self.do_test(parent / file)

    def test_language_unknown(self):
        with self.assertRaises(KeyError):
            compact_script('not_found', '')
