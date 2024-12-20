"""
A peak element in a 2D grid is an element that is strictly greater than 
all of its adjacent neighbors to the left, right, top, and bottom.

Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, 
find any peak element mat[i][j] and return the length 2 array [i,j].

You may assume that the entire matrix is surrounded by an outer perimeter 
with the value -1 in each cell.
You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.

Input: mat = [[1,4],[3,2]]
Output: [0,1]
Explanation: Both 3 and 4 are peak elements 
so [1,0] and [0,1] are both acceptable answers.
"""

#--------------------------
# leetcode  #check vertical element
#-------------------------

def findPeakGrid1(mat):
    rows,cols = len(mat),len(mat[0])
    low, high = 0,rows-1

    while low<high:
        mid=low + (high-low)//2
        if(max(mat[low]) > max(mat[mid])):
            mid = high
        else:
            low = mid + 1
    return [low,mat[low].index(max(mat[low]))]
    

print(findPeakGrid1([[1,4],[3,2]]))




#-----------------------------------------
# Striver video     #check horizontal element
#---------------------------------------
def find_max_row(mat,rows,mid):
    maxi=-1
    ind=-1
    for i in range(rows):
        if maxi < mat[i][mid]:
            maxi = mat[i][mid]
            ind = i
    return ind
def find_peak(mat,rows,cols):
    low = 0
    high = cols-1
    while low<=high:
        mid = low + (high-low)//2
        maxirow = find_max_row(mat,rows,mid)
        if mid-1>=0:
            left = mat[maxirow][mid-1]
        else:
            left = -1
        if mid+1<cols:
            right = mat[maxirow][mid+1]
        else:
            right = -1
        if left < mat[maxirow][mid] and right < mat[maxirow][mid]:
            return [maxirow,mid]
        elif left>mat[maxirow][mid]:
            high = mid - 1
        else:
            low = mid + 1
    return [-1,-1]
def findPeakGrid(mat):
    rows,cols = len(mat),len(mat[0])
    return find_peak(mat,rows,cols)

print(findPeakGrid([[1,4],[3,2]]))