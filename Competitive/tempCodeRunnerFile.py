
n=11
ans=""
while(n>0):
    if(n%2==0):
        ans+=str('0')
    else:
        ans += str('1')
    n = n//2
print(ans)