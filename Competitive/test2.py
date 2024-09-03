arr = [1,2,3,6,10,11,13,21,5,4]

even, odd = 0,0
for i in arr:
    if(i%2==0):
        even += i
    else:
        odd += i

print(even,"  ",odd)