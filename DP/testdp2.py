def f(i,j,pattern,text,dp):
    if i<0 and j<0:
        return True
    if i<0 and j>=0:
        return False
    if i>=0 and j<0:
        for k in range(i+1):
            if pattern[k]!='*':
                return False
        return True
    if dp[i][j]!=-1:
        return dp[i][j]
    if pattern[i]==text[j] or pattern[i]=='?':
        dp[i][j]=f(i-1,j-1,pattern,text,dp)
        return dp[i][j]
    elif pattern[i]=='*':
        dp[i][j]= f(i-1,j,pattern,text,dp) or f(i,j-1,pattern,text,dp)
        return dp[i][j]
    dp[i][j]=False
    return dp[i][j]
def wildcardMatching(pattern, text):
    # Write your code here.
    n,m=len(pattern),len(text)
    dp=[[-1]*m for _ in range(n)]
    return f(n-1,m-1,pattern,text,dp)

print(wildcardMatching("**","abcdefhjo"))