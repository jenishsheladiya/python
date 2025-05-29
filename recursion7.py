# Calculate Product of Elements in List
def product_list(arr, idx=0):
    if idx == len(arr):
        return 1
    return arr[idx] * product_list(arr, idx + 1)

print(product_list([1, 2, 3, 4]))  # Output: 24
