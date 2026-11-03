import unittest

import _path  # noqa: F401

from balanced_brackets import is_balanced


class TestBalancedBrackets(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(is_balanced(""))

    def test_simple_balanced(self):
        self.assertTrue(is_balanced("()"))
        self.assertTrue(is_balanced("[]"))
        self.assertTrue(is_balanced("{}"))

    def test_multiple_types(self):
        self.assertTrue(is_balanced("()[]{}"))
        self.assertTrue(is_balanced("{[()()]}"))

    def test_nested(self):
        self.assertTrue(is_balanced("((()))"))
        self.assertTrue(is_balanced("[{()}]"))

    def test_wrong_closer(self):
        self.assertFalse(is_balanced("(]"))
        self.assertFalse(is_balanced("([)]"))

    def test_unclosed_openers(self):
        self.assertFalse(is_balanced("(("))
        self.assertFalse(is_balanced("{["))

    def test_extra_closers(self):
        self.assertFalse(is_balanced("())"))
        self.assertFalse(is_balanced("]"))

    def test_ignores_non_bracket_characters(self):
        self.assertTrue(is_balanced("int main() { return [1]; }"))


if __name__ == "__main__":
    unittest.main()
