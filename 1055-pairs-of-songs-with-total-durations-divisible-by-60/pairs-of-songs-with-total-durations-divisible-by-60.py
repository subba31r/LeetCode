class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res = 0
        n = len(time)
        hm = {}
        for i in range(0,n):
            val = time[i]%60
            res += hm.get((60-val)%60,0)
            if val not in hm:
                hm[val] = 0
            hm[val] += 1
        return res
        