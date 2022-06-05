class Solution:
    def isPalindrome(self, s: str) -> bool:
        processed = ''.join(filter(str.isalnum, s.lower()))
        return processed == processed[::-1]
        
