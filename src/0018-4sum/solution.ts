function fourSum(nums: number[], target: number): number[][] {
    const results: number[][] = [];
    
    // Sort the array (though it's already sorted in your input)
    nums.sort((a, b) => a - b);

    const len = nums.length;

    for (let i = 0; i < len - 3; i++) {
        if (i > 0 && nums[i] === nums[i - 1]) continue; // Skip duplicates
        
        for (let j = i + 1; j < len - 2; j++) {
            if (j > i + 1 && nums[j] === nums[j - 1]) continue; // Skip duplicates
            
            let left = j + 1;
            let right = len - 1;
            
            while (left < right) {
                const sum = nums[i] + nums[j] + nums[left] + nums[right];
                
                if (sum === target) {
                    results.push([nums[i], nums[j], nums[left], nums[right]]);
                    
                    // Move both pointers to skip duplicates
                    while (left < right && nums[left] === nums[left + 1]) left++;
                    while (left < right && nums[right] === nums[right - 1]) right--;
                    
                    left++;
                    right--;
                } else if (sum < target) {
                    left++;
                } else {
                    right--;
                }
            }
        }
    }
    
    return results;
}