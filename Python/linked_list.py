"""Singly linked list built from ListNode nodes."""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, values=None):
        self.head = None
        if values is not None:
            for value in values:
                self.append(value)

    def append(self, val):
        node = ListNode(val)
        if self.head is None:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def to_list(self):
        values = []
        cur = self.head
        while cur:
            values.append(cur.val)
            cur = cur.next
        return values

    def __len__(self):
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count


def from_values(values):
    """Build a linked list head from an iterable of values."""
    dummy = ListNode()
    cur = dummy
    for value in values:
        cur.next = ListNode(value)
        cur = cur.next
    return dummy.next
