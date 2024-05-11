class Solution:
    def mySqrt(self, x: int) -> int:
        """
        This is a binary search question, as we can go from 0 to the ideal number by seeing if the product is
        close to the answer of x

        So we test by having mid * mid, where mid is between 0 and x

        Time: O(log n)
        Space: O(1)
        """
        left, right = 0, x
        while left <= right:
            mid = left + ((right - left) // 2)
            if mid * mid < x:
                left = mid + 1
            elif mid * mid > x:
                right = mid - 1
            else:
                return mid
        return right
