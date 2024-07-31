# Problem statement
# You are given an array 'arr' of length 'n', consisting of integers.
# A subarray is a contiguous segment of an array. In other words, a subarray can be formed by removing 0 or more integers from the beginning and 0 or more integers from the end of an array.

# Find the sum of the subarray (including empty subarray) having maximum sum among all subarrays.

# The sum of an empty subarray is 0.

# Example :
# Input: 'arr' = [1, 2, 7, -4, 3, 2, -10, 9, 1]

# Output: 11

# Explanation: The subarray yielding the maximum sum is [1, 2, 7, -4, 3, 2].
# https://www.naukri.com/code360/problems/maximum-subarray-sum_630526?interviewProblemRedirection=true&leftPanelTabValue=PROBLEM&count=25&page=1&search=&sort_entity=order&sort_order=ASC
# https://youtu.be/GrNSGC8Z2T0?t=468


## **** Kadane's algorithm ****

def maxSubarraySum(arr, n) :
	# Your code here
    # return the answer
    curr_max=arr[0]
    ans=arr[0]
    for i in range(1,len(arr)):
        curr_max=max(arr[i],arr[i]+curr_max)
        ans=max(ans, curr_max)
    if (ans >0):
        return ans
    else:
        return 0
	

arr=[5,4,-1,7,8]
print(maxSubarraySum(arr,10))