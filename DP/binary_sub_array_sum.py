def bin_sum(nums,k):
    if(k<0):
        return 0
    r=0
    l=0
    sum=0
    count = 0
    while r<len(nums):
        sum += nums[r]
        while sum>k :
            sum -= nums[l]
            l += 1
        count += (r-l)+1
        r += 1
    return count

nums = [1,0,0,1,1,0]
k = 2

print(bin_sum(nums,k))