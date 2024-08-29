function orangesRotting(grid: number[][]): number {
    /**
    * 1. Multiple rotten oranges -- multisource bfs
    * 2. Fresh orange thats not accessible -- we need to keep track of all fresh oranges
    * we need time, which means go layer by layer.
    * Time: O(N * M)
    * Space: O(N * M)
    */
    const ROWS = grid.length;
    const COLS = grid[0].length;
    let fresh = 0;
    const q = new Queue.Queue();
    const visited = new Set<string>();
    let time = 0;
    const directions = [[1, 0], [0, 1], [-1, 0], [0, -1]];

    // Populate the q with all the starting nodes
    for (let r = 0; r < ROWS; r++) {
        for (let c = 0; c < COLS; c++) {
            if (grid[r][c] === 1) {
                fresh++;
            } else if (grid[r][c] === 2) {
                q.enqueue([r, c]);
            }
        }
    }

    // basically make sure no fresh oranges and queue is empty
    while (fresh > 0 && !q.isEmpty()) {
        const queueSize = q.size();
        for (let i = 0; i < queueSize; i++) {
            const [row, col] = q.dequeue();
            for (const [dr, dc] of directions) {
                const newRow = dr + row;
                const newCol = dc + col;
                if (
                    // we dont need a set, as we wont ever
                    // visit nodes that are rotten or now accessible
                    // since we turn nodes into rotten oranges
                    newRow < 0 || newRow >= ROWS ||
                    newCol < 0 || newCol >= COLS ||
                    grid[newRow][newCol] !== 1
                ) {
                    continue;
                }
                // means we found a fresh orange in bounds
                grid[newRow][newCol] = 2;
                fresh--;
                q.enqueue([newRow, newCol]);
            }
        }
        time += 1
    }

    if (fresh === 0) return time;
    return -1;
};
