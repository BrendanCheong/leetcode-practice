class Solution:
    def mySqrt(self, x: int) -> int:
        """
        This question is secretly a binary search question
        
        Think of Brute force first, we would check every number from 1
        x 1 all the way to n x n to find the closet number. Example:
        
        1 x 1 = 1
        2 x 2 = 4
        3 x 3 = 9
        
        we can use binary search to find the correct digit. Upper bound is always  x // 2 since square root of the number is always less . Edge case for when if x < 2, the only square root is itself
        """
        if x >= 2:
            left, right = 2, x
            
            while left <= right:
                mid = left + (right - left) // 2
                number = mid * mid
                if number > x:
                    right = mid - 1
                elif number < x:
                    left = mid + 1
                else:
                    return mid
            return right
        return x
        
