class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        If you want to reach the end, your furthest possible position must
        be greater than the every index you face!
        """
        position = 0
        for i, jump in enumerate(nums):
            if i > position:
                # if the index is greater than the furthest possible position that can be jumped
                # it means that our furthest position is less than whats required
                # so we terminate 
                return False
            position = max(position, i + jump)
        return True
