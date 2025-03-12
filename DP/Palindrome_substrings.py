# https://leetcode.com/problems/palindromic-substrings/description/
# https://youtu.be/J5P4OBhFKq0

"""
Example 1:
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"  #### Length 1 is approved so other wise o/p ==> 3
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
"""

class Solution:
    def expan(self,left,right,s):
        count=0
        while left>=0 and right<len(s) and s[left]==s[right]:
            count+=1 # when length 1 is approved
            # if right>left:   # when length is minimum 2
            #     count+=1
            left-=1
            right+=1
        return count
    def countSubstrings(self, s: str) -> int:
        ans=0
        for i in range(len(s)):
            even=self.expan(i,i+1,s)
            odd=self.expan(i,i,s)
            ans+=odd+even
        return ans

obj=Solution()
print(obj.countSubstrings("aaa"))  #o/p==>6 (when 1 lenght is approved) or ==> 3(minimum len is 2)
        