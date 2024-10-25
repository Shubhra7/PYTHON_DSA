s1 = "adventure"
s2 = "fadvenuture"

row = len(s2)
col = len(s1)

dp =[[0 for i in range(col+1)]for j in range(row+1)]
maxi=-1
ro,co=-1,-1

for i in range(1,row+1):
    for j in range(1,col+1):
        if(s2[i-1] == s1[j-1]):
            dp[i][j] = dp[i-1][j-1]+1
            if(maxi < dp[i][j]):
                maxi = dp[i][j]
                ro,co = i,j
        else:
            dp[i][j]=0

print("Max same length: ",maxi)
ans =""
for i in range(ro-1,ro-maxi-1,-1):
    ans = s2[i]+ans
print(ans)