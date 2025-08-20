class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        # Understanding
        '''
        Example with a 1D array
        [0, 0, 0]
        if m = 2
        [1, 1, 0]
        if m = 3
        [2, 2, 1]
        if m = 1
        [3, 2, 1]

        we see that the maximum is 3, and it is occurring once. This is 
        because we have to understand that the maximum occurs in the intersection
        so the intersection for 3, 2, 1 is 1. So we have to find the minimum intersection.
        '''

        # Questions to ask:
        '''
        What should the function return if ops is empty?
        (In this problem, it should return m * n, since all values are 0 and equally max.)
        '''
        if not ops:
            return m * n
        min_row, min_col = m, n

        for op in ops:
            min_row = min(min_row, op[0])
            min_col = min(min_col, op[1])

        return min_row * min_col
        

        return min_row * min_col
