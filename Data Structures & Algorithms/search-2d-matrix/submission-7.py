class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        target_row = 0

        for i in range(len(matrix)):
            if target == matrix[i][-1]:
                return True

            elif target > matrix[i][-1]:
                target_row += 1

            else:
                break

        if target_row > len(matrix) - 1:
            return False

        l, r = 0, len(matrix[0]) - 1

        while l <= r:
            m = (l+r) // 2

            if target == matrix[target_row][m]:
                return True

            elif target > matrix[target_row][m]:
                l = m + 1
            
            else:
                r = m - 1
        
        return False
