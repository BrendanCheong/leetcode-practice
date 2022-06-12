class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length = len(nums)
        # finds the difference between numbers in the full set that is not in the given set
        ans = set(range(1, length + 1)) - set(nums)
        return ans
        
