import unittest

import _path  # noqa: F401

from binary_search_tree import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):
    def test_empty_tree(self):
        tree = BinarySearchTree()
        self.assertIsNone(tree.root)
        self.assertEqual(len(tree), 0)
        self.assertEqual(tree.inorder(), [])
        self.assertFalse(tree.contains(1))

    def test_insert_and_inorder(self):
        tree = BinarySearchTree()
        for value in (5, 3, 7, 1, 4):
            tree.insert(value)
        self.assertEqual(len(tree), 5)
        self.assertEqual(tree.inorder(), [1, 3, 4, 5, 7])

    def test_contains(self):
        tree = BinarySearchTree([10, 5, 15, 3, 7])
        self.assertTrue(tree.contains(7))
        self.assertTrue(tree.contains(10))
        self.assertFalse(tree.contains(99))
        self.assertFalse(tree.contains(0))

    def test_build_from_values(self):
        tree = BinarySearchTree([8, 3, 10, 1, 6, 14, 4])
        self.assertEqual(tree.inorder(), [1, 3, 4, 6, 8, 10, 14])

    def test_duplicate_not_counted_twice(self):
        tree = BinarySearchTree()
        tree.insert(2)
        tree.insert(2)
        tree.insert(2)
        self.assertEqual(len(tree), 1)
        self.assertEqual(tree.inorder(), [2])


if __name__ == "__main__":
    unittest.main()
