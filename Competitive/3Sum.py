class Solution:
    def threeSum(self,nums):
        nums.sort()
        ans=[]
        # st=set() not need as already sorted
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while j<k:
                sum1 = nums[i]+nums[j]+nums[k]
                if sum1<0:
                    j += 1
                elif sum1>0:
                    k -= 1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    # st.add(tuple([nums[i],nums[j],nums[k]]))
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j += 1
                    while j<k and nums[k]==nums[k+1]:
                        k -= 1
        # ans=[list(i) for i in st]
        return ans
obj=Solution()
print(obj.threeSum([-1,0,1,2,-1,-4]))

        