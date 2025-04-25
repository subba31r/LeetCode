class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hm = {}
        # for num in nums:
        #     if num not in hm:
        #         hm[num] = 0
        #     hm[num] += 1
        # sortedHm = sorted(hm.items(),key=lambda x:x[1],reverse=True)
        # res = []
        # for i in range(k):
        #     res.append(sortedHm[i][0])
        # return res
        hm = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            if num not in hm:
                hm[num] = 0
            hm[num] += 1

        for num, cnt in hm.items():
            freq[cnt].append(num)


        res = []
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        