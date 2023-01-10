class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        1. go through the nums array to form the prefix array. 
        """
        prev_mult = 1
        prefix_array = [1 for i in range(len(nums))]
        for i, ele in enumerate(nums):
            if i == 0:
                prefix_array[i] = 1
                continue
            prefix_array[i] = nums[i - 1] * prev_mult
            prev_mult = prefix_array[i]
        
        prev_mult = 1
        for i in range(len(nums) - 1, -1, -1):
            prefix_array[i] *= prev_mult
            prev_mult *= nums[i]
        return prefix_array


            
        
