
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board) -> bool:
        rows = defaultdict(set) # for every key a default value is assigned that is of type SET
        cols = defaultdict(set)
        boxes = defaultdict(set)

        # for i, row in enumerate(board):
        #     for j, col in enumerate(row):
        #         if col == ".": continue
        #         if i not in rows:
        #             rows[i] = [col]
        #         else:
        #             if col in rows[i]:
        #                     return False
        #             else:
        #                 rows[i].append(col)
        #         if j not in cols:
        #             cols[j] = [col]
        #         else:
        #             if col in cols[j]:
        #                     return False
        #             else:
        #                 cols[j].append(col)

        #         # box
        #         if (i//3, j//3) not in box:
        #              box[(i//3, j//3)] = [col]
        #         else:
        #             if col in box[((i//3, j//3))]:
        #                     return False
        #             else:
        #                 box[((i//3, j//3))].append(col)

        for r in range(9):
            for c in range(9):
                ele = board[r][c]

                if ele == ".": continue
                
                if (ele in rows[r] or ele in cols[c] or ele in boxes[(r // 3, c // 3)]):
                    return False

                rows[r].add(ele)
                cols[c].add(ele)
                boxes[(r // 3, c // 3)].add(ele)

        return True

board = [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
Solution().isValidSudoku(board)
