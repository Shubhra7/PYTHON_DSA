s1,s2=map(str,input().split())
n,m=len(s1),len(s2)
dp=[[-1]*(m+1) for _ in range(n+1)]
maxi=0
ro,co=-1,-1
for i in range(1,n+1):
    for j in range(1,m+1):
        if s1[i-1]==s2[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
            if maxi<dp[i][j]:
                maxi=dp[i][j]
                ro,co=i,j
        else:
            dp[i][j]=0
print(maxi)
ans=""
for i in range(ro,ro-maxi,-1):
    ans=s1[i-1]+ans
print(ans)
    