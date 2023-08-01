from typing import Optional,List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums,0,len(nums)-1,target)

    def binarySearch(self,nums,l,r,target):
        if l>r:
            return -1
        mid = (l + r)//2
        if nums[mid]==target:
            return mid
        
        if nums[mid]>target:
            return self.binarySearch(nums,l,mid-1,target)
        else:
            return self.binarySearch(nums,mid+1,r,target)
sol = Solution()
sol.search([5,4,3,2],5)