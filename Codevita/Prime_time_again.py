import math

# def isPrime(n):
#     """Check if a number n is a prime number."""
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True

def isPrime(n):
    if n<=3:
        return True
    else:
        if( ((n**2)-1)%24==0):
            return True
    return False

def checkPrime(l, ad):
    """Check if all numbers in the list l incremented by ad are prime."""
    pi = [x + ad for x in l]
    return all(isPrime(x) for x in pi)

# Read inputs
d = int(input("Enter d: "))
p = int(input("Enter p: "))

n = d // p

# Initialize list l
l = [0] * p
print("Initial list l:", l)

# Modify the list l
val = 1
for i in range(p):
    l[i] += val
    val += n

print("Modified list l:", l)

# Check prime status for various ad values
count = 0
print()
for i in range(1,n):
    if checkPrime(l, i):
        count += 1
        print(f"List l with ad = {i}: {[x + i for x in l]}")

print("Count of valid ad values:", count)