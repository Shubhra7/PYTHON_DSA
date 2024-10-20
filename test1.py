def cal(arr):
    ans1, ans2 = arr[0],arr[1]
    for i in range(2,len(arr)):
        if(i%2==0):
            ans1 += arr[i]
        else:
            ans2 ^= arr[i]
    return ans1 + ans2

arr = [1,2,4,2,1]
print(cal(arr))