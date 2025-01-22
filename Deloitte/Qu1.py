# Write a function that takes an array of integers and a positive integer k as arguments. 
# The function should return the maximum value of the minimum values of each subarray of length 
# k in the input array. For example, if the input array is [3, 1, 4, 6, 2, 5] and k is 3, then the
#  function should return 4, because the subarrays of length 3 are [3, 1, 4], [1, 4, 6], [4, 6, 2],
#  and [6, 2, 5], and the minimum values of these subarrays are 1, 1, 2, and 2, respectively, and the
#  maximum of these values is 4.
# https://youtu.be/e7AxCPzcBtg?t=199

def ans_min(arr,k):
    n=len(arr)
    res=[]
    for i in range(0,n-k+1):
        print(arr[i:i+k])
        val = min(arr[i:i+k])
        res.append(val)
    print(res)
    return max(res)


# arr=[3,1,4,6,2,5]
# k=3
arr=[1,2,3,4,5]
k=3
print(ans_min(arr,k))