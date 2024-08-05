class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def bruteForceMemoised(r: int, c: int, rows: int, cols: int, cache: List[List[int]]) -> int:
            # Do not go out of bounds
            if r == rows or c == cols:
                return 0
            # means already visited this path
            if cache[r][c] > 0:
                return cache[r][c]
            # we have reached the corner
            if r == rows - 1 and c == cols - 1:
                return 1
            cache[r][c] = bruteForceMemoised(r + 1, c, rows, cols, cache) + bruteForceMemoised(r, c + 1, rows, cols, cache)
            return cache[r][c]

        def dp(rows: int, cols: int) -> int:
            prevRow = [0] * cols

            for i in range(rows - 1, -1, -1):
                currRow = [0] * cols
                currRow[cols - 1] = 1
                for j in range(cols - 2, -1, -1):
                    currRow[j] = currRow[j + 1] + prevRow[j]
                prevRow = currRow
            return prevRow[0] 

        return dp(m, n)

