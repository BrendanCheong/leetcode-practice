function fourSumCount(nums1: number[], nums2: number[], nums3: number[], nums4: number[]): number {
    /**
    If num1 + num2 + num3 + num4 = 0
    Then num1 + num2 = -(num3 + num4)
    From O(n^4) to O(n^2)
     */
    const sumMap: Map<number, number> = new Map();
    let count = 0;

    // Step 1: Calculate all possible sums of pairs from nums1 and nums2
    for (let a of nums1) {
        for (let b of nums2) {
            const sum = a + b;
            const currentCountForPair = sumMap.get(sum) || 0
            sumMap.set(sum, currentCountForPair + 1);
        }
    }

    // Step 2: For each pair from nums3 and nums4, check if the negation of their sum exists in sumMap
    for (let c of nums3) {
        for (let d of nums4) {
            const target = -(c + d);
            if (sumMap.has(target)) {
                count += sumMap.get(target)!;  // Add the count from sumMap to the result
            }
        }
    }

    return count;
};
