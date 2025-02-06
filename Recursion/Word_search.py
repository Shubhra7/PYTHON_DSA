# https://leetcode.com/problems/word-search/description/
# https://www.youtube.com/watch?v=whyax_vB8xY

def find(board,i,j,word,idx,m,n):
    direction=[[1,0],[-1,0],[0,1],[0,-1]]
    if idx==len(word):
        return True
    if(i<0 or j<0 or i>=m or j>=n or board[i][j]=='$'):
        return False
    if(board[i][j] != word[idx]):
        return False
    temp = board[i][j]
    board[i][j]='$'
    for di in direction:
        newR,newC = i+di[0],j+di[1]
        if(find(board,newR,newC,word,idx+1,m,n)):
            return True
    board[i][j]=temp
    return False
    
def exist(board,word):
    m,n=len(board),len(board[0])
    for i in range(m):
        for j in range(n):
            if board[i][j]==word[0] and find(board,i,j,word,0,m,n):
                return True
    return False

board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
word="ABCCED"  #True
# word="ABCCXD" #False

print(exist(board,word))