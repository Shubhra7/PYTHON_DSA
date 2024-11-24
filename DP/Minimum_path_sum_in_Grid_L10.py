# video: https://www.youtube.com/watch?v=_rgTlyky1uQ&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=11

# link: https://leetcode.com/problems/minimum-path-sum/

"""
Given a m x n grid filled with non-negative numbers, find a path from 
top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""

"""
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
"""
import sys

# grid = [[1,3,1],
#         [1,5,1],
#         [4,2,1]]

grid = [[1,2,3],[4,5,6]]

m=len(grid)
n=len(grid[0])


#-------------------------
# Using Recursion
#-------------------------

def find_minval_path(i,j,grid,dp):
    if(i==0 and j==0):
        return grid[i][j]
    elif(i<0 or j<0):
        return sys.maxsize
    elif(dp[i][j] != -1):
        return dp[i][j]
    else:
        up = grid[i][j] + find_minval_path(i-1,j,grid,dp)
        down = grid[i][j] + find_minval_path(i,j-1,grid,dp)
        dp[i][j] = min(up,down)
        return dp[i][j]

dp=[[-1 for i in range(n)] for j in range(m)]
print(find_minval_path(m-1,n-1,grid,dp))
