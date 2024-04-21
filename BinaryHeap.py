class BinaryHeap:
    def __init__(self, key=lambda x: x):
        self.heap = []
        self.key = key

    def insert(self, item):
        # Inserts new item into heap.
        self.heap.append(item)
        self._bubble_up(len(self.heap) - 1)

    def extract_min(self):
        # Removes and returns smallest item from heap.
        if not self.heap:
            raise IndexError("extract_min() called on empty heap")
        self._swap(0, len(self.heap) - 1)
        min_item = self.heap.pop()
        if self.heap:
            self._bubble_down(0)
        return min_item

    def _bubble_up(self, index):
        # Pushes up item at provided index to correct position in heap.
        parent_index = (index - 1) // 2
        while index > 0 and self.key(self.heap[index]) < self.key(self.heap[parent_index]):
            self._swap(index, parent_index)
            index = parent_index
            parent_index = (index - 1) // 2

    def _bubble_down(self, index):
        # Pushes down item at provided index to correct position in heap.
        child_index = 2 * index + 1
        while child_index < len(self.heap):
            right_child_index = child_index + 1
            if (right_child_index < len(self.heap) and
                    self.key(self.heap[right_child_index]) < self.key(self.heap[child_index])):
                child_index = right_child_index

            if self.key(self.heap[child_index]) >= self.key(self.heap[index]):
                break

            self._swap(child_index, index)
            index = child_index
            child_index = 2 * index + 1

    def _swap(self, i, j):
        # Swaps elements at provided indices.
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def peek(self):
        # Returns smallest item without removing it.
        if not self.heap:
            raise IndexError("peek() called on empty heap")
        return self.heap[0]

    def size(self):
        # Returns number of items in heap.
        return len(self.heap)
