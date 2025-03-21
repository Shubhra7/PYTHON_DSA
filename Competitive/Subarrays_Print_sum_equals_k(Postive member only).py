# https://www.naukri.com/code360/problems/subarray-with-given-sum_842487?leftPanelTabValue=PROBLEM

"""
ven an array arr[] containing only non-negative integers, your task is to find a continuous 
subarray (a contiguous sequence of elements) whose sum equals a specified value target. 
You need to return the 1-based indices of the leftmost and rightmost elements of this subarray.
 You need to find the first subarray whose sum is equal to the target.

Note: If no such array is possible then, return [-1].

Input: arr[] = [1, 2, 3, 7, 5], target = 12
Output: [2, 4]
Explanation: The sum of elements from 2nd to 4th position is 12.
"""

def subarraySum(arr, target):
    # code here
    start=0
    sum1=0
    for i in range(len(arr)):
        sum1 += arr[i]
        while sum1 > target and start < i:
            sum1 -= arr[start]
            start += 1
        if sum1 == target:
            return [start+1,i+1]
    return [-1]

print(subarraySum([1, 2, 3, 7, 5],12))  #o/p==> 2,4