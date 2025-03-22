def print_max_LCS(word1,word2):
    ro,co=len(word1),len(word2)
    m,n=-1,-1
    dp=[[0]*(co+1) for _ in range(ro+1)]
    maxi=0
    for i in range(1,ro+1):
        for j in range(1,co+1):
            if word1[i-1]==word2[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
                if maxi<dp[i][j]:
                    maxi=dp[i][j]
                    m,n=i,j
            else:
                dp[i][j]=0
    for i in dp:
        print(i)
    ans=""
    for i in range(m,m-maxi,-1):
        ans=word1[i-1]+ans
    print(ans)
    return maxi
    



word1="adventure"
word2="erventpo"
print("The Largest Common subsequence is: ",print_max_LCS(word1, word2))