# Striver video

"""
You are given an integer array coins representing coins of different denominations
 and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
"""

"""
Input: coins = [1,2,5], amount = 11
Output: 3
"""

#------------------------------------
#       Recursion Method
#------------------------------------

import sys
def min_coin_need(ind,coins,amount,dp):
    if(ind==0):
        if(amount % coins[0]==0):       # Last coin case
            return amount//coins[0]
        else:
            return sys.maxsize
    if(dp[ind][amount] != -1):
        return dp[ind][amount]
    notake = 0 + min_coin_need(ind-1,coins,amount,dp)
    take=sys.maxsize
    if(amount >= coins[ind]):
        take = 1 + min_coin_need(ind,coins,amount-coins[ind],dp)
    dp[ind][amount]=min(notake,take)
    return dp[ind][amount]
    
coins=[1,2,5]
amount=11
n=len(coins)
dp=[[-1 for i in range(amount+1)]for j in range(n)]
ans = min_coin_need(n-1,coins,amount,dp)
if ans>=sys.maxsize:
    print(-1)
else:
    print(ans)



#------------------------------------
#       Tabulation Method
#------------------------------------

coins=[1,2,5]
amount=11
n=len(coins)

dp=[[-1 for i in range(amount+1)]for j in range(n)]

for i in range(amount+1):
    if(i%coins[0] == 0):
        dp[0][i] = i//coins[0]
    else:
        dp[0][i] = sys.maxsize

for i in range(1,n):
    for j in range(amount+1):
        notake = 0+dp[i-1][j]
        take = sys.maxsize
        if(j >= coins[i]):
            take = 1 + dp[i][j-coins[i]]
        dp[i][j]=min(notake,take)
print(dp[n-1][amount])
