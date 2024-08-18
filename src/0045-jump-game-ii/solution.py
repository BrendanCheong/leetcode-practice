class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        reach: Tracks the farthest index that can be reached at any point.
        count: Counts the number of jumps made.
        last: Represents the rightmost index reached with the current number of jumps.

        Greedy Approach: This solution is a greedy algorithm. It always jumps to the farthest possible position to minimize the total number of jumps.

Efficient: By tracking the farthest reachable point (reach) and updating the jump count only when necessary, the solution efficiently finds the minimum jumps needed.
        """
        reach, count, last = 0, 0, 0

        # Loop through the array excluding the last element
        for i, n in enumerate(nums[:-1]):
            # 1. maximum between reach and i + nums[i]
            reach = max(reach, i + n)

            # 2. # If i has reached the last index that can be reached with the current number of jumps
            if i == last:
                # 3. Update last to the new maximum reachable index
                last = reach
                count += 1
        return count
