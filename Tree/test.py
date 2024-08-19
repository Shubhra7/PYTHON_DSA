
def maxSubarraySum(arr,n):
    ans = 0
    cur_max=arr[0]
    for i in range(1,len(arr)):
        cur_max=max(arr[i],arr[i]+cur_max)
        ans=max(cur_max,ans)
    return ans


arr=[5,4,-1,7,8]
print(maxSubarraySum(arr,10))
arr1=[5]
print(maxSubarraySum(arr1,10))