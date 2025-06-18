#User function Template for python3

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
                print(newR," ",newC," ")
                if newR in range(rows) and newC in range(cols) and visit[newR][newC]==0 and grid[newR][newC]==1:
                    print("hi")
                    dfs(newR,newC,visit,grid,ds,rowB,colB)
                    print(ds)
                    
        
        ans=set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1 and visit[i][j]==0:
                    print("Hello: ",i," ",j)
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
print(obj.countDistinctIslands(grid))
                    
                    