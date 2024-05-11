class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        This qns is quite interesting in the sense that its just 2 binary searches
        The trick is determining the first binary search, which row is the target in?
        We can alter our if statements for the first binary search to check if the
        target is within the row itself by looking at the range of values, aka the 
        start number of the array and end number of the array, where the target must be in between that

        After finding the row we can just binary search on that row

        Note: Must account for when target is the exact value of the head or end of the row, we need
        <= and >= operators

        Time: O(log (m * n)), m = row, n = col
        Space: O(1)
        """
        # Finding matrix values is always Matrix[ROW][COL]
        ROWS, COLS = len(matrix), len(matrix[0])
        selected_row = 0

        # Lets determine which row the answer is in first!
        top, bottom = 0, ROWS - 1
        while top <= bottom:
            mid_row = top + ((bottom - top) // 2)

            # Need to account for if the target is exactly at the head or end
            # of the row, so we need <= and >=
            if matrix[mid_row][0] <= target and matrix[mid_row][-1] >= target:
                selected_row = mid_row
                break
            elif matrix[mid_row][0] < target and matrix[mid_row][-1] < target:
                top = mid_row + 1
            elif matrix[mid_row][0] > target and matrix[mid_row][-1] > target:
                bottom = mid_row - 1
        
        # Now that we have found our selected row, we can do regular binary search
        arr = matrix[selected_row]
        return self.binarySearch(arr, target)
    
    def binarySearch(self, arr: List[int], target: int) -> bool:
        left, right = 0, len(arr) - 1
        while left <= right:
            middle = left + ((right - left) // 2)
            if arr[middle] < target:
                left = middle + 1
            elif arr[middle] > target:
                right = middle - 1
            else:
                return True
        return False

