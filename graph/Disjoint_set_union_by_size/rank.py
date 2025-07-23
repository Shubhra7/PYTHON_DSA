# Disjoint Set Union (DSU) with Rank/Size: Use to efficiently manage and merge disjoint sets, especially in Kruskal’s MST or cycle detection in graphs.

class DisjointSet:
    def __init__(self,n):
        self.rank=[0 for _ in range(n+1)]
        self.parent=[i for i in range(n+1)]
        self.size=[1 for _ in range(n+1)]

    def findUPar(self,node):
        if node==self.parent[node]:
            return node
        self.parent[node] = self.findUPar(self.parent[node])  #Path compression
        return self.parent[node]

    # Union by Rank
    def unionByRank(self,u,v):
        ulp_u=self.findUPar(u)
        ulp_v=self.findUPar(v)
        if ulp_u == ulp_v:
            return
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u]=ulp_v
        elif self.rank[ulp_u] > self.rank[ulp_v]:
            self.parent[ulp_v]=ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1
    
    #Union by Size
    def unionBySize(self,u,v):
        ulp_u=self.findUPar(u)
        ulp_v=self.findUPar(v)
        if ulp_u == ulp_v:
            return
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u]=ulp_v
            self.size[ulp_v]= self.size[ulp_v] + self.size[ulp_u]
        else:
            self.parent[ulp_v]=ulp_u
            self.size[ulp_u] = self.size[ulp_v] + self.size[ulp_u]

ds = DisjointSet(7)

ds.unionByRank(1,2)
ds.unionByRank(2,3)
ds.unionByRank(4,5)
ds.unionByRank(6,7)
ds.unionByRank(5,6)

ds.unionBySize(1,2)
ds.unionBySize(2,3)
ds.unionBySize(4,5)
ds.unionBySize(6,7)
ds.unionBySize(5,6)

if ds.findUPar(3) == ds.findUPar(7):
    print("Same")
else:
    print("Not Same")

ds.unionByRank(3,7)
ds.unionBySize(3,7)

if ds.findUPar(3) == ds.findUPar(7):
    print("Same")
else:
    print("Not Same")

