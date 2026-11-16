"""
Input: grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]
Output: 6

Input: grid = [
  [1]
]
Output: 1

Input: grid = [
  [0]
]
Output: 0

1 <= grid.length, grid[i].length <= 50
grid[i][j] = 0 or 1

approach
dfs (iterative or recursive)
1. iterate grid[i][j]
2. if not visited, use dfs to get the current island area
3. update max island area if the current island area is bigger

visted = {}

dfs implentation (recursive)
# base

# recursive
visited.add((i,j))
cur_sum = 1
iterate 4 directions from (i,j) -> nxt_i, nxt_j
    if nxt_i, nxtj are in the valid grid and value 1 and not visited
        cur_sum += dfs((nxt_i,nxt_j))
return cur_sum

"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(-1,0),(1,0),(0,-1),(0,1)]
        visited = set()
        ans = 0

        def dfs(r, c):
            # base
            # recursive
            visited.add((r,c))
            cur_area = 1

            for dr, dc in DIRECTIONS:
                nxt_r, nxt_c = r + dr, c + dc

                if 0 <= nxt_r < ROWS and 0 <= nxt_c < COLS and (nxt_r, nxt_c) not in visited and grid[nxt_r][nxt_c] == 1:
                    cur_area += dfs(nxt_r,nxt_c)
            
            return cur_area


        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c] == 1:
                    cur_area = dfs(r,c)
                    ans = max(ans, cur_area)

        return ans