
# video: https://www.youtube.com/watch?v=6i_T5kkfv4A&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=29
# link: https://leetcode.com/problems/longest-palindromic-subsequence/description/

# Input: s = "bbbab"
# Output: 4
# Explanation: One possible longest palindromic subsequence is "bbbb".


# *** DO the reverse and Same like LCS(Longest Common Subsequences) ***

def find_long_lcs(word1,word2):
    n,m = len(word1),len(word2)
    prev = [0]*(m+1)
    for i in range(1,n+1):
        cur=[0]*(m+1)
        for j in range(1,m+1):
            if(word1[i-1] == word2[j-1]):
                cur[j] = prev[j-1] + 1
            else:
                cur[j] = max(prev[j],cur[j-1])
        prev = cur
    return prev[m]
                
def longestPalindromeSubseq(s: str) -> int:
    s1=s[::-1]
    return find_long_lcs(s,s1)

print(longestPalindromeSubseq("babad"))  # Output: 3
print(longestPalindromeSubseq("bbbab"))  # Output: 4
