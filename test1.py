def solve(n,e,d):
    if(n==0):
        return -1
    if(e==0 or d==0):
        return 0
    if((e*7) > (n*6)):
        return -1
    if(d <7):
        val = d*e
        return (val//n +(val%n !=0))
    
    week = d//7 
    need = week*7*e
    pur_count = (need//n) + (need%n != 0)
    left = (pur_count*n) - need
    left_days = d%7
    req = (left_days*e) - left

    pur_count += (req//n) + (req%n != 0)

    return pur_count



n=5
e=2
d=10
print(solve(n,e,d))