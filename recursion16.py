# Print Digits of a Number
def print_digits(n):
    if n == 0:
        return
    print_digits(n // 10)
    print(n % 10)

print_digits(1234)

