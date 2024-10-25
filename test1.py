def max_profit(price):
    pick = -price[0]
    nopick = 0
    for i in range(1,len(price)):
        newpick = max(pick, nopick-price[i])
        newnopick = max(nopick, pick + price[i])
        pick, nopick = newpick, newnopick
    return nopick

price = [7,1,5,3,6,4]
print("The maximum profit will be: ",max_profit(price))