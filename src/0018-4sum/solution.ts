function fourSum(nums: number[], target: number): number[][] {
    nums.sort((a, b) => a - b);
    const [result, quad] = [[], []];
    const [K_SUM, START_INDEX] = [4, 0];

    function kSum(k: number, start: number, target: number) {
        if (k !== 2) {
            // recursive case
            for (let i = start; i < nums.length - k + 1; i++) {
                // ignore duplicates, start cahnges as we move the sliding window
                if (i > start && nums[i] === nums[i - 1]) {
                    continue;
                }
                quad.push(nums[i]);
                // create more loops according to k
                kSum(k - 1, i + 1, target - nums[i]);
                // backtrack
                quad.pop();
            }
            // exit recursive case
            return;
        }
        let [left, right] = [start, nums.length - 1];
        while (left < right) {
            const twoSum = nums[left] + nums[right];
            
            if (twoSum === target) {
                const sumArray = [...quad, nums[left], nums[right]];
                result.push(sumArray);
                left++;
                // get rid of duplicates when progressing array
                while (left < right && nums[left] === nums[left - 1]) {
                    left++;
                }
            } else if (twoSum < target) {
                left++;
            } else {
                right--;
            }
        }
    }

    kSum(K_SUM, START_INDEX, target);
    return result;
};
