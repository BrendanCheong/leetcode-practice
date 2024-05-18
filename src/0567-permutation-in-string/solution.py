from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        The most straight foward solution is to create a sliding window.
        Our slidng window will have the size of s1
        Then move the window throughout s2, if the window is converted to hashmap with character count
        equal to that of the hashmap character count of s1, we can return true

        Time: O(26) + O(n) = O(n)
        Space: O(n)
        """
        s1_counter = Counter(s1)
        window = Counter(s2[:len(s1)])  # Initialize window with the first len(s1) characters of s2

        # O(26) Check
        if s1_counter == window:
            return True

        for right in range(len(s1), len(s2)):
            window_start = right - len(s1)
            start_char, end_char = s2[window_start], s2[right]
            window[start_char] -= 1  # Remove the starting/leftmost character from the window

            # Clean up counter, so we dont have to O(26) check all the time
            if window[start_char] == 0:
                del window[start_char]
    
            window[end_char] += 1  # Add the new character to the window

            # O(26) operation
            if s1_counter == window:
                return True
        return False

        
