from collections import defaultdict

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashmap = defaultdict(int)
        for i in words:
            hashmap[i] += 1
        sorted_hashmap = sorted(hashmap, key=lambda x: (-hashmap[x], x))
        return sorted_hashmap[:k]
