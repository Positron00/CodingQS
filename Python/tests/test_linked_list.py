import unittest

import _path  # noqa: F401

from linked_list import LinkedList, ListNode, from_values


class TestLinkedList(unittest.TestCase):
    def test_empty_list(self):
        ll = LinkedList()
        self.assertIsNone(ll.head)
        self.assertEqual(len(ll), 0)
        self.assertEqual(ll.to_list(), [])

    def test_append(self):
        ll = LinkedList()
        for value in (1, 2, 3):
            ll.append(value)
        self.assertEqual(len(ll), 3)
        self.assertEqual(ll.to_list(), [1, 2, 3])

    def test_construct_from_values(self):
        ll = LinkedList([10, 20, 30])
        self.assertEqual(ll.to_list(), [10, 20, 30])

    def test_from_values_helper(self):
        head = from_values(["a", "b", "c"])
        values = []
        cur = head
        while cur:
            values.append(cur.val)
            cur = cur.next
        self.assertEqual(values, ["a", "b", "c"])

    def test_manual_node_chain(self):
        head = ListNode(1, ListNode(2, ListNode(3)))
        ll = LinkedList()
        ll.head = head
        self.assertEqual(ll.to_list(), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
