class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != "O":
                return 
            board[r][c] = "T"

            directions = [(1, 0), (-1, 0),(0, 1),(0, -1)]

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)

        for r in range(rows):
            for c in range(cols):
                cell = board[r][c]
                if cell == "T":
                    board[r][c] = "O"
                elif cell == "O":
                    board[r][c] = "X"

            
            


        