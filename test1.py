n=9

ans=""
while n>0:
    ans = str(0+(n%2!=0)) + ans
    n=n//2
print(ans)