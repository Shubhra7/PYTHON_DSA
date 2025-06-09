# https://www.youtube.com/watch?v=muncqlKJrH0&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=8
# https://leetcode.com/problems/number-of-islands/description/

"""
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

############################################
#               Using BFS
############################################

from collections import deque
class Solution:
    def numIslands(self, grid):
        visited=set()
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        def bfs(i,j):
            q=deque()
            visited.add((i,j))
            q.append((i,j))
            while q:
                ro,co=q.popleft()
                for m,n in directions:
                    newRo,newCo=ro+m,co+n
                    if newRo in range(row) and newCo in range(col) and grid[newRo][newCo]=='1' and (newRo,newCo) not in visited:
                        q.append((newRo,newCo))
                        visited.add((newRo,newCo))
        row=len(grid)
        col=len(grid[0])
        count=0
        for i in range(row):
            for j in range(col):
                if (i,j) not in visited and grid[i][j]=='1':
                    bfs(i,j)
                    count+=1
        return count

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

obj=Solution()
print(obj.numIslands(grid))


############################################
#               Using DFS
############################################

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])

        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]=='0':
                return
            
            grid[i][j]='0'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            return 1
        
        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    count+=dfs(i,j)
        
        # print(grid) // orginal data changed***
        return count

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

obj=Solution()
print(obj.numIslands(grid))
        
        