from typing import *

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        if nums[left] < nums[-1]:
            return nums[left]

        if len(nums) == 1:
            return nums[0]
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1
            
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid] < nums[mid - 1]:
                return nums[mid]
        return -1

