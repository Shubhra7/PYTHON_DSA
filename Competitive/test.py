def fact(n):
    ans=1
    for i in range(1,n+1):
        ans *= i
    return ans

def permut(s):

    l=['a','e','i','o','u','A','E','I','O','U']

    d={}
    count1=0

    for i in range(len(s)):
        if (s[i] not in l):
            count1 += 1
            d[s[i]] = d.get(s[i],0)+1
    ans = 1
    for i in d.values():
        if(i>1):
            ans *= fact(i)

    return int(fact(count1) / ans)

s="ybghjahebuyitob"
print(permut(s))


