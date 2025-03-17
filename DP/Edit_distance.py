# https://youtu.be/fJaKO8FbDdo
"""
Given two strings word1 and word2, return the minimum number of operations 
required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
"""

#################################################
#     Tabulation method
#################################################
class Solution1:
    def minDistance1(self,word1,word2):
        def f(n,m):
            dp=[[0]*(m+1) for _ in range(n+1)]
            #for base case
            for i in range(n+1):
                dp[i][0]=i
            for j in range(m+1):
                dp[0][j]=j
            for i in range(1,n+1):
                for j in range(1,m+1):
                    if word1[i-1]==word2[j-1]:
                        dp[i][j]=dp[i-1][j-1]
                    else:
                        dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
            return dp[n][m]
        n,m=len(word1),len(word2)
        ans=f(n,m)
        return ans
        
 
#################################################
#     Recusrsion + memozitation
#################################################

# https://youtu.be/fJaKO8FbDdo
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def f(i,j,dp):
            if i==0:  #when word1 exhausted
                return j
            if j==0:  #when word2 exhausted
                return i
            if dp[i][j]!=-1:
                return dp[i][j]
            if word1[i-1]==word2[j-1]:
                dp[i][j]=f(i-1,j-1,dp)
                return dp[i][j]
            else:
                dp[i][j]= 1 + min(f(i-1,j,dp),f(i,j-1,dp),f(i-1,j-1,dp))
                #first for delete, insert, replace
                return dp[i][j]
        n,m=len(word1),len(word2)
        dp=[[-1]*(m+1) for _ in range(n+1)]
        ans=f(n,m,dp)
        return ans
        
obj=Solution()
print(obj.minDistance("horse","ros"))  #o/p==>3
obj1=Solution1()
print(obj1.minDistance1("horse","ros"))  #o/p==>3
print(obj1.minDistance1("intention","execution"))  #o/p==>5
