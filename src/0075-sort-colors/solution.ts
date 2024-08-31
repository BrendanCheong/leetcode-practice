/**
 Do not return anything, modify nums in-place instead.
 */
function sortColors(nums: number[]): void {
    /**
    * White, Red, Blue -> 0, 1, 2
    * This is the Dutch national flag partitioning problem, using Modified quick sort partition.
    * if we see 0, swap 1 with 0 for their pointers, and move 1 and 0 forward
    * if we see 1, move 1 forward
    * if we see 2, swap 1 and 2 for their pointers, move 2 backwards
    The Main Idea
        White pointer is used to traverse the array.
        Red pointer keeps track of the position where the next 0 should be placed.
        Blue pointer keeps track of the position where the next 2 should be placed.
    */
    let [red, white, blue] = [0, 0, nums.length - 1];
    while (white <= blue) {
        // white is our moving pointer
        // we encounter red, first color
        if (nums[white] === 0) {
            // white portion moves forward
            // and so does red so we know the middle part of the array
            [nums[white], nums[red]] = [nums[red], nums[white]];
            white++;
            red++;
        } else if (nums[white] === 1) {
            // red portion is the middle part of array, so it stays constant and moves forward
            white++;
        } else {
            // blue portion shrinks 
            [nums[white], nums[blue]] = [nums[blue], nums[white]]
            blue--;
        }
    }
    
};
