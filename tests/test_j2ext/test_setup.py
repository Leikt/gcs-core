import unittest

from jinja2 import Environment, BaseLoader
from gcscore import ScriptTemplatesExtension


class MockCommandRenderer:
    def render_command(self, _command: str, _environment: Environment) -> str:  # NOQA
        return "Hello, World!"


class TestSetup(unittest.TestCase):
    def test_valid(self):
        ScriptTemplatesExtension.configure(MockCommandRenderer())
        # This should not raise errors
        Environment(loader=BaseLoader(), extensions=[ScriptTemplatesExtension])

    def test_missing_configuration(self):
        with self.assertRaises(AttributeError):
            Environment(loader=BaseLoader(), extensions=[ScriptTemplatesExtension])

    def test_preset_consumption(self):
        commands_renderer = MockCommandRenderer()
        ScriptTemplatesExtension.configure(commands_renderer)
        # This should not raise errors
        Environment(loader=BaseLoader(), extensions=[ScriptTemplatesExtension])

        # The preset is consumed, preset should be called again
        with self.assertRaises(AttributeError):
            Environment(loader=BaseLoader(), extensions=[ScriptTemplatesExtension])
