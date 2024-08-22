class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        There are 3 scenarios
        1. I just put the new interval first then the next interval
        2. Merge and combine the intervals
        3. I put the new interval at the very end

        Time: O(n)
        Space: O(n)
        """
        res = []
        newInterval_start, newInterval_end = newInterval[0], newInterval[-1]

        for i, interval in enumerate(intervals):
            curr_start, curr_end = interval[0], interval[-1]
            # 1. the new interval must be placed before
            # since its sorted intervals, we can return early
            if newInterval_end < curr_start:
                res.append([newInterval_start, newInterval_end])
                # append rest of the array
                return res + intervals[i:]
            # 2. the new interval must be placed at the end
            # Note: we can't decide to place at the end until we iterated through the whole thing
            elif newInterval_start > curr_end:
                res.append(interval)
            # Merge the intervals
            else:
                merged_interval = [
                    min(newInterval_start, curr_start),
                    max(newInterval_end, curr_end)
                ]
                # Update new interval
                newInterval_start, newInterval_end = merged_interval[0], merged_interval[-1]

        # Remember now we can decide to add the newInterval at the end
        res.append([newInterval_start, newInterval_end])
        
        return res

