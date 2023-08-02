from typing import Optional,List
# https://leetcode.com/problems/maximum-average-subarray-i/description/
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = 0 
        for i in range(0,k):
            curr_sum += nums[i]
        max_avg = curr_sum/k
        print(curr_sum)
        for i in range(k,len(nums)):
            curr_sum +=  nums[i] - nums[i-k]
            max_avg = max(curr_sum/k,max_avg)
        return max_avg