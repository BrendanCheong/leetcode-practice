class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        If you notice the palindrome, the longest palindrome is gonna be
        largest even number of occurrences for each character to the length.
        If there is an odd count number of elements, + 1 to the length
        """
        from collections import Counter
        c = Counter(s)
        length = 0
        for v in c.values():
            even_count = v // 2 * 2  # Turns odd values into even values
            length += even_count    # Add the even count to the length

        # Check if there's any odd numbers
        if any(v % 2 == 1 for v in c.values()):
            length += 1

        return length
        
        
