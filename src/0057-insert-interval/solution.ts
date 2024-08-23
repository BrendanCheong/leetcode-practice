function insert(intervals: number[][], newInterval: number[]): number[][] {
    /**
    * 3 Scenarios:
    * 1. Add at the start
    * 2. Add at the end
    * 3. Merge the intervals and add
    */
    const res: number[][] = [];
    let [newIntervalStart, newIntervalEnd] = newInterval;

    for (let i = 0; i < intervals.length; i++) {
        const [currIntervalStart, currIntervalEnd] = intervals[i];

        // 1. place at start
        if (newIntervalEnd < currIntervalStart) {
            res.push([newIntervalStart, newIntervalEnd]);
            return res.concat(intervals.slice(i))
        }
        // 2. Place at end
        else if (newIntervalStart > currIntervalEnd) {
            res.push(intervals[i]);
        }
        // 3. Merge intervals
        else {
            newIntervalStart = Math.min(newIntervalStart, currIntervalStart)
            newIntervalEnd = Math.max(newIntervalEnd, currIntervalEnd);
        }
    }

    res.push([newIntervalStart, newIntervalEnd]);

    return res
};
