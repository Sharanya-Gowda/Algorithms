import random
import time
import matplotlib.pyplot as plt

# Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Function to generate random array
def generate_random_array(n):
    return [random.randint(0, 10000) for _ in range(n)]

# Function to measure sorting times
def measure_sorting_times(sizes):
    merge_times = []
    insertion_times = []
    selection_times = []

    for size in sizes:
        arr = generate_random_array(size)
        
        arr_copy = arr.copy()
        start_time = time.time()
        merge_sort(arr_copy)
        merge_times.append(time.time() - start_time)
        
        arr_copy = arr.copy()
        start_time = time.time()
        insertion_sort(arr_copy)
        insertion_times.append(time.time() - start_time)
        
        arr_copy = arr.copy()
        start_time = time.time()
        selection_sort(arr_copy)
        selection_times.append(time.time() - start_time)
    
    return merge_times, insertion_times, selection_times

# Main
if __name__ == "__main__":
    sizes = [100, 200, 300, 500, 1000, 2000, 3000, 5000, 6000, 8000, 10000, 50000]
    merge_times, insertion_times, selection_times = measure_sorting_times(sizes)
    
    # Print table header
    print(f"{'n':<10}{'Merge sort time':<20}{'Insertion sort time':<20}{'Selection sort time':<20}")
    
    # Print each row of the table
    for i, size in enumerate(sizes):
        print(f"{size:<10}{merge_times[i]:<20.6f}{insertion_times[i]:<20.6f}{selection_times[i]:<20.6f}")
    
    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, merge_times, label='Merge Sort')
    plt.plot(sizes, insertion_times, label='Insertion Sort')
    plt.plot(sizes, selection_times, label='Selection Sort')
    
    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.title('Sorting Algorithms Time Complexity')
    plt.legend()
    plt.grid(True)
    plt.show()