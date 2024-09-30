from functools import cache
from typing import Tuple

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Bottom-up approach
        
        Bounds:
            i: [0, len(nums) - 1]
        
        Order:
            General term i requires general term max_prod and min_prod.
            
            Term i:
                - We need to track both max_prod and min_prod at each index because:
                    - A negative number can flip the sign, making the current max_prod become a min_prod, and vice versa.
                - For each index i, there are three possibilities:
                    1. Start a new subarray at nums[i].
                    2. Extend the previous max subarray by multiplying nums[i] with max_prod(i - 1).
                    3. Extend the previous min subarray by multiplying nums[i] with min_prod(i - 1) (important for handling negative numbers).
            
            Transition:
                - max_prod[i] = max(nums[i], nums[i] * max_prod[i - 1], nums[i] * min_prod[i - 1])
                - min_prod[i] = min(nums[i], nums[i] * max_prod[i - 1], nums[i] * min_prod[i - 1])
                - Track the global max product at each step.
        """
        @cache
        def dp(i: int) -> Tuple[int, int, int]: # (min, max, global max product)
                # Base case: For the first element, both max and min products are the element itself
                if i == 0:
                    return (nums[0], nums[0], nums[0])
                # Get the max and min products for the previous index
                prev_max, prev_min, global_max = dp(i - 1)

                # Decision 1: start new sub array
                new_arr = nums[i]

                # Decision 2: exntend sub array for both max and min
                curr_max = max(new_arr, nums[i] * prev_max, nums[i] * prev_min)
                curr_min = min(new_arr, nums[i] * prev_max, nums[i] * prev_min)
            
                return (curr_min, curr_max, max(global_max, curr_max))

        # The global maximum product is returned from the last recursive call
        return dp(len(nums) - 1)[-1]


