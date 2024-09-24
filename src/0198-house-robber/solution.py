from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        There are 2 decisions here
        1. Rob the current house, move on to next non-adjacent house (+2 index)
        2. Skip current house, move on to adjacent house (+1 index)

        Base case here:
        1. We must stay within bounds of the array, (0 <= i <= len(arr))

        Return case:
        1. We want to find the maximum of both decisions
        """
        @cache
        def dp(start: int):
            # we are out of bounds, return 0 to not add anything to the robbery
            if start >= len(nums):
                return 0
            # Decision 1, rob the house we are on and go on to next house (non-adjacent)
            take = dp(start + 2) + nums[start]
            # Decision 2, skip the house, move on to adjacent house
            skip = dp(start + 1)

            # Return case: Find the maximum robbery
            return max(take, skip)
    
        # start from 0, within bounds
        return dp(0)
