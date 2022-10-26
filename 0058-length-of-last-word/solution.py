class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        The single O(n) loop solution!
        The answer must be less than len(s)
        
        The trick is to iterate backwards!
        If we encounter a letter with a space, we decrease
        If we encounter a non space, we increase!
        """
        if not s:
            return 0
        
        letter_found, length = False, 0
        for i in range(len(s) - 1, -1, -1):
            print(i)
            if s[i] != ' ':
                letter_found = True
                length += 1
            if letter_found == True and (s[i] == ' ' or i == 0):
                return length
        return 0
