import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.heap = [i for i in range(1,1001)]
        heapq.heapify(self.heap)

    def popSmallest(self) -> int:
        h = heapq.heappop(self.heap)
        return h

    def addBack(self, num: int) -> None:
        if num not in self.heap:
            heapq.heappush(self.heap,num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)