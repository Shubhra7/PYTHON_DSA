
def maxSubarraySum(arr,n):
    cur_max=arr[0]
    ans=arr[0]
    for i in range(1,len(arr)):
        cur_max = max(arr[i], cur_max + arr[i])
        ans = max(ans, cur_max)
    return ans


arr=[5,4,-1,7,8]
print(maxSubarraySum(arr,10))

s= [2, 3, 4, -3, 5, -9, 7]
print(maxSubarraySum(s,5))