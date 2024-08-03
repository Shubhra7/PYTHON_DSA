def ex(i):
    ans=0
    while (i % 2==0):
        ans+=1
        i=i // 2
    return ans

def MaxExpo(a,b):
    max=0
    ans=a
    for i in range(a,b+1):
        expo = ex(i)
        if (expo > max):
            max=expo
            ans = i
    return ans


print(MaxExpo(7,12))
print(MaxExpo(9,17))