class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_num = nums[0]
        curr = 0 # initial value
        
        for ele in nums:
            if curr < 0: # if adding a ele gets a negative value, reset to 0 to get max sum
                curr = 0
            curr += ele
            max_num = max(curr, max_num)
        return max_num
        
