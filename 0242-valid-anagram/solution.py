from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = Counter(s)
        count2 = Counter(t)
        return count1 == count2
        
