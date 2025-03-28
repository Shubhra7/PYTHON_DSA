# video: https://www.youtube.com/watch?v=TmhpgXScLyY&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=10

# https://leetcode.com/problems/unique-paths-ii/description/

"""
You are given an m x n integer array grid. There is a robot initially located at the top-left corner 
(i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot 
include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The testcases are generated so that the answer will be less than or equal to 2 * 109.
"""

# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2

# obstacleGrid = [[0,1],[0,0]]
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right



#-----------------------------
# Using Recursion 
#-----------------------------

def find_uni_path(m,n,arr,dp):
    if(m>=0 and n>=0 and arr[m][n]==1): # for avoiding the obstacle
        return 0
    if(m<0 or n<0):
        return 0
    if(m==0 and n==0): # stating point
        return 1
    if(dp[m][n] != -1):  #Memorization
        return dp[m][n]
    up = find_uni_path(m-1,n,arr,dp)
    right = find_uni_path(m,n-1,arr,dp)
    dp[m][n]=up + right
    return dp[m][n]

obstacleGrid = [[0,0,0],
                [0,1,0],
                [0,0,0]]

# obstacleGrid = [[0,1],[0,0]]

m,n = len(obstacleGrid), len(obstacleGrid[0])
dp= [[-1 for i in range(n)] for j in range(m)]
print(find_uni_path(m-1,n-1,obstacleGrid,dp))


#-----------------------------
# Using Tabulation
#-----------------------------

dp=[[0 for i in range(n)] for j in range(m)]

for i in range(m):
    for j in range(n):
        if(i==0 and j==0):  # staring point
            dp[i][j]=1
        elif( i>=0 and j>=0 and obstacleGrid[i][j]==1):  # obstacle trackel
            dp[i][j]=0
        else:
            up,down = 0,0
            if(i>0):
                up = dp[i-1][j]
            if(j >0):
                down = dp[i][j-1]
            dp[i][j] = up+down
print(dp[m-1][n-1])