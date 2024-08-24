class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        We do a BFS or DFS on each land piece we see.
        This will fill up a particular island and we keep track of islands visited
        and land pieces visited. We do not do BFS or DFS on the same piece of land
        we have visited.

        Time: O(N * M) visit every cell as all cells are land
        Space: O(N * M) all cells are land
        """
        rows, cols = len(grid), len(grid[0])
        # 0. Edge case
        if not rows or not cols:
            return 0
        
        visited = set()
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        res = 0

        def dfs(r: int, c: int) -> None:
            # Base case exit condition
            if (
                (r, c) in visited or
                r not in range(rows) or
                c not in range(cols) or
                grid[r][c] == '0'
            ):
                return
            # Visit all directions
            visited.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        # For each cell, run dfs to create the island on land
        # Do not run on already created islands
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    res += 1
                    dfs(r, c)
        return res
