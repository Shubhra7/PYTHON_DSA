# https://youtu.be/PwMVNSJ5SLI?list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn
# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/

class Solution:
    def findTheCity(self, n, edges, distanceThreshold):
        dist=[[1e8]*n for _ in range(n)]
        for i in range(n):
            dist[i][i]=0
        for u,v,wt in edges:
            dist[u][v]=wt
            dist[v][u]=wt
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k]<1e8 and dist[k][j]<1e8:
                        dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
        ans=-1
        minReachNode=float('inf')
        for i in range(n):
            cnt=0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    cnt+=1
            if minReachNode >= cnt:
                minReachNode = cnt
                ans=i
        return ans
        
n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold = 4
# Output: 3
obj=Solution()
print(obj.findTheCity(n,edges,distanceThreshold))