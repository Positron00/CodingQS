import unittest

import _path  # noqa: F401

from trie import Trie


class TestTrie(unittest.TestCase):
    def test_empty_trie(self):
        trie = Trie()
        self.assertEqual(len(trie), 0)
        self.assertFalse(trie.search("anything"))
        self.assertFalse(trie.starts_with("a"))

    def test_insert_and_search(self):
        trie = Trie()
        trie.insert("cat")
        trie.insert("car")
        self.assertEqual(len(trie), 2)
        self.assertTrue(trie.search("cat"))
        self.assertTrue(trie.search("car"))
        self.assertFalse(trie.search("ca"))
        self.assertFalse(trie.search("cats"))

    def test_starts_with(self):
        trie = Trie()
        trie.insert("hello")
        self.assertTrue(trie.starts_with("he"))
        self.assertTrue(trie.starts_with("hello"))
        self.assertFalse(trie.starts_with("help"))
        self.assertFalse(trie.starts_with(""))

    def test_duplicate_insert_does_not_inflate_size(self):
        trie = Trie()
        trie.insert("one")
        trie.insert("one")
        self.assertEqual(len(trie), 1)
        self.assertTrue(trie.search("one"))

    def test_shared_prefixes(self):
        trie = Trie()
        for word in ("app", "apple", "apt"):
            trie.insert(word)
        self.assertEqual(len(trie), 3)
        self.assertTrue(trie.search("app"))
        self.assertTrue(trie.search("apple"))
        self.assertTrue(trie.starts_with("ap"))
        self.assertFalse(trie.search("ap"))


if __name__ == "__main__":
    unittest.main()
