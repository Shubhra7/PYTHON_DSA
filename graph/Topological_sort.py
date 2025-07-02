# https://www.geeksforgeeks.org/problems/topological-sort/1
# https://youtu.be/73sneFXuTEg?si=cZDu8c9V01OdV7Z5

"""
Input: V = 4, E = 3, edges[][] = [[3, 0], [1, 0], [2, 0]]
Explanation: The output true denotes that the order is valid. Few valid Topological orders for the given graph are:
[3, 2, 1, 0]
[1, 2, 3, 0]
[2, 3, 1, 0]
"""
######################################
# For dfs just this part:
#  https://youtu.be/ZUFQfFaU-8U?list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&t=309
######################################



class Solution:
    def topoSort(self, V, edges):
        # Code here
        ###########################
        #  USing DFS
        ############################
        def dfs(node,adj,ds,visit):
            visit[node]=1
            for it in adj[node]:
                if visit[it]==0:
                    dfs(it,adj,ds,visit)
            ds.append(node)

        adj=[[] for _ in range(V)]
        visit=[0]*V
        for u,v in edges:
            adj[u].append(v)
        ds=[]
        for i in range(V):
            if visit[i]==0:
                dfs(i,adj,ds,visit)
        ans=list(reversed(ds))
        return ans
         
V = 4
E = 3
edges= [[3, 0], [1, 0], [2, 0]]
obj=Solution()
print("Using dfs do topo: ", end=" ")
print(obj.topoSort(V,edges))

# First write the indegree
# whose indegree are 0 are pushed into the queue
# the go with queue and push in the answer the node and 
# reduce the indegeree of the connected nodes

from collections import deque
class Solution:
    def topoSort(self, V, edges):
        # Code here
        ###########################
        #  USing BFS (khan's Algo)
        ############################
        q=deque()
        indegree=[0]*V
        adj=[[] for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)
        for i in range(V):
            for subN in adj[i]:
                indegree[subN]+=1
        for i in range(V):
            if indegree[i]==0:
                q.append(i)
        tpoAns=[]
        while q:
            ele=q.popleft()
            tpoAns.append(ele)
            for subN in adj[ele]:
                indegree[subN]-=1
                if indegree[subN]==0:
                    q.append(subN)
        return tpoAns
    
V = 4
E = 3
edges= [[3, 0], [1, 0], [2, 0]]
obj=Solution()
print(obj.topoSort(V,edges))
            
        
        