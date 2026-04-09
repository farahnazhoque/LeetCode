import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_dict = collections.defaultdict(set)
        cols_dict = collections.defaultdict(set)
        boxes_dict = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == ".":
                    continue

                if (val in rows_dict[r] or val in cols_dict[c] or val in boxes_dict[(r //3, c//3)]):
                    return False

                rows_dict[r].add(val)
                cols_dict[c].add(val)
                boxes_dict[(r//3, c//3)].add(val)

        return True
        