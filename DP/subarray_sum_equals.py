# Keeping subarray sums equal k

# nums = [1,1,1]
# k=2

# nums = [1,2,3]
# k=3

nums = [1,0,0,1,1,0]
k = 2

mp={0:1}
count=0
sum=0
for i in range(0,len(nums)):
    sum += nums[i]
    count += mp.get(sum-k,0)
    mp[sum] = mp.get(sum,0)+1
print(mp)
print(count)
