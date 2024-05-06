class Solution:
    def trap(self, height: List[int]) -> int:
        """
        The solution uses two pointers, one from each end, to determine the water level at each position
        based on the maximum height from either side. 
        
        We move the pointer with the smaller maximum height because that height determines 
        the water level at the current position. 
        The water level is limited by the lower of the two maximum heights from either side.

        so water between the current position and the corresponding maximum height is captured for every point

        Time: O(n)
        Space: O(1)
        """
        left, right = 0, len(height) - 1
        res = 0
        left_max, right_max = height[left], height[right]
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                res += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                res += right_max - height[right]
        return res
