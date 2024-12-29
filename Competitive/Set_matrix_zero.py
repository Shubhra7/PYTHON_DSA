# https://www.naukri.com/code360/problems/set-matrix-zeros_3846774?leftPanelTabValue=SUBMISSION
# https://www.youtube.com/watch?v=N0MgLvceX7M

from math import *
from collections import *
from sys import *

from typing import List

def setZeros(matrix):
	# Write your code here.
    col0=1
    n,m=len(matrix),len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==0:
                matrix[i][0]=0
                if j!=0:    #Important
                    matrix[0][j]=0
                else:
                    col0=0
    
    for i in range(1,n):
        for j in range(1,m):
            if matrix[i][j]!=0:
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j]=0
    
    if matrix[0][0]==0:
        for i in range(m):
            matrix[0][i]=0
    if col0==0:
        for i in range(n):
            matrix[i][0]=0
    return matrix

print(setZeros([[7, 19, 3],
[4, 21, 0]]))

# op==> [[7, 19, 0], [0, 0, 0]]