class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        prime = [True for _ in range(right+1)]
        p=2
        while(p*p<=right):
            if (prime[p] == True):
                for i in range(p * p, right+1, p):
                    prime[i] = False
            p += 1
        prime[1] = False
        cur = []
        for p in range(left, right+1):
            if prime[p]:
                cur.append(p)

        res = [-1,-1]
        if len(cur)<2:
            return res
        
        prev = float('inf')
        for i in range(0,len(cur)-1):
            temp = cur[i+1] - cur[i]
            if temp < prev:
                prev=temp
                res = [cur[i],cur[i+1]]
        return res

