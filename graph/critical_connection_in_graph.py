# https://www.geeksforgeeks.org/problems/critical-connections/1
# https://youtu.be/qrAub5z8FeA?list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn

# Tarjan's Algorithm
#check by adj can i reach you without you
# tin==> DFS time insert on
# low[] ==> min lowest time insertion of all adjacent nodes apart from parent

class Solution:
    def criticalConnections(self, v, adj):
        # code here
        def dfs(node,parent,visit,adj,tin,low,timer,bridges):
            visit[node]=True
            tin[node]=timer
            low[node]=timer
            timer += 1
            for it in adj[node]:
                if it==parent:
                    continue
                if not visit[it]:
                    dfs(it,node,visit,adj,tin,low,timer,bridges)
                    low[node] = min(low[node],low[it])
                    if low[it] > tin[node]:
                        bridges.append(sorted([node,it]))
                else:
                    low[node]=min(low[node],low[it])
                    
        bridges=[]
        visit=[False]*v
        tin=[-1]*v
        low=[-1]*v
        dfs(0,-1,visit,adj,tin,low,0,bridges)
        bridges.sort()
        return bridges
    
adj=[[1, 2], [0], [0]]
v=3 
obj=Solution()
print(obj.criticalConnections(v,adj))
"""
Output: 
0 1
0 2
"""