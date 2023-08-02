from typing import Optional,List
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = 0
        curr_sum = 0
        curr_sum2 = 0
        for i in nums:
            curr_sum += i
            curr_sum2 += i
            # normal kadane's algorithm
            if curr_sum < 0 :
                curr_sum = 0
            # keeping th track of all negative array
            if curr_sum2 > 0 :
                curr_sum2 = 0
            max_sum = max(curr_sum,max_sum,abs(curr_sum2))
        return max_sum
