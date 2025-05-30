# Count Occurrences of Element in List
def count_occurrences(arr, target, idx=0):
    if idx == len(arr):
        return 0
    return (arr[idx] == target) + count_occurrences(arr, target, idx + 1)

print(count_occurrences([1, 2, 3, 2, 2, 4], 2))  # Output: 3
