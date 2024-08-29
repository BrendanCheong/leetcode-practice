function pacificAtlantic(heights: number[][]): number[][] {
    /**
    * Iterate from left to right border
    * Iterate from top to bottom border
    * if can reach both sides, means mark the coordinate as valid
    */
    const ROWS = heights.length; const COLS = heights[0].length;
    const pacificVisited = new Set<string>();
    const atlanticVisited = new Set<string>();
    const directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    
    function dfs(r: number, c: number, visited: Set<string>): void {
        visited.add(`${r},${c}`);
        for (const [dr, dc] of directions) {
            const newRow = dr + r;
            const newCol = dc + c;
            if (
                newRow < 0 || newRow >= ROWS ||
                newCol < 0 || newCol >= COLS ||
                visited.has(`${newRow},${newCol}`) ||
                heights[newRow][newCol] < heights[r][c] 
            ) {
                continue
            }
            dfs(newRow, newCol, visited);
        }
    }

    // Left to right
    for (let i = 0; i < ROWS; i++) {
        // leftmost col down
        dfs(i, 0, pacificVisited);
        // rightmost col down
        dfs(i, COLS - 1, atlanticVisited)
    }

    // top to bottom
    for (let j = 0; j < COLS; j++) {
        // topmost row go right
        dfs(0, j, pacificVisited);
        // bottommost row go right
        dfs(ROWS - 1, j, atlanticVisited)
    }

    const mergedOceans = [...pacificVisited].filter((x) => atlanticVisited.has(x))
    // convert string to number
    return mergedOceans.map((coordinate) => coordinate.split(',').map(Number))

};
