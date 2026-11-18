"""
Input: [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]
q = [(0,2),(3,0)]

step 1
[
  [2147483647,-1,0,1],
  [2147483647,2147483647,1,-1],
  [1,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]
q = [(1,2),(0,4),(2,0)]

step 2
[
  [2147483647,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,2147483647,2147483647]
]

step 3
[
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,2147483647]
]

step 4
[
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]

constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 100
    grid[i][j] is one of {-1, 0, 2147483647}

approach - bfs from 0, time = O(m*n), space = O(m*n)
1. put all (r,c) of grid[r][c] == 0 to q and visited set
2. traverse q by each level
    3. popleft q
    4. explore neighbors and check validation below
        1) out of range
        2) not in visited
        3) not 0 or -1
        
        5. append q, visited, and change value to current step



"""

from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(-1,0),(1,0),(0,-1),(0,1)]
        q = deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))

        step = 1

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                
                for dr, dc in DIRECTIONS:
                    nxt_r, nxt_c = r + dr, c + dc

                    if 0 <= nxt_r < ROWS and 0 <= nxt_c < COLS and (nxt_r,nxt_c) not in visited and grid[nxt_r][nxt_c] != -1:
                        q.append((nxt_r,nxt_c))
                        visited.add((nxt_r,nxt_c))
                        grid[nxt_r][nxt_c] = step
            
            step += 1

        