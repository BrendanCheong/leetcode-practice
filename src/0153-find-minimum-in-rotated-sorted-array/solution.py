class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        In this case, whenever we rotate, we will always put larger values to
        the left of the array (thats what the qns describes). Since there is always
        at least one rotation, we can conclude that one part of the array contains sorted
        bigger numbers, the other sorted smaller numbers.

        If we're in the so called smaller numbers, we probably already found our answer,
        but we should check the other sorted portion of the array just in case
        Elsewise, if we're in the big sorted, check the smaller sorted numbers.

        The array is not rotated at all, meaning the smallest element is at the beginning.

        The array is rotated, which creates a pivot point where the pattern changes.

        nums[mid] >= nums[left]
            - search right
        nums[mid] < nums[right]
            - search left

        Time: O(log n)
        Space: O(1)
        """
        left, right, current_min = 0, len(nums) - 1, float("inf")
        while left <= right:
            middle = left + ((right - left) // 2)
            current_min = min(current_min, nums[middle])

            # The left has the minimum
            # Array is likely not rotated, so smallest starts from beginning
            if nums[right] > nums[middle]:
                right = middle - 1

            # The right has the minimum
            # Array is likely rotated, so smallest starts at the right far end
            else:
                left = middle + 1

        return current_min


