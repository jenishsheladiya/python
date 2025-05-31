# Find Maximum Element in a List
def find_max(arr, idx=0):
    if idx == len(arr) - 1:
        return arr[idx]
    return max(arr[idx], find_max(arr, idx + 1))

print(find_max([1, 5, 3, 9, 2]))  # Output: 9
