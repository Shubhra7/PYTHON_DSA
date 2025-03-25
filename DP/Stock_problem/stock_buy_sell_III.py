# When only two transaction are allowed 
from sys import *
class Solution:
    def maxProfit(self, prices):
        buy1,buy2,sell1,sell2 = maxsize,maxsize,0,0
        pick1,pick2,notpick1,notpick2=-maxsize,-maxsize,0,0

        for p in prices:
            pick1=max(pick1,-p) #only -p very important thing**
            notpick1=max(notpick1,pick1+p)
            pick2=max(pick2,notpick1-p)
            notpick2=max(notpick2,pick2+p)
        return notpick2

        # for p in prices:
        #     buy1=min(buy1,p)
        #     sell1=max(sell1,p-buy1)
        #     buy2=min(buy2,p-sell1)
        #     sell2=max(sell2,p-buy2)
        # return sell2

        #**************** Recusrsion 
        # def f(ind,buy,cap,dp):
        #     if ind==len(prices) or cap==0:
        #         return 0
        #     if dp[ind][buy][cap]!=-1:
        #         return dp[ind][buy][cap]
        #     if buy==1:
        #         dp[ind][buy][cap]=max(-prices[ind]+f(ind+1,0,cap,dp),0+f(ind+1,1,cap,dp))
        #         return dp[ind][buy][cap]
        #     else:
        #         dp[ind][buy][cap]=max(prices[ind]+f(ind+1,1,cap-1,dp),0+f(ind+1,0,cap,dp))
        #         return dp[ind][buy][cap]
        # dp=[[[-1]*(3) for _ in range(2)]for _ in range(len(prices))]
        # ans=f(0,1,2,dp)
        # return ans


        # ************** Tabulation method
        # dp=[[[0]*3 for _ in range(2)]for _ in range(len(prices)+1)]
        # n=len(prices)
        # for ind in range(n-1,-1,-1):
        #     for buy in range(0,2):
        #         for cap in range(1,3):
        #             if buy==1:
        #                 dp[ind][buy][cap]=max(-prices[ind]+dp[ind+1][0][cap], 0+dp[ind+1][1][cap] )
        #             else:
        #                 dp[ind][buy][cap]=max(prices[ind]+dp[ind+1][1][cap-1], 0+dp[ind+1][0][cap])
        # return dp[0][1][2]

obj=Solution()
print(obj.maxProfit([3,3,5,0,0,3,1,4]))    
