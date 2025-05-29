# Flatten a Nested List
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result += flatten(item)
        else:
            result.append(item)
    return result

print(flatten([1, [2, [3, 4]], 5]))  # Output: [1, 2, 3, 4, 5]
