from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        You can either do DFS or BFS to solve this question.
        Since this is a matrix, the time complexity is O(VE) and NOT O(V+E) [only for Adj List]
        
        To solve this question, we want to go through each cell and do a BFS/DFS if its a "1". The BFS/DFS will then visit all the neighbours of that cell in the visited set. If the cell is visited it will not add to the island count, instead it will skip the cells that are market visited. That way we only count cells that are grouped together, and not count multiple cells.
        
        edge cases:
        empty grid, empty cells.
        
        BFS:
        search for the first neighbouring cells that we see. That way we are searching for neighbours in "layers". 
        
        DFS:
        search for the most recently added neighbours. That way we are go through all closest neighbours of a cell before backtracking.
        """
#         if not grid or not grid[0]:
#             return 0
        
#         islands, visited = 0, set()
#         rows, cols = len(grid), len(grid[0])
        
#         def dfs(r: int, c: int) -> None:
#             q = deque()
#             visited.add((r, c))
#             q.append((r, c))
#             directions = ((1, 0), (-1, 0), (0, 1), (0, -1)) # go in the 4 directions to find neighbours
            
#             # keep finding neighbours until there are no more neighbours
#             while q:
#                 neighbour_row, neighbour_col = q.pop()
#                 #! to turn this into DFS, just do a q.pop() to get most recent cell
#                 # go through all directions
#                 for direction_row, direction_col in directions:
#                     search_row, search_col = neighbour_row + direction_row, neighbour_col + direction_col
#                     if (search_row in range(rows) and search_col in range(cols) and grid[search_row][search_col] == "1" and (search_row, search_col) not in visited):
#                         visited.add((search_row, search_col))
#                         q.append((search_row, search_col))
                
        
        
#         # for every cell, do BFS to find all neigbours to form an island
#         # we only want to do BFS on cells that are not visited and cells that are marked as "1"
#         # as those cells are new cells in which we have not visited or created island groups
#         for r in range(rows):
#             for c in range(cols):
#                 if ((r, c) not in visited and grid[r][c] == "1"):
#                     dfs(r, c)
#                     islands += 1
        
#         return islands
        # edge case, empty grids
        if (not grid or not grid[0]):
            return 0
        
        # we want to go through each row and column and do BFS on those with 1
        # this will add all connected 1s into a visited array, which will mean it will not count those 1s to the island again
        rows, cols = len(grid), len(grid[0])
        visited, islands, directions = set(), 0, ((1, 0), (-1, 0), (0, 1), (0, -1))
        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))
            # keep finding neighbours of the cells until no more neighbours
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    # the neighbours of that cell
                    n_row, n_col = dr + row, dc + col
                    # make sure inbound of grid
                    # make sure not visited
                    # make sure its a land
                    if (n_row in range(rows) and n_col in range(cols) and (n_row, n_col) not in visited and grid[n_row][n_col] == '1'):
                        q.append((n_row, n_col))
                        visited.add((n_row, n_col))
        for i in range(rows):
            for j in range(cols):
                if (grid[i][j] == '1' and (i, j) not in visited):
                    bfs(i, j)
                    islands += 1
        return islands
        


