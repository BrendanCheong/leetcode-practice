class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        We need num1 + num2 + num3 = 0
        The trick is this: based of several assumptions AFTER SORTING, we can assume:
        1. assume we sort the list, we can easily find duplicate numbers by asking ourselves
            what number is behind me.
            For ex: [-3, -3, -1, 0, 1, 4, 5]
            We can easily find 2 x of -3
        2. If we pick a number in the sorted list, we should only go towards the right, where bigger numbers are.
            Going backwards doesn't make sense, we need to get to number 0.
            For ex: if I pick -3, then going back to pick a smaller number like -5 doesn't make sense, I need bigger numbers
            like 2 and 1
        This means that after picking a number in a sorted list, the rest of the array can be treated like
        2 Sum

        Time: O(n log n) + O(n)
        Space: O(n) if you use hashmap, O(1) if 2 pointers
        """
        nums.sort()
        res = []

        for i, n in enumerate(nums):
            if n > 0:
                return res
            # check duplicate numbers by looking behinf
            # if we start at index 0, we ignore this step
            # theres nothing behind index 0
            if i > 0 and n == nums[i - 1]:
                continue
            
            # i + 1 because the 2 SUM array starts from after picking the first number
            left, right = i + 1, len(nums) - 1
            while left < right:
                # we need to hit == 0. Left pointer is smaller numbers
                # Right pointer is bigger
                # if too big, shrink the right
                # if too small, increase the left
                current_sum = n + nums[left] + nums[right]
                if current_sum < 0:
                    left += 1
                elif current_sum > 0:
                    right -= 1
                else:
                    # means the sum is correctly 0
                    res.append([n, nums[left], nums[right]])
                    # Now we must move on to the next 2 sum array
                    # we only move the left pointer, as we want arrays from left to right
                    # so we get smaller and smaller numbers, closer to 0
                    left += 1

                    # This part is for when we face another duplicate when moving the left pointer
                    # We just move the pointer to the next number and start again
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
            
        return res

            

