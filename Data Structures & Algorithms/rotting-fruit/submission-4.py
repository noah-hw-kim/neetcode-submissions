"""
Input: grid = [
[1,1,0],
[0,1,1],
[0,1,2]]
Output: 4

Input: grid = [
[1,0,1],
[0,2,0],
[1,0,1]]
Output: -1

1 <= grid.length, grid[i].length <= 10
grid[i][j] == 0 or 1 or 2

=======================
Approach - graph traverse
Input: grid = [
[1,1,0],
[0,1,1],
[0,1,2]]
Output: 4

min = 0
[
[1,1,0],
[0,1,1],
[0,1,2]
]
q = [[2,2]]

min = 1
[
[1,1,0],
[0,1,2],
[0,2,2]
]

...

use visited set
1. add all rotten oranges in q
2. every min, pop rotten oranges only in a current min (could be multiple)
    1) rotten fresh oranges
    2) put rotten fresh oranges in q

* how to filter out impossible to rot
- fresh orange counter or iterate grid and check if there's still a fresh orange


"""

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(-1,0), (1,0), (0,-1), (0,1)]
        
        q = deque()
        visited = set()
        fresh_count = 0
        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r,c))
                elif grid[r][c] == 1:
                    fresh_count += 1


        while q and fresh_count:
            rotten_count = len(q)

            for i in range(rotten_count):
                r, c = q.popleft()

                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < ROWS and
                        0 <= nc < COLS and
                        (nr,nc) not in visited and 
                        grid[nr][nc] == 1):
                        visited.add((nr,nc))
                        q.append((nr,nc))
                        fresh_count -= 1

            res += 1

        if fresh_count:
            return -1
        
        return res

                        





        