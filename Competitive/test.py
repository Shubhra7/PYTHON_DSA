# https://leetcode.com/problems/3sum/description/
"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 
"""
# https://www.youtube.com/watch?v=DhFh8Kw7ymk

def threeSum(nums):
    nums.sort()
    st=set()
    for i in range(len(nums)):
        if i>0 and nums[i]==nums[i-1]:
            i += 1
        j=i+1
        k=len(nums)-1
        while j<k:
            sum1 = nums[i]+nums[j]+nums[k]
            if sum1<10:
                j += 1
            elif sum1>10:
                k -= 1
            else:
                st.add(tuple([nums[i],nums[j],nums[k]]))
                j+=1
                k-=1
                while j<k and nums[j]==nums[j-1]:
                    j += 1
                while j<k and nums[k]==nums[k+1]:
                    k -= 1
    ans=[list(i) for i in st]
    return ans

print(threeSum([-26,32,4,17,-16,18,1,8,6,8,3,-13]))
# print(threeSum([2,-95,9,1,-79,88,96,0,5]))
# print(threeSum([-1,0,1,2,-1,-4]))
#[[-1, 0, 1], [-1, -1, 2]]