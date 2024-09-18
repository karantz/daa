import heapq

def merge_k_sorted_arrays(arrays):
    
    heap = []
    
   
    for i, array in enumerate(arrays):
        if array: 
            heapq.heappush(heap, (array[0], i, 0))  
    
    result = []

    while heap:
        value, array_index, element_index = heapq.heappop(heap)
        result.append(value)
        if element_index + 1 < len(arrays[array_index]):
            next_value = arrays[array_index][element_index + 1]
            heapq.heappush(heap, (next_value, array_index, element_index + 1))
    
    return result


merged_array = merge_k_sorted_arrays([[1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10, 11]])
print("Merged array:", merged_array)



merged_array = merge_k_sorted_arrays([[1, 3, 7], [2, 4, 8], [9, 10, 11]])
print("Merged array:", merged_array)
