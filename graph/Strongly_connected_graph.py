# https://youtu.be/R6uoSjZ2imo?list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn
# https://www.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo/1


"""
Strongly Connected Components ==> Kosaraju's Algorithm
    1. Sort all the edges according to the finishing time.
    2. Reverse the Graph.
    3. Do the dfs.
"""
class Solution:
    def kosaraju(self, adj):
        #code here
        def dfs1(node,adj,visit,st):
            visit[node]=True
            for it in adj[node]:
                if not visit[it]:
                    dfs1(it,adj,visit,st)
            st.append(node)
            
        def dfs2(node,adj,visit):
            visit[node]=True
            for it in adj[node]:
                if not visit[it]:
                    dfs2(it,adj,visit)
            
        v=len(adj)
        visit=[False]*v
        st=[]
        for i in range(v):
            if not visit[i]:
                dfs1(i,adj,visit,st)
        adjT=[[] for _ in range(v)]
        for i in range(v):
            visit[i]=False
            for it in adj[i]:
                adjT[it].append(i)
        ans=0
        while st:
            node=st.pop()
            if not visit[node]:
                ans+=1
                dfs2(node,adjT,visit)
        return ans
                
adj= [[2, 3], [0], [1], [4], []]   # 3
obj=Solution()
print(obj.kosaraju(adj))