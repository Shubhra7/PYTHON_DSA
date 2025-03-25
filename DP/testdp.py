class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def f(i,j,dp):
            if i<0 and j<0:
                return True
            if i<0 and j>=0:
                return False
            if i>=0 and j<0:
                for k in range(0,i+1):
                    if p[k]!='*':
                        return False
                return True
            if dp[i][j]!=-1:
                return dp[i][j]
            if p[i]==s[j] or p[i]=='?':
                dp[i][j]= f(i-1,j-1,dp) 
                return dp[i][j]
            if p[i]=='*':  #Main Trick place
                dp[i][j]=f(i-1,j,dp) or f(i,j-1,dp) #Either * like noting or any length 
                return dp[i][j]
            dp[i][j]= False
            return dp[i][j]
        n=len(p)
        m=len(s)
        dp=[[-1]*(m) for _ in range(n)]
        ans=f(n-1,m-1,dp)
        return ans
obj=Solution()
print(obj.isMatch("abcdefhjo","**"))