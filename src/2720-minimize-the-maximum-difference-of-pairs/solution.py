class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        left, right = 0, abs(nums[-1] - nums[0])
        def can_form_pairs(chosen_difference: int) -> bool:
            count = 0
            i = 0
            # leave space for 1 indexing
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= chosen_difference:
                    count += 1
                    i += 2  # skip next number since we used it
                else:
                    i += 1
            return count >= p

        res = right
        while left <= right:
            diff = (right + left) // 2
            if can_form_pairs(diff):
                res = diff
                # try smaller values
                right = diff - 1
            else:
                left = diff + 1
        return res
