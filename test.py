from typing import List

class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Next Greater Left & Right
        left = [-1] * n
        right = [n] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                right[stack.pop()] = i
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        
        # Step 2: Count bowls
        count = 0
        for i in range(n):
            # left candidates: (left[i], i) plus left[i] itself
            l_count = sum(1 for j in range(left[i], i) if j >= 0 and nums[j] > nums[i])
            # right candidates: (i, right[i]) plus right[i] itself
            r_count = sum(1 for k in range(i+1, right[i]+1) if k < n and nums[k] > nums[i])
            count += l_count * r_count
        
        return count

pbj=Solution()
nums=[2,5,3,1,4]
print(pbj.bowlSubarrays(nums))