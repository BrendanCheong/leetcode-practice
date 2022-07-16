from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for ele in nums:
            res = ele ^ res
        return res
