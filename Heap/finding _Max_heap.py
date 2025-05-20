def max_heapify(heap, n, i):
    largest = i
    left = 2 * i
    right = 2 * i + 1

    if left <= n and heap[left] > heap[largest]:
        largest = left
    if right <= n and heap[right] > heap[largest]:
        largest = right

    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        max_heapify(heap, n, largest)

def build_max_heap(arr):
    # Add dummy value at index 0 for 1-based indexing
    heap = [None] + arr
    n = len(heap) - 1

    # Apply max_heapify from the last parent down to root
    for i in range(n // 2, 0, -1):
        max_heapify(heap, n, i)

    return heap

# Example usage
arr = [10, 20, 50, 30, 40]
heap = build_max_heap(arr)

print("Max Heap:", heap[1:])  # Skip index 0
