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

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        
        def dfs(i,j):
            # base
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or (i,j) in visited or grid[i][j] != "1":
                return

            # iterative
            visited.add((i,j))
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j -1)
            dfs(i, j + 1)
        
        res = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    res += 1
        
        return res