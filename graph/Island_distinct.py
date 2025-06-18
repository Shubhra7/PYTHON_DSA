# https://www.geeksforgeeks.org/problems/number-of-distinct-islands/1
# https://youtu.be/7zmgQSJghpo?si=YgEP8q7OkE3HVn6y

#Same like isLand problem
# but need to check the shape, so do use Base row and column
# put into set to make distinct the shapes

####################################################
#                Using BFS
####################################################

from collections import deque
class Solution:
    def countDistinctIslands(self, grid):
        # code here
        rows,cols = len(grid),len(grid[0])
        visit=[[0]*cols for _ in range(rows)]
        
        def bfs(row,col,visit,grid,ds,rowB,colB):
            q=deque()
            visit[row][col]=1
            directions=[[1,0],[-1,0],[0,1],[0,-1]]
            ds.append((row-rowB,col-colB))
            q.append((row,col))
            while q:
                first,second = q.popleft()
                for u,v in directions:
                    newR,newC = first+u,second+v
                    if newR in range(rows) and newC in range(cols) and grid[newR][newC]==1 and visit[newR][newC]==0:
                        q.append((newR,newC))
                        visit[newR][newC]=1
                        ds.append((newR-rowB,newC-colB))
            
        
        ans=set()
        for i in range(rows):
            for j in range(cols):
                if visit[i][j]==0 and grid[i][j]==1:
                    ds=[]
                    bfs(i,j,visit,grid,ds,i,j)
                    ans.add(tuple(ds))
        return len(ans)
grid = [[1, 1, 0, 1, 1],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [1, 1, 0, 1, 1]]
obj=Solution()
print("Using BFS: ",end=" ")
print(obj.countDistinctIslands(grid))



####################################################
#              Using DFS
####################################################


import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    def countDistinctIslands(self, grid):
        # code here
        rows,cols = len(grid),len(grid[0])
        visit=[[0]*cols for _ in range(rows)]
        
        def dfs(row,col,visit,grid,ds,rowB,colB):
            visit[row][col]=1
            ds.append((row-rowB,col-colB))
            directions=[[1,0],[-1,0],[0,1],[0,-1]]
            for u,v in directions:
                newR,newC = row+u,col+v
                if newR in range(rows) and newC in range(cols) and visit[newR][newC]==0 and grid[newR][newC]==1:
                    dfs(newR,newC,visit,grid,ds,rowB,colB)
        
        ans=set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1 and visit[i][j]==0:
                    ds=[]
                    dfs(i,j,visit,grid,ds,i,j)
                    ans.add(tuple(ds))
        print(ans)
        return len(ans)
    
grid = [[1, 1, 0, 1, 1],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [1, 1, 0, 1, 1]]
obj=Solution()
print("\n\nUsing DFS: ")
print(obj.countDistinctIslands(grid))
                    
                    