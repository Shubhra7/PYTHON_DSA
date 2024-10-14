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
    if(n*6)<(e*7):
        return -1
    print("hi")#
    ans=0
    if((d*e)%n == 0):
        ans = (d*e)//n
    else:
        ans = (d*e)//n + 1
   
    
    return ans
    

n=5
e=2
d=10

# n=12
# e=11
# d=7

print(solve(n,e,d))