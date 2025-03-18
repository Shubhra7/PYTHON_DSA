import sys

########################################
#       Recursion + memo
########################################
class Solution:
    def knapsack(self,maxiW,val,wt):
        def f(ind,maxiW,dp):
            if ind==0:
                if maxiW>=wt[0]:
                    return val[0]
                return 0
            if dp[ind][maxiW]!=-1:
                return dp[ind][maxiW]
            notake=0+f(ind-1,maxiW,dp)
            take=-sys.maxsize
            if wt[ind]<=maxiW:
                take=val[ind]+f(ind-1,maxiW-wt[ind],dp)
            return max(take,notake)
        n=len(wt)
        dp=[[-1]*(maxiW+1) for _ in range(n)]
        ans=f(n-1,maxiW,dp)
        return ans
        

# maxiW=4
# val=[1,2,3]  #o/p==>3
# wt=[4,5,1]

maxiW=3
val=[1,2,3]   #o/p==>0
wt=[4,5,6]
obj=Solution()
print(obj.knapsack(maxiW,val,wt))