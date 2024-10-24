https://www.codechef.com/problems/TWOCLOSE

import sys

def swap(ind,arr):
    temp = arr[ind]
    arr[ind]=arr[-1]
    arr[-1]=temp

n=4
# arr = [16,4,8,2,1]
# arr = [3,10,30,1]
arr = [20,100,30,49,15]
mini = sum(arr[:n])

flag=1
while flag==1:
    flag = 0
    for i in range(n):
        # for j in range(n+1):
        if(arr[i] > arr[n] and arr[i] <= (2*arr[n])):
            swap(i,arr)
            # print(i,": ",arr)
            val = sum(arr[:n])
            if(mini > val):
                mini = val
                flag=1
    # print("Hello")

print(mini)