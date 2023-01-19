import math

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        The trick is that every element value - 1 = an index in the array
        The trick is that for every element, we will take its val - 1 and make nums[val - 1] = -nums[val - 1], marking it as a negative number

        if we run into another same number, WE WILL ALWAYS go back to the same index, and we will know if duplicate if its a negative number
        """
        # edge case, numbers ahead can be marked as negative, so can numbers behind. So we must use absolute
        res = []
        for i, ele in enumerate(nums):
            new_idx = abs(nums[i]) - 1
            if nums[new_idx] < 0:
                res.append(abs(ele))
            nums[new_idx] *= - 1
        return res

