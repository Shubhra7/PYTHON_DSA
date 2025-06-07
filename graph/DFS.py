# https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1

def dfs(node,adj,visit,ans):
    ans.append(node)
    for i in adj[node]:
        if visit[i]==0:
            visit[i]=1
            dfs(i,adj,visit,ans)

# adj=[[2,3,1],[0],[0,4],[0],[2]] #[0, 2, 4, 3, 1]
adj= [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]   #[0, 1, 2, 3, 4]
V=len(adj)
ans=[]
visit=[0]*V
visit[0]=1

dfs(0,adj,visit,ans)
print("The DFS traversal answer: ",ans)