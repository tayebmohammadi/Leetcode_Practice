class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        n = len(matrix)
                
        ## transpose
        for r in range(n):
            for c in range(1 + r, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        ## reverse vertically
        for r in range(n):
            for c in range(n // 2):
                matrix[r][c], matrix[r][n - c - 1] = matrix[r][n - c - 1], matrix[r][c]


        

        