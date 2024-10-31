class Solution:
    def maxArea(self, height: List[int]) -> int:
        first, last, max_area = 0, len(height) - 1, -1
        while first < last:
            area = (last - first) * min(height[first], height[last])
            max_area = max(area, max_area)
            # greedy, we want as tall as possible, go through all possible width
            if height[first] < height[last]:
                first += 1
            else:
                last -= 1
        return max_area
