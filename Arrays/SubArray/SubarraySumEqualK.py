
# https://leetcode.com/problems/subarray-sum-equals-k/
from typing import Optional,List
class Solution:
    def presentInArray(self,my_dict,my_key)->int:
        if my_key in my_dict:
            return my_dict[my_key]
        return 0
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sum_count = 0 
        sub_array_sum = [0]*n
        sub_array_sum[0] = nums[0]
        sum_array_dict = {}
        sum_array_dict[nums[0]] = 1
        if nums[0]== k:
            sum_count +=1

        for i in range(1,n):
            sub_array_sum[i] = sub_array_sum[i-1] + nums[i]
            if sub_array_sum[i]==k:
                sum_count += 1
            
            sum_count += self.presentInArray(sum_array_dict,sub_array_sum[i]-k)
            if sub_array_sum[i] in sum_array_dict:
                sum_array_dict[sub_array_sum[i]] += 1
            else:
                sum_array_dict[sub_array_sum[i]] = 1

        return sum_count
sol = Solution()
sol.subarraySum([0,0,0,0],0)