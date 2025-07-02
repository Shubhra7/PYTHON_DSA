#User function Template for python3

from typing import List

# TopoSort + Relaxation 
# make the adjacent list
# Do topoSort for getting the sequence
# Then relaxation for distance
# If not reachable then make the dist for that node "-1"


class Solution:

    def shortestPath(self, V: int, E: int,
                     edges: List[List[int]]) -> List[int]:
        # TopoSort using DFS
        def dfs_topo(node,adj,visit,st):
            visit[node]=1
            for ele in adj[node]:
                if visit[ele[0]]==0:
                    dfs_topo(ele[0],adj,visit,st)
            st.append(node)
            
        adj=[[] for _ in range(V)]
        for u,v,wt in edges:
            adj[u].append([v,wt])
        
        # Do the toposort using DFS
        visit=[0]*V
        st=[]
        for i in range(V):
            if visit[i]==0:
                dfs_topo(i,adj,visit,st)
        
        # relaxation with help of toposort
        dist=[1e8]*V
        dist[0]=0
        while st:
            node=st.pop()
            for v,wt in adj[node]:
                if dist[v] > dist[node]+wt:
                    dist[v]=dist[node]+wt
        
        for i in range(V):  # Because it take only the not reachable node as "-1"
            if dist[i]==1e8:
                dist[i]=-1
        return dist
