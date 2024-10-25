def solve(n,e,d):
    if(n==0):
        return -1
    if(e==0 or d==0):
        return 0
    if(d<7):
        if((d*e)%n == 0):
            return (d*e)//n
        else:
            return ((d*e)//n + 1)
    if((n*6) < (e*7)):
        return -1
    
    weeks = (d//7)
    ans=0
    ans += ((weeks*e*7)//n) + ((weeks*e*7)%n!=0)
    left = (ans*n) - (weeks*e*7)
    left_days = d%7
    req = (left_days*e) - left
    ans += (req//n) + (req%n!=0)
    return ans

n=5
e=2
d=10

print(solve(n,e,d))