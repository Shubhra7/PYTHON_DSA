# https://leetcode.com/problems/contiguous-array/
# https://www.youtube.com/watch?v=1WugaISSWx8

"""
Given a binary array nums, return the maximum length 
of a contiguous subarray with an equal number of 0 and 1.

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray
 with an equal number of 0 and 1.
"""

def findMaxLength(nums):
    h={0:-1}
    ans=0
    sum=0
    for i in range(len(nums)):
        if nums[i]==0:
            sum -= 1
        elif nums[i]==1:
            sum +=1
        if sum in h:
            prevInd = h[sum]
            diff = i-prevInd
            ans = max(ans,diff)
        else:
            h[sum]=i
    return ans
print(findMaxLength([1, 0, 1, 1, 1, 0, 0]))
# o/p => 6