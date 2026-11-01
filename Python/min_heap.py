"""Array-based min heap. Parent at index i has children at 2*i+1 and 2*i+2."""


class MinHeap:
    def __init__(self, items=None):
        self._data = list(items) if items else []
        if self._data:
            self._heapify()

    def __len__(self):
        return len(self._data)

    def peek(self):
        if not self._data:
            raise IndexError("peek from empty heap")
        return self._data[0]

    def push(self, value):
        self._data.append(value)
        self._sift_up(len(self._data) - 1)

    def pop(self):
        if not self._data:
            raise IndexError("pop from empty heap")
        if len(self._data) == 1:
            return self._data.pop()
        root = self._data[0]
        self._data[0] = self._data.pop()
        self._sift_down(0)
        return root

    def _heapify(self):
        for i in range(len(self._data) // 2 - 1, -1, -1):
            self._sift_down(i)

    def _sift_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self._data[index] >= self._data[parent]:
                break
            self._data[index], self._data[parent] = (
                self._data[parent],
                self._data[index],
            )
            index = parent

    def _sift_down(self, index):
        n = len(self._data)
        while True:
            left = 2 * index + 1
            right = left + 1
            smallest = index
            if left < n and self._data[left] < self._data[smallest]:
                smallest = left
            if right < n and self._data[right] < self._data[smallest]:
                smallest = right
            if smallest == index:
                break
            self._data[index], self._data[smallest] = (
                self._data[smallest],
                self._data[index],
            )
            index = smallest
