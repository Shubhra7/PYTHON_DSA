# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# video link: https://youtu.be/XdbPH2tfXF4?t=1190&si=DnZSpyK62eHm92yi

def max_profit(price):
    onestock = -price[0]
    noshare = 0
    for i in range(1,len(price)):
        print(onestock," ", noshare)
        onestock = max(noshare - price[i], onestock)
        noshare = max(onestock + price[i], noshare)
    print(onestock," ", noshare)
    return noshare

price = [7,1,5,3,6,4]
print("The maximum profit will be: ",max_profit(price))