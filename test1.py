def fibo(n):
    if(n==0 or n==1):
        return n
    prev=1
    prev2=0
    for i in range(1,n):
        ans = prev + prev2
        prev2 = prev
        prev = ans
    return prev

n=1
print(fibo(n))
print(fibo(2))
print(fibo(3))
print(fibo(4))