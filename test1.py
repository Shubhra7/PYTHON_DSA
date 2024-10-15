import sys
def second_lar_count(arr):
    min,mini2 = sys.maxsize, sys.maxsize
    for i in range(len(arr)):
        if(arr[i] < min):
            mini2 = min
            min = arr[i]
        elif(arr[i]<mini2):
            mini2 = arr[i]
    if(min == mini2):
        return 0
    return mini2

arr = [1,2,3,3,4,4]
print(second_lar_count(arr))
arr1 = [2,2,2,2,2]
print(second_lar_count(arr1))
