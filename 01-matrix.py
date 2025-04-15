# Approach:
# 1. Initialize the output matrix with `inf` and set cells with 0 in `mat` to 0 in `output`, pushing their positions into the queue.
# 2. Use BFS to propagate distances from each 0 to all reachable 1s by updating the `output` matrix with the minimum distance.
# 3. For each step in BFS, explore 4 directions and update neighbor distances only if a shorter path is found.

# Time Complexity: O(N * M) — where N is the number of rows and M is the number of columns (each cell is visited at most once)
# Space Complexity: O(N * M) — for the queue and output matrix

from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        q = deque()
        output = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Add all 0's to queue and set output to 0
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    output[r][c] = 0
                    q.append((r, c, 0))

        # BFS to update minimum distances
        while q:
            row, col, step = q.popleft()
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < rows and 0 <= c < cols and output[r][c] > step + 1:
                    output[r][c] = step + 1
                    q.append((r, c, step + 1))

        return output
