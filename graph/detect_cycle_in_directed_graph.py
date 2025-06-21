# https://youtu.be/9twcmtQj4DU?si=aetTdzNBjIZthB9y
# https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1

# if same occurance detect in same path then only cycle occured
# modified version of normal cycle detection of undirected graph

################################
#   Using two array: visit, pathVisited
################################

class Solution:
    def isCycle(self, V, edges):
        # code here
        def dfs(node,adj,visit,pathVis):
            visit[node]=1
            pathVis[node]=1
            for adjN in adj[node]:
                if visit[adjN]==0:
                    if dfs(adjN,adj,visit,pathVis):
                        return True
                elif pathVis[adjN]==1:
                    return True
            pathVis[node]=0
            return False
        adj=[[] for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)
        visit=[0]*V
        pathVis=[0]*V
        for i in range(V):
            if(visit[i]==0):
                if(dfs(i,adj,visit,pathVis)):
                    return True
        return False

V = 4
# edges =[[0, 1], [0, 2], [1, 2], [2, 0], [2, 3]]   #True
edges= [[0, 1], [0, 2], [1, 2], [2, 3]]  #False
obj=Solution()
print("Cycle detection check: ",end=" ")
print(obj.isCycle(V,edges))    

################################
#   Using Single array: visit (1), pathVisited (2)
################################

class Solution:
    def isCycle(self, V, edges):
        # code here
        def dfs(node,adj,visit):
            visit[node]=2
            for adjN in adj[node]:
                if visit[adjN]==0:
                    if dfs(adjN,adj,visit):
                        return True
                elif visit[adjN]==2:
                    return True
            visit[node]=1
            return False
            
        adj=[[] for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)
            
        visit=[0]*V
        for i in range(V):
            if(visit[i]==0):
                if(dfs(i,adj,visit)):
                    return True
        return False

V = 4
# edges =[[0, 1], [0, 2], [1, 2], [2, 0], [2, 3]]   #True
edges= [[0, 1], [0, 2], [1, 2], [2, 3]]  #False
obj=Solution()
print("Cycle detection check: ",end=" ")
print(obj.isCycle(V,edges))   