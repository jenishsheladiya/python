# Check Palindrome (String)
def is_palindrome(s):
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and is_palindrome(s[1:-1])

print(is_palindrome("madam"))  # True
print(is_palindrome("hello"))  # False
