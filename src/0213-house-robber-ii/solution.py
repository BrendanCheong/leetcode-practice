from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        This is an interesting question, there are actually 2 cases, with each case having 2 decisions.
        Since its a circular array, an array of [2, 3, 4, 5] can actually be like 2,3,4 or 3,4,5. We can
        either pick choose the first element to be in our array, or choose the last element.
    
        Case 1: let the first element be in our array
        Case 2: let the last element be in our array

        Decisions:
        1. Take = take the current house and move on to non-adjacent house (+2 index)
        2. Skip = skip current house and move on to next house (+1 index)

        Base case:
        - must be within bounds of the array (0 <= i <= len(arr))
        - If N = 2, its either arr[0] or arr[1]
        - If N = 1, its arr[0]
        - If N = 0, invalid qns

        Return value:
        - Max of both skip and take
        - Max of both cases (first index case, last index case)
        """
        # Edge cases
        n = len(nums)
        if n == 2:
            return max(nums[0], nums[-1])
        elif n == 1:
            return nums[0]
        
        @cache
        def dp(start: int, end: int):
            # base case, stay within bounds
            if start > end or start < 0:
                return 0
            # Decision 1, take the house and move on
            take = dp(start + 2, end) + nums[start]

            # Decision 2, skip the house and move on
            skip = dp(start + 1, end)

            # Return value: find maximum robbery
            return max(take, skip)

        # cases for first element and last element included
        # still within bounds of 0 <= i <= len(nums)
        case1 = dp(0, len(nums) - 2)
        case2 = dp(1, len(nums) - 1)

        # return val, find the maximum robbery for both cases
        return max(case1, case2)
