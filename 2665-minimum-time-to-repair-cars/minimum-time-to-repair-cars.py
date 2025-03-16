class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l, r = 1, min(ranks)*cars*cars
        
        while l < r:
            m = (l+r)//2
            repaired = sum(int((m/rank)**0.5) for rank in ranks)
            if repaired < cars:
                l = m+1
            else:
                r=m
        return l

