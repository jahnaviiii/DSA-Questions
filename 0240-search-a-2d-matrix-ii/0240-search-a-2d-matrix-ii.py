class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        i, j = 0, m-1

        while i>=0 and i<n and j>=0 and j<m:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j-=1
            elif matrix[i][j] < target:
                i+=1
        return False