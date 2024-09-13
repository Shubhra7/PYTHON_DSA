s1="adventure"
s2="future"

row,col =len(s1), len(s2)
dp=[[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]
maxi=-1
ro,co =-1,-1

for i in range(1,row+1):
    for j in range(1,col+1):
        if(s1[i-1] == s2[j-1]):
            dp[i][j]=dp[i-1][j-1]+1
            if(dp[i][j] > maxi):
                maxi=dp[i][j]
                ro,co=i,j
        else:
            dp[i][j]=0

print(maxi)

ans=""
for i in range(maxi):
    ans =s1[ro-1] + ans
    ro -= 1

print(ans)


