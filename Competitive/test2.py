import sys
# arr = [5,4,2,1,-2,1,3]
arr=[3,3]

min, min2 = sys.maxsize, sys.maxsize

for i in range(len(arr)):
    if(min > arr[i]):
        min2 = min
        min = arr[i]
    elif(min2 > arr[i] and min!=arr[i]): # 2nd condition for avoid duplicate values
        min2=arr[i]

if(min2 == sys.maxsize):
    print("Not possible")
else:
    print(min2)
    

