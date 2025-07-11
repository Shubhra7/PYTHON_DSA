# https://www.geeksforgeeks.org/problems/shortest-path-in-a-binary-maze-1655453161/1
# https://youtu.be/M3_pLsDdeuU?list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn

#User function Template for python3

from typing import List
from collections import deque

class Solution:
    
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        # code here
        if source[0] == destination[0] and source[1]==destination[1]:
            return 0
        q=deque()
        row,col = len(grid), len(grid[0])
        dist= [[float('inf')]*col for _ in range(row)]
        dist[source[0]][source[1]]=0
        q.append((0,[source[0],source[1]]))
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        
        while q:
            dis,ele=q.popleft()
            r,c = ele[0], ele[1]
            for u,v in directions:
                newR,newC = r+u, c+v
                if newR in range(row) and newC in range(col) and grid[newR][newC]==1:
                    if dist[newR][newC] > dis+1:
                        dist[newR][newC]=dis+1
                        q.append((dis+1, [newR,newC]))
                        if newR == destination[0] and newC==destination[1]:
                            return dist[newR][newC]
        return -1
    
obj=Solution()
grid = [[1, 1, 1, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 1],
            [1, 1, 0, 0],
            [1, 0, 0, 1]]
source= [0, 1]
destination = [2, 2]
print("The Shortes path from source to destination is: ",end=" ")
print(obj.shortestPath(grid, source, destination))  # Output:3