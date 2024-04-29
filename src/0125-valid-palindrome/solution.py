class Solution:
    def isPalindrome(self, s: str) -> bool:
        # do the 2 pointers technique
        # this is a O(1) space technique
        # With a O(n) time
        start = 0
        end = len(s) - 1
        while start < end: # iterate until start passes the end
            while not s[start].isalnum() and start < end:
                # skip spaces/non-alphanumeric characters
                # do not execute if the pointers pass each other (edge case)
                start += 1 # move pointer towards end
            while not s[end].isalnum() and start < end:
                # same idea here
                end -= 1 # move pointer to the start
            # if statement must come first to check edge case of beginning letter
            # account for edge case of lowercased letters.
            # do not do s = s.lower() as its O(N) time
            if (s[start].lower() != s[end].lower()):
                return False
            start += 1
            end -= 1
        return True
        
        
