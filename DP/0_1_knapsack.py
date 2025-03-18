import sys
class Solution:
    def knapsack(self,maxiW,val,wt):
        def f(ind,maxiW):
            if ind==0:
                if maxiW>=wt[0]:
                    return val[0]
                return 0
            notake=0+f(ind-1,maxiW)
            take=-sys.maxsize
            if wt[ind]<=maxiW:
                take=val[ind]+f(ind-1,maxiW-wt[ind])
            return max(take,notake)
        n=len(wt)
        ans=f(n-1,maxiW)
        return ans
        

maxiW=4
val=[1,2,3]  #o/p==>3
wt=[4,5,1]

# maxiW=3
# val=[1,2,3]   #o/p==>0
# wt=[4,5,6]
obj=Solution()
print(obj.knapsack(maxiW,val,wt))