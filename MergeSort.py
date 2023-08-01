from typing import Optional,List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums)
        self.merge_sort(nums,0,len(nums)-1)
        print("sorted arra",nums)
        return nums

    def merge_sort(self,nums,l,r):
        if l>=r :
            return

        mid = (l + r)//2
        self.merge_sort(nums,l,mid)
        self.merge_sort(nums,mid+1,r)
        self.merge(nums,l,r,mid)

    def swap(self,nums,i,j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
    def merge(self, nums: List[int],l,r,mid) -> List[int]:
        left_copy = nums[l:mid+1]
        right_copy = nums[mid+1:r+1]
        sorted_arr = [0]*(len(left_copy)+len(right_copy))
        l_cnt,r_cnt,sorted_cnt = 0,0,0

        while l_cnt < len(left_copy) and r_cnt < len(right_copy):
            if left_copy[l_cnt] < right_copy[r_cnt]:
                sorted_arr[sorted_cnt] = left_copy[l_cnt]
                sorted_cnt +=1
                l_cnt +=1
            else:
                sorted_arr[sorted_cnt] = right_copy[r_cnt]
                sorted_cnt +=1
                r_cnt += 1

        while l_cnt < len(left_copy):
            sorted_arr[sorted_cnt] = left_copy[l_cnt]
            l_cnt +=1
            sorted_cnt +=1
        while r_cnt < len(right_copy):
            sorted_arr[sorted_cnt] = right_copy[r_cnt]
            r_cnt +=1
            sorted_cnt +=1

        for i in range(0,len(sorted_arr)):
             nums[l+i] = sorted_arr[i]
sol = Solution() 
sol.sortArray([5,1,1,2,0,0])