# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
class Solution:
    def maxProfit(self, prices):
        mini=prices[0]
        maxi=0
        for i in range(len(prices)):
            maxi=max(maxi,prices[i]-mini)
            mini=min(mini,prices[i])
        return maxi
        
obj=Solution()
print(obj.maxProfit([7,1,5,3,6,4]))  #O/P =>5