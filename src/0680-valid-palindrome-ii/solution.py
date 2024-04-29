class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        The solution is just to just recompute the palindrome again 
        for when either mismtach letter is removed.
        
        But what if you are allowed to remove n elements from the palindrome?
        The what happens? we will have to recursively use call the palindrome substring helper
        function, until we run out of allowed n removal of elements
            
        """
#         def palindrome(i, j):
#             while i < j:
#                 if s[i] != s[j]:
#                     return False
#                 j -= 1
#                 i += 1
#             return True

#         i = 0
#         j = len(s) - 1
#         while i < j:
#             if s[i] != s[j]:
#                 return palindrome(i + 1, j) or palindrome(i, j - 1)
#             j -= 1
#             i += 1
        
#         return True
        def palindrome_substring(i, j, removals):
            while i < j:
                if s[i] != s[j]:
                    return removals > 0 and (palindrome_substring(i + 1, j, removals - 1) or palindrome_substring(i, j - 1, removals - 1))
                i += 1
                j -= 1
            return True
        removals = 1
        return palindrome_substring(0, len(s) - 1, removals)
