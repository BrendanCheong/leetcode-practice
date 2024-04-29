class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # left_index: int = 0
        # right_index: int = len(nums) - 1
        
        # while left_index <= right_index:
        #     # find the middle of the array
        #     # stop when the left pointer is more than the right, in which we have exceeded the target and cannot find anything 
        #     mid_index: int = left_index + (right_index - left_index) // 2
            
        #     if nums[mid_index] == target:
        #         return mid_index
        #     elif nums[mid_index] < target:
        #         # if I am less than the target, it means that I must go right
        #         # so bring left pointer to the right side more
        #         left_index = mid_index + 1
        #     elif nums[mid_index] > target:
        #         # I must go left as I am too big, so right goes smaller
        #         right_index = mid_index - 1
        # # if left pointer exceeds then we cannot find the index
        # # in which element is not present in the array
        # return -1
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
        
