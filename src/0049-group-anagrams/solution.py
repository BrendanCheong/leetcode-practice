class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        If we sort a word that is an anagram, we essentially get the common anagram word
        Like if we sort "eat" and "tea" we get both "aet"
        We can then use hashmaps to store these results

        You could also speed up the default sort using bucket sort, which is O(n) sort
        and not n log n

        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        ans[tuple(count)].append(s)

        Since max length is n = 100, fastest speed is O(100), slow sort is O(100 log(100))

        Time: O(n * n log n) if not bucket sort
        O(n) if bucket sort
        Space: O(n)
        """
        hashmap = defaultdict(list)
        for i, word in enumerate(strs):
            common_word = ''.join(sorted(word))
            hashmap[common_word].append(word)

        return list(hashmap.values())
