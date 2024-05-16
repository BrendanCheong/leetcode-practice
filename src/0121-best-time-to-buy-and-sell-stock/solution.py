class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Greedy sliding window problem, we compute every scenario where we can get 
        a profit!

        The sliding window starts at the smallest price we found so far
        Then compute the profit when the current price goes high (but low sell high)

        Time: O(n)
        Space: O(1)
        """
        min_price, profit = prices[0], 0
        for p in prices:
            if p < min_price:
                # update the new minimum price, this is the start of
                # our sliding window
                min_price = p
            # Greedily compute every scenario where the current price
            # can bring us a profit
            elif p - min_price > profit:
                profit = max(p - min_price, profit)
        return profit


