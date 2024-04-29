from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        O(1) space solution
        O(n) time
        """
        c = Counter(nums)
        n = len(nums)
        check = n // 2
        for k, v in c.items():
            if v > check:
                return k
        return 0


        
        
