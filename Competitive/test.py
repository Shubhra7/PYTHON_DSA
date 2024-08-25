import collections

grid = [[2,1,1],[0,1,1],[1,0,1]]


visited=set()
directions = [[1,0],[-1,0],[0,1],[0,-1]]
q = collections.deque()
row =len(grid)
col =len(grid[0])
fresh=set()

for i in range(row):
    for j in range(col):
        if( grid[i][j] == 1):
            fresh.add((i,j))
        if( grid[i][j] == 2):
            q.append((i,j,0))
ans=0
while q:
    i,j,time = q.popleft()
    for x,y in directions:
        ro= i+x
        co= j+y
        if( ro in range(row) and co in range(col) and 
           grid[ro][co]==1 ):
            grid[ro][co]=2
            q.append((ro,co,time+1))
            fresh.pop()
            ans=max(ans,time+1)

for i in range(len(grid)):
    for j in range(len(grid[0])):
        print(grid[i][j],end=" ")
    print()

if(len(fresh)==0):
    print(ans)
else:
    print(-1)
        
        

