from typing import *
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        visited, q = set(), deque()

        #0. edge case
        if not image or not image[0]:
            return [[]]

        #1. start off from the given cell, cell is valid
        q.append((sr, sc))

        while q:
            curr_r, curr_c = q.popleft()
            if (curr_r, curr_c) not in visited:
                visited.add((curr_r, curr_c))
            for x, y in directions:
                neighbor_r, neighbor_c = curr_r + x, curr_c + y
                if neighbor_r in range(rows) and neighbor_c in range(cols) and image[neighbor_r][neighbor_c] == image[sr][sc] and (neighbor_r, neighbor_c) not in visited:
                    image[neighbor_r][neighbor_c] = color
                    q.append((neighbor_r, neighbor_c))
        image[sr][sc] = color
        return image
