import sys

min = min2 = sys.maxsize

arr = [5,4,2,1,2,1,3]

for i in range(len(arr)):
    if(arr[i]<min):
        min2=min
        min=arr[i]
    elif(arr[i]<min2 and min!=arr[i]):
        min2 = arr[i]

if(min2 != sys.maxsize):
    print(min2)
else:
    print("Not possible")