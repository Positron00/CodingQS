"""Hash table with separate chaining for collision resolution."""


class HashTable:
    DEFAULT_CAPACITY = 8
    LOAD_FACTOR = 0.75

    def __init__(self, capacity=None):
        cap = max(capacity or self.DEFAULT_CAPACITY, 1)
        self._buckets = [[] for _ in range(cap)]
        self._size = 0

    def __len__(self):
        return self._size

    def __contains__(self, key):
        bucket = self._buckets[self._index(key)]
        return any(k == key for k, _ in bucket)

    def put(self, key, value):
        index = self._index(key)
        bucket = self._buckets[index]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self._size += 1
        if self._size > len(self._buckets) * self.LOAD_FACTOR:
            self._resize()

    def get(self, key):
        bucket = self._buckets[self._index(key)]
        for k, value in bucket:
            if k == key:
                return value
        raise KeyError(key)

    def delete(self, key):
        index = self._index(key)
        bucket = self._buckets[index]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self._size -= 1
                return
        raise KeyError(key)

    def _index(self, key):
        return hash(key) % len(self._buckets)

    def _resize(self):
        old_items = []
        for bucket in self._buckets:
            old_items.extend(bucket)
        new_cap = len(self._buckets) * 2
        self._buckets = [[] for _ in range(new_cap)]
        self._size = 0
        for key, value in old_items:
            self.put(key, value)
