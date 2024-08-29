class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        Interesting problem, it seems that we can only capture "islands" connected by 'O'
        which are not connected/accessible by the border regions.

        One idea is this:
        1. Search only the border areas for 'O'. If its an 'O' DFS or BFS through it and mark
        that island as a border island. This means we wont be able to change these border islands into 'X'
        2. Go through all the cells and mark all remaining non-border islands 'O's as 'X'
        3. This means all our border islands are preserved! and our solution is correct
        """
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(r: int, c: int) -> None:
            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                (r, c) in visited or
                # In this special case, we don't actually need visited set,
                # we wont revisit nodes that are marked as 'B'
                board[r][c] != 'O'
            ):
                return
            board[r][c] = 'B' # B for border island, mark as visited
            for dr, dc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                dfs(dr + r, dc + c)
            
        for r in range(ROWS):
            for c in range(COLS):
                # check to see if cell is in border region
                if board[r][c] == 'O' and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
                    # now we can preserve the border islands by marking them as so border islands using dfs
                    dfs(r, c)
        
        # Now we can go through the rest of the cells and mark them as 'X'
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        # Finally, since border islands are preserved, mark them back to 'O' to solve the question
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'B':
                    board[r][c] = 'O'


        
