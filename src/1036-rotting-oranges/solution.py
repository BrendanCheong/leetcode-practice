from typing import *
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        We want to traverse the grid using BFS in Layers.
        """
        rows, cols = len(grid), len(grid[0])
        visited, q = set(), deque()
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        fresh, time = 0, 0

        # find all the rotting oranges in the queue
        # find all the fresh oranges, we will deplete the fresh oranges until there are nothing left
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        while fresh != 0 and q:
            # we want to process ALL the rotten oranges for EACH minute, note more oranges will be added here as time goes by
            for i in range(len(q)):
                r, c = q.popleft() # BFS popleft from queue
                for x, y in directions:
                    n_r, n_c = r + x, c + y
                    # only connect to fresh oranges, ignore 0s or empty cells
                    if n_r in range(rows) and n_c in range(cols) and grid[n_r][n_c] == 1:
                        fresh -= 1
                        # rot that orange! remember to add the neighbors to queue
                        grid[n_r][n_c] = 2
                        q.append((n_r, n_c))
                # for each minute, is a "layer" in the BFS
            time += 1
        # now to think about the edge cases
        # how is the answer impossible? what if a cell is not reachable?
        # then fresh > 0
        return -1 if fresh > 0 else time

        

