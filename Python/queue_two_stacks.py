"""Queue implemented with two stacks (amortized O(1) enqueue/dequeue)."""


class Stack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def push(self, value):
        self._data.append(value)

    def pop(self):
        if not self._data:
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        if not self._data:
            raise IndexError("peek from empty stack")
        return self._data[-1]


class Queue:
    def __init__(self):
        self._in_stack = Stack()
        self._out_stack = Stack()

    def __len__(self):
        return len(self._in_stack) + len(self._out_stack)

    def enqueue(self, value):
        self._in_stack.push(value)

    def dequeue(self):
        self._shift_if_needed()
        return self._out_stack.pop()

    def peek(self):
        self._shift_if_needed()
        return self._out_stack.peek()

    def _shift_if_needed(self):
        if len(self._out_stack) == 0:
            while len(self._in_stack) > 0:
                self._out_stack.push(self._in_stack.pop())
