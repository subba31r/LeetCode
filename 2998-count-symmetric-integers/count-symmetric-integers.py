class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low,high+1):
            s = [int(c) for c in str(i)]
            if len(s)%2 == 0:
                s1 = s[0:len(s)//2]
                s2 = s[len(s)//2:]
                t1 = sum(s1)
                t2 = sum(s2)
                if t1 == t2:
                    count += 1
        return count