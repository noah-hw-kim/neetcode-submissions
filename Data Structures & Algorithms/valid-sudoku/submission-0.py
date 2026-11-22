"""
Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.

Approach 1:
Input: board =
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
Output: true

row and col -> use 9 sets for each to check if valid

rows_set = [{1,2},{},{},...]
cols_set = [{1},{2},{},...]
boxes_set = [{1,2},{},{},...]

problem -> how do we differenciate the sub-boxes

r,c
(0,0) -> sub-box0
(0,1)
(0,2)
(1,0)
(1,1)
(1,2)
(2,0)
(2,1)
(2,2)

row: divide by 3 and disregard the remainder
col: divide by 3 and disregard the remainder

(0,3) -> sub-box1
(0,4)
...
(2,5)

row: divide by 3 and disregard the remainder
col: divide by 3 and disregard the remainder

(0,7) -> sub-box2
...
(2,8)

row: divide by 3 and disregard the remainder
col: divide by 3 and disregard the remainder

(3,0) -> sub-box3
...
(5,2)

row: divide by 3 and disregard the remainder * 3
col: divide by 3 and disregard the remainder

=> (row // 3) * 3 + col // 3

map (r,c) to correct set groups and if the current number exist -> return false

"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS,COLS = len(board), len(board[0])
        rows_set = [set() for i in range(ROWS)]
        cols_set = [set() for i in range(COLS)]
        boxes_set = [set() for i in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                num = board[r][c]

                if num == ".":
                    continue

                if num in rows_set[r]:
                    print("already in row" + str(r) + str(c))
                    return False
                rows_set[r].add(num)

                if num in cols_set[c]:
                    print("already in col" + str(r) + str(c))
                    return False
                cols_set[c].add(num)

                box_idx = (r // 3) * 3 + c // 3

                if num in boxes_set[box_idx]:
                    print("already in box" + str(r) + str(c))
                    return False
                boxes_set[box_idx].add(num)

        return True





        