def max_profit(price):
    pick=-price[0]
    nopick=0
    for i in range(1,len(price)):
        pick = max(pick, nopick-price[i])
        nopick = max(nopick, pick+price[i])
        print(pick," ",nopick)
    return nopick

price = [7,1,5,3,6,4]
print("The maximum profit will be: ",max_profit(price))