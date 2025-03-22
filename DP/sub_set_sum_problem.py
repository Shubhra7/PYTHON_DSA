# https://youtu.be/fWX9xDmIzRI
# https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1

"""
Given an array of positive integers arr[] and a value sum, determine if there is a subset of arr[] 
with sum equal to given sum. 
Input: arr[] = [3, 34, 4, 12, 5, 2], sum = 9
Output: true 
Explanation: Here there exists a subset with target sum = 9, 4+3+2 = 9.

"""

class Solution:
    def isSubsetSum (self, arr, sum):
        # code here 
        ##------------------------------------
        #       Tabulation 
        ##------------------------------------
        n=len(arr)
        dp=[[False]*(sum+1) for _ in range(n)]
        for i in range(n):
            dp[i][0]=True
        if arr[0]<=sum:  #*** very important because first element might more big
            dp[0][arr[0]]=True
        for i in range(1,n):
            for j in range(1,sum+1):
                notake=dp[i-1][j]
                take=False
                if j>=arr[i]:
                    take=dp[i-1][j-arr[i]]
                dp[i][j]=take or notake
        return dp[n-1][sum]

        ##------------------------------------
        #       Recursion + memorization 
        ##------------------------------------
        # def f(ind,k,arr,dp):
        #     if k==0:
        #         return True
        #     if ind==0:
        #         if arr[ind]==k:
        #             return True
        #         return False
        #     if dp[ind][k]!=-1:
        #         return dp[ind][k]
        #     notake=f(ind-1,k,arr,dp)
        #     take=False
        #     if arr[ind]<=k:
        #         take=f(ind-1,k-arr[ind],arr,dp)
        #     dp[ind][k]=take or notake
        #     return dp[ind][k]
        # n=len(arr)
        # dp=[[-1]*(sum+1) for _ in range(n)]
        # ans=f(n-1,sum,arr,dp)
        # return ans

obj=Solution()
print(obj.isSubsetSum([3, 34, 4, 12, 5, 2],9)) #True
