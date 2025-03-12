# https://leetcode.com/problems/longest-palindromic-substring/description/

"""
Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

example 3:
"aacabdkacaa"
o/p==> 'aca'
"""

# Normal reverse and do LCS will not work, it only worked for subsequences
# Mancher Algorithm done
def expan(left,right,s):
    while left>=0 and right<len(s) and s[left]==s[right]:
        left-=1
        right+=1
    return s[left+1:right]

s="aacabdkacaa"
res=""
for i in range(len(s)):
    res=max(res,expan(i,i,s),expan(i,i+1,s),key=len)
print(res)