class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find the row that it belongs to
        m = len(matrix)
        n = len(matrix[0]) - 1
        potential_row = -1
        for row in range(m):
            if target <= matrix[row][n] and target >= matrix[row][0]:
                potential_row = row
        if potential_row < 0: 
            return False
        # binary search on that row
        left = 0
        right = n
        while left <= right:
            middle = (right + left) // 2
            if matrix[potential_row][middle] < target:
                left = middle + 1
            elif matrix[potential_row][middle] > target:
                right = middle - 1
            else:
                return True
        return False