import unittest
from unittest.mock import MagicMock

from jinja2 import Environment, FileSystemLoader

from gcscore import ScriptTemplatesExtension


class TestScriptNoArgs(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_commands_renderer = MagicMock()
        self.mock_commands_renderer.render_command = MagicMock(return_value="Hello, World!")

        ScriptTemplatesExtension.configure(self.mock_commands_renderer)  # NOQA
        loader = FileSystemLoader("data")
        self.environment = Environment(loader=loader, extensions=[ScriptTemplatesExtension])

    def test_most_simple(self):
        self.environment.get_template('simple_script001.sh').render()
        self.mock_commands_renderer.render_command.assert_called_once()
