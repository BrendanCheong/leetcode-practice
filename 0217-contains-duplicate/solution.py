class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        O(n) solution, we just add to a set and see if the element
        is already inside
        """
        if len(nums) == len(set(nums)):
            return False
        return True
        
