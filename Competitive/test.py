def maxSubarraySum(arr):
    cur_max=arr[0]
    ans=arr[0]
    for i in range(1,len(arr)):
        cur_max = max(arr[i], arr[i]+cur_max)
        ans=max(ans,cur_max)
    return ans



arr=[5,4,-1,7,8]
print(maxSubarraySum(arr))