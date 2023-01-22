class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Create the decision tree for this, its either buying/selling or cooldown, 2 decisions, and theres
        a forced decision to cooldown if we sell, so its almost a binary tree but with some single branches

        Time: O(n) with cache, with no cache(create entire tree) its O(2^n)
        space: O(n) with cache, O(2^n) with whole tree
        """
        cache = dict() #key = (i, buying boolean), val = max_profit
        def dfs(index: int, buying: bool) -> int:
            if index >= len(prices): # empty array of prices, so return 0. When we finish iterating
                return 0
            if (index, buying) in cache:
                return cache[(index, buying)]
            # now to do the decision, are we buying or selling state?
            if buying:
                # if buying, we either buy or cooldown
                # we must create the subtrees for both
                buy = dfs(index + 1, not buying) - prices[index] # change state from buying to not buying since we bought already, we bought so we lost some money
                cooldown = dfs(index + 1, buying)

                #add to the cache, compute the max value
                cache[(index, buying)] = max(buy, cooldown)
            else:
                # if selling, we either sell or cooldown
                # create subtrees for both
                sell = dfs(index + 2, not buying) + prices[index] # increment by 2 because we HAVE to take a cooldown day if we sell, we sold so we made money
                cooldown = dfs(index + 1, buying)
                cache[(index, buying)] = max(sell, cooldown)
            return cache[(index, buying)]
        
        return dfs(0, True) # we are always buying when we start from the beginning, we cannot be selling

