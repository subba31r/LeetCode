class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # 1 + a[0] = a[1]
        # -3 + 1 + a[0] = a[2]
        # 4 -2 + a[0] = a[3]
        # a[0] + 2  = a[3]
        # a[0] + 1 = a[1]
        # a[0] - 2 = a[2]
        # lower  = 1
        # upper = 6

        # a[0] + 3 = a[1]
        # a[0] - 1 = a[2]
        # a[0] + 4 = a[3]
        # a[0] + 5 = a[4]
        # a[0] + 3 = a[5]

        # a[0] - 1, a[0]+5
        #should be in range of -4 and 5
        # -3
        # -2
        # -1
        # 0
        minEle = 0
        maxEle = 0
        cur = 0
        for diff in differences:
            cur = cur + diff
            minEle =  min(minEle, cur)
            maxEle = max(maxEle, cur)
        
        res = 0
        for i in range(lower,upper+1):
            if lower <= i + minEle <= upper and lower <= i + maxEle <= upper:
                res += 1
        return res