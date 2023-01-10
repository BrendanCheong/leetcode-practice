from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Straight forward O(26n) solution as we have to do max(char_map.values()) with O(n) space

        The algo is like so: we want to find the maximum sliding window created, we start with left = 0 and right = 0, where right increments as we go along the string, and we add to the character count dict.


        """
        char_map = defaultdict(int)
        l, res = 0, 0
        for right, ele in enumerate(s):
            char_map[ele] += 1
            if (right - l + 1 - max(char_map.values())) > k:
                char_map[s[l]] -= 1
                l += 1

            res = max(res, right - l + 1)
        return res
        
