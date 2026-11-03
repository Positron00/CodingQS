"""Depth-first search on graphs (adjacency list) and binary trees."""


def graph_dfs(adjacency, start):
    """Return visit order for DFS from start on a directed adjacency-list graph."""
    visited = set()
    order = []

    def visit(node):
        if node in visited:
            return
        visited.add(node)
        order.append(node)
        for neighbor in adjacency.get(node, []):
            visit(neighbor)

    visit(start)
    return order


def tree_dfs_preorder(root):
    """Preorder DFS on a TreeNode (visit node, then left, then right)."""
    order = []

    def visit(node):
        if node is None:
            return
        order.append(node.val)
        visit(node.left)
        visit(node.right)

    visit(root)
    return order
