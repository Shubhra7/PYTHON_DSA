def add_xor(arr):
    ans1=0
    ans2=0
    for i in range(len(arr)):
        if(i%2==0):
            ans1 += arr[i]
        else:
            ans2 ^= arr[i]
    return ans1 + ans2


arr = [1,2,4,2,1]
print(add_xor(arr))