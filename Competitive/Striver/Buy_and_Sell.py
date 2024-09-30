# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

def maxProfit(prices):
    mini = prices[0]
    profit = 0
    for i in range(0,len(prices)):
        cost = prices[i] - mini
        profit = max(profit, cost)
        mini = min(mini, prices[i])
    return profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))  #op=5

prices1 = [7,6,4,3,1]
print(maxProfit(prices1)) # op=0