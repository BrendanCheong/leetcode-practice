from typing import *

class Solution:
    def isValid(self, s: str) -> bool:
        """
        Edge cases: What if the string is equal to one?
        what if the string is (()), its still invalid!
        """
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack
                
            
            
