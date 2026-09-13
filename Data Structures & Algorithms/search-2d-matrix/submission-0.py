class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        l = 0
        h = row*col - 1
        while l<=h:
            mid = (l+h)//2
            r = mid//col
            c = mid % col
            val = matrix[r][c]
            if val == target:
                return True
            elif val <= target:
                l = mid + 1
            else:
                h = mid - 1
        return False