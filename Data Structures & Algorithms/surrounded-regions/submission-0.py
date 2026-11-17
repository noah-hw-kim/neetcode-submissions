"""
constraints:
    1 <= board.length, board[i].length <= 200
    board[i][j] is 'X' or 'O'.

example
Input: board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","X","O","X"],
  ["X","O","X","X"]
]

1. check each region if they're connect with any edge with "O" -> reverse it and check from the edge "O"

[
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","O","O","X"],
  ["X","O","X","X"]
]

starting from (3,1), traverse and find the region and keep the coordinate or change the marker temporarily so later when we change O to X it survives

Output: [
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","O","X","X"]
]

approach bfs or dfs - O(m * n), O(1)
1. store edge "O" (r,c) and change the mark to "*"
2. use stack and perform dfs
    3. while stack is exist, pop the item, change the mark and traverse next coordinates (add to stack, change marker to "*")

4. iterate board and change O to X
5. iterate board and change "*" to O

"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        DIRECTIONS = [(-1,0),(1,0),(0,-1),(0,1)]
        stack = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1) and board[r][c] == "O":
                    stack.append((r,c))
                    board[r][c] = "*"
        
        while stack:
            r, c = stack.pop()

            for dr, dc in DIRECTIONS:
                nxt_r, nxt_c = r + dr, c + dc

                if 0 <= nxt_r < ROWS and 0 <= nxt_c < COLS and board[nxt_r][nxt_c] == "O":
                    stack.append((nxt_r,nxt_c))
                    board[nxt_r][nxt_c] = "*"
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "*":
                    board[r][c] = "O"






