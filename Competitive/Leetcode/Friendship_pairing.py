# link: https://leetcode.com/discuss/general-discussion/1349122/friends-pairing-problem
# link2: https://youtu.be/SHDu0Ufjyk8?si=tsM5p4z-v-qiN218


n= 4 # number of friends  o/p==> 10
# n= 5 # number of friends o/p ==> 26
dp=[0 for i in range(n+1)]
dp[1]=1 # only single possible
dp[2]=2 # single or pair

for i in range(3,n+1):
    dp[i] = dp[i-1] + (i-1)*dp[i-2]  #i-2 ==> nija and right ar jon chere tai 
                                     # i-1 ==> nija chara bakider jnno brunch

print(dp[n])
