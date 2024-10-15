n=14
print(bin(n)[2:])
count=0
while(n>0):
    count += n&1
    n >>= 1

print(count)
