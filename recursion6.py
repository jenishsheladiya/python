
# Reverse a String
def reverse(str):
    if len(str) == 0 :
        return str
    return str[-1] + reverse(str[:-1])

print(reverse("hello"))