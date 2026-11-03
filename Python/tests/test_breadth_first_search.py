import unittest

import _path  # noqa: F401

from binary_search_tree import BinarySearchTree, TreeNode
from breadth_first_search import graph_bfs, tree_bfs
from depth_first_search import graph_dfs, tree_dfs_preorder


class TestBreadthFirstSearch(unittest.TestCase):
    def test_graph_bfs_linear(self):
        adj = {"A": ["B"], "B": ["C"], "C": []}
        self.assertEqual(graph_bfs(adj, "A"), ["A", "B", "C"])

    def test_graph_bfs_branching(self):
        adj = {
            "A": ["B", "C"],
            "B": ["D"],
            "C": [],
            "D": [],
        }
        self.assertEqual(graph_bfs(adj, "A"), ["A", "B", "C", "D"])
        self.assertNotEqual(graph_dfs(adj, "A"), graph_bfs(adj, "A"))

    def test_graph_bfs_handles_cycle(self):
        adj = {"A": ["B"], "B": ["C"], "C": ["A"]}
        self.assertEqual(graph_bfs(adj, "A"), ["A", "B", "C"])

    def test_graph_bfs_single_node(self):
        adj = {"X": []}
        self.assertEqual(graph_bfs(adj, "X"), ["X"])

    def test_tree_bfs_level_order(self):
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(4), TreeNode(5)),
            TreeNode(3),
        )
        self.assertEqual(tree_bfs(root), [1, 2, 3, 4, 5])
        self.assertNotEqual(tree_bfs(root), tree_dfs_preorder(root))

    def test_tree_bfs_on_bst(self):
        tree = BinarySearchTree([5, 3, 7, 1, 4])
        self.assertEqual(tree_bfs(tree.root), [5, 3, 7, 1, 4])


if __name__ == "__main__":
    unittest.main()
