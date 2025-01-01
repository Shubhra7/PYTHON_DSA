from collections import Counter
def countPairs(arr, target):
    #Your code here
    dp={}
    count=0
    for i in range(len(arr)):
        tar = target-arr[i]
        count += dp.get(tar,0)
        dp[arr[i]] = dp.get(arr[i],0)+1
    return count

print(countPairs([5,6,5,7,7,8],13))