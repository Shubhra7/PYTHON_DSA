# https://youtu.be/fJaKO8FbDdo
class Solution:
    def change(self, amount, coins):
        n=len(coins)
        dp=[[0]*(amount+1) for _ in range(n)]
        for i in range(amount+1):
            if i%coins[0] == 0:
                dp[0][i]=1
        for i in range(1,n):
            for j in range(amount+1):
                notake=dp[i-1][j]
                take=0
                if j>=coins[i]:
                    take=dp[i][j-coins[i]]
                dp[i][j]=notake+take
        for i in dp:
            print(i)
        return dp[n-1][amount]


obj=Solution()
print(obj.change(5,[2,5]))