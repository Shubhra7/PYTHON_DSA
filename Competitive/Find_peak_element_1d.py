# https://leetcode.com/problems/find-peak-element/description/
# Stiver video search

"""
A peak element is an element that is strictly greater than its neighbors.
Given a 0-indexed integer array nums, find a peak element, and return its index. 
If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is 
always considered to be strictly greater than a neighbor that is outside the array.
You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
"""


def bin_search(nums):
    if len(nums)==1:
        return 0
    if nums[0]>nums[1]: #when first one is peak
        return 0
    if nums[-1]>nums[-2]:  # when last one is peak
        return (len(nums)-1)
    low,high = 1,len(nums)-2    # avoid the two corner cases
    while low<=high:
        mid = low + (high-low)//2
        if nums[mid]>nums[mid+1] and nums[mid]>nums[mid-1]: #peak condition
            return mid
        elif nums[mid] < nums[mid+1]:
            low = mid + 1
        else:       # **** important beacuse when mid is smaller than both side then it need to do any one
            high = mid - 1
    return -1
def findPeakElement(nums):
    return bin_search(nums)
print(findPeakElement([1,2,1,3,5,6,4]))   #5
print(findPeakElement([1,2,3,1]))  #2
     