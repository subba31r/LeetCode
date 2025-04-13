class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7

        def goodNumbers(x,y):
            res, curmul = 1, x
            while y > 0:
                if y%2 == 1:
                    res = res*curmul % mod
                curmul = curmul*curmul%mod
                y //= 2
            return res
        return goodNumbers(5,(n+1)//2)*goodNumbers(4,(n//2))%mod
