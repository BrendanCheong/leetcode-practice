class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        We will start from the outer square first, then reduce the square size
        until no more squares can be made
        For each square we rotate the array
        """
        l, r = 0, len(matrix) - 1
        while l < r:
            # iterate through entire row except last element, which is left from right - 1
            for i in range(r - l):
                top, bottom = l, r # its the same since its square matrix

                # save the top-left
                top_left = matrix[top][l + i]

                # move bottom-left to top-left, we are doing this counter clockwise swapping
                matrix[top][l + i] = matrix[bottom - i][l]

                # move bottom-right to bottom-left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move top-right to bottom-right
                matrix[bottom][r - i] = matrix[top + i][r]

                # move top-left to top-right
                matrix[top + i][r] = top_left

                # Remember to use 'i' variable to move the pointers
                # so in the top row we move the pointer to the right, the right col move it down
                # the bottom row move it left, and left col move it up


            # update left and right, make square smaller
            l += 1
            r -= 1
        
