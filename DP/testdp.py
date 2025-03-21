class Solution:
	def minJumps(self, arr):
	    # code here
	    def f(ind,dp):
	        if ind+arr[ind]>= len(arr):
	            dp[ind]=1
	            return
	        else:
	            val=float['inf']
	            for i in range(1,arr[ind]+1):
	                val=min(val,dp[ind+i])
	            dp[ind]=val
	            return 
	                
	    dp=[float('inf')]*len(arr)
	    n=len(arr)
		for i in range(n-1,-1,-1):
			f(i,dp)
	    # ans=f(n-1,dp)
	    print(dp)
	    if dp[0]<float('inf'):
	        return dp[0]
	    return -1

arr=[1,3,5,8,9,2,6,7,6,8,9]
obj=Solution()
print(obj.minJumps(arr))

