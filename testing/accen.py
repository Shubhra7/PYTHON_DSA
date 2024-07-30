
def expo(n):
    count=0
    while (n%2==0):
        count+=1
        n=n//2
    return count


def MaxEx(a,b):
    ex=0
    ans=0
    for i in range(a,b+1):
        val=expo(i)
        if val > ex:
            ex=val
            ans=i
    return(ans)




print(MaxEx(7,12))
print(MaxEx(4,7))