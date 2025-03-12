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
    ans=0
    while left>=0 and right<len(s) and s[left]==s[right]:
        if right>left:
            ans+=1
        left-=1
        right+=1
        # ans+=1
    return ans
    # if ans>1:
    #     print("hi")
    #     print(s[left+1:right])
    #     return ans
    # return 0
# s="abc"
s="aaa"
# s="aacabdkacaa"
res=0
for i in range(len(s)):
    odd=expan(i,i,s)
    even=expan(i,i+1,s)
    res+=odd+even
    # res=max(res,expan(i,i,s),expan(i,i+1,s),key=len)
print(res)

# class Solution:
#     def expan(self,left,right,s):
#         count=0
#         while left>=0 and right<len(s) and s[left]==s[right]:
#             left-=1
#             right+=1
#             count+=1
#         return count
#     def countSubstrings(self, s: str) -> int:
#         ans=0
#         for i in range(len(s)):
#             even=self.expan(i,i,s)
#             odd=self.expan(i,i+1,s)
#             ans+=even+odd
#         return ans
# obj=Solution()
# print(obj.countSubstrings("aaa"))