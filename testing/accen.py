
def DectoN(n,num):
    rem=[]
    while (num!=0):
        rem.append(num%n)
        num=num//n
    rem=rem[::-1]
    ans=""
    for i in rem:
        if i > 9:
            extra=i-9
            val=(ord('A')-1) + extra
            ans += chr(val)
        else:
            ans += str(i)
    return ans


print(DectoN(12,718))
print(DectoN(21,5678))