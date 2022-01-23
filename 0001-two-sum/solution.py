class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = dict()
        for ele in range(0, len(nums)):
            complement = target - nums[ele]
            if (complement in dct):
                return [dct[complement], ele]
            else:
                dct[nums[ele]] = ele 
        
