class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        primay_diagonal = 0 
        secondary_diagonal = 0  
        for i in range (len(mat)) :   
            primay_diagonal +=  mat[i][i]   
            secondary_diagonal += mat[i][(i+1)*-1]
            if len(mat) % 2 != 0 :  
                result = ( primay_diagonal + secondary_diagonal) - mat[len(mat)//2][len(mat)//2]   
            else :   
                result =  primay_diagonal + secondary_diagonal
        return result 