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
# Space Optimization 
#-------------------------

cur=[0 for i in range(n)]   # only previous row

for i in range(m):
    temp = [0 for k in range(n)]    #only current row
    for j in range(n):
        if(i==0 and j==0):
            temp[j] = grid[i][j]
        else:
            up,left = sys.maxsize, sys.maxsize
            if(i>0):
                up = grid[i][j] + cur[j]
            if(j>0):
                left = grid[i][j] + temp[j-1]
            temp[j] = min(up,left) 
    cur=temp

print(cur[n-1])


#-------------------------
# Using Tabulation
#-------------------------

tabu = [[0 for i in range(n)] for j in range(m)]

for i in range(m):
    for j in range(n):
        if(i==0 and j==0):
            tabu[i][j] = grid[i][j]
        else:
            down,right = sys.maxsize,sys.maxsize
            if(i>0):
                down = grid[i][j] + tabu[i-1][j]
            if(j>0):
                right = grid[i][j] + tabu[i][j-1]
            tabu[i][j] = min(down,right)
print(tabu[m-1][n-1])
# for i in tabu:
#     print(i)


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
        left = grid[i][j] + find_minval_path(i,j-1,grid,dp)
        dp[i][j] = min(up,left)
        return dp[i][j]

dp=[[-1 for i in range(n)] for j in range(m)]
print(find_minval_path(m-1,n-1,grid,dp))
