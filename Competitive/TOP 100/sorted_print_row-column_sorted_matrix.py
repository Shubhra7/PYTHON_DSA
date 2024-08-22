# https://prepinsta.com/java-program/print-elements-in-sorted-order-using-row-column-wise-sorted-matrix/

# Treated Like Min heap
# The grid[0][0] like root and taking this
# Rest will adjust according to property 

import sys

maxi = sys.maxsize

def youngify(grid, i, j):
    if( (i+1) in range(len(grid))):
        downVal = grid[i+1][j]
    else:
        downVal = maxi
    if (j+1) in range(len(grid[0])):
        rightVal = grid[i][j+1]
    else:
        rightVal = maxi
    
    if (downVal == maxi and rightVal == maxi):
        return

    if (downVal < rightVal):
        grid[i][j] = downVal
        grid[i+1][j] = maxi
        youngify(grid, i+1, j)
    else:
        grid[i][j] = rightVal
        grid[i][j+1] = maxi
        youngify(grid, i, j+1)

def extractMin(grid):
    res = grid[0][0]
    grid[0][0] = maxi
    youngify(grid, 0, 0)
    return res


def printSorted(grid):
    row= len(grid)
    col = len(grid[0])
    for i in range(row * col):
        print(extractMin(grid),end=" ")

grid = [[10, 20, 30, 40],
        [15, 25, 35, 45],
        [27, 29, 37, 48],
        [32, 33, 39, 50]]

printSorted(grid)