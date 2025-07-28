# https://www.geeksforgeeks.org/problems/number-of-islands/1

# https://youtu.be/Rn6B-Q4SNyA?list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn

#all individual code my r*cols + c
#the DSU for connected or not
#then ans count

from typing import List
class DisjoinSet:
    def __init__(self,V):
        self.size=[1 for _ in range(V+1)]
        self.parent=[i for i in range(V+1)]
        
    def findUPar(self,u):
        if self.parent[u]==u:
            return u
        self.parent[u]=self.findUPar(self.parent[u])
        return self.parent[u]
        
    def unionBySize(self,u,v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_v == ulp_u:
            return
        if self.size[ulp_u] > self.size[ulp_v]:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_u] += self.size[ulp_v]
            
class Solution:
    def numOfIslands(self, rows: int, cols : int, operators : List[List[int]]) -> List[int]:
        # code here
        visit=[[0]*cols for _ in range(rows)]
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        ds=DisjoinSet(rows*cols)
        cnt=0
        ans=[]
        for r,c in operators:
            if visit[r][c] == 1:
                ans.append(cnt)
                continue
            cnt+=1
            visit[r][c]=1
            for u,v in directions:
                newR,newC = r+u,c+v
                if newR in range(rows) and newC in range(cols):
                    if visit[newR][newC]==1:
                        nodeNo = r*cols + c #formula for idvidual node
                        adjNo = newR*cols + newC
                        if ds.findUPar(nodeNo) != ds.findUPar(adjNo):
                            cnt -= 1
                            ds.unionBySize(nodeNo,adjNo)
            ans.append(cnt)
        return ans
            
            