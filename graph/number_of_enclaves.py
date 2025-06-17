# https://www.geeksforgeeks.org/problems/number-of-enclaves/1
# https://youtu.be/rxKcepXQgU4?si=XuNKlz1SQ5hehpdE

# border check 1
#then bfs so touched island can get
# then check not touched island just

"""
grid[][] = {{0, 0, 0, 0},
            {1, 0, 1, 0},
            {0, 1, 1, 0},
            {0, 0, 0, 0}}
Output:
3
"""

###########################
#   Using dfs
###########################


from collections import deque
class Solution:    
    def numberOfEnclaves(self, grid):
        # code here
        q=deque()
        row,col = len(grid),len(grid[0])
        visit=[[0]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                # for last row or last column or first col or row
                if(i==0 or j==0 or i==row-1 or j==col-1):
                    if(grid[i][j] == 1):
                        q.append((i,j))
                        visit[i][j]=1
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        while q:
            first,second = q.popleft()
            for u,v in directions:
                newR,newC = first+u,second+v
                if newR in range(row) and newC in range(col) and grid[newR][newC]==1 and visit[newR][newC]==0:
                    q.append((newR,newC))
                    visit[newR][newC]=1
        cnt=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1 and visit[i][j]==0:
                    cnt+=1
        return cnt
            
        
grid = [[0, 0, 0,0],
        [1, 0, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]]    #o.p==> 3   
obj=Solution()
print(obj.numberOfEnclaves(grid))   