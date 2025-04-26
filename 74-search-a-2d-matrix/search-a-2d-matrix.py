class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])
        l,r = 0,r*c-1
        while l<=r:
            m = (l+r)//2
            if matrix[m//c][m%c] == target:
                return True
            elif matrix[m//c][m%c] > target:
                r = m-1
            else:
                l = m+1
        return False