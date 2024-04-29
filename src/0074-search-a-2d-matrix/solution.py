class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])
        top, bottom = 0, ROW - 1
        while top <= bottom:
            row = top + (bottom - top) // 2
            first, last = matrix[row][0], matrix[row][-1]
            if first > target:
                bottom = row - 1
            elif first < target and last < target:
                top = row + 1
            else:
                break
        target_index = (top + bottom) // 2

        # check out of bounds edge cases
        if target_index > ROW or target_index < 0:
            return False

        # conduct binary search on target row as per usual
        target_col = matrix[target_index]

        def binary_search(arr: List[int], target: int) -> bool:
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if arr[mid] > target:
                    right = mid - 1
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    return True
            return False
        return binary_search(target_col, target)

