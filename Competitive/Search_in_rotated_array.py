# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/


class Solution:
    def modifiedBinarySearch(self,nums,target,left,right):
        if (left > right):
            return -1
        mid = left + ((right - left) //2 )
        # print(mid)
        if (nums[mid] == target):
            return mid
        #When the first left segment is sorted!!
        if (nums[left] <= nums[mid]):
            # check the target is present in first segment or not?
            if (nums[left] <= target and nums[mid]>=target):
                return self.modifiedBinarySearch(nums,target,left,mid - 1)
            else:
                # if no then do the modifiedBinarySearch in right segment!!
                return self.modifiedBinarySearch(nums,target,mid+1,right)
        # When the second right segment is sorted
        else:
            # check the target is present in second segment or not?
            if (nums[mid] <= target and nums[right]>=target ):
                return self.modifiedBinarySearch(nums,target,mid+1,right)
            else:
                # if no then do the modifiedBinarySearch in left segment!!
                return self.modifiedBinarySearch(nums,target,left,mid-1)


    def search(self, nums, target) -> int:
        ans = self.modifiedBinarySearch(nums,target,0,len(nums)-1)
        return ans
        

obj=Solution()
# arr=[7,8,9,0,1,2,3,4,5,6]
arr=[3,5,1,2]  #o/p = -1
print(obj.search(arr,6))
        