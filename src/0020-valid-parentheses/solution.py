class Solution:
    def isValid(self, s: str) -> bool:
        """
        Algo is simple O(n) time, O(n) space.
        We keep adding starting brackets until we can find a closing bracket.
        By popping, we make sure we are always finding the best closing bracket
        """
        guide = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for char in s:
            if char not in guide:
                stack.append(char)
                continue
            else:
                if not stack or guide[char] != stack[-1]:
                    return False
                # Here we find that current {char} matches the top of stack
                # so we can close the bracket. Once closed, remove from stack
                # to move on to next character
                stack.pop()
        # Stack must be emptied
        return not stack
        
