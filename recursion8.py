#  Check if List is Sorted
def is_sorted(arr, idx=0):
    if idx == len(arr) - 1:
        return True
    return arr[idx] <= arr[idx + 1] and is_sorted(arr, idx + 1)

print(is_sorted([1, 2, 3, 4]))  # True
print(is_sorted([1, 3, 2]))    # False
