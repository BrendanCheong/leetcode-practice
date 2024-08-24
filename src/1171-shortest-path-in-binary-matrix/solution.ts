function shortestPathBinaryMatrix(grid: number[][]): number {
    const directions = [[-1, -1], [1, 1], [-1, 0], [0, -1], [1, 0], [0, 1], [1, -1], [-1, 1]];
    const rows = grid.length;
    const cols = grid[0].length;
    const q = new Queue.Queue();
    const visited = new Set<string>(); 

    // Edge case: We are blocked from the start and the end, we can't even move!
    if (grid[rows - 1][cols - 1] === 1 || grid[0][0] === 1) {
        return -1;
    }

    // Edge case: Single cell that is open
    if (grid[0][0] === 0 && rows === 1 && cols === 1) {
        return 1;
    }

    function bfs(r: number, c: number): number {
        q.enqueue([r, c]);
        visited.add(`${r},${c}`);
        let area = 1;

        while (q.size()) {
            const levelSize = q.size();
            for (let i = 0; i < levelSize; i++) {
                const [currentRow, currentCol] = q.dequeue();

                for (const [dr, dc] of directions) {
                    const newRow = currentRow + dr;
                    const newCol = currentCol + dc;

                    // We reached the end, return the path length
                    if (newRow === rows - 1 && newCol === cols - 1) {
                        return area + 1;
                    }

                    if (
                        newRow < 0 || newRow >= rows ||
                        newCol < 0 || newCol >= cols ||
                        visited.has(`${newRow},${newCol}`) ||
                        grid[newRow][newCol] === 1
                    ) {
                        continue;
                    }
                    q.enqueue([newRow, newCol]);
                    visited.add(`${newRow},${newCol}`);
                }
            }
            area++;
        }

        // Return -1 if no path, we should find the path after traversal
        return -1;
    }

    return bfs(0, 0);
}
