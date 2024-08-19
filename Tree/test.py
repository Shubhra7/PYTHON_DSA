import collections
visited = set()
q=collections.deque()
direction = [[1,0],[-1,0],[0,1],[0,-1]]

def bfs(i,j):
    visited.add((i,j))
    q.append((i,j))
    while q:
        r,c = q.popleft()
        for k,l in direction:
            ro = k+r
            co = l+c
            if(ro in range(row) and co in range(col) and 
               grid[ro][co]==1 and (ro,co) not in visited):
                visited.add((ro,co))
                q.append((ro,co))





grid = [[1,0,0,1],
        [1,1,0,1],
        [1,0,1,0]]

row = len(grid)
col = len(grid[0])
count=0
for i in range(row):
    for j in range(col):
        if (grid[i][j]==1 and (i,j) not in visited):
            bfs(i,j)
            count += 1
print(count)