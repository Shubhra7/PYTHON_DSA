import collections

def bfs(i,j):
    d.append((i,j))
    visited.add((i,j))
    while d:
        m,n = d.popleft()
        for r,c in direction:
            ro,co = r+m, c+n
            if (ro in range(row) and co in range(col) and
                grid[ro][co]==1 and (ro,co) not in visited):
                d.append((ro,co))
                visited.add((ro,co))

d=collections.deque()
visited=set()
direction = [[1,0],[-1,0],[0,1],[0,-1]]

grid = [[1,1,0,1],
        [1,0,0,1],
        [0,1,0,0]]

row = len(grid)
col = len(grid[0])

count = 0
for i in range(row):
    for j in range(col):
        if(grid[i][j]==1 and (i,j) not in visited):
            # print(i," ",j)
            bfs(i,j)
            count += 1

print(count)