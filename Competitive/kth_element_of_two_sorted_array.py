"""
Problem statement
You're given two sorted arrays 'arr1' and 'arr2' of size 'n' and 'm' respectively and an element 'k'.
Find the element that would be at the 'kth' position of the combined sorted array.
Position 'k' is given according to 1 - based indexing, but arrays 'arr1' and 'arr2' are using 0 - based indexing.

For example :
Input: 'arr1' = [2, 3, 45], 
'arr2' = [4, 6, 7, 8] and 'k' = 4

Output: 6

Explanation: The merged array will be 
[2, 3, 4, 6, 7, 8, 45]. The element at
 position '4' of this array is 6. Hence we return 6."""

import sys
def kth_element(arr1,n,arr2,m,k):
    if n>m:
        return kth_element(arr2,m,arr1,n,k)
    low = max(0,k-m)
    high = min(k,n)

    while low<=high:
        cut1 = low + (high-low)//2
        cut2 = k-cut1
        
        if cut1 == 0:
            l1 = -sys.maxsize
        else:
            l1 = arr1[cut1-1]
        if cut2 == 0:
            l2 = -sys.maxsize
        else:
            l2 = arr2[cut2-1]
        
        if cut1 == n:
            r1 = sys.maxsize
        else:
            r1 = arr1[cut1]
        if cut2 == m:
            r2 = sys.maxsize
        else:
            r2 = arr2[cut2]
        
        if l1<=r2 and l2<=r1:
            return max(l1,l2)
        elif l1 > r2:
            high = cut1-1
        else:
            low = cut1 +1
    return 1


arr1= [2,3,45]
arr2 = [4,6,7,8]
k=4  # o/p ==> 6
print(kth_element(arr1,len(arr1),arr2,len(arr2),k))