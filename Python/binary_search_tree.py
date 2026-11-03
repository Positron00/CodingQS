"""Binary search tree (BST)."""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self, values=None):
        self.root = None
        self._size = 0
        if values is not None:
            for value in values:
                self.insert(value)

    def __len__(self):
        return self._size

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
            self._size += 1
            return
        cur = self.root
        while True:
            if val < cur.val:
                if cur.left is None:
                    cur.left = TreeNode(val)
                    self._size += 1
                    return
                cur = cur.left
            elif val > cur.val:
                if cur.right is None:
                    cur.right = TreeNode(val)
                    self._size += 1
                    return
                cur = cur.right
            else:
                return

    def contains(self, val):
        cur = self.root
        while cur:
            if val < cur.val:
                cur = cur.left
            elif val > cur.val:
                cur = cur.right
            else:
                return True
        return False

    def inorder(self):
        out = []

        def walk(node):
            if node is None:
                return
            walk(node.left)
            out.append(node.val)
            walk(node.right)

        walk(self.root)
        return out
