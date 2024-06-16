import collections
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Understanding
        # questions to ask: what would be within the empty boxes


        # Matching
        # hash map

        # Planning
        """
        for columns, we will have a hash set to ensure there are no duplicates and do the same for row
        for the 3 x 3 squares, we will create a hash set of pairs (rows, columns) where rows // 3 and columns // 3, in this way we can fit all the 9 numbers for each square in rows 0-2 and columns 0-2
        def isValidSudoku(self, board: List[List[str]]) -> bool:
            columns = collections.defaultdict(set)
            rows = collections.defaultdict(set)
            squares = collections.defaultdict(set) # key = (r/3, c/3)

            for r in range(9):
                for c in range(9):
                    if board[r][c] is empty:
                        continue
                    if value is in rows[r] or value is in columns[c] or value in squares[(r//3, c//3)]:
                        return false
            return true

        """

        # Implementing

        columns = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)


        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in columns[c] or board[r][c] in squares[(r//3, c//3)]:
                    return False
                rows[r].add(board[r][c])
                columns[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True

        # Reviewing: Correct


        # Evaluating
        # Time complexity: O(81) = O(1)
        # Space complexity: O(81) = O(1)