class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        start_color = image[sr][sc]
        
        # If the start color is already the new color, no changes are needed
        if start_color == color:
            return image
        
        def dfs(r: int, c: int) -> None:
            if (
                r not in range(ROWS) or
                c not in range(COLS) or
                image[r][c] != start_color
            ):
                return
            image[r][c] = color
            for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                dfs(r + dr, c + dc)

        dfs(sr, sc)
        return image
