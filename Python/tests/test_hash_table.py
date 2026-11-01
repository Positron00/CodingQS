import unittest

import _path  # noqa: F401

from hash_table import HashTable


class TestHashTable(unittest.TestCase):
    def test_empty_table(self):
        table = HashTable()
        self.assertEqual(len(table), 0)
        self.assertNotIn("missing", table)
        with self.assertRaises(KeyError):
            table.get("missing")
        with self.assertRaises(KeyError):
            table.delete("missing")

    def test_put_and_get(self):
        table = HashTable()
        table.put("a", 1)
        table.put("b", 2)
        self.assertEqual(len(table), 2)
        self.assertEqual(table.get("a"), 1)
        self.assertEqual(table.get("b"), 2)
        self.assertIn("a", table)

    def test_update_existing_key(self):
        table = HashTable()
        table.put("x", 10)
        table.put("x", 99)
        self.assertEqual(len(table), 1)
        self.assertEqual(table.get("x"), 99)

    def test_delete(self):
        table = HashTable()
        table.put("one", 1)
        table.put("two", 2)
        table.delete("one")
        self.assertEqual(len(table), 1)
        self.assertNotIn("one", table)
        self.assertEqual(table.get("two"), 2)
        with self.assertRaises(KeyError):
            table.get("one")

    def test_many_keys_survive_resize(self):
        table = HashTable(capacity=4)
        pairs = [(f"key{i}", i) for i in range(20)]
        for key, value in pairs:
            table.put(key, value)
        self.assertEqual(len(table), 20)
        for key, value in pairs:
            self.assertEqual(table.get(key), value)


if __name__ == "__main__":
    unittest.main()
