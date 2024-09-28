import collections

q= collections.deque()
visited = set()
direction = [[1,0],[-1,0],[0,1],[0,-1]]

def bfs(i,j):
    visited.add((i,j))
    q.append((i,j))
    while q:
        r,c = q.popleft()
        for m,n in direction:
            ro,co = r+m, c+n
            while( ro in range(row) and co in range(col)
                  and grid[ro][co]==1 and (ro,co) not in visited):
                q.append((ro,co))
                visited.add((ro,co))
grid = [[1,1,0,0,1],
        [1,1,0,0,1],
        [1,0,1,0,0]]

row = len(grid)
col = len(grid[0])

count = 0
for i in range(row):
    for j in range(col):
        if(grid[i][j]==1 and (i,j) not in visited):
            count += 1
            bfs(i,j)

print(count)