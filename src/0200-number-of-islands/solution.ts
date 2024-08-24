function numIslands(grid: string[][]): number {
    const rows = grid.length;
    const cols = grid[0].length;

    if (!rows || !cols) {
        return 0;
    }

    const visited = new Set<string>();
    const directions = [[1, 0], [0, 1], [-1, 0], [0, -1]];
    let res = 0;

    function bfs(r: number, c: number): void {
        const queue = new Queue.Queue();
        visited.add(`${r}, ${c}`);
        queue.enqueue([r, c]);

        while (!queue.isEmpty()) {
            const [currentRow, currentCol] = queue.dequeue();
            for (const [dr, dc] of directions) {
                const directionRow = dr + currentRow;
                const directionCol = dc + currentCol;
                if (
                    visited.has(`${directionRow}, ${directionCol}`) ||
                    directionRow < 0 || directionRow >= rows ||
                    directionCol < 0 || directionCol >= cols ||
                    grid[directionRow][directionCol] === '0' 
                ) {
                    continue;
                }

                queue.enqueue([directionRow, directionCol]);
                visited.add(`${directionRow}, ${directionCol}`);
            }
        }
    }

    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (!visited.has(`${r}, ${c}`) && grid[r][c] === '1') {
                res++;
                bfs(r, c);
            }
        }
    }

    return res;
};
