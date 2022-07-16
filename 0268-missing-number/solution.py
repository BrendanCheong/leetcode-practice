class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 1. find the given sum from the given arr
        given_sum = sum(nums) # O(n) 
        # 2. find the actual sum from 0 to n
        actual_sum = sum(range(len(nums) + 1)) # O(n)
        # 3. now subtract to find the odd one out
        return actual_sum - given_sum
        
