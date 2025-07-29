# https://www.geeksforgeeks.org/problems/making-a-large-island/1
# https://youtu.be/lgiz0Oup6gM?list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn

"""
Input: grid[] = [[1,0],[0,1]]
Output: 3
Explanation: Change any one 0 to 1 and connect two 1s, then we get an island with area = 3.
"""

#DO DSU will get seperated islands then
#DO check by making every 0 to 1

from typing import List
class DisjoinSet:
    def __init__(self,n):
        self.size=[1 for _ in range(n)]
        self.parent=[i for i in range(n)]
    def findUp(self,u):
        if self.parent[u]==u:
            return u
        self.parent[u]=self.findUp(self.parent[u])
        return self.parent[u]
    def unionBySize(self,u,v):
        ulp_u = self.findUp(u)
        ulp_v = self.findUp(v)
        if ulp_u == ulp_v:
            return
        if self.size[ulp_u] > self.size[ulp_v]:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]
        else:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        
class Solution:
    def largestIsland(self, grid : List[List[int]]) -> int:
        # Code here
        n=len(grid)
        ds=DisjoinSet(n*n)
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        ans=0
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    for u,v in directions:
                        newR,newC = i+u,j+v
                        if newR in range(n) and newC in range(n) and grid[newR][newC]==1:
                            nodeP = i*n + j
                            adjP = newR*n + newC
                            ds.unionBySize(nodeP,adjP)
        ans=max(ds.size)
        for i in range(n):
            for j in range(n):
                if grid[i][j]==0:
                    seen=set()
                    tot=0
                    for u,v in directions:
                        newR,newC = i+u,j+v
                        if newR in range(n) and newC in range(n) and grid[newR][newC]==1:
                            pos=newR*n + newC
                            pos_par = ds.findUp(pos)
                            if pos_par not in seen:
                                seen.add(pos_par)
                                tot += ds.size[pos_par]
                    ans = max(ans, tot+1)
        return ans

grid= [[1,0],[0,1]]
obj=Solution()
print(obj.largestIsland(grid))   # 3
                            
                        
                
        

