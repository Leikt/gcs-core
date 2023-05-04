import unittest

from jinja2 import FileSystemLoader, Environment

from gcscore import CommandRenderer, ScriptTemplatesExtension, ParserError


class TestNoCommandsBlock(unittest.TestCase):
    def setUp(self) -> None:
        self.command_renderer = CommandRenderer()
        ScriptTemplatesExtension.configure(self.command_renderer)
        self.environment = Environment(loader=FileSystemLoader('data'), extensions=[ScriptTemplatesExtension])

    def test_no_arguments(self):
        result = self.command_renderer.render_command('command001.sh', self.environment)
        self.assertEqual('echo "Hello, World!"', result)

    def test_no_argument_multiline(self):
        result = self.command_renderer.render_command('command002.sh', self.environment)
        self.assertEqual('echo "Hello, Raj!"\necho "Hi, how are you?"', result)

    def test_with_simple_arguments(self):
        result = self.command_renderer.render_command('command100.sh Robin', self.environment)
        self.assertEqual('echo "Hello, Robin!"', result)

    def test_missing_argument(self):
        self.command_renderer.render_command('command100.sh', self.environment)
        self.assertIsInstance(self.command_renderer.errors_history[0], ParserError)

    def test_arguments_1(self):
        result = self.command_renderer.render_command('command101.sh s1 s2 s3 -a', self.environment)
        expected = 'echo "Do A"\necho "s1"\necho "s2"\necho "s3"\n'
        self.assertEqual(expected, result)

    def test_composition_1(self):
        result = self.command_renderer.render_command('script002.sh vm01', self.environment)
        expected = 'echo "Do thinks for vm01"\necho "Hello, World!"\n\n\necho "Hello, World!"\n\n\necho "Do A"\n' \
                   'echo "s1"\necho "s2"\necho "s3"\n\n\n\necho "Hello, vm01!"'
        self.assertEqual(expected, result)

    def test_composition_with_error_display(self):
        result = self.command_renderer.render_command('command101.sh -a', self.environment)
        self.assertIsNone(result)
        print(self.command_renderer.errors_history.render())
