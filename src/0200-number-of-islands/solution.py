class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        We do a BFS or DFS on each land piece we see.
        This will fill up a particular island and we keep track of islands visited
        and land pieces visited. We do not do BFS or DFS on the same piece of land
        we have visited.

        Time: O(NM(N + M)) if checkered board grid
        """
        # 0. Edge case
        if not grid or not grid[0]:
            return 0

        islands = 0
        visited = set()
        n, m = len(grid), len(grid[0])
        def dfs(rows: int, cols: int):
            # 1. Base case
            if (
                # check visited
                (rows, cols) in visited or
                # check out of bounds
                rows not in range(n) or
                cols not in range(m) or
                # check obstruction
                grid[rows][cols] == "0"
            ):
                # do not progress if we face water
                return
            
            # 2. Visit the neighbors
            visited.add((rows, cols))
            directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
            for dr, dc in directions:
                dfs(rows + dr, cols + dc)
        
        # 3. For each piece of land we do the DFS or BFS algo
        for r in range(n):
            for c in range(m):
                if (r, c) not in visited and grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)
        return islands
