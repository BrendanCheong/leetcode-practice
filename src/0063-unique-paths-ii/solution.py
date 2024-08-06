class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        # The bottom right corner is the destination, when we reach here,
        # we know we can stop and unravel the recursive calls
        cache = { (rows - 1, cols - 1): 1 }

        def dfs(r, c):
            # if we reach the end or obstacle, start backtracking
            if r == rows or c == cols or obstacleGrid[r][c]:
                return 0
            # if we have visited before
            if (r, c) in cache:
                return cache[(r, c)]
            # update cache
            cache[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
            return cache[(r, c)]
        return dfs(0, 0)
