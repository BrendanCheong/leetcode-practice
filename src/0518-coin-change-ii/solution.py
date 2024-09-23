from functools import cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        Top down approach
        Time: O(n^2)
        Space: O(n)
        """
        @cache
        def dp(start: int, current_amount: int):
            # Base case or Bounds of the problem
            # we cant go beyond coins array
            if start == len(coins):
                # this means that, found our answer, or we need to back up the recursion tree for our answer (dead-end)
                return 1 if current_amount == 0 else 0

            # Decision 1: When do we take a coin? when we cant reach the amount
            take = 0
            if coins[start] <= current_amount:
                take = dp(start, current_amount - coins[start])
            
            # Decision 2: we skip this coin, as taking this coin will not make us closer to amount needed
            skip = dp(start + 1, current_amount)
            
            # end case, we take the sum of our decisions
            return skip + take
        return dp(0, amount)
