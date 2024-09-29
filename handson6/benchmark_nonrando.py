
import random
import time
import matplotlib.pyplot as plt


def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]
    return j

def quicksort(arr):
    stack = [(0, len(arr) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = partition(arr, low, high)
            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))
    return arr

def generate_best_case(n):
    return list(range(n//2, n)) + [n//2-1] + list(range(n//2-1))

def generate_worst_case(n):
    return list(range(n))

def generate_average_case(n):
    return random.sample(range(n), n)

def benchmark(generate_func, sizes):
    times = []
    for n in sizes:
        arr = generate_func(n)
        start_time = time.time()
        quicksort(arr)
        end_time = time.time()
        times.append(end_time - start_time)
    return times

sizes = [1, 2, 5, 10, 50, 100, 500, 1000, 2000]

#benchmarks
best_times = benchmark(generate_best_case, sizes)
worst_times = benchmark(generate_worst_case, sizes)
average_times = benchmark(generate_average_case, sizes)

plt.figure(figsize=(10, 6))
plt.plot(sizes, best_times, 'go-', label='Best Case')
plt.plot(sizes, worst_times, 'ro-', label='Worst Case')
plt.plot(sizes, average_times, 'bo-', label='Average Case')

plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.title('Quicksort Performance')
plt.legend()
plt.grid(True)
plt.savefig('quicksort_performance.png')