function majorityElement(nums: number[]): number {
    let candidate = -1; // any number
    let votes = 0 // how votes does the majority number have
    nums.forEach((num, index) => {
        // start off by choosing the first element as the candidate
        // just to start off only
        if (votes === 0) {
            candidate = num;
            votes = 1;
        } else if (num !== candidate) {
            // means not the candidate, remove vote
            // eventually majority will survive (no votes === 0)
            votes--;
        } else if (num === candidate) {
            votes++;
        }
    });
    return candidate;
};
