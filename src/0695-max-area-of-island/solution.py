class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Time: O(m x n), we visit every cell once
        """
        max_area = 0
        rows, cols = len(grid), len(grid[0])
        if not rows or not cols:
            return max_area
        visited = set()

        def dfs(r: int, c: int) -> int:
            # 1. No visiting conditions
            if (
                (r, c) in visited or
                r not in range(rows) or
                c not in range(cols) or
                grid[r][c] == 0
            ):
                return 0
            
            # 2. For each land visited, update visited land and calculate area
            visited.add((r, c))
            # since we see a land, area starts of as 1, and we add the previous area to the variable
            area = 1
            directions = ((1, 0), (0, 1), (0, -1), (-1, 0))
            # go in all directions to add to area
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            return area
        for r in range(rows):
            for c in range(cols):
                max_area = max(max_area, dfs(r, c))
        return max_area

