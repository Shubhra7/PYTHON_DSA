n=6

print(bin(n)[2:])
ans=""
while n>0:
    rem = n%2
    ans = str(rem) + ans
    n = n//2
print(ans)