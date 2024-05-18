from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        From the getgo this is quite obviously a sliding window kind of qns.
        But how do we decide what is out sliding window? We can first start of by
        having the window at the beginning, left and right = 0 index.
        For each sliding window, we can calculate whats the best character to remove
        by replacing window - max_occuring characters. However this result count must be <= k, if its more than k we:
        1. Cannot replace more than k characters
        2. So we change the sliding window, by pushing left forward
        If the window is valid (can replace k characters), we can expand the window.
        Then keep track of the longest window we have found.
        The formula is window_size - max_occuring_char_count, because our substring
        will be made of the max occuring character, so replace those which are not!

        Note: If instead of characters it was some kind of symbol (more than 26 possible chars)
        We would use a min heap to find the minimum quickly

        Time: O(26N), since max 26 possible characters to find least frequent char in O(26)
        Space: O(26)
        """
        left, res = 0, 0
        char_count = defaultdict(int)

        for right, char in enumerate(s):
            char_count[char] += 1
            # check if the window is valid
            # if not valid we must move the left pointer until valid
            # Window length has a plus one since we start at 0 index
            while ((right - left) + 1) - max(char_count.values()) > k:
                char_count[s[left]] -= 1 
                left += 1
            res = max((right - left) + 1, res)
        return res
    
    def characterReplacementOptimised(self, s: str, k: int) -> int:
        # Optional optimisation, keep track of max occuring element frequency so avoid O(26) computation
        left, res, max_freq = 0, 0, 0
        char_count = defaultdict(int)

        for right, char in enumerate(s):
            char_count[char] += 1
            max_freq = max(max_freq, char_count[char])

            while ((right - left) + 1) - max_freq > k:
                char_count[s[left]] -= 1
                left += 1
            res = max((right - left) + 1, res)
        return res



