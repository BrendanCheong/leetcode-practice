class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        We are gonna use Kadanes greedy algo here.
        Basically, we reset the sliding window once the currSum < 0.
        So lets say we are 4, -1, 5, the window is fine.
        But if its 4, -1, 5, -7, 2, 3, the window is reset at -7 (since the sum is now < 0), we start
        from the next number after -7.

        We can use greedy here because we want the maximum possible value
        and negative values don't let us do that

        Time: O(n)
        Space: O(1)
        """
        max_sum = nums[0]
        curr_sum = 0
        for n in nums:
            curr_sum += n
            max_sum = max(max_sum, curr_sum)

            # reset window if less than 0, greedy algos want maximum possible number!
            if curr_sum < 0:
                curr_sum = 0
        return max_sum
