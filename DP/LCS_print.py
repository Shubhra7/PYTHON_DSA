def print_max_LCS(word1, word2):
    n,m  = len(word1), len(word2)
    dp = [[0]*(m+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][m]

word1, word2 = map(str,input().split())
print(print_max_LCS(word1, word2))
