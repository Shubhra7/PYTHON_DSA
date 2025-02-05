# https://leetcode.com/problems/n-queens/description/


def solve(col,ans,board,leftRow,upDiag,lowDiag,n,gfgans,gfgsub):
    if col==n:
        ans.append(board[:])
        gfgans.append(gfgsub[:])
        return
    for row in range(n):
        if not leftRow[row] and not upDiag[row+col] and not lowDiag[n-1+col-row]:
            board[row]=board[row][:col]+'Q'+board[row][col+1:]
            leftRow[row]=upDiag[row+col]=lowDiag[n-1+col-row]=True
            gfgsub.append(row)
            solve(col+1,ans,board,leftRow,upDiag,lowDiag,n,gfgans,gfgsub)
            gfgsub.pop()
            board[row]=board[row][:col]+'.'+board[row][col+1:]
            leftRow[row]=upDiag[row+col]=lowDiag[n-1+col-row]=False
def solveNQueens(n,gfgans):
    ans=[]
    board=['.'*n for _ in range(n)]
    leftRow=[False]*n
    upDiag=[False]*(2*n-1)
    lowDiag=[False]*(2*n-1)
    gfgsub=[]
    solve(0,ans,board,leftRow,upDiag,lowDiag,n,gfgans,gfgsub)
    for i in ans:
        for j in i:
            print(j)
        print()
    return ans

n=4
gfgans=[]
print(solveNQueens(n,gfgans))
print("0 based solution answer: ")
print(gfgans)
    