# video: https://youtu.be/sdE0A2Oxofw?si=P3FC9Sx6qUkg4jis

"""
There is a robot on an m x n grid. The robot is initially located at the 
top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right 
corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right 
at any point in time.

Given the two integers m and n, return the number of possible unique paths that 
the robot can take to reach the bottom-right corner.
The test cases are generated so that the answer will be less than or equal to 2 * 109.
"""

# I/p ==> m=3,n=7
# o/p==? 28

m=3
n=7

#-----------------------------
# Using Tabulation
#-----------------------------
tabu = [[0 for i in range(n+1)]for j in range(m+1)]
tabu[1][1]=1    #for making the starting point as value 1
for i in range(1,m+1):
    for j in range(1,n+1):
        if(i==1 and j==1): #for avoid to overwrite the staring point
            continue
        tabu[i][j] = tabu[i-1][j] + tabu[i][j-1]

print(tabu[m][n])


#-----------------------------
# Using Recursion 
#-----------------------------

def find_uniquePath(m,n,dp):
    if(m==0 and n==0):  #base case when reached the destination
        return 1
    if(m <0 or n<0): # other edges case when don't reach the starting point
        return 0
    if(dp[m][n] != -1):
        return dp[m][n]
    up=find_uniquePath(m-1,n,dp)
    left= find_uniquePath(m,n-1,dp)
    dp[m][n]= up+left
    return dp[m][n]

dp=[[-1 for i in range(n+1)]for j in range(m+1)]
print(find_uniquePath(m-1,n-1,dp))
# for i in dp:
#     print(i)



#-----------------------------
# space optimal
#-----------------------------
prev = [0 for i in range(n)]
  #for making the starting point as value 1

for i in range(0,m):
    cur=[0 for i in range(n)]
    for j in range(0,n):
        if(i==0 and j==0): 
            cur[j]=1   #For making the staring point vlaue 1
        else:
            up,left =0,0
            if(i>0):
                up=prev[j]
            if(j>0):
                left=cur[j-1]
            cur[j]=up+left
    prev=cur


print(prev[-1])


