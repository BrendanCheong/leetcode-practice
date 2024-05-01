from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        string_s_count, string_t_count = Counter(s), Counter(t)

        # You can do Counter(t) == Counter(s) but this is the 
        # less abstracted version
        for k, v in string_s_count.items():
            if string_t_count[k] != v:
                return False
        return True
