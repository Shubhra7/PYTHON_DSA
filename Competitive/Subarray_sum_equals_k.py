"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
Input: nums = [1,1,1], k = 2
Output: 2
"""
from collections import defaultdict
def subArraySumEquals_k(nums,k):
    ans=0
    d=defaultdict(int)   # has advantage, if not present give get value 0 by default
    d[0]=1
    prefixSum=0
    for num in nums:
        prefixSum += num
        ans += d[prefixSum-k]
        d[prefixSum] += 1
    return ans


nums=[1,1,1]
k=2
print(subArraySumEquals_k(nums,k))