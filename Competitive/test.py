def ProSma(sum,arr):
    if (len(arr) == 0):
        return -1
    arr.sort()
    if ((arr[0] + arr[1]) <= sum):
        return arr[0]*arr[1]
    return 0


arr=list(map(int,input().split()))
print(ProSma(6,arr))