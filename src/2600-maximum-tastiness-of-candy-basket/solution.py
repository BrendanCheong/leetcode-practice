class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        """
        The idea here is this:
        1. Given a tastiness (max tastiness)
        2. Search for the k values to make up that tastiness
        We dont know what the max tastiness is, so we can go through all tastiness values
        And to find the k values that make up that tastiness, we can use binary search O(log n)
        So for all M tastiness, use log N each time

        Time: O(M log N)
        Space: O(1)
        """
        # 1. Sort the array in O(n log n) to do binary search
        price.sort()
        def canMakeBasket(tastiness: int) -> bool:
            """
            Given a tastiness, can we make a basket? if not we'll have to move on
            to other tastiness values.
            We greedily form the basket here, because we want to find a valid solution
            by going through all solutions (array is sorted also)
            """
            count = 1
            last = price[0]
            for candy in price[1:]:
                tasty_value = candy - last
                if tasty_value >= tastiness:
                    count += 1
                    last = candy
            return count >= k
        
        # 2. Since we want max possible tastiness, we go from 0 to max(tastiness)
        # which is max - min candy
        left, right = 0, price[-1] - price[0]

        while left <= right:
            mid = (left + right) // 2
            if canMakeBasket(mid):
                # tastiness found! it could be the max tastiness
                # Since bigger numbers are towards the right of the array, we can find more tastiness there
                # we want the maximum tastiness
                left = mid + 1
            else:
                right = mid - 1
        return right
