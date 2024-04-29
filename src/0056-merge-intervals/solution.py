class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Time: O(n log n), we must sort based on start value
        
        """
        START, END = 0, -1
        intervals = sorted(intervals, key=lambda int: int[START])
        # usually we can assume that its sorted according to start time, but in this case its not lol.
        res = []
        for i, curr_int in enumerate(intervals):
            prev = res[END] if res else None
            # edge cases:
            # new interval goes before all the intervals, no merging
            # new interval goes after all the intervals, no merging
            if (i == 0):
                # edge case where there is only 1 interval
                res.append(curr_int)
            elif (curr_int[START] <= prev[END]):
                # merge when there is an overlap
                merged_interval = [min(curr_int[START], prev[START]), max(curr_int[END], prev[END])]
                res.pop() and res.append(merged_interval)
            else:
                # if there is no overlap, just append
                res.append(curr_int)
        return res
        
