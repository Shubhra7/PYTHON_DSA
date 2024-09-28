text1 = 'adventureabba'
text2 = 'fventuture'

lt1, lt2 =len(text1), len(text2)

dp = [ [0 for i in range(lt1+1)] for j in range(lt2+1)]
maxi=0
ro,co = -1,-1

for i in range(1,lt2+1):
    for j in range(1,lt1+1):
        if(text2[i-1]==text1[j-1]):
            print(text2[i-1])
            dp[i][j] = dp[i-1][j-1]+1
            if(dp[i][j] > maxi):
                print(i," : ",j)
                maxi=dp[i][j]
                ro,co = i,j
        else:
            dp[i][j]=max(dp[i][j-1], dp[i-1][j])

for i in dp:
    print(i)

print("The maximum substring is length of: ",maxi)

i=0
ans=""
while i<maxi:
    ans = text2[ro-1] + ans
    ro -=1
    i+=1
print(ans)

