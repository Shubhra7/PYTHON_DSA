# https://youtu.be/vRVfmbCFW7Y
# https://www.naukri.com/code360/problems/matrix-chain-multiplication_975344?leftPanelTabValue=PROBLEM

"""
I/P==
4
4 5 3 2

O/P ==> 70
"""
def f(i,j,arr,dp):
    #Base case
    if i==j:    
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    mini=float('inf')
    # Partitioning 
    for k in range(i,j): # k will go from [i,j-1]
        val=arr[i-1]*arr[k]*arr[j] + f(i,k,arr,dp) + f(k+1,j,arr,dp)
        mini=min(mini,val)
    # Minimum cost
    dp[i][j]=mini
    return dp[i][j]


def Matrix_chain_multiplication(arr,n):
    dp=[[-1]*n for _ in range(n)]
    return f(1,n-1,arr,dp)

n=int(input())
arr=list(map(int,input().strip().split(' ')))

#print(n)
#print(arr)
print(Matrix_chain_multiplication(arr,n))
