function topKFrequent(nums: number[], k: number): number[] {
    const occurence = new Map<number, number>();
    for (const n of nums) {
        if (occurence.has(n)) {
            occurence.set(n, occurence.get(n) + 1);
        } else {
            occurence.set(n, 1);
        }
    }

    // Our bucket sort is like so
    // number of occurences array => contains number for that occurence
    // create as many buckets as there is elements
    // Step 2: Create the buckets array (each bucket should be a separate empty array)
    const buckets = Array.from({ length: nums.length + 1 }, () => [])

    for (const [number, occured] of occurence) {
        buckets[occured].push(number)
    }

    // Step 3, iterate backwards, as last few buckets are the top occuring elements
    const res = [];
    console.log(buckets)
    for (let i = buckets.length - 1; i >= 0; i--) {
        if (res.length === k) {
            return res;
        }
        if (buckets[i].length > 0) {
            res.push(...buckets[i])
        }
    }
    return res;
};
