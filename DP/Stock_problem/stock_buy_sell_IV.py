"""
Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
"""

class Solution:
    def maxProfit(self, k: int, prices):
        buy=[-float('inf')]*(k+1)
        sell=[0]*(k+1)
        for p in prices:
            for i in range(1,k+1):
                buy[i]=max(buy[i],sell[i-1]-p)
                sell[i]=max(sell[i],buy[i]+p)
        return sell[k]
obj=Solution()
print(obj.maxProfit(2,[2,4,1])) #o/p=>2