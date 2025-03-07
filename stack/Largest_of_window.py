# https://leetcode.com/problems/sliding-window-maximum/
# Striver video

from collections import deque
class Solution:
    def maxOfSubarrays(self, nums, k):
        res=[]
        stack=deque()
        for i in range(len(nums)):
            while stack and nums[stack[-1]]<nums[i]:    #stack will only take higher 
                stack.pop()
            stack.append(i)
            if i-stack[0]>=k:   # size maintain and correct sequence maintain
                stack.popleft()
            if stack and i>=k-1:    #taking answer time
                res.append(nums[stack[0]])
        return res
                
obj=Solution()
print(obj.maxOfSubarrays([33,38,46,24,26,6,42,28],2))