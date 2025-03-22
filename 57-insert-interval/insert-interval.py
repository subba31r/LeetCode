class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        intervals.append(newInterval)

        n = len(intervals)
        if n == 1:
            return [newInterval]
        intervals.sort(key= lambda x: x[0])
        res.append(intervals[0])
        for i in range(1,n):
            preStart, preEnd = res[-1][0], res[-1][1]
            if intervals[i][0]<=preEnd:
                res[-1][0] = min(res[-1][0], intervals[i][0])
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])
        return res