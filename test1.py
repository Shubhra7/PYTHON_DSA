def solve(n,e,d):
    if(e==0 or d==0):
        return 0
    if(n==0):
        return -1
    if(n*6 < e*7):
        return -1
    if(d<7):
        ans = ((e*d)//n) + ((e*d)%n != 0)
        return ans
    weeks = d//7
    ans = ((weeks*e*7)//n) + ((weeks*e*7)%n != 0)
    left = (ans*n) - (weeks*7*e)
    left_days = d%7
    req = (left_days*e)-left
    ans += (req//n) + (req%n !=0)
    return ans


# n=5
# e=2
# d=10

n=12
e=11
d=7

print(solve(n,e,d))