from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = Counter(nums).most_common()
        return [res[-1][0], res[-2][0]]
        
