# https://youtu.be/oO5uLE7EUlM?t=765
# https://www.geeksforgeeks.org/problems/longest-consecutive-subsequence2449/1


"""
Given an array arr[] of non-negative integers. Find the length of the longest 
sub-sequence such that elements in the subsequence are consecutive integers,
 the consecutive numbers can be in any order.
"""

""""
Input: arr[] = [2, 6, 1, 9, 4, 5, 3]
Output: 6
Explanation: The consecutive numbers here 
are 1, 2, 3, 4, 5, 6. These 6 numbers form the longest consecutive subsquence.
"""

import sys
def longestConsecutive(arr):
        #code here
        arr.sort()
        if len(arr)==0:
            return 0
        n=len(arr)
        lastSmaller= -sys.maxsize
        cnt=0
        longest=1
        for i in range(n):
            if arr[i]-1 == lastSmaller:
                cnt += 1
                lastSmaller = arr[i]
            elif arr[i]!= lastSmaller:
                cnt = 1
                lastSmaller = arr[i]
            longest = max(longest,cnt)
        return longest

print(longestConsecutive([2, 6, 1, 9, 4, 5, 3]))  #op==>6