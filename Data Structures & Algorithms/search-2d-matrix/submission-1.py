class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        leftM = 0
        rightM = len(matrix) -1

        while leftM <= rightM:

            if rightM == leftM:
                
                leftN = 0
                rightN = len(matrix[0]) -1
                while leftN <= rightN:
                    midN = (leftN + rightN) // 2
                    if target == matrix[leftM][midN]:
                        return True
                    elif target > matrix[leftM][midN]:
                        leftN = midN + 1
                    else:
                        rightN = midN - 1
                return False

            midM = (leftM + rightM) // 2
            first = matrix[midM][0]
            last  = matrix[midM][-1]

            if target < first:
                rightM = midM - 1
            elif target > last:
                leftM = midM + 1
            else:
                # target lies within this row's range; collapse to this row
                leftM = midM
                rightM = midM
        return False



