
# *** DO the reverse and Same like LCS(Longest Common Subsequences) ***

# Example 1:

# Input: s = "zzazz"
# Output: 0
# Explanation: The string "zzazz" is already palindrome we do not need any insertions.
# Example 2:

# Input: s = "mbadm"
# Output: 2
# Explanation: String can be "mbdadbm" or "mdbabdm".
# Example 3:

# Input: s = "leetcode"
# Output: 5
# Explanation: Inserting 5 characters the string becomes "leetcodocteel".

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
    long_lcs_palin = find_long_lcs(s,s1)
    return (len(s) - long_lcs_palin)

print(longestPalindromeSubseq("leetcode"))  # Output: 5
print(longestPalindromeSubseq("mbadm"))  # Output: 2
