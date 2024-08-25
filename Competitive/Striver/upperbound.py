# Problem statement
# You are given a sorted array ‘arr’ containing ‘n’ integers and an integer ‘x’.Implement the 
# ‘upper bound’ function to find the index of the upper bound of 'x' in the array.

# Note:
# 1. The upper bound in a sorted array is the index of the first value that is greater than a given value. 
# 2. If the greater value does not exist then the answer is 'n', Where 'n' is the size of the array.
# 3. Try to write a solution that runs in log(n) time complexity.


# Example:

# Input : ‘arr’ = {2,4,6,7} and ‘x’ = 5,

# Output: 2

# Explanation: The upper bound of 5 is 6 in the given array, which is at index 2 (0-indexed).

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

import bisect

arr=[1, 4, 7, 7,7,8, 10]
n=7
low=0
high=len(arr)
ans=high
while (low<=high):
    mid = low + (high - low)//2
    if (arr[mid] > n):   # > will be >= in lowerbound search
        ans=mid
        high = mid -1
    else:
        low = mid +1
print(ans)