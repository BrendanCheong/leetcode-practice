from functools import cache
class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        # Bounds, 0 to n
        dp = [0] * (n + 1)

        # edge case, n <= 1 is 1
        dp[0] = 1
        dp[1] = 1

        # outer loop, from 2 to n + 1, since we handled base cases
        for i in range(2, n + 1):
            # the same as the recursive function (n - 1) + (n - 2)
            dp[i] = dp[i - 1] + dp[i - 2]

        # return the end
        return dp[n]
