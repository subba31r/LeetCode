import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            if len(heap) < k:
                heapq.heappush(heap,n)
            elif n > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap,n)
        return heap[0]
            
        