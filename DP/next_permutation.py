# link: https://leetcode.com/problems/next-permutation/description/

# video: https://youtu.be/JDOXKqF60RQ?si=IvTAEKKvV5or2LvY

"""
For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] 
because [3,2,1] does not have a lexicographical larger rearrangement.
"""

def find_nextpermutation(arr):
    n=len(arr)
    pivot=-1
    for i in range(n-2,-1,-1):
        if(arr[i]<arr[i+1]):
            pivot=i
            break
    if(pivot == -1):
        arr.reverse()
        return
    for i in range(n-1,pivot,-1):
        if(arr[pivot] < arr[i]):
            arr[pivot],arr[i] = arr[i],arr[pivot]
            break
    left,right = pivot+1,n-1
    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left += 1
        right -= 1



# arr=[1,2,3]  #o/p [1, 3, 2]
# arr = [2,3,1] #o/p [3,1,2]
arr = [3,2,1] # o/p [1,2,3] 

find_nextpermutation(arr)
print(arr)