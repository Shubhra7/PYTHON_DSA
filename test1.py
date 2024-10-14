
def fib(n):
    if(n==0 or n==1):
        return 1
    else:
        return (fib(n-1)**2)+(fib(n-2)**2)

n=int(input("Enter the value of n: "))
print(fib(n)%47)