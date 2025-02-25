# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
# https://www.youtube.com/watch?v=F9c7LpRZWVQ

"""
Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""

import sys

def findMedianSortedArrays(nums1, nums2):
    n=len(nums1)
    m=len(nums2)
    if n>m:
        return findMedianSortedArrays(nums2,nums1)
    left_tot = (n+m+1)//2
    low,high = 0,n
    total_ele = n+m
    # Edge cases
    if n==0:
        if m%2==1:
            return float(nums2[m//2])
        else:
            val=m//2
            return (nums2[val]+nums2[val-1])/2
    if m==0:
        if n%2==1:
            return float(nums1[n//2])
        else:
            val=n//2
            return (nums1[val]+nums1[val-1])/2

    while low <= high:
        mid1 = low + (high-low)//2
        mid2 = left_tot-mid1
        l1,l2= -sys.maxsize, -sys.maxsize
        r1,r2 = sys.maxsize, sys.maxsize
        if mid1<n:
            r1=nums1[mid1]
        if mid1>0:
            l1=nums1[mid1-1]
        if mid2<m:
            r2=nums2[mid2]
        if mid2>0:
            l2=nums2[mid2-1]
        if l1<=r2 and l2<=r1:
            if total_ele%2==0:
                return (max(l1,l2)+min(r1,r2))/2
            else:
                return float(max(l1,l2))
        if l1>r2:
            high=mid1-1
        else:
            low=mid1+1
    # return -1

print(findMedianSortedArrays([1,2],[3,4]))   #2.5
print(findMedianSortedArrays([1,3],[2]))   #2
print(findMedianSortedArrays([1,2,3,4,6],[5]))   #2

    