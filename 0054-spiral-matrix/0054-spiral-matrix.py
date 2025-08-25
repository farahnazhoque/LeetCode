class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        l, r = 0, len(matrix[0])
        t, b = 0, len(matrix)
        
        while l < r and t < b:
        
            # get every i in the top row
            for i in range(l, r):
                res.append(matrix[t][i])
            t += 1 # lowering the top boundary
            
            # get every i in the right col
            for i in range(t, b):
                res.append(matrix[i][r-1])
            r -= 1
        
            if not (l < r and t < b):
                break
            
            # get ever i in the bottom row
            for i in range(r-1, l-1, -1):
                res.append(matrix[b-1][i])
            b -= 1
            
            # get every i in the left col
            for i in range(b-1, t-1, -1):
                res.append(matrix[i][l])
            l += 1

        return res
        