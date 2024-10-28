# nums = [1,1,1]
nums = [1,2,3,-3,1,1,1,4,2,-3]
k=3
sum=0
count=0
for i in range(0,len(nums)):
    sum =0
    for j in range(i,len(nums)):
        sum += nums[j]
        if(sum == k):
            count += 1

print(count)

