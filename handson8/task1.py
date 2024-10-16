def quickselect(arr, left, right, i):
    if left == right:  # If the array contains only one element
        return arr[left]

    # Partition the array and get the pivot index
    pivot_index = partition(arr, left, right)

    # The pivot is in its final sorted position
    if i == pivot_index:
        return arr[i]
    elif i < pivot_index:
        return quickselect(arr, left, pivot_index - 1, i)
    else:
        return quickselect(arr, pivot_index + 1, right, i)

def partition(arr, left, right):
    pivot = arr[right]
    i = left
    for j in range(left, right):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i

# Example usage:
def find_ith_statistic(arr, i):
    if i < 0 or i >= len(arr):
        raise IndexError("Index is out of bounds")
    return quickselect(arr, 0, len(arr) - 1, i)

# Example
arr = [3, 6, 8, 10, 1, 2, 1]
i = int(input("enter the i elemnt :"))
result = find_ith_statistic(arr, i)
print(f"The {i+1}th order statistic is: {result}")
