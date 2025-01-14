# https://www.naukri.com/code360/problems/count-subarrays-with-given-xor_1115652
"""
Given an array of integers ‘ARR’ 
and an integer ‘X’, you are supposed to find the number of
 subarrays of 'ARR' which have bitwise XOR of the elements
equal to 'X'.
"""
def total_subarray_xor_equals(arr,tar):
    cnt=0
    h={0:1}
    xr=0
    for i in range(len(arr)):
        xr ^= arr[i]
        cnt += h.get(xr^tar,0)
        h[xr] = h.get(xr,0)+1
    return cnt

arr=[5,3,8,3,10]
tar=8  # o/p=2
print(total_subarray_xor_equals(arr,tar))
print(total_subarray_xor_equals([5,2,9],7))