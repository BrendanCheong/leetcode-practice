class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Handle empty string case
        if not s:
            return 0
        
        # Dictionary for tracking characters (works for all characters)
        char_index = {}
        first, res = 0, 0
        
        for second in range(len(s)):
            # If the character is already in the current window, move 'first'
            if s[second] in char_index and char_index[s[second]] >= first:
                first = char_index[s[second]] + 1
            
            # Update the last seen index of the character
            char_index[s[second]] = second
            
            # Calculate the length of the current substring
            res = max(res, second - first + 1)
        
        return res
