from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set) # key = (r//3, c//3)

        for r in range(9):
            for c in range(9):
                if(board[r][c] == "."):
                    continue
                if(board[r][c] in rows[r] or
                   board[r][c] in cols[c] or
                   board[r][c] in squares[(r//3, c//3)]):
                   return False
                cols[c].add(board[r][c])   #Hashmap value is set thats the reason we do add
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
            
        return True