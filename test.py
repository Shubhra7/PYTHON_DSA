import heapq
class Solution:
    # Returns shortest distances from src to all other vertices
    def dij(self,adj,src):
        pq=[]
        heapq.heappush(pq,(0,src))
        dist=[float('inf')]*len(adj)
        dist[src]=0
        while pq:
            dis,node = heapq.heappop(pq)
            for adjNode,edgeWeight in adj[node]:
                if dis+edgeWeight < dist[adjNode]:
                    dist[adjNode]=dis+edgeWeight
                    heapq.heappush(pq,(dist[adjNode],adjNode))
        return dist
    def dijkstra(self, V, edges, src):
        # code here
        adj=[[] for _ in range(V)]
        for i in edges:
            print(i[0]," ",i[1]," ",i[2])
            adj[i[0]].append([i[1],i[2]])
            adj[i[1]].append([i[0],i[2]])
            # print(adj)
        for i in adj:
            print(i)
        return self.dij(adj,src)
    
V = 3
edges= [[0, 1, 1], [1, 2, 3], [0, 2, 6]]
src = 2

obj=Solution()
print(obj.dijkstra(V,edges,src))