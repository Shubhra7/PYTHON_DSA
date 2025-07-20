class Solution:
    def floydWarshall(self, dist):
        n = len(dist)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] < 1e8 and dist[k][j] < 1e8:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

obj = Solution()
dist = [
    [0, 4, 108, 5, 108],
    [108, 0, 1, 108, 6],
    [2, 108, 0, 3, 108],
    [108, 108, 1, 0, 2],
    [1, 108, 108, 4, 0]
]

obj.floydWarshall(dist)
for row in dist:
    print(row)

