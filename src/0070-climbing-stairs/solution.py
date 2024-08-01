class Solution:
    def climbStairs(self, n: int) -> int:
        """
        This is a DP question, as it requires optimising the recursion tree.
        The decision we can make is, we can make the left subtree = n - 1 and the right
        subtree = n - 2.

        We can either do this using 
        1. 1D DP - memoization with a hashmap (top-down DP), 
        2. 1D DP - bottom-up approach with 2 values or a small array
        """
        if n < 2:
            return 1
        else:
            dp = [1, 1]
            i = 2
            while i <= n:
                next_val = dp[1] + dp[0]
                dp[0] = dp[1]
                dp[1] = next_val
                i += 1
            return dp[1]
