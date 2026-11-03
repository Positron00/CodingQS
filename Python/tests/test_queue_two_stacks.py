import unittest

import _path  # noqa: F401

from queue_two_stacks import Queue, Stack


class TestQueueTwoStacks(unittest.TestCase):
    def test_empty_queue_raises(self):
        queue = Queue()
        self.assertEqual(len(queue), 0)
        with self.assertRaises(IndexError):
            queue.dequeue()
        with self.assertRaises(IndexError):
            queue.peek()

    def test_fifo_single_batch(self):
        queue = Queue()
        for value in (1, 2, 3):
            queue.enqueue(value)
        self.assertEqual(len(queue), 3)
        self.assertEqual(queue.peek(), 1)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
        self.assertEqual(len(queue), 0)

    def test_interleaved_enqueue_dequeue(self):
        queue = Queue()
        queue.enqueue("a")
        queue.enqueue("b")
        self.assertEqual(queue.dequeue(), "a")
        queue.enqueue("c")
        self.assertEqual(queue.dequeue(), "b")
        self.assertEqual(queue.dequeue(), "c")

    def test_stack_used_by_queue(self):
        stack = Stack()
        stack.push(10)
        stack.push(20)
        self.assertEqual(stack.peek(), 20)
        self.assertEqual(stack.pop(), 20)
        self.assertEqual(len(stack), 1)


if __name__ == "__main__":
    unittest.main()
