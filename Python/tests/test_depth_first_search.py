import unittest

import _path  # noqa: F401

from binary_search_tree import BinarySearchTree, TreeNode
from depth_first_search import graph_dfs, tree_dfs_preorder


class TestDepthFirstSearch(unittest.TestCase):
    def test_graph_dfs_linear(self):
        adj = {"A": ["B"], "B": ["C"], "C": []}
        self.assertEqual(graph_dfs(adj, "A"), ["A", "B", "C"])

    def test_graph_dfs_branching(self):
        adj = {
            "A": ["B", "C"],
            "B": ["D"],
            "C": [],
            "D": [],
        }
        self.assertEqual(graph_dfs(adj, "A"), ["A", "B", "D", "C"])

    def test_graph_dfs_handles_cycle(self):
        adj = {"A": ["B"], "B": ["C"], "C": ["A"]}
        self.assertEqual(graph_dfs(adj, "A"), ["A", "B", "C"])

    def test_graph_dfs_single_node(self):
        adj = {"X": []}
        self.assertEqual(graph_dfs(adj, "X"), ["X"])

    def test_tree_dfs_preorder(self):
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(4), TreeNode(5)),
            TreeNode(3),
        )
        self.assertEqual(tree_dfs_preorder(root), [1, 2, 4, 5, 3])

    def test_tree_dfs_on_bst(self):
        tree = BinarySearchTree([5, 3, 7, 1, 4])
        self.assertEqual(tree_dfs_preorder(tree.root), [5, 3, 1, 4, 7])
        self.assertNotEqual(tree_dfs_preorder(tree.root), tree.inorder())


if __name__ == "__main__":
    unittest.main()
