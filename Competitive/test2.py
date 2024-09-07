import collections

l=[]
def bfs(i,j):
    q.append((i,j))
    visited.add((i,j))
    while q:
        m,n = q.popleft()
        for r,c in direction:
            ro = r+m
            co = c+n
            # l.append((ro,co))
            if(ro in range(row) and co in range(col) 
               and grid[ro][co]==1 and (ro,co) not in visited):
                l.append((ro,co))
                q.append((ro,co))
                visited.add((ro,co))

grid = [[1,1,0,1,1],
        [0,1,0,0,1],
        [1,0,1,0,0]]

q = collections.deque()
visited = set()
direction = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]
row = len(grid)
col = len(grid[0])

count = 0
for i in range(row):
    for j in range(col):
        if(grid[i][j]==1 and (i,j) not in visited):
            bfs(i,j)
            print(i," ",j)
            count += 1

print("The number of island: ",count)
print(l)


