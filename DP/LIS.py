# https://youtu.be/on2hvxBXJH4?si=FOkgPQhqXtC281MJ
# https://leetcode.com/problems/longest-increasing-subsequence/
"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.
Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.'
"""

##############################################
#-------------Normal dp method with n^2 --------------
##############################################

class Solution1:
    def lengthOfLIS1(self, nums):
        dp=[1]*len(nums)
        maxi=1
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]>nums[j] and dp[j]+1>dp[i]:
                    dp[i]=dp[j]+1
            maxi=max(maxi,dp[i])
        return maxi
obj=Solution1()
print(obj.lengthOfLIS1([10,9,2,5,3,7,101,18]))

##############################################
#--------------- To make n*logn --------------
##############################################

import bisect
class Solution:
    def lengthOfLIS(self, nums):
        if len(nums)==0:
            return 0
        temp=[nums[0]]
        ans=1
        for i in range(1,len(nums)):
            if temp[-1]<nums[i]:
                temp.append(nums[i])
                ans+=1
            else:
                ind=bisect.bisect_left(temp,nums[i])
                temp[ind]=nums[i]
        return ans
obj=Solution()
print(obj.lengthOfLIS([10,9,2,5,3,7,101,18]))

        