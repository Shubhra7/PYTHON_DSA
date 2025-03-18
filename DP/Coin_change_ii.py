# https://leetcode.com/problems/coin-change-ii/description/
"""
You are given an integer array coins representing coins of different denominations 
and an integer amount representing a total amount of money.
Return the number of combinations that make up that amount. If that amount of money 
cannot be made up by any combination of the coins, return 0.
You may assume that you have an infinite number of each kind of coin.

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

"""

######################################
#       Tabulation
######################################
class Solution:
    def change(self,amount,coins):
        n=len(coins)
        dp=[[0]*(amount+1) for _ in range(n)]
        for i in range(amount+1):
            if i%coins[0]==0:
                dp[0][i]=1
        for i in range(1,n):
            for j in range(amount+1):
                notake=0+dp[i-1][j]
                take=0
                if j>=coins[i]:
                    take=dp[i][j-coins[i]]
                dp[i][j]=notake+take
        return dp[n-1][amount]
amount=5
coins=[1,2,5]
obj=Solution()
print(obj.change(amount,coins))
print(obj.change(5,[2,5]))


######################################
#       Recursion + memo
######################################
class Solution:
    def change(self,amount,coins):
        def f(ind,amount,dp):
            if ind==0:
                if amount%coins[0]==0:
                    return 1
                return 0
            if dp[ind][amount]!=-1:
                return dp[ind][amount]
            notake=0+f(ind-1,amount,dp)
            take=0
            if coins[ind]<=amount:  #Important to check
                take=f(ind,amount-coins[ind],dp)
            dp[ind][amount]=take+notake
            return dp[ind][amount]
        n=len(coins)
        dp=[[-1]*(amount+1) for _ in range(n)]
        ans=f(n-1,amount,dp)
        return ans

amount=5
coins=[1,2,5]
obj=Solution()
print(obj.change(amount,coins))
print(obj.change(5,[2,5]))