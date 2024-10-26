from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        """
        Same idea as modified bucket sort
        Get frequency of elements: ele -> freq
        Then create a bucket sort based on freq
        freq -> [ele1, ele2]
        Then iterate backwards

        Time: O(n)
        SpaceL O(n)
        """
        counts = defaultdict(int)
        for string in s:
            counts[string] += 1
        buckets = [[] for _ in range(len(s) + 1)]

        # populate by freq -> ele
        for s, freq in counts.items():
            buckets[freq].append(s)
        res = ""
        for i in range(len(buckets) - 1, -1, -1):
            if buckets[i]:
                for c in buckets[i]:
                    res += c * i
        return res

        
