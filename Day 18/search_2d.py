from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Understanding
        # 


        # Matching
        # Binary tree


        # Planning
        """
        1. define ROWS and COLS with rows being the length of the matrix and columns being the length of one array within the matrix
        2. for top matrix (row), we will set its index to be 0, and for the bottom, it will be the bottom row
        3. then we will loop through all the rows
        4. find the mid row = (top + bottom) //2
        5. if the target is greater the right most value of the row, then we shift the top below
        6. if the target is less than the left most value of the row, then we shift the bottom above
        7. if we find the perfect match, we break from the while loop
        8. if the top is no longer smaller than the bottom row, we know there is no such row which contain the value, so we immediately return false
        9. else, we then get the row = (top + bot) // 2
        10. we put left to 0, and right to COLS -1
        11. repeat the same way as above, but now just for the columns
        """


        # Implementing
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False


        # Reviewing: Correct


        # Evaluating:
        # Time Complexity: O(logn)
        # Space Complexity: O(1)