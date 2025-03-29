class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            cur = 2
            while cur*cur <= num:
                while num%cur == 0:
                    num //= cur
                    s.add(cur)
                cur += 1
            if num > 1:
                s.add(num)
        return len(s)
        
        
