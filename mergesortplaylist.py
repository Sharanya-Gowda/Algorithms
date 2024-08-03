def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0  

    mid = len(arr) // 2
    left_half, left_inversions = merge_sort(arr[:mid])
    right_half, right_inversions = merge_sort(arr[mid:])

    merged_arr, merge_inversions = merge(left_half, right_half)

    total_inversions = left_inversions + right_inversions + merge_inversions

    return merged_arr, total_inversions

def merge(left, right):
    merged = []
    inversions = 0  

    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inversions += len(left) - i  # Count inversions
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, inversions

arrays = [
    [1, 3, 5, 2, 4, 6],
    [5, 4, 3, 2, 1],
    [2, 1, 3, 4, 6, 5]]

for arr in arrays:
    sorted_arr, inversions = merge_sort(arr)
    print("Original array:", arr)
    print("Sorted array:", sorted_arr)
    print("Number of inversions:", inversions)
    print()
