import unittest

import _path  # noqa: F401

from linked_list import ListNode, from_values
from linked_list_cycle import has_cycle


def _head_with_cycle(values, cycle_index):
    """Build a list from values; tail.next points to nodes[cycle_index], or None."""
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if cycle_index >= 0:
        nodes[-1].next = nodes[cycle_index]
    return nodes[0]


class TestLinkedListCycle(unittest.TestCase):
    def test_empty_list(self):
        self.assertFalse(has_cycle(None))

    def test_single_node_no_cycle(self):
        self.assertFalse(has_cycle(ListNode(1)))

    def test_linear_list(self):
        self.assertFalse(has_cycle(from_values([1, 2, 3, 4])))

    def test_cycle_back_to_head(self):
        head = _head_with_cycle([1, 2, 3], cycle_index=0)
        self.assertTrue(has_cycle(head))

    def test_cycle_to_middle(self):
        head = _head_with_cycle([1, 2, 3, 4], cycle_index=1)
        self.assertTrue(has_cycle(head))

    def test_self_loop(self):
        node = ListNode(99)
        node.next = node
        self.assertTrue(has_cycle(node))


if __name__ == "__main__":
    unittest.main()
