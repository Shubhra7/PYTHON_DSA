import heapq
import sys 

def dijk(v,adj,source):
    pq=[]
    heapq.heappush(pq,(0,source))
    dist=[sys.maxsize]*v
    dist[source]=0
    while pq:
        dis,Node = heapq.heappop(pq)
        for adjNode,edgeWieght in adj[Node]:
            if dis+edgeWieght < dist[adjNode]:
                dist[adjNode]=dis+edgeWieght
                heapq.heappush(pq,(dist[adjNode],adjNode))
    return dist


graph=   [  [0, 4, 0, 0, 0, 0, 0, 8, 0],
            [4, 0, 8, 0, 0, 0, 0, 11, 0],
            [0, 8, 0, 7, 0, 4, 0, 0, 2],
            [0, 0, 7, 0, 9, 14, 0, 0, 0],
            [0, 0, 0, 9, 0, 10, 0, 0, 0],
            [0, 0, 4, 14, 10, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 1, 6],
            [8, 11, 0, 0, 0, 0, 1, 0, 7],
            [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]
v=len(graph)
adj=[[] for _ in range(v)]
for i in range(v):
    for j in range(v):
        if graph[i][j]!=0:
            adj[i].append((j,graph[i][j]))
print(adj)
source=0
print(dijk(v,adj,source))


