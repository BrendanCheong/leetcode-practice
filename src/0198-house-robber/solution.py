class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Consider the case [2,1,1,5] we must create a decision tree of all decisions.
        So its 2 and 1, 1 and 5 or 2 and 5. Note that we if we brute force we would have
        duplicate combinations. So we must use DP here!
        The sub-problem is:
        rob = max(nums[i] + rob[i + 2 : n], rob[i : n])
        So its either we take the number we have now plus the previous max value, or the
        current max value
        repeated values are found because we computed the previous max before.
        """
        # edge cases:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        
        dp = [nums[0], max(nums[0], nums[1])]
        i = 2
        while i < n:
            max_val = max(nums[i] + dp[0], dp[1])
            dp[0] = dp[1]
            dp[1] = max_val
            i += 1

        return dp[-1]

        
