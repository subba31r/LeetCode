class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l, r = 0, n-1
        while l <= r:
            t = numbers[l] + numbers[r]
            if t == target:
                return [l+1,r+1]
            elif t > target:
                r -= 1
            else:
                l += 1
        