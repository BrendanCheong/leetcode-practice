class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Since the array is already sorted, we can use binary search.
        Note that middle of array is first pointer + (last - first) // 2

        Also note that binary search is about chopping the array into half based
        on the 2 pointers

        You may find that other binary search qns have different if statements
        But all evolve around left/right = middle -1/+1

        Time: O(log n)
        Space: O(1)
        """
        left, right = 0, len(nums) - 1

        # We use left <= right and not left < right
        # for edge case when array is length 1, like arr = [5]
        while left <= right:
            middle = left + ((right - left) // 2)
            if nums[middle] < target:
                # we are too small, so we need to go bigger
                # which is the right hand side
                left = middle + 1
            elif nums[middle] > target:
                # we are too big, so we need go smaller
                # which is left hand side
                right = middle - 1
            else:
                return middle
        # If no answer can be found
        return -1
