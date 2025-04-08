class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        zero = 0
        one = 1
        two = 1
        for i in range(3,n+1):
            t = two + one + zero
            two, one, zero = t, two, one
        return two