class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        After sorting, merge overlapping intervals.
        An interval can be merged if
        - The start of the next interval is less than or equal to the end of the current interval.
        """
        # Edge case
        if not intervals:
            return []

        # We must sort to get intervals starting from the start timing in O(n log n)
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]

        # O(n) time to loop through all
        for i in range(1, len(intervals)):
            current_interval = res[-1]
            next_interval = intervals[i]
            # Check if can merge, then merge
            if next_interval[0] <= current_interval[-1]:
                # Note the ends are not sorted order, so we must find highest
                res[-1] = [current_interval[0], max(next_interval[-1], current_interval[-1])]
            else:
                res.append(intervals[i])
        return res

