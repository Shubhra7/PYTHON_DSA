# https://youtu.be/MM7fXopgyjw
# https://www.geeksforgeeks.org/problems/boolean-parenthesization5610/1

class Solution:
    def f(self,i,j,isTrue,s,dp):
        if i>j:
            return 0
        if i==j:
            if isTrue==1:
                return int(s[i]=='T')
            else:
                return int(s[i]=='F')
        if dp[i][j][isTrue]!=-1:
            return dp[i][j][isTrue]
        ways=0
        for k in range(i+1,j,2):
            lT=self.f(i,k-1,1,s,dp)
            lF=self.f(i,k-1,0,s,dp)
            rF=self.f(k+1,j,0,s,dp)
            rT=self.f(k+1,j,1,s,dp)

            if s[k]=='|':
                if isTrue==1:
                    ways+= (lT*rF)+(lF*rT)+(lT*rT)
                else:
                    ways+= (lF*rF)
            elif s[k]=='&':
                if isTrue==1:
                    ways+= (lT*rT)
                else:
                    ways+= (lT*rF)+(lF*rT)+(lF*rF)
            else:
                if isTrue==1:
                    ways+= (lT*rF)+(lF*rT)
                else:
                    ways+= (lT*rT)+(lF*rF)
        dp[i][j][isTrue]=ways
        return ways

    def countWays(self,s):
        n=len(s)
        dp=[[[-1]*2 for _ in range(n)]for _ in range(n)]
        return self.f(0,n-1,1,s,dp)

obj=Solution()
print(obj.countWays("T|T&F^T"))
print(obj.countWays("T^F|F"))