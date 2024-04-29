# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        Binary Search, O(log N) time using a weird question
        """
        left, right = 1, n # we start from version 1, stop at given n version
        
        # binary search terminates when left == right or left more than right
        while left < right:
            mid = left + (right - left) // 2
            if (isBadVersion(mid)):
                # we need to go left, so we shift right pointer to the left
                right = mid
            else:
                # we need to go right so we shift left pointer to right
                left = mid + 1
        return right # can return left or right doesn't matter
        
        
