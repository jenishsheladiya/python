# calculate the sum of first n natural numbers use recursion

def sum(n):
    if(n == 0):
        return 0
    return sum(n-1) + n
    
print(sum(5))