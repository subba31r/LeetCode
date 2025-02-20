class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        fb = len(flowerbed)
        if n == 0:
            return True
        for i in range(fb):
            if flowerbed[i] == 0:
                if (i==0 or flowerbed[i-1] == 0) and (i==fb-1 or flowerbed[i+1] == 0):
                    flowerbed[i] = 1
                    n -= 1
                    if n==0:
                        return True
        return False
