# https://www.naukri.com/code360/problems/k-th-element-of-2-sorted-array_1164159
# https://www.youtube.com/watch?v=D1oDwWCq50g
"""
Input: 'arr1' = [2, 3, 45], 'arr2' = [4, 6, 7, 8] and 'k' = 4
Output: 6
Explanation: The merged array will be [2, 3, 4, 6, 7, 8, 45]. 
The element at position '4' of this array is 6. Hence we return 6.
"""
import sys

def find_kth_element(nums1,nums2,k):
        n1,n2 = len(nums1),len(nums2)
        low = max(k-n2,0)
        high=min(k,n1)
        while low<=high:
            mid1 = low + (high-low)//2
            mid2 = k - mid1
            l1,l2 = -sys.maxsize,-sys.maxsize
            r1,r2 = sys.maxsize, sys.maxsize
            if mid1<n1:
                r1=nums1[mid1]
            if mid2<n2:
                r2=nums2[mid2]
            if mid1>0:
                l1 = nums1[mid1-1]
            if mid2>0:
                l2 = nums2[mid2-1]
            if l1<=r2 and l2<=r1:
                return max(l1,l2)
            if l1>r2:
                high = mid1-1
            else:
                low = mid1+1
        return -1

print(find_kth_element([2,3,45],[4,6,7,8],4))
"""
Input: 'arr1' = [2, 3, 45], 'arr2' = [4, 6, 7, 8] and 'k' = 4
Output: 6
"""