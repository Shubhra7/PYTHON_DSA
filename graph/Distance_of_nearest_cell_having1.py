# https://youtu.be/edXdVwkYHF8?si=f1p_WzThUFnT_ERZ
# https://www.geeksforgeeks.org/problems/distance-of-nearest-cell-having-1-1587115620/1

# Start from 1 then dfs and add the zero for their distance

"""
Input: 
grid = [[0,1,1,0], [1,1,0,0], [0,0,1,1]]
Output: 
[[1,0,0,1], [0,0,1,1], [1,1,0,0]]


Input: 
grid = [[1,0,1], [1,1,0], [1,0,0]]
Output: 
[[0,1,0], [0,0,1], [0,1,2]]
"""
from collections import deque
class Solution:
    def nearest(self,grid):
        q=deque()
        row,col= len(grid),len(grid[0])
        visit=[[0]*col for _ in range(row)]
        disit=[[0]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    q.append(((i,j),0))
                    visit[i][j]=1
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        while q:
            first,second = q.popleft()
            r,c = first[0],first[1]
            disit[r][c]=second
            for u,v in directions:
                newR,newC = r+u,c+v
                if newR in range(row) and newC in range(col) and grid[newR][newC]==0 and visit[newR][newC]==0:
                    visit[newR][newC]=1
                    q.append(((newR,newC),second+1))

        return disit


# grid = [[0,1,1,0], [1,1,0,0], [0,0,1,1]]
# #[[1, 0, 0, 1], [0, 0, 1, 1], [1, 1, 0, 0]] 

grid = [[1,0,1], [1,1,0], [1,0,0]]
# [[0,1,0], [0,0,1], [0,1,2]]
obj=Solution()
print(obj.nearest(grid))