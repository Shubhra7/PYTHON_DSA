import math
arr = [4,3,5,2]

n=len(arr)

count = 0
for i in range(0,n-1):
    for j in range(i+1,n):
        if(arr[i]^arr[j]) > (arr[i]&arr[j]):
            count += 1
            print(i,' ',j)

print(count)




