s1="adventure"
s2="fadvenuture"

row = len(s1)
col = len(s2)

dp=[[0 for i in range(col+1)]for j in range(row+1)]
maxi=0
ro,co = -1,-1
for i in range(1,row+1):
    for j in range(1,col+1):
        if(s1[i-1] == s2[j-1]):
            dp[i][j] = dp[i-1][j-1]+1
            if(maxi < dp[i][j]):
                maxi = dp[i][j]
                ro,co = i,j
        else:
            dp[i][j]=0

print(maxi)
print(ro,co)
print(s1[ro-maxi:ro])
