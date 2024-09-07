s2= "adventuref"
s1 = "ventfuturef"

row = len(s1)
col = len(s2)

dp = [[0 for i in range(col+1)] for j in range(row+1)]
maxi=0
ro,co= 0,0

for i in range(1,row+1):
    for j in range(1,col+1):
        if(s1[i-1] == s2[j-1]):
            dp[i][j]= dp[i-1][j-1]+1
            if( maxi < dp[i][j]):
                maxi = dp[i][j]
                ro,co = i,j
        else:
            dp[i][j]=0


    
ans = ""
pos = ro
for i in range(maxi):
    ans =  s1[pos-1] + ans
    pos -= 1

print(maxi)
print(ans)