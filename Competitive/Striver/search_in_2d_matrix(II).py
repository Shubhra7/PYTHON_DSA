# Link: https://youtu.be/9ZbB397jU4k
# Problem : https://leetcode.com/problems/search-a-2d-matrix-ii/description/

def bin_sear_2d_matrix(grid,target):
    row = len(grid)
    col = len(grid[0])
    i=0
    j=col-1
    while (i<row and j>=0):
        if(grid[i][j]==target):
            return (i,j)
        elif (grid[i][j] > target):
            j -= 1
        else:
            i += 1
    return False


grid = [[1,4,7,11,15],
        [2,5,8,12,19],
        [3,6,9,16,22],
        [10,13,14,17,24],
        [18,21,23,26,30]]


print(bin_sear_2d_matrix(grid,12))
