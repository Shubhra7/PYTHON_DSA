def dfs(start,adj,visited):
    visited.add(start)
    print(start)
    for i in set(adj[start])-visited:
        dfs(i,adj,visited)


V = 4
adj = [[1,3], [2,0], [1], [0]]

visited=set()
dfs(2,adj,visited)