# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
class Solution:
    def maxProfit(self, prices):
        pick=-prices[0]
        nopick=0
        for i in range(1,len(prices)):
            newPick=max(pick,nopick-prices[i])
            newNopick=max(nopick,pick+prices[i])
            pick,nopick=newPick,newNopick
        return max(pick,nopick)

obj=Solution()
print(obj.maxProfit([7,1,5,3,6,4]))  #O/P==>7