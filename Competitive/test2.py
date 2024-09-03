def max_sub(s1,s2):
    row =len(s1)
    col = len(s2)

    dp=[[0 for i in range(col+1)]for j in range(row+1)]
    maxi=0
    ro,co=-1,-1
    
    for i in range(row+1):
        for j in range(col+1):
            if(i==0 or j==0):
                dp[i][j]=0
            else:
                if(s1[i-1]==s2[j-1]):
                    dp[i][j] = dp[i-1][j-1]+1
                    if (dp[i][j] > maxi):
                        maxi = dp[i][j]
                        ro,co = i,j
                else:
                    dp[i][j]=0
    
    for i in dp:
        print(i)
    ans=""
    i=maxi
    j=0
    ans=""
    while(i > 0):
        ans = s1[ro-j-1] + ans
        i -= 1
        j += 1
    
    print(ans)
    return maxi

s1 = "future"
s2 = "adventure"

print(max_sub(s1,s2))