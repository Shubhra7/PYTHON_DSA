# https://leetcode.com/problems/jump-game-ii
# https://www.youtube.com/watch?v=7SBVnw7GSTk

"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, 
if you are at nums[i], you can jump to any nums[i + j] where:

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. 
Jump 1 step from index 0 to 1, then 3 steps to the last index.
"""

def jump(nums):
        jumps=0
        r,l=0,0
        n=len(nums)
        while r<n-1:
            farest=0
            for i in range(l,r+1):
                farest=max(farest,i+nums[i])
            l=r+1
            r=farest
            jumps+=1
        return jumps

nums=[2,3,1,1,4]  #o/p=2
print("Minimum jumps need: ",jump(nums))