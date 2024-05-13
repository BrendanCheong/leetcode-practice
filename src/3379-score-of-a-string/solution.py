from functools import reduce

class Solution:
    def scoreOfString(self, s: str) -> int:
        return reduce(
            lambda total, pair: total + abs(ord(pair[1]) - ord(pair[0])), 
            zip(s, s[1:]), 
            0
        )
