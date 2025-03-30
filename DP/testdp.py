# adventure xyzadvklptu
# Highest common subsequences length:  5
# The Largest Common subsequence is:  advtu

s1,s2=map(str,input().strip().split())
# print(s1," ",s2)
n,m=len(s1),len(s2)
dp=[[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if s1[i-1]==s2[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
print(dp[n][m])

ans=""
i=n
j=m
while i>0 and j>0:
    if s1[i-1]==s2[j-1]:
        ans=s1[i-1]+ans
        i-=1
        j-=1
    else:
        if dp[i-1][j]>dp[i][j-1]:
            i=i-1
        else:
            j=j-1
print(ans)