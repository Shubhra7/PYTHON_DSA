
def decN(n,num):
    l=[]
    while num!=0:
        rem=num%n
        l.append(rem)
        num=num//n
    l=l[::-1]
    ans=""
    for i in l:
        if i>9:
            extra=i-9
            val= (ord('A')-1) + extra
            ans+=chr(val)
        else:
            ans+=str(i)
    return ans




print(decN(12,718))
print(decN(21,5678))