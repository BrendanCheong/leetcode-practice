class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        We can solve this qns based off this observation:
        A big area means large width and large height.
        Now increasing the width of the container may not lead to a larger area
        if the height of the container isn't high as well.
        So the greedy solution is this:
        Have 2 pointers, one at each end. We want to greedily find the tallest possible heights
        and explore all possible containers, because the tallest heights may lead to the greatest area.
        Of course width will be taken into account, so we would have to check for all widths as well.

        Time: O(n)
        Space: O(1)
        """
        left, right = 0, len(height) - 1
        res = 0
        while left < right:
            current_left_val, current_right_val = height[left], height[right]
            # we pick the smallest height, because water will overflow from a lower height container
            # if you know what I mean (gravity)
            area = (right - left) * min(current_left_val, current_right_val)

            # We want the biggest area possible
            # hence the greedy algo
            res = max(area, res)
            if current_left_val < current_right_val:
                left += 1
            else:
                right -= 1
        return res


        
