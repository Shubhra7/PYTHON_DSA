#********* Median in a row-wise sorted Matrix *********

### Striver video link: https://youtu.be/Q9wXgdxJq48

## Problem Statement:: https://www.naukri.com/code360/problems/median-of-a-row-wise-sorted-matrix_1115473

## 1) First take the lowest and highest element from the first element and last elements from subarrays
    # 2)calculate the req '<=' element by = (m*n)//2
    # 3)Then implement the binary search 
    # 4) use upperbound()
import sys
import bisect

def upperBound(mat,x,m):
    ans = bisect.bisect_right(mat,x)
    return ans

def countSmallEqual(mat,m,n,x):
    count = 0
    for i in range(m):
        count += upperBound(mat[i],x,m)
    return count

def median(mat,m,n):
    low = min([mat[i][0] for i in range(len(mat))])
    high = max([mat[i][n-1] for i in range(len(mat))])
    # print(low)
    # print(high)
    req = (m * n)//2
    # print(req)
    while (low <= high):
        mid = low + (high - low)//2
        smallEqual = countSmallEqual(mat,m,n,mid)
        # print("(",low," , " ,high, ")","==>",mid," : ",smallEqual)
        if(smallEqual <= req):
            low = mid + 1
        else:
            high = mid - 1
    return low



matrix = [ [ 1, 5, 7, 9, 11 ],
            [ 2, 3, 4, 8, 9 ],
            [ 4, 11, 14, 19, 20 ],
            [ 6, 10, 22, 99, 100 ],
            [ 7, 15, 17, 24, 28 ]   ]


print(median(matrix,len(matrix),len(matrix[0])))

