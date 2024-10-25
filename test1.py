def special_fibo(n):
    if(n==0 or n==1):
        return 1
    a=1
    b=1
    for i in range(2,n+1):
        c = (a**2)+(b**2)
        a=b
        b=c
    return (b%47)

n=int(input("Enter the value of n: "))
print(special_fibo(n))   