import random

def partition_random(arr, low, high):
    pivot_index = random.randint(low, high)
    print(f"pivot:{arr[pivot_index]}")
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]  # Swap pivot with last element
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quicksort_random_inplace(arr, low, high):
    
    if low < high:
        pi = partition_random(arr, low, high)
        quicksort_random_inplace(arr, low, pi - 1)
        quicksort_random_inplace(arr, pi + 1, high)
def main():
    n = int(input("Enter the number of elements: "))
    arr = []
    print(f"Enter {n} elements: ", end="")
    arr = list(map(int, input().split()))

    print("Original array:", ' '.join(map(str, arr)))
    quicksort_random_inplace(arr, 0, n - 1)
    print("Sorted array:", ' '.join(map(str, arr)))

if __name__ == "__main__":
    main()
