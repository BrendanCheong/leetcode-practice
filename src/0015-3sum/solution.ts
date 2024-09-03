function threeSum(nums: number[]): number[][] {
    /**
     * Solution is similar to two-pointers combined with sliding window idea
     * a sorted array, we pick a number
     * then the rest of the array, since its sorted, we have sort of a sliding window
     * which we can expand or shrink to get closer to num[i] + num[l] + num[r] === 0
     * But also remember to skip duplicates
     */
    nums.sort((a, b) => a - b);
    const result = new Array<number[]>();

    for (let i = 0; i < nums.length; i++) {
        let left = i + 1;
        let right = nums.length - 1;

        // edge case
        if (nums[i] > 0) {
            break; // or continue, since sorted we can break
        }

        if (i > 0 && nums[i] === nums[i - 1]) {
            // ignore duplicates
            continue;
        }

        // since sorted we can do our sliding window
        while (left < right) {
            const threeSum = nums[i] + nums[left] + nums[right];
            if (threeSum === 0) {
                result.push([nums[i], nums[left], nums[right]]);
                // we need to continue finding subarrays
                // notice how our array sum must still be === 0?
                // so we move left and right both!
                left++
                right--;
                // we also need to get rid of duplicate numbers
                while (left < right && nums[left] === nums[left - 1]) {
                    left++;
                }

            } else if (threeSum < 0) {
                // we need bigger numbers
                left++;
            } else {
                // we need smaller numbers
                right--;
            }
        }
    };

    return result;
};
