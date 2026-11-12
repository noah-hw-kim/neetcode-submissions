"""
Input: grid = [
[1,0,1],
[0,2,0],
[1,0,1]
]
Output: -1

constraints:
    1 <= grid.length, grid[i].length <= 10
    grid[i] == 0 or 1 or 2

approach 1 - bfs with queue (inplace), O(m*n) O(1)
Input: grid = [
[1,1,0],
[0,1,1],
[0,1,2]
]
Output: 4

time = 0
q = [(2,2)]
fresh oranges = 5


time = 1
q = [(1,2),(2,1)] -> we need to change state of fresh oranges when we put in the queue so it won't visit again
fresh oranges = 3

time = 2
q = [(1,1)]
fresh oranges = 2

time = 3
q = [(0,1)]
fresh oranges = 1

time = 4
q = [(0,0)]
fresh oranges = 0


"""

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1,0), (0,1), (-1,0), (0,-1)]
        q = deque()
        num_of_fresh = 0
        time = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    num_of_fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))

        while q and num_of_fresh:
            time += 1
            
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in DIRECTIONS:
                    nxt_r, nxt_c = r + dr, c + dc

                    if 0 <= nxt_r < ROWS and 0 <= nxt_c < COLS and grid[nxt_r][nxt_c] == 1:
                        grid[nxt_r][nxt_c] = 2
                        q.append((nxt_r,nxt_c))
                        num_of_fresh -= 1

        return time if num_of_fresh == 0 else -1

        