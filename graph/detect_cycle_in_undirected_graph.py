# https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
# https://youtu.be/BPlrALf1LDU?si=rqHUNtfpCMn6n4ZT


# Input: V = 4, E = 4, edges[][] = [[0, 1], [0, 2], [1, 2], [2, 3]]
# Output: true

# Input: V = 4, E = 3, edges[][] = [[0, 1], [1, 2], [2, 3]]
# Output: false

########################
#  Using BFS
######################

from collections import * 
class Solu:
    def isCycle(self,V,edges):
        visit=[False]*V
        adj=[[] for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def check(i):
            q=deque()
            q.append((i,-1))
            visit[i]=True
            while q:
                val=q.popleft()
                node, parent = val[0],val[1]
                for adjNd in adj[node]:
                    if not visit[adjNd]:
                        visit[adjNd]=True
                        q.append((adjNd,node))
                    elif adjNd!=parent:
                        return True
            return False


        for i in range(V):
            if not visit[i]:
                if check(i):
                    return True
        return False

# V = 4 
# E = 4
# edges= [[0, 1], [0, 2], [1, 2], [2, 3]] #True
V = 4
E = 3
edges= [[0, 1], [1, 2], [2, 3]] #False
obj=Solu()
print(obj.isCycle(V,edges))


########################
#  Using DFS
######################

from collections import *
class Solu:
    def isCycle(self,V,edges):
        adj=[[] for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visit=[False]*V
        def check(node,parent):
            visit[node]=True
            for adjNd in adj[node]:
                if not visit[adjNd]:
                    return check(adjNd,node)
                elif adjNd!=parent:
                    return True
            return False
        for i in range(V):
            if not visit[i]:
                if check(i,-1):
                    return True
        return False

V = 4 
E = 4
edges= [[0, 1], [0, 2], [1, 2], [2, 3]] #True
# V = 4
# E = 3
# edges= [[0, 1], [1, 2], [2, 3]] #False
obj=Solu()
print("Using dfs: ",end=" ")
print(obj.isCycle(V,edges))
