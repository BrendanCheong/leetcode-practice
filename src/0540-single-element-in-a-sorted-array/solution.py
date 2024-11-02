class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        nums = [ 1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8 ]
        first:   ^     ^     ^     ^  ^     ^     ^     ^
        index:   0     2     4     6  7     9     11    13
        So clearly after the single number, the rest of the duplicated numbers are odd indices
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (right + left) // 2
            # make mid even just for the check
            if mid % 2 == 1:
                mid -= 1
            
            if nums[mid] == nums[mid + 1]:
                # we are on even number index. Right now we are on a valid pair
                # so to the left are more even index pairs, and the right probably odd index pairs
                # so since the single number is on the tail end of this series of even index pairs, we should
                # go to the right. + 2 because we want to skip this pair we are on
                left = mid + 2
            else:
                # means we are on the odd index pairs, so the single number is more to the left
                # which is the tail end of the even index pairs. No -1 or -2, we want to maintain that we 
                # always start on even indexes
                right = mid
        return nums[left]
