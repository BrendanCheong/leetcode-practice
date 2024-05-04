class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        2 pointer solution with minimal memory usage.
        Have 2 pointers, one on each end of the string
        left pointer goes right, right pointer goes left, stop until they cross
        Skip non alpha numeric characters by just progressing the pointers when you see one
        For each character we compare it, if its not the same we return False

        Time: O(n)
        Space: O(1)
        """
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[right].lower() != s[left].lower():
                return False
            left += 1
            right -= 1
        return True

