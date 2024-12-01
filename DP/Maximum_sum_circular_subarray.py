# video : https://youtu.be/Q1TYVUEr-wY?si=0xR3Om4BqJq4W01Z
# link: https://leetcode.com/problems/maximum-product-subarray/description/

"""
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.
A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].
A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.
Example 1:

Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.
Example 2:

Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
Example 3:

Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.
"""
import sys

nums = [1,-2,3,-2]   #O/P ==>3

temp_maxSum , temp_minSum = 0,0
max_straight_sum = -sys.maxsize
min_straight_sum = sys.maxsize
arr_sum = 0

for i in range(len(nums)):
    arr_sum += nums[i]

    temp_maxSum += nums[i]
    max_straight_sum = max(max_straight_sum,temp_maxSum)
    if(temp_maxSum < 0):
        temp_maxSum = 0

    temp_minSum += nums[i]
    min_straight_sum = min(min_straight_sum,temp_minSum)
    if(temp_minSum > 0):
        temp_minSum = 0

# Condition for answer 
if(min_straight_sum == arr_sum):
    print(max_straight_sum)
else:
    ans = max(max_straight_sum, (arr_sum - min_straight_sum))
    print(ans)
