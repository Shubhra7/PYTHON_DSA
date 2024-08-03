
def largeSmall(arr):
    even=[]
    odd=[]
    for i in range(len(arr)):
        if (i % 2 == 0):
            even.append(arr[i])
        else:
            odd.append(arr[i])
    even.sort()
    odd.sort()
    return even[-2] + odd[1]




arr=list(map(int,input().split()))
print(largeSmall(arr))