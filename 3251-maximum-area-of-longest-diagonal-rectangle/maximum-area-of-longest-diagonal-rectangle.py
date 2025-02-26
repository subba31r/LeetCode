class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        rows, cols = len(dimensions), len(dimensions[0])
        area = 0
        maxdag = 0
        for r in range(rows):
            x,y = dimensions[r]
            dist = math.sqrt(x*x + y*y)
            if dist > maxdag:
                maxdag = dist
                area = x*y
            elif dist == maxdag:
                area = max(area,x*y)
        return area