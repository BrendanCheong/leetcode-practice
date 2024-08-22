class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Basically, we can either sort by start time or end time. Lets say
        we sort by start time.

        The interval to remove if overlapping is the interval that has the
        biggest/latest end time. This is because if we remove
        the earlier end time we will have to still remove another interval
        Like:
        [1, 3], [2, 5], [4, 6]
        if I remove (1, 3), I still have to remove (2, 5).
        So just remove (2, 5)

        Removal based on end time
        """
        intervals.sort(key=lambda x: x[0])
        curr_end = intervals[0][-1]
        removed_count = 0
        for i in range(1, len(intervals)):
            # Check if intervals do not merge
            start_time, end_time = intervals[i][0], intervals[i][-1]
            if start_time >= curr_end:
                # Update the most recent end time
                curr_end = end_time
            else:
                # Here we have to merge
                removed_count += 1
                # only select the smallest end time, removing the biggest end time
                curr_end = min(end_time, curr_end)
        return removed_count


