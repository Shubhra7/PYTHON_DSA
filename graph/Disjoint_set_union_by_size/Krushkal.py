# https://youtu.be/DMnDM_sxVig?list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn
# https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1

# check the ulimate parent of the vertices
# then do the DisjoinSet union by size

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
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V: int, adj: List[List[int]]) -> int:
        #code here
        edges=[]
        for i in range(V):
            for adjNode,wt in adj[i]:
                edges.append([wt,i,adjNode])
        
        edges.sort(key= lambda x: x[0])
        mstWt = 0
        ds = DisjoinSet(V)
        
        for wt,u,v in edges:
            if ds.findUPar(u) != ds.findUPar(v):
                mstWt += wt
                ds.unionBySize(u,v)
                
        return mstWt

V=3
adj=[[[1, 5], [2, 1]], [[0, 5], [2, 3]], [[1, 3], [0, 1]]]
obj=Solution()
print(obj.spanningTree(V,adj))      #4