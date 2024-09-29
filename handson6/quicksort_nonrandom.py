
def partition(arr, low, high):
    pivot = arr[high] #last element as pivot
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

# Example usage:
def main():
    n = int(input("Enter the number of elements: "))
    arr = []
    print(f"Enter {n} elements: ", end="")
    arr = list(map(int, input().split()))

    print("Original array:", ' '.join(map(str, arr)))
    quicksort(arr, 0, n - 1)
    print("Sorted array:", ' '.join(map(str, arr)))

if __name__ == "__main__":
    main()


