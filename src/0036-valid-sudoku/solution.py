class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        This solution aims to collect all the numbers for all the 3x3 grids in the sudoku board
        if you do num // 3, you will split the grid into 3x3 sub boxes
        you can use a set make sure you get no duplicate numbers. If the number is already in the set, you have a problem!

        We follow the (row, column) format here, since we iterate for i in j
        (i, ele) - has ele been placed in this row?
        (ele, j) - has ele been placed in this column?
        (i // 3, j // 3, ele) - has ele been placed in this 3x3 grid? (follows: row, column, element)

        Time: O(9^2)
        Memory: O(9^2)
        """
        res = set()
        for i in range(9):
            for j in range(9):
                ele = board[i][j]
                if ele != '.' and ((i, ele) in res or (ele, j) in res or (i // 3, j // 3, ele) in res):
                    return False
                res.add((i, ele)) # this is for the row
                res.add((ele, j)) # this is for the column
                res.add((i // 3, j // 3, ele)) # this is for the 3x3 sub grid
        return True
