"""
Input: heights = [
  [4,2,7,3,4],
  [7,4,6,4,7],
  [6,3,5,3,6]
]
Output: [[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]

pacific
[
  [1,1,1,1,1],
  [1,1,1,1,1],
  [1,0,0,0,0]
]

atlantic
[
  [0,0,1,0,1],
  [1,1,1,1,1],
  [1,1,1,1,1]
]

result = output

constraints:
    1 <= heights.length, heights[r].length <= 100
    0 <= heights[r][c] <= 1000

approach:
1. get coordinates (r,c) can reach pacific ocean
2. get coordinates (r,c) can reach atlantic ocean 
3. get overlap from 1 and 2 -> result

how to get coordinates for pacific/atlantic ocean
pacific
1. top row
2. left col
3. from (r,c) use dfs to see if we can reach the top row or left col position (sea level equal or less) -> slow?

from (r,c) in pacific neighbors, expand where it can be reached (reverse logic to neighbor sea level is higher or equal)

but why do we need to start from the edges not one by one from the other locations. Is it really efficient?

atlantic
1. bottom row
2. right col

"""
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        DIRECTIONS = [(-1,0), (1,0), (0,-1), (0,1)]
        pacific_q = deque([])
        pacific_visited = set()
        atlantic_q = deque([])
        atlantic_visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                # pacific
                if r == 0 or c == 0:
                    pacific_q.append((r,c))
                    pacific_visited.add((r,c))
                # atlantic
                if r == ROWS - 1 or c == COLS - 1:
                    atlantic_q.append((r,c))
                    atlantic_visited.add((r,c))

        while pacific_q:
            r,c = pacific_q.popleft()
            
            for dr, dc in DIRECTIONS:
                nxt_r, nxt_c = r + dr, c + dc

                if 0 <= nxt_r < ROWS and 0 <= nxt_c < COLS and heights[nxt_r][nxt_c] >= heights[r][c] and (nxt_r,nxt_c) not in pacific_visited:
                    pacific_q.append((nxt_r,nxt_c))
                    pacific_visited.add((nxt_r,nxt_c))

        
        while atlantic_q:
            r,c = atlantic_q.popleft()
            
            for dr, dc in DIRECTIONS:
                nxt_r, nxt_c = r + dr, c + dc

                if 0 <= nxt_r < ROWS and 0 <= nxt_c < COLS and heights[nxt_r][nxt_c] >= heights[r][c] and (nxt_r,nxt_c) not in atlantic_visited:
                    atlantic_q.append((nxt_r,nxt_c))
                    atlantic_visited.add((nxt_r,nxt_c))

        
        res = []

        for r, c in pacific_visited:
            if (r,c) in atlantic_visited:
                res.append([r,c])

        return res



        