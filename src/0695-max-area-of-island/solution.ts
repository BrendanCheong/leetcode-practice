function maxAreaOfIsland(grid: number[][]): number {
    let maxArea = 0;
    const directions = [[1, 0], [0, 1], [-1, 0], [0, -1]];
    const rows = grid.length;
    const cols = grid[0].length;

    const visited = new Set<string>();
    if (!rows || !cols) {
        return maxArea;
    }

    function dfs(r: number, c: number): number {
        // Base case
        if (
            r < 0 || r >= rows ||
            c < 0 || c >= cols ||
            visited.has(`${r},${c}`) ||
            grid[r][c] === 0
        ) {
            return 0;
        }
        let area = 1;
        visited.add(`${r},${c}`);
        for (const [dr, dc] of directions) {
            area += dfs(r + dr, c + dc);
        }
        return area;
    }

    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (grid[r][c] === 1 && !visited.has(`${r},${c}`)) {
                maxArea = Math.max(maxArea, dfs(r, c));
            }
        }
    }

    return maxArea;
};
