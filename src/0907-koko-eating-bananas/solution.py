class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        The intuition in this case is that the number 'k' is actually a number between
        k = 1 and max value of piles. Why? k is eating speed, k = 0 doesn't make sense cuz we eat no bananas
        if k was the largest value of the piles, we could everything in 1 hour!
        But hey, we want the minimum 'k', so now we have an lower and upper bound
        1 <= k <= max_pile

        Sounds familiar? its a binary search! We just keep finding the hours it took to eat all the bananas
        and close to 'h', by testing the values of k within 1 <= k <= max_pile.
        Instead of testing all of k, we just binary search to get close to 'h'

        Time: O(n * log(max_piles))
        Space: O(1)
        """
        left, right = 1, max(piles)
        res = right
        while left <= right:
            accumulated_time = 0
            k = left + ((right - left)) // 2
            # given k, lets the total possible hours
            for banana in piles:
                # We round up in this case
                # if we have 3 bananas and k = 4, we take 1 hour, so 3/4 round up is 1
                accumulated_time += math.ceil(float(banana) / k)
            if accumulated_time <= h:
                # we are too fast, go slower
                # We do result = k, because we have technically found a solution
                # but its not the minimum k, so we keep searching
                res = k
                right = k - 1
            else:
                # we are too slow, go faster
                left = k + 1
        return res

        
