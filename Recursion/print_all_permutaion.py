# https://youtu.be/f2ic2Rsc9pU?si=eW5RzrlW3_hn90pG

class Solution:
    def f(self,ind,nums,ans):
        if ind==len(nums):
            ans.append(nums[:])
            return
        for i in range(ind,len(nums)):
            nums[i],nums[ind]=nums[ind],nums[i]
            self.f(ind+1,nums,ans)
            nums[i],nums[ind]=nums[ind],nums[i]

    def permute(self,nums):
        ans=[]
        self.f(0,nums,ans)
        return ans
obj=Solution()
print(obj.permute([1,2,3]))