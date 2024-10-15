class Solution:
    def maxProfit(self, prices) -> int:
        ans=0
        mini=prices[0]
        for i in range(1,len(prices)):
            if(ans < (prices[i] - mini)):
                ans = prices[i]-mini
            if(mini > prices[i]):
                mini = prices[i]
        return ans 
        
obj = Solution()
print(obj.maxProfit([7,1,5,3,6,4]))