# Link: https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=dfs_of_graph

def dfs(start,visit, adj, l):
    visit.add(start)
    l.append(start)
    for i in adj[start]:
        if(i not in visit):
            dfs(i,visit,adj,l)

# V= 5
# adj = [[2,3,1] , [0], [0,4], [0], [2]]
# # op==> [0, 2, 4, 3, 1]

V = 4
adj = [[1,3], [2,0], [1], [0]]
# op==> [0, 1, 2, 3]


visit = set()
l=[]
dfs(0,visit,adj,l)
print(l)