function eraseOverlapIntervals(intervals: number[][]): number {
    /**
      * The interval to remove is the one with the smallest end timing
     */
     // sort ascending by start timings
     intervals.sort((a, b) => a[0] - b[0]);
     let currentEndTime = intervals[0].at(-1);
     let res = 0

     for (let i = 1; i < intervals.length; i++) {
        const [startTime, endTime] = intervals[i];

        // Check if can be placed infront
        if (currentEndTime <= startTime) {
            currentEndTime = endTime
        } else {
            res++;
            currentEndTime = Math.min(currentEndTime, endTime)
        }
     }
     return res;

};
