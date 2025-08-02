# https://www.geeksforgeeks.org/problems/articulation-point-1/1
# https://youtu.be/j1QDfU21iZk

#same with
# Strongly Connected Components ==> Kosaraju's Algorithm
#     1. Sort all the edges according to the finishing time.
#     2. Reverse the Graph.
#     3. Do the dfs.
# *****But difference****
# if low[it]>=tin[node] and parent!=-1:
# low[node] = min(low[node],tin[it])

import sys
sys.setrecursionlimit(10**6)

class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def articulationPoints(self, V, adj):
        def dfs(node,parent,tin,low,visit,adj,timer,mark):
            visit[node]=True
            tin[node]=timer
            low[node]=timer
            timer += 1
            child=0
            for it in adj[node]:
                if it==parent:
                    continue
                if not visit[it]:
                    dfs(it,node,tin,low,visit,adj,timer,mark)
                    low[node] = min(low[node],low[it])
                    if low[it]>=tin[node] and parent!=-1:
                        mark[node]=1
                    child += 1
                else:
                    low[node] = min(low[node],tin[it])

            if child>1 and parent==-1: # Edge case for parent node
                mark[node]=1
                
        # code here
        tin=[-1]*V
        low=[-1]*V
        visit = [False]*V
        mark=[0]*V
        for i in range(V):
            if not visit[i]:
                dfs(i,-1,tin,low,visit,adj,0,mark)
        ans=[]
        for i in range(V):
            if mark[i]==1:
                ans.append(i)
        if len(ans)==0:
            return [-1]
        return ans
                
adj=[[1], [0, 4], [4, 3], [4, 2], [1, 2, 3]]
V=5
obj=Solution()
print(obj.articulationPoints(V,adj))