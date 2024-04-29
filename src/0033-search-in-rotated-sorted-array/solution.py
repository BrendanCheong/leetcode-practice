class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while (left <= right):
            mid = (left + right) // 2
            
            if (nums[mid] == target):
                return mid
            
            # are we in the left sorted portion?
            # if the middle value is greater than the leftmost value?
            # if so, left to mid are increasing numbers
            if (nums[left] <= nums[mid]):
                if (target > nums[mid] or target < nums[left]):
                    # if the target is smaller than leftmost, I cannot be in the leftmost due to increasing numbers
                    # if the target is bigger than middle, I cannot be left most, since left of middle are smaller numbers
                    # go right
                    left = mid + 1
                else:
                    # go left
                    right = mid - 1
            else: # 5, 6, 0, <1>, 2, 3, 4
                if (target < nums[mid] or target > nums[right]):
                    # go left
                    right = mid - 1
                else:
                    # go left
                    left = mid + 1
        return -1 # if cannot be found, exit program
