class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        O(1) space solution
        O(n) time
        """
        res, count = 0, 0
        for ele in nums:
            if not count:
                res = ele
            if ele != res:
                count -= 1
            else:
                count += 1
        return res
        
