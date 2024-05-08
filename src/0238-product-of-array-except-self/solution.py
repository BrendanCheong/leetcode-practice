class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Consider the input array nums = [1, 2, 3, 4]

        First Pass (Right to Left):
        - Start with `right_pointer_val = 1`.
        - Traverse from the end to the beginning:
        - For `i = 3` (last element), set `res[3] = 1` (since there's nothing on its right). Update `right_pointer_val = 1 * 4 = 4`.
        - For `i = 2`, set `res[2] = 4` (product of elements right of index 2). Update `right_pointer_val = 4 * 3 = 12`.
        - For `i = 1`, set `res[1] = 12`. Update `right_pointer_val = 12 * 2 = 24`.
        - For `i = 0`, set `res[0] = 24`. 

        Second Pass (Left to Right):
        - Start with `left_pointer_val = 1`.
        - Traverse from the beginning to the end:
        - For `i = 0`, `res[0]` remains `24`. Update `left_pointer_val = 1 * 1 = 1`.
        - For `i = 1`, set `res[1] = 12 * 1 = 12`. Update `left_pointer_val = 1 * 2 = 2`.
        - For `i = 2`, set `res[2] = 4 * 2 = 8`. Update `left_pointer_val = 2 * 3 = 6`.
        - For `i = 3`, set `res[3] = 1 * 6 = 6`.

        Final output: `[24, 12, 8, 6]`, where each element is the product of all other elements in the array.

        Time: O(n)
        Space: O(1)

        You could do multiple arrays (makes understanding easier)
        But thats space of O(n)
        """
        res = [1 for i in range(len(nums))]

        right_pointer_val = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = right_pointer_val
            right_pointer_val *= nums[i]
        # After the first pass we need elements from the left to right to finish up the array
        # for example, if at index 1, we need the product at index 0 from the left to right pass
        
        left_pointer_val = 1
        for i, n in enumerate(nums):
            res[i] *= left_pointer_val
            left_pointer_val *= nums[i]

        return res
