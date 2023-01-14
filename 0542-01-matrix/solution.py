from collections import deque
from typing import *

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Go through all the 0s only and mark the non-zeroes
        Then do BFS on them, you cannot visit other zeroes but you can visit non-zeroes. 
        You can visit the non-zeroes more than once
        """
        # m, n = len(mat), len(mat[0])
        # DIR = [0, 1, 0, -1, 0]

        # q = deque([])
        # for r in range(m):
        #     for c in range(n):
        #         if mat[r][c] == 0:
        #             q.append((r, c))
        #         else:
        #             mat[r][c] = -1  # Marked as not processed yet!

        # while q:
        #     r, c = q.popleft()
        #     for i in range(4):
        #         nr, nc = r + DIR[i], c + DIR[i + 1]
        #         if nr < 0 or nr == m or nc < 0 or nc == n or mat[nr][nc] != -1: continue
        #         mat[nr][nc] = mat[r][c] + 1
        #         q.append((nr, nc))
        # return mat
        rows, cols = len(mat), len(mat[0])
        q = deque()
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    mat[r][c] = -1
        # perform BFS on all the zeroes, only connect to non-zeroes
        while q:
            r, c = q.popleft()
            for x, y in directions:
                neighbor_r, neighbor_c = r + x, c + y
                if neighbor_r in range(rows) and neighbor_c in range(cols) and mat[neighbor_r][neighbor_c] == -1:
                    q.append((neighbor_r, neighbor_c))
                    # you must add the value of the connecting node + 1
                    # since we started from negative 1
                    mat[neighbor_r][neighbor_c] = mat[r][c] + 1
        return mat






