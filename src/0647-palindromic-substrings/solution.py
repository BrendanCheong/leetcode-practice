class Solution:
    def expandPalindrome(self, l: int, r: int, s: str) -> int:
        count, length = 0, len(s)
        while (l >= 0 and r < length and s[l] == s[r]):
            l -= 1
            r += 1
            count += 1
        return count
    def countSubstrings(self, s: str) -> int:
        """
        This is a sliding window problem
        """
        ans = 0
        for i in range(len(s)):
            ans += self.expandPalindrome(i, i, s) + self.expandPalindrome(i, i + 1, s)
        return ans
            
        
