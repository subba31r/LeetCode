class Solution:
    def countLargestGroup(self, n: int) -> int:
        hm = {}
        for i in range(1,n+1):
            s = sum([int(x) for x in str(i)])
            if s not in hm:
                hm[s] = 0
            hm[s] += 1
        maxVal = max(hm.values())
        res = sum(1 for v in hm.values() if v==maxVal)
        return res