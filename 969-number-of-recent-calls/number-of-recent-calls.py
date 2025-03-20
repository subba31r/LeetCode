class RecentCounter:

    def __init__(self):
        self.counter = []

    def ping(self, t: int) -> int:
        self.counter.append(t)
        while len(self.counter) != 0 and 3000+self.counter[0]-t < 0:
            self.counter.pop(0)
        return len(self.counter)




        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)