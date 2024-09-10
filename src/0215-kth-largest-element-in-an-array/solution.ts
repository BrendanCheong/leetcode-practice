function findKthLargest(nums: number[], k: number): number {
    const smallest = Math.min(...nums);
    const biggest = Math.max(...nums);

    // 1. Create the bucket, I am using bucket sort, so if I have smallest -1 and biggest 5
    // means I have indexes for numbers -1 to 5, which is 6 elements
    // [0, 0, 0, 0, 0, 0];
    const occurences = new Array(biggest - smallest + 1).fill(0);

    // 2. Fill the buckets, if negative number, I can go at the back
    // so for -1 to 5, -1 is the first element and so on
    for (const n of nums) {
        occurences[n - smallest]++;
    }

    // 3. Find the kth largest, buckets of value 0 means that number doesn't exist
    // Traverse the `occurences` array from the largest possible value to the smallest
    let count = 0;
    for (let i = occurences.length - 1; i >= 0; i--) {
        count += occurences[i]; // Add the frequency of the current number
        if (count >= k) {
            // The index `i` represents the number `i + smallest`
            return i + smallest;
        }
    }
};
