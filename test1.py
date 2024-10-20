n = 14
count = 0
while(n>0):
    val = n & 1
    if(val == 1):
        count += 1
    n >>= 1
print(count)
