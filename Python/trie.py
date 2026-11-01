"""Prefix tree (trie) for string keys."""


class TrieNode:
    __slots__ = ("children", "is_end")

    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self._root = TrieNode()
        self._size = 0

    def __len__(self):
        return self._size

    def insert(self, word):
        node = self._root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        if not node.is_end:
            self._size += 1
        node.is_end = True

    def search(self, word):
        node = self._find_node(word)
        return node is not None and node.is_end

    def starts_with(self, prefix):
        if not prefix:
            return False
        return self._find_node(prefix) is not None

    def _find_node(self, prefix):
        node = self._root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
