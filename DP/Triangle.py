# video: https://youtu.be/SrP-PiLSYC0?si=ipPbeQrB9Gx3hmft

# https://www.naukri.com/code360/problems/triangle_1229398?leftPanelTabValue=SUBMISSION
# https://leetcode.com/problems/triangle/description/

# Starting from down to top

"""
Given a triangle array, return the minimum path sum from top to bottom.
For each step, you may move to an adjacent number of the row below. 
More formally, if you are on index i on the current row, you may move 
to either index i or index i + 1 on the next row.

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11

Input: triangle = [[-10]]
Output: -10
"""


# --------------------------------
#   Recursion Method
#---------------------------------
def min_path_val(i,j,n,triangle,dp):
    if(i==n-1):
        return triangle[i][j]
    if(dp[i][j] != -1):
        return dp[i][j]
    down = triangle[i][j] + min_path_val(i+1,j,n,triangle,dp)
    dg = triangle[i][j] + min_path_val(i+1,j+1,n,triangle,dp)
    dp[i][j] = min(down,dg)
    return dp[i][j]

# triangle = [[2],
#             [3,4],
#             [6,5,7],
#             [4,1,8,3]]
## O/P ===> 11

# triangle = [[-10]]
# #o/p ===> -10

triangle = [[1],
            [2,3],
            [3,6,7],
            [8,9,6,10]]
# O/P ===> 14

n=len(triangle)
dp=[[-1 for i in range(n)] for j in range(n)]
print(min_path_val(0,0,n,triangle,dp))

