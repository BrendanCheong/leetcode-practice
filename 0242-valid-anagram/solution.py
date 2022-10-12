from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        you can use a counter, or in this case you can
        use just one dictionary, then decrease the count of each letter
        if the letter count is not 0, its not an anagram
        """
        dct = defaultdict(int)
        for i, ele in enumerate(s):
            dct[ele] += 1
        for i, ele in enumerate(t):
            dct[ele] -= 1
        for k, v in dct.items():
            if (v != 0):
                return False
        return True
