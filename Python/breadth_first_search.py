"""Breadth-first search on graphs (adjacency list) and binary trees."""

from collections import deque


def graph_bfs(adjacency, start):
    """Return visit order for BFS from start on a directed adjacency-list graph."""
    visited = {start}
    order = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in adjacency.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order


def tree_bfs(root):
    """Level-order BFS on a TreeNode (left to right, top to bottom)."""
    if root is None:
        return []
    order = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        order.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return order
