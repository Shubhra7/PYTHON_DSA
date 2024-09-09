n=14

# print(bin(n)[2:].count('1'))

count = 0
while (n>0):
    count += n & 1
    n >>= 1

print(count)

n=11
ans=""
while(n>0):
    if(n%2==0):
        ans+=str('0')
    else:
        ans += str('1')
    n = n//2
print(ans[::-1])

