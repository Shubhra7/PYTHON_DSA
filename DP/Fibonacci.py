# Using memorization  (Recursion so top to bottom)
def fibo(n,dp):
    if(n<=1):
        return n
    if(dp[n]!=-1):
        return dp[n]
    else:
        dp[n] = fibo(n-1,dp) + fibo(n-2,dp)
        return dp[n]


n=5
dp = [-1 for i in range(n+1)]
print(fibo(n,dp))
# print(dp)

# T.C = O(n)
# S.C = O(n) + O(n) for array and recursion stack

# ---------------------------------
# Using Tabular form (Bottom to up)
# ---------------------------------

n=5
dp=[0 for i in range(n+1)]
dp[0], dp[1]=0,1
for i in range(2,n+1):
    dp[i] = dp[i-1]+dp[i-2]

print(dp[n])

# TC ==> O(n)
# SC ==> O(n)  only for array

# --------------------
# Normal is SC = 1
# --------------------

n=5
prev, prev2=0,1
ans=0
for i in range(2,n+1):
    ans = prev + prev2
    prev = prev2
    prev2 = ans
print(ans)

# TC ==> O(n)
# SC ==> 1


