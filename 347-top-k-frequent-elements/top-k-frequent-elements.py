class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for num in nums:
            if num not in hm:
                hm[num] = 0
            hm[num] += 1
        sortedHm = sorted(hm.items(),key=lambda x:x[1],reverse=True)
        res = []
        for i in range(k):
            res.append(sortedHm[i][0])
        return res