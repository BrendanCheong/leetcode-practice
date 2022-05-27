from typing import *

class Solution:
    def isValid(self, s: str) -> bool:
        """
        Edge cases: What if the string is equal to one?
        what if the string is (()), its still invalid!
        """
        brackets: Dict[str] = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = list()
        if len(s) == 1:
            return False
        for char in s:
            if char in brackets:
                stack.append(char)
                continue
            if not stack or brackets[stack.pop()] != char:
                return False

        return not stack
