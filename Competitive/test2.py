def maxSubarraySum(arr,n):
    cur_max=arr[0]
    ans=0
    for i in range(1,len(arr)):
        cur_max = max(arr[i], cur_max + arr[i])
        ans = max(cur_max,ans)
    return ans

arr=[5,4,-1,-17,8]
print(maxSubarraySum(arr,10))