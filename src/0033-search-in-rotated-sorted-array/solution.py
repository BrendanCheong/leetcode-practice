class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        We can essentially split the array into left and right sorted array
        By checking the numbers between the middle value and the left and right pointers.

        For ex: If the values between left and mid are 4,5,6,7 -> it shows that left is less than mid value
        meaning a left sorted array.
        We keep doing this until we find our target, and where out left and right sorted arrays eventually
        become small enough to find the answer

        Then we can binary search within this sub-array accordingly

        Time: O(log n)
        Space: O(1)
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + ((right - left)) // 2
            if nums[mid] == target:
                return mid
            # If left is less than mid
            # it means we are in the left sorted array
            if nums[left] <= nums[mid]:
                # Is the target in this left sorted array?
                # if so we must bring the right pointer to the left
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # else we are in the right sorted array
            else:
                # Is the target in the right sorted array?
                # if so we must bring the left pointer right
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        # if no result
        return -1

                
        
