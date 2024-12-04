# Link: https://youtu.be/0W8dVZUL1MQ?t=2524

# Longest common substring between
# If multiple present the first one only
# Give the sum of ascci value that word

# I/O = adventure
# O/P = future

def max_subString_Asccivalue(s1,s2):
    row = len(s1)
    col = len(s2)
    
    dp = [[0 for i in range(col+1)]for j in range(row+1)]
    maxi=0
    ro,co = 0,0

    for i in range(1,row+1):
        for j in range(1,col+1):
            if(s1[i-1]==s2[j-1]):
                dp[i][j]=dp[i-1][j-1]+1
                if(maxi < dp[i][j]):
                    maxi = dp[i][j]
                    ro,co = i,j
            else:
                dp[i][j]=0          #That is when subarray (means contiguous)
                # dp[i][j] = max(dp[i-1][j], dp[i][j-1])       #That is when subsequences say

    ans=""
    # For getting the String
    for i in range(ro-1,ro-maxi-1,-1):
        ans = s1[i] + ans
    # print(maxi)
    
    return ans


s1, s2 = map(str,input().split())

print(max_subString_Asccivalue(s1,s2))