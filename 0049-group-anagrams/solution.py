from collections import Counter
from collections import defaultdict
import string

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            alphabet = dict.fromkeys(string.ascii_lowercase, 0)
            for char in word:
                alphabet[char] += 1
            key = tuple(alphabet.items())
            res[key].append(word)
        return res.values()
                
        
