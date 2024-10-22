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
print(dp)

# T.C = O(n)
# S.C = O(n) + O(n) for array and recursion stack


# Using Tabular form (Bottom to up)

