
def ProductSmallest(sum,arr):
    if (len(arr)<2):
        return -1
    arr.sort()
    if ((arr[0] + arr[1]) <= sum):
        return (arr[0]*arr[1])
    else:
        return 0



sum = 4
arr=list(map(int,input().split()))

print(ProductSmallest(sum,arr))