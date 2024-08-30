s1 = "adfutventur"
s2 = "future"

row = len(s2)
col = len(s1)

dp = [[0  for i in range(col+1)]for j in range(row+1)]
maxi = 0
ro,co = 0,0

for i in range(1,row+1):
    for j in range(1,col+1):
        if(s2[i-1]==s1[j-1]):
            dp[i][j]=dp[i-1][j-1]+1
            if(maxi < dp[i][j]):
                maxi = dp[i][j]
                ro,co = i,j
        else:
            dp[i][j]=0

#For see the dp matrix
for i in dp:
    print(i)

print(maxi)
print(ro,"  ",co)

ans =""
for i in range(ro-1,ro-1-maxi,-1):
    ans = s2[i] + ans

print(ans)

