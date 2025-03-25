# https://youtu.be/ZmlQ3vgAOMo?t=1690

class Solution:
    ########################################
    # ----------- Recursion ----------------
    ########################################
    def isMatch(self,s,p):
        def f(i,j,dp):
            if i<0 and j<=0:
                return True
            if i<0 and j>=0:
                return False
            if i>=0 and j<0:
                for k in range(i+1):
                    if p[k]!='*': #** most tricky place
                        return False
                return True
            if dp[i][j]!=-1:
                return dp[i][j]
            if s[j]==p[i] or p[i]=='?':
                dp[i][j]=f(i-1,j-1)
                return dp[i][j]
            elif p[i]=='*':     #****** Bang on place
                dp[i][j] = f(i-1,j,dp) or f(i,j-1,dp)  #--** "*" act like Nothing or matches
                return dp[i][j]
            dp[i][j]=False
            return dp[i][j]
        n,m=len(p),len(s)
        dp=[[-1]*m for i in range(n)]
        return f(n-1,m-1,dp)
    ########################################
    # ----------- Tabulation method ----------------
    ########################################
    def isMatch1(self,s,p):
        m,n=len(s),len(p)
        dp=[[False]*(m+1) for _ in range(n+1)]
        dp[0][0]=True
        for j in range(1,m+1):
            dp[0][j]=False
        for i in range(1,n+1):
            flag=True
            for j in range(i+1):
                if p[j-1]!='*':
                    flag=False
                    break
            dp[i][0]=flag
        for i in range(1,n+1):
            for j in range(1,m+1):
                if p[i-1]==s[j-1] or p[i-1]=='?':
                    dp=dp[i-1][j-1]
                elif p[i-1]=='*':
                    dp[i][j]= dp[i-1][j] or dp[i][j-1]
                else:
                    dp[i][j]=False
        return dp[n][m]
    

obj=Solution()
print(obj.isMatch("abcdefhjo","**")) #o/p==>True
print(obj.isMatch1("abcdefhjo","**")) #o/p==>True
