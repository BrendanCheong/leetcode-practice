class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Bounds:
            i: 0 - len(coins)
            x: 0 - amount

        Order:
            general term is a minimum of take and skip

            take:
                => i is constant
                => x - coins[i], note coins[i] > 0
                => since x - coins[i] < x (always look at change vs original)
                => small before big
                => 0 before amount, we solve smaller subproblems

            skip:
                => x is constant
                => i + 1 > i (change vs original)
                => big before small
                => len(coins) before 0, we process larger indices
        """
        # Base case: no combination possible, coin collected < amount. We'll just make all impossible for now then update later
        dp = [float('inf')] * (amount + 1)

        # Base case: 0 coins to make amount 0, x == 0 case
        dp[0] = 0

        # Loop through amounts and coins
        for coin in coins:
            # this serves as our dp[i + 1][x], no need for i + 1 since we start from the coin value
            for x in range(coin, amount + 1):
                # Decision 1: take the coin at this index, if the coin value is <= current amount
                if coin <= x:
                    take = dp[x - coin] + 1
                else:
                    take = float('inf')

                # Decision 2: skip this coin, move on to the next coin to get to amount
                skip = dp[x]

                # End case, we needed fewest combination
                dp[x] = min(take, skip)

        # If dp[0][amount] is still infinity, it means we cannot make that amount with the given coins
        return -1 if dp[amount] == float('inf') else dp[amount]
