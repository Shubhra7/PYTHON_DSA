# Video: https://youtu.be/-zI4mrF2Pb4?si=aREvaiJ3rgaN2uip

# adventure xyzadvklptu
# Highest common subsequences length:  5
# The Largest Common subsequence is:  advtu

def print_max_LCS(word1, word2):
    n,m  = len(word1), len(word2)
    dp = [[0]*(m+1) for _ in range(n+1)]
    
    for i in range(1, n+1):         #  ****Straing index from 1 is very important****
        for j in range(1, m+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print("Highest common subsequences length: ",dp[n][m])
    i, j = len(word1), len(word2)
    ans = ""
    while i>0 and j>0:
        if(word1[i-1] == word2[j-1]):
            ans = word1[i-1] + ans
            i-=1
            j-=1
        else:
            if(dp[i-1][j]> dp[i][j-1]):
                i -= 1
            else:
                j -= 1
    return ans


word1, word2 = map(str,input().split())
print("The Largest Common subsequence is: ",print_max_LCS(word1, word2))
