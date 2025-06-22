# https://youtu.be/uRbJ1OF9aYM?list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn

"""
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
"""

# check if the part of the cycle or
# is connecting inbounded as to any node of the cycle


class Solution:
    def eventualSafeNodes(self, graph):

        def dfs(node,adj,visit,pathVis,check):
            visit[node],pathVis[node] = 1,1
            for subN in adj[node]:
                if visit[subN]==0:
                    # if not visited node then do dfs
                    if dfs(subN,adj,visit,pathVis,check):
                        # not terminal so unsafe
                        check[subN]=0
                        return True
                    # check if that is parent?
                elif pathVis[subN]==1:
                    check[subN]=0
                    return True
            # would be tends to terminal so safe one
            pathVis[node]=0
            check[node]=1
            return False

        V=len(graph)
        visit=[0]*V
        pathVis=[0]*V
        check=[0]*V
        safeNodes=[]
        for i in range(V):
            if visit[i]==0:
                dfs(i,graph,visit,pathVis,check)
        for i in range(V):
            if check[i]!=0:
                safeNodes.append(i)
        return safeNodes
    
graph = [[1,2],[2,3],[5],[0],[5],[],[]]
obj=Solution()
print(obj.eventualSafeNodes(graph))
    

