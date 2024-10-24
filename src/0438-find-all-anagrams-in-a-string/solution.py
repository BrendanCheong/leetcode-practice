class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # edge cases
        if len(s) < len(p):
            return []
        
        # create result array
        result = []
        
        # create target frequency array
        target = [0] * 26
        for c in p:
            target[ord(c) - ord('a')] += 1
            
        # create window frequency array
        window = [0] * 26
        
        # initialize first window
        for i in range(len(p)):
            window[ord(s[i]) - ord('a')] += 1
            
        # check if first window is anagram
        if window == target:
            result.append(0)
            
        # slide window and check rest
        for i in range(len(p), len(s)):
            # remove leftmost character from window
            window[ord(s[i-len(p)]) - ord('a')] -= 1
            # add new character to window
            window[ord(s[i]) - ord('a')] += 1
            
            # if frequencies match, we found an anagram, O(26) check
            if window == target:
                result.append(i - len(p) + 1)
                
        return result
