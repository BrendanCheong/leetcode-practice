class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        The window can either be a middle window (normal Kadane's algorithm)
        or a circular window (where the end connects to the start).

        To find circular window, its just total - minimum middle window = max
        circular window

        Time: O(n)
        Space: O(1)
        """
        # Initialize variables
        global_max, global_min = nums[0], nums[0]
        curr_max, curr_min = 0, 0
        total = 0

        for n in nums:
            # Update current max and min subarray sums
            curr_max = max(n, curr_max + n)
            curr_min = min(n, curr_min + n)

            # Update global max and min
            global_max = max(global_max, curr_max)
            global_min = min(global_min, curr_min)

            # Update total sum
            total += n

        # If all numbers are negative, return the maximum found using Kadane's algorithm
        if global_max < 0:
            return global_max
        else:
            # Return the maximum of non-circular and circular subarray sums
            return max(global_max, total - global_min)
