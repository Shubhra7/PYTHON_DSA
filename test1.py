
num = 9
ans=""
while num>0:
    ans = str(int((num%2 !=0)))+ans
    num = num//2
print(ans)