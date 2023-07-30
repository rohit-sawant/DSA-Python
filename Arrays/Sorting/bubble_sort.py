from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==0:
            return
        
        for i in range(0,len(nums)-1):
            min_val = nums[i]
            min_index = i
            for j in range(i+1,len(nums)):
                if min_val>nums[j]:
                    min_val = nums[j]
                    min_index = j
            temp = nums[min_index]
            nums[min_index] = nums[i]
            nums[i] = temp

                