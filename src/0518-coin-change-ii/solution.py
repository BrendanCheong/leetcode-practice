from functools import cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        Bottom-up approach

        Bounds:
            i: [0, len(coins)]
            x: [0, amount]
        
        Order:
            general term i, x, requires general term take and skip.

            Term i, x:
                take: i, x - coins[i]
                    - since 'i' does not change
                    - x-coins[i] before x
                    - since coins[i] > 0, x - coins[i] < x
                    - small before big
                    - 0 before amount

                skip: i + 1, x
                    - since 'x' does not change
                    - i+1 before i
                    - since i+1 > i
                    - big before small
                    - biggest value of i is len(coins), smallest is 0 (see the bounds above)
                    - len(coins) before 0

                order of for loops dont matter here, since its eiter take first or skip first

            General term: take + skip

            1. We can just replace return statements with dp[i][x], since our recursion call was func_dp(i, x)
            2. base case: i == len(coins): 1 if x == 0 else 0, we can just make default value 0. Then if x == 0 when len(coins)
            is i, then the answer is dp[len(coins)][0] = 1
        """

        dp = [1] + [0] * amount

        for c in coins:
            for x in range(c, amount + 1):
                dp[x] += dp[x - c]
        
        return dp[amount]

