class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = { (m - 1, n - 1): 1 }
        def dfs(r, c):
            if r == m or c == n:
                return 0
            if (r, c) in cache:
                return cache[(r, c)]
            cache[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
            return cache[(r, c)]
        return dfs(0, 0)
