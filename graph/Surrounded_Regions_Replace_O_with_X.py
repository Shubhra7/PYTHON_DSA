# https://www.geeksforgeeks.org/problems/replace-os-with-xs0052/1
# https://youtu.be/BtdgAys4yMk?list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&t=1225

# broder ar stha suru kore dfs, segulo hobe na so visit kra de

class Solution:
    def fill(self,  mat):
        # code here
        def dfs(r,c,visit,mat):
            directions=[[1,0],[-1,0],[0,1],[0,-1]]
            visit[r][c]=1
            for u,v in directions:
                newR,newC = r+u,c+v
                if newR in range(row) and newC in range(col) and visit[newR][newC]==0 and mat[newR][newC]=='O':
                    dfs(newR,newC,visit,mat)
                    
        row,col = len(mat),len(mat[0])
        visit=[[0]*col for _ in range(row)]
        for i in range(col):
            #first row
            if visit[0][i]==0 and mat[0][i]=='O':
                dfs(0,i,visit,mat)
            #last row
            if visit[row-1][i]==0 and mat[row-1][i]=='O':
                dfs(row-1,i,visit,mat)
                
        for j in range(row):
            # first column
            if visit[j][0]==0 and mat[j][0]=='O':
                dfs(j,0,visit,mat)
            # last column
            if visit[j][col-1]==0 and mat[j][col-1]=='O':
                dfs(j,col-1,visit,mat)
        
        for i in range(row):
            for j in range(col):
                if visit[i][j]==0 and mat[i][j]=='O':
                    mat[i][j]='X'
        return mat