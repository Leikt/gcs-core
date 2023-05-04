import unittest

from gcscore._error_history import ErrorHistory  # NOQA


class TestErrorHistory(unittest.TestCase):
    def test_simple(self):
        history = ErrorHistory()
        history.append(FileNotFoundError("Machin is not found."))
        history.append(KeyError("Key was not found in {}"))

        print(history.render(backtraces=True))

    def test_clear(self):
        history = ErrorHistory()
        history.append(Exception('ex'))
        self.assertEqual(1, len(history))
        history.clear()
        self.assertEqual(0, len(history))
