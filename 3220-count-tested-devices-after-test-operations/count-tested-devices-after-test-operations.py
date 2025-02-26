class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        res = 0
        ops = 0
        for num in batteryPercentages:
            if (num-ops) > 0:
                res += 1
                ops += 1
        return res