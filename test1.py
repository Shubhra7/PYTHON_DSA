def sq_fibo(n):
    if(n==0 or n==1):
        return 1
    else:
        return (sq_fibo(n-1)**2) + (sq_fibo(n-2)**2)
    

n=int(input())
print(sq_fibo(n)%47)