class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        What we will do here is that we will go through the spiral for one cycle
        Then we will make the boundaries smaller after each cycle until we are out of bounds
        But we must account for all the edge cases, like what if its a single row, or single column

        Time: O(n * m)
        Space: O(n * m)
        """
        height, width = len(matrix), len(matrix[0])
        left, right, top, bottom = 0, width - 1, 0, height - 1
        res = []
        # Keep iterating in spiral pattern
        while left < right and top < bottom:

            # top row, left to right
            for i in range(left, right):
                res.append(matrix[top][i])

            # right-most col, top to bottom
            for i in range(top, bottom):
                res.append(matrix[i][right])

            # bottom row, right to left
            for i in range(right, left, -1):
                res.append(matrix[bottom][i])

            # left-most col, bottom to top
            for i in range(bottom, top, -1):
                res.append(matrix[i][left])

            # make the boundaries smaller
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        # If a matrix remainder inside it is either a 1 row or a 1 column matrix
        # a linear scan will return the same order as spiral for these
        if len(res) < height * width:
            for row in range(top, bottom + 1):
                for col in range(left, right + 1):
                    res.append(matrix[row][col])

        return res
