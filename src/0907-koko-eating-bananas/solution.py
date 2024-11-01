class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Clearly we are searching for what level of k is ideal.
        So its a binary search, so we need to find the lower and upper bounds
        k = 0 doesn't make sense, we want to eat bananas
        lower: 1
        upper: max(piles)

        basically, 'k' must be <= h, and as small as possible

        Thats the first part. The second part is, given k, how do we know if the k is the number we want?
        compare the time taken to eat all bananas with h hours
        """
        lower, upper = 1, max(piles)
        res = upper
        while lower <= upper:
            k = (upper + lower) // 2
            total_time = 0
            for pile in piles:
                # time to eat is pile/eating_rate, eating rate is k. We math.ceil to round up, cuz lets say its 3/4. Means answer is 1 hour
                total_time += math.ceil(float(pile) / k)
            if total_time <= h:
                # less than equal, means we found a valid k, but could we go smaller? We dont know until we try!
                res = k
                # lets aim for small times
                upper = k - 1
            else:
                # we are too small, lets aim for bigger times
                lower = k + 1
        return res

        
