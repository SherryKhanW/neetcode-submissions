class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bottom = 0, ROWS - 1
        target_row = -1

        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        while top <= bottom:
            mid = (top + bottom) // 2

            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                target_row = mid
                break
        
        if target_row == -1:
            return False
        
        l, r = 0, COLS - 1

        while l <= r:
            m = (l + r) // 2
            if target > matrix[target_row][m]:
                l = m + 1
            elif target < matrix[target_row][m]:
                r = m - 1
            else:
                return True

        return False            
        
        
        


        


