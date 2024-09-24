class MinHeap:
    def __init__(self, data=None):
        # Initialize the heap; if data is provided, build the heap
        self.heap = [] if data is None else data
        if data:
            self.build_min_heap()

    def parent(self, i):
        # Calculate the parent index using bit manipulation
        return (i - 1) >> 1  # Equivalent to (i - 1) // 2

    def left(self, i):
        # Calculate the left child index
        return (i << 1) + 1  # Equivalent to 2 * i + 1

    def right(self, i):
        # Calculate the right child index
        return (i << 1) + 2  # Equivalent to 2 * i + 2

    def build_min_heap(self):
        # Build the min-heap from an unsorted array
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.min_heapify(i)

    def min_heapify(self, i):
        # Heapify the node at index i (downward direction)
        left = self.left(i)
        right = self.right(i)
        smallest = i

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            # Swap with the smallest child and continue heapifying
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.min_heapify(smallest)

    def insert(self, value):
        # Insert a new element into the heap
        self.heap.append(value)  # Add to the end
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, i):
        # Heapify upwards from index i to restore the heap property
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            # Swap with parent until heap property is satisfied
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def pop(self):
        # Remove and return the minimum element (root of the heap)
        if len(self.heap) == 0:
            return None  # Heap is empty
        if len(self.heap) == 1:
            return self.heap.pop()  # Only one element, no need to heapify

        # Replace root with the last element and heapify downwards
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.min_heapify(0)
        return root

    def peek(self):
        # Return the minimum element (root) without removing it
        if len(self.heap) > 0:
            return self.heap[0]
        return None

    def print_heap(self):
        # Utility function to print the heap array
        print("Heap:", self.heap)


# Example usage of the MinHeap
if __name__ == "__main__":
    # Create a heap with an initial list of values
    heap = MinHeap([800, 499, 71, 1, 100, 30])

    print("Initial heap:")
    heap.print_heap()

    # Insert a new value into the heap
    heap.insert(0)
    print("\nHeap after inserting 0:")
    heap.print_heap()

    # Remove the root and show the new heap
    popped = heap.pop()
    print(f"\nPopped root: {popped}")
    print("Heap after popping root:")
    heap.print_heap()

    # Peek at the current root without removing it
    print(f"\nCurrent root: {heap.peek()}")
