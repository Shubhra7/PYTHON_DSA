import sys
arr=[2,3,4,-3,5,-9,10]
maxi=-sys.maxsize
sum1=0
for i in range(len(arr)):
    sum1=max(arr[i],arr[i]+sum1)
    maxi=max(maxi,sum1)
print(maxi)
