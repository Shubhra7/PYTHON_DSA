# https://www.naukri.com/code360/problems/count-inversions_615
# https://www.youtube.com/watch?v=AseUmwVNaoY


"""
Problem statement
For a given integer array/list 'ARR' of size 'N' containing all distinct values, find the total number of 'Inversions' that may exist.

An inversion is defined for a pair of integers in the array/list when the following two conditions are met.

A pair ('ARR[i]', 'ARR[j]') is said to be an inversion when:

1. 'ARR[i] > 'ARR[j]' 
2. 'i' < 'j'

Sample Input 1 :
3
3 2 1
Sample Output 1 :
3
Explanation of Sample Output 1:
We have a total of 3 pairs which satisfy the condition of inversion. (3, 2), (2, 1) and (3, 1).
"""

def merge(arr,low,mid,high):
    left,right = low,mid+1
    b=[]
    cnt=0
    while left<= mid and right<=high:
        if arr[left] <= arr[right]:
            b.append(arr[left])
            left +=1
        else:
            b.append(arr[right])
            cnt += mid - left + 1
            right += 1
    while left<=mid:
        b.append(arr[left])
        left += 1
    while right<=high:
        b.append(arr[right])
        right += 1
    for i in range(low,high+1):
        arr[i]=b[i-low]
    return cnt


def merge_sort(arr,low,high):
    cnt=0
    if low >= high:
        return cnt
    mid = low + (high-low)//2
    cnt += merge_sort(arr,low,mid)
    cnt += merge_sort(arr,mid+1,high)
    cnt += merge(arr,low,mid,high)
    return cnt
def getInversions(arr, n):
    # write your code here !!
    return merge_sort(arr,0,n-1)


print(getInversions([3,2,1],3))