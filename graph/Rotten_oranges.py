# https://leetcode.com/problems/rotting-oranges/

"""
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
"""
import collections
class Solution:
    def orangesRotting(self, grid):
        row=len(grid)
        col=len(grid[0])

        q=collections.deque()
        fresh=0
        direction=[[1,0],[-1,0],[0,1],[0,-1]]

        for i in range(row):
            for j in range(col):
                if (grid[i][j]==2):
                    q.append((i,j,0))
                if (grid[i][j]==1):
                    fresh+=1

        ans=0
        while q:
            r,c,time = q.popleft()
            for i,j in direction:
                rows = r + i
                cols= c + j
                if(rows in range(row) and cols in range(col)
                    and grid[rows][cols]==1):
                    grid[rows][cols]=2
                    q.append((rows,cols,time+1))
                    fresh-=1
                    ans=max(ans,time+1)

        if (fresh==0):
            return ans
        else:
            return -1
                
obj=Solution()
# grid = [[2,1,1],[0,1,1],[1,0,1]] #-1
grid = [[2,1,1],[1,1,0],[0,1,1]]  #4
print(obj.orangesRotting(grid))