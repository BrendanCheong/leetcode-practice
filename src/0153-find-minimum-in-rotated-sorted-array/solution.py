class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        The trick here is that the numbers are only rotated to the right.
        Ex: 6, 7, 0, 1, 2, 4, 5. Here we rotated 2 times! notice that if we only look at the right most number compare with middle number,
        we can tell that we rotated such that big numbers are on the left. This is one kind of rotation

        Ex: 0, 1, 2, 4, 5, 6 ,7. Here we rotated 0 or 7 times, where all the numbers made a full turn.
        Look at the right most number, now we can tell big numbers are on the right.

        Ex: 4, 5, 6, 7, 0, 1, 2. 

        Theres only 2 kinds of states, full rotation or partial rotation. And partial rotation always has big numbers on the left
        """
        left, right, curr_min = 0, len(nums) - 1, float("inf")
        while left <= right:
            mid = (left + right) // 2
            curr_min = min(curr_min, nums[mid])
            # check the rightmost number
            if nums[mid] > nums[right]:
                # means big numbers are on left, small numbers are on right
                left = mid + 1
            else:
                # means small numbers are on left, big numbers on right
                right = mid - 1
        return curr_min

