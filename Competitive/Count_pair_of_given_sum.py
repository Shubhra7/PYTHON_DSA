# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/hashing-gfg-160/problem/count-pairs-with-given-sum--150253
"""
Input: arr[] = [1, 5, 7, -1, 5], target = 6 
Output: 3
Explanation: Pairs with sum 6 are (1, 5), (7, -1) and (1, 5). 
Input: arr[] = [1, 1, 1, 1], target = 2 
Output: 6
Explanation: Pairs with sum 2 are (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1).
"""

def countPairs(arr, target):
        #Your code here
        dp={}
        count = 0
        for i in range(len(arr)):
            tar = target-arr[i]
            count += dp.get(tar,0)
            dp[arr[i]]=dp.get(arr[i],0)+1
        return count

print(countPairs([1, 5, 7, -1, 5],6))  #o/p=3