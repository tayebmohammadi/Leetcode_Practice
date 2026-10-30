class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        dp = [[-1] * cols for _ in range(rows)]

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            elif dp[r][c] >= 0:
                return dp[r][c]

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            res = 1
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if (0 <= nr < rows and 0 <= nc < cols) and matrix[r][c] < matrix[r + dr][c + dc]:
                    res = max(res, dfs(nr, nc) + 1)

            dp[r][c] = res
            return res

        longest = 0
        for r in range(rows):
            for c in range(cols):
                longest = max(longest, dfs(r, c))

        return longest
                

            




        