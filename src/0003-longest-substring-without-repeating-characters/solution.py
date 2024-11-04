class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        char_position = dict()
        left, res = 0, 0
        for right, ele in enumerate(s):
            if ele in char_position:
                left = max(char_position[ele] + 1, left)
            char_position[ele] = right
            res = max(res, right - left + 1)
        return res

