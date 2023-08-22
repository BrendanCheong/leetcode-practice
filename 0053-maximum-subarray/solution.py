class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        DP memoised recursion tree solution
        """
        from functools import cache
        @cache
        def solve(i, must_pick):
            # Base Case, if reach end of array, I must decide to end
            # if I must pick the next num but end of array, pick 0
            # if no need to pick the next num, just return the smallest possible num 
            # so it doesn't mess with the max() function 
            if i >= len(nums):
                if must_pick:
                    return 0
                else:
                    return float("-inf")

            # Include current number and go on to the next number
            # this is the first decision
            include_current = nums[i] + solve(i + 1, True)

            # Exclude current number (only if must_pick is False)
            # this is the second decision
            exclude_current = 0 if must_pick else solve(i + 1, False)

            return max(include_current, exclude_current)

        return solve(0, False)
        

        
