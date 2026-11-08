"""
Input: grid = [
[0,1,0]
[0,1,0]
[0,0,1]
]
Output: 2

grid=[
["1","1","0","0","1"],
["1","1","0","0","1"],
["0","0","1","0","0"],
["0","0","0","1","1"]
]

Constraints:
    1 <= grid.length <= 100
    1 <= grid[i].length <= 100
    grid[i][j] = "0" or "1"

Approach
DFS or BFS

DFS - traverse each grid cells and add each cell indicies to visited set and once done counting current traverse, add one to # of islands

iterate row -> index i
    iterate col -> index j
        if (i,j) not in visited and land: dfs(i, j)
        increment # of islands

time: O(m*n), space: O(m*n)

"""
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(-1,0), (1,0), (0,-1), (0,1)]
        visited = set()
        res = 0
        
        def bfs(i,j):
            q = deque()
            q.append((i,j))
            visited.add((i,j))

            while q:
                r, c = q.popleft()
                
                for dr, dc in DIRECTIONS:
                    nxt_r, nxt_c = r + dr, c + dc

                    if (0 <= nxt_r < ROWS and 0<= nxt_c < COLS and (nxt_r, nxt_c) not in visited and grid[nxt_r][nxt_c] == "1"):
                        q.append((nxt_r,nxt_c))
                        visited.add((nxt_r,nxt_c))
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i,j) not in visited:
                    bfs(i,j)
                    res += 1
        
        return res