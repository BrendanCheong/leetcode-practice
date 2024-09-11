class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        vertical_xor = start ^ goal
        return vertical_xor.bit_count()
