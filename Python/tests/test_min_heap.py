import unittest

import _path  # noqa: F401

from min_heap import MinHeap


class TestMinHeap(unittest.TestCase):
    def test_empty_heap_raises(self):
        heap = MinHeap()
        self.assertEqual(len(heap), 0)
        with self.assertRaises(IndexError):
            heap.peek()
        with self.assertRaises(IndexError):
            heap.pop()

    def test_push_and_pop_in_order(self):
        heap = MinHeap()
        for value in (5, 1, 8, 3, 2):
            heap.push(value)
        self.assertEqual(len(heap), 5)
        self.assertEqual(heap.peek(), 1)
        extracted = [heap.pop() for _ in range(5)]
        self.assertEqual(extracted, [1, 2, 3, 5, 8])

    def test_build_from_list(self):
        heap = MinHeap([9, 4, 7, 1, 3, 6])
        self.assertEqual(heap.peek(), 1)
        extracted = [heap.pop() for _ in range(6)]
        self.assertEqual(extracted, [1, 3, 4, 6, 7, 9])

    def test_single_element(self):
        heap = MinHeap([42])
        self.assertEqual(heap.peek(), 42)
        self.assertEqual(heap.pop(), 42)
        self.assertEqual(len(heap), 0)


if __name__ == "__main__":
    unittest.main()
