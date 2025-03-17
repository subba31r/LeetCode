class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        pre = 0
        res = 0
        for g in gain:
            pre = pre+g
            res = max(pre,res)
        return res
