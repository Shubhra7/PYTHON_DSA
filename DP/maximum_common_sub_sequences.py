# Link: https://youtu.be/NPZn9jBrX8U?si=fTiqRril12rzgJJU
# leecode: https://leetcode.com/problems/longest-common-subsequence/
# LCS: Largest Common Sequence

# i/p: adventure furue
# o/p: 3 (ure)


#-------------------------
# Optimal Methods
#-------------------------

def find_lcs(ind1,ind2,text1,text2):
        prev = [0 for i in range(ind2+1)]
        for i in range(1,ind1+1):
            cur=[0 for i in range(ind2+1)]
            for j in range(1,ind2+1):
                if(text1[i-1] == text2[j-1]):
                    cur[j] = prev[j-1] + 1
                else:
                    cur[j] = max(prev[j], cur[j-1])  # Crucial for sub sequences
            prev=cur
        return prev[ind2]
def longestCommonSubsequence(text1: str, text2: str):
    n,m = len(text1),len(text2)
    return find_lcs(n,m,text1,text2)


#-------------------------
# Recursion Methods
#-------------------------

def using_recursion(ind1,ind2,str1,str2,dp):
     if(ind1<1 or ind2<1):  # Base case (as we checked with -1 index so used 1)
          return 0
     if(str1[ind1-1]==str2[ind2-1]):
          dp[ind1][ind2] = 1 + using_recursion(ind1-1,ind2-1,str1,str2,dp)
          return dp[ind1][ind2]
     else:
          dp[ind1][ind2] = max(using_recursion(ind1-1,ind2,str1,str2,dp), using_recursion(ind1,ind2-1,str1,str2,dp))
          return dp[ind1][ind2]


word1,word2 = map(str,input().split())
print("Using the tabulation method maximum length of LCS :",longestCommonSubsequence(word1,word2))

recu = [[-1 for i in range(len(word2)+1)]for j in range(len(word1)+1)]
print("Using the tabulation method maximum length of LCS :",using_recursion(len(word1),len(word2),word1,word2,recu))