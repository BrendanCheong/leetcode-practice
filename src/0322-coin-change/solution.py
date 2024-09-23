from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(start: int, current_amount: int) -> int:
            # Base case: If we successfully found the amount needed, we return 0 (go back up the recursion tree)
            # means we have chosen all the needed coins, amount is 0
            if current_amount == 0:
                return 0
            # Base case: Invalid state, if we ran out of coins to choose from or overshot the amount, mark as invalid state
            # overshot meaning we took the wrong coin, ran out of coins means reached end of bounds
            # use infinity here since its min problem, as infinity means we wont choose this combination with min()
            if start == len(coins) or current_amount < 0:
                return float('inf')

            # Decision 1: take the coin at this index, +1 means we found a valid coin to take
            take = dp(start, current_amount - coins[start]) + 1

            # Decision 2: skip this coin, move on to the next coin to get to amount
            skip = dp(start + 1, current_amount)

            # End case, we needed fewest combination
            return min(take, skip)
        res = dp(0, amount)
        return -1 if res == float('inf') else res
