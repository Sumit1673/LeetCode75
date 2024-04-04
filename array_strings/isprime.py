import math

# TIme complexity O(sqrt(n))
def isprime(n):
    x = 2
    while x <= math.sqrt(n):
        if n % x == 0:
            return False
        x += 1
    return True
    
print(isprime(4))