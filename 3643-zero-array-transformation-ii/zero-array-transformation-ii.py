class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        def check(m):
            #sweep line algorithm
            line = [0 for _ in range(n+1)]

            for i in range(m):
                start, end, val = queries[i]
                line[start] += val
                line[end+1] -= val
            for i in range(1,n+1):
                line[i] = line[i] + line[i-1]

            for i in range(n):
                if line[i] < nums[i]:
                    return False
            return True
        
        if not check(len(queries)):
            return -1
        
        # binary search
        l, r = 0, len(queries)
        while l<=r:
            m = l + (r-l)//2
            if check(m):
                r = m-1
            else:
                l = m+1
        return l
            