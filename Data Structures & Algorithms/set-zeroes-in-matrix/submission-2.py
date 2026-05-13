class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        row = [False] * len(matrix)
        col = [False] * len(matrix[0])

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    row[r] = True
                    col[c] = True
        

        for r in range(len(matrix)):
            if row[r]:
                matrix[r] = [0] * len(matrix[0])
        for c in range(len(matrix[0])):
            if col[c]:
                for r in range(len(matrix)):
                    matrix[r][c] = 0

        