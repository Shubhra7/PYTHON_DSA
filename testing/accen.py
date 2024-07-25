
def diff(n,m):
    sum1=0
    sum2=0
    for i in range(1,m+1):
        if (i % n ==0):
            sum1+=i
        else:
            sum2+=i
    return abs(sum1-sum2)

n=3
m=10
print(diff(n,m))