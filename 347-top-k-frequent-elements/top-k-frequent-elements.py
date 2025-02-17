from collections import Counter
from heapq import nlargest
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dic = {}
        # for n in nums:
        #     if n not in dic:
        #         dic[n] = 1
        #     else:
        #         dic[n] += 1
        # sorted_dic = {
        #     k:v for k,v in sorted(dic.items(),
        #     key=lambda item:item[1],reverse=True)
        # }

        # key = list(sorted_dic.keys())
        # return key[:k]
        count = Counter(nums) #we can use this for counting occurences
        return nlargest(k, count.keys(), key=count.get)  
        #count.get ensures that sorting is done based on frequency, not the number itself