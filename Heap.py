# PriorityQueue class
# heap class

class PriorityQueueBase:
    """Base Class For a Priority Queue"""

    class _Item:
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __less__(self, other):
            return self._key < other._key

    def is_empty(self):
        return len(self) == 0


class Heap(PriorityQueueBase):
    """
    A priority queue implemented with a binary heap
    """

    # nonpublic behaviors
    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def _has_left(self, i):
        return self._left(i) < len(self._data)

    def _has_right(self, i):
        return self._right(i) < len(self._data)

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _heapify_up(self, i):
        """
        Up-heap bubbling
        """
        parent = self._parent(i)
        if i > 0 and self._data[i] < self._data[parent]:
            self._swap(i, parent)
            self._heapify_up(parent)

    def _heapify_down(self, i):
        """
        Down-Heap Bubbling
        """
        if self._has_left(i):
            left = self._left(i)
            small_child = left
            if self._has_right(i):
                right = self._right(i)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[i]:
                self._swap(i, small_child)
                self._heapify_down(small_child)

    # public behavior
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def push(self, key, value):
        self._data.append(self._Item(key, value))
        self._heapify_up(len(self._data) - 1)

    def pop(self):
        if self.is_empty():
            print('Priority queue is empty.')
        else:
            self._swap(0, len(self._data) - 1)
            item = self._data.pop()
            self._heapify_down(0)
            return item._key, item._value
