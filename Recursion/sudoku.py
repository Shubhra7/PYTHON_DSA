# https://youtu.be/FWAIf_EVUKE?si=CuZJ7Cx9MYXsX6NH
# https://leetcode.com/problems/sudoku-solver/description/
# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/recursion-and-backtracking-gfg-160/problem/solve-the-sudoku-1587115621


def solve(board,ro,co):
    for row in range(9):
        for col in range(9):
            if board[row][col] == '.':
                for num in '123456789':
                    if isSafe(board,row, col, num):
                        board[row][col] = num
                        if solve(board,0,0):
                            return True
                        board[row][col] = '.'
                return False
    return True

def isSafe(mat,row,col,num):
    for i in range(9):
        if mat[i][col]==num:
            return False
        if mat[row][i]==num:
            return False
        if mat[3*(row//3)+i//3][3*(col//3)+i%3]==num:
            return False
    return True
   

# def solve(mat,row,col):
#         if row==8 and col==9:
#             return True
#         if col==9:
#             row+=1
#             col=0
#         if mat[row][col]!=0:
#             return solve(mat,row,col+1)
#         for num in range(1,10):
#             if isSafe(mat,row,col,num):
#                 mat[row][col]=num
#                 if solve(mat,row,col+1):
#                     return True
#                 mat[row][col]=0
#         return False
 

def sudoku(board):
    solve(board,0,0)
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

# board = [[5,3,0,0,7,0,0,0,0],
#          [6,0,0,1,9,5,0,0,0],
#          [0,9,8,0,0,0,0,6,0],
#          [8,0,0,0,6,0,0,0,3],
#          [4,0,0,8,0,3,0,0,1],
#          [7,0,0,0,2,0,0,0,6],
#          [0,6,0,0,0,0,2,8,0],
#          [0,0,0,4,1,9,0,0,5],
#          [0,0,0,0,8,0,0,7,9]]

sudoku(board)
for i in board:
    print(i)