from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        This is essentially BFS, count the layers it takes to get to rows - 1, cols - 1 coordinates

        Time: O(N * M)
        Space: O(N * M)
        """
        directions = [(-1, -1), (1, 1), (-1, 0), (0, -1), (1, 0), (0, 1), (1, -1), (-1, 1)]
        rows, cols = len(grid), len(grid[0])

        # Edge case: We are blocked from the start and the end, we can't even move!
        if (
            grid[-1][-1] == 1 or
            grid[0][0] == 1
        ):
            return -1

        def bfs(r: int, c: int) -> int:
            length = 1
            q = deque([(r, c)])
            visited = set((r, c))

            while q:
                # Go through layer by layer in the queue
                #! NOTE: This is a modified layer by layer BFS
                #! NOTE: You usually dont need this
                for _ in range(len(q)):
                    curr_r, curr_c = q.popleft()
                    
                    # If reached destination just return length
                    if curr_r == rows - 1 and curr_c == cols - 1:
                        return length

                    # Go through each directions
                    for dr, dc in directions:
                        new_r, new_c = dr + curr_r, dc + curr_c
                        if (
                            new_r < 0 or new_r >= rows or
                            new_c < 0 or new_c >= cols or
                            (new_r, new_c) in visited or
                            grid[new_r][new_c] == 1
                        ):
                            continue
                        q.append([new_r, new_c])
                        visited.add((new_r, new_c))
                # After emptying current q, we gone through a layer
                # which means we travelled one unit forward
                length += 1

            return -1
        return bfs(0, 0)

