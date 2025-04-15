# Approach:
# 1. Start from the given pixel (sr, sc), store its original color and change it to the new color.
# 2. Perform BFS using a queue to traverse 4-directionally (up, down, left, right) from the starting pixel.
# 3. For every neighboring pixel with the original color, change it to the new color and add it to the queue.

# Time Complexity: O(N * M) — where N is the number of rows and M is the number of columns (each pixel is visited once)
# Space Complexity: O(N * M) — for storing the queue in the worst case (all pixels of the same color)

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        image[sr][sc] = color
        rows = len(image)
        cols = len(image[0])
        q = deque()
        q.append((sr, sc))
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                r, c = row + dr, col + dc

                if (r in range(rows) and c in range(cols) and image[r][c] != color):
                    if image[r][c] == original_color:
                        image[r][c] = color
                        q.append((r, c))

        return image
