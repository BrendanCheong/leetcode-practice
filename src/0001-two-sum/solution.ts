function twoSum(nums: number[], target: number): number[] {
    const hashmap = new Map<number, number>();

    for (let index = 0; index < nums.length; index++) {
        const num = nums[index];
        const result = target - num;

        if (hashmap.has(result)) {
            return [hashmap.get(result)!, index];
        }

        hashmap.set(num, index);
    }

    // In case there's no solution, though the problem usually guarantees one.
    throw new Error("No two sum solution found");
}
