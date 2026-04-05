class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in board:    
            for j in i:
                if j in seen:
                    return False
                elif j.isdigit():
                    seen.add(j)
            seen.clear()

        
        for i in range(9):
            for j in range(9):
                num = board[j][i]
                if num in seen:
                    return False
                elif num.isdigit():
                    seen.add(num)
            seen.clear()

        set1, set2, set3 = set(), set(), set()
        for i in range(9):
            if i % 3 == 0:
                set1.clear()
                set2.clear()
                set3.clear()

            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                if j < 3:
                    if num in set1:
                        return False 
                    set1.add(num)
                elif j < 6:
                    if num in set2:
                        return False    
                    set2.add(num)
                else:
                    if num in set3:
                        return False 
                    set3.add(num)

        return True

            
