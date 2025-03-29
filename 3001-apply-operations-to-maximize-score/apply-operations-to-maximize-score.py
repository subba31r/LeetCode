import heapq
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        def getDistinctPrimes(num):
            s = set()
            cur = 2
            while cur*cur <= num:
                while num%cur == 0:
                    num //= cur
                    s.add(cur)
                cur += 1
            if num > 1:
                s.add(num)
            return len(s)

        primeScores = [getDistinctPrimes(num) for num in nums]

        n = len(nums)
        left = [-1] * n
        right = [n] * n
        stack = []

        # Find next greater element to the left
        for i in range(n):
            while stack and primeScores[stack[-1]] < primeScores[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        
        stack = []
        # Find next greater or equal element to the right
        for i in range(n-1, -1, -1):
            while stack and primeScores[stack[-1]] <= primeScores[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        counts = [(right[i] - i) * (i - left[i]) for i in range(n)]

        heap = []
        for i in range(n):
            heapq.heappush(heap, (-nums[i], counts[i]))

        result = 1
        mod = 10**9 + 7
        while k > 0 and heap:
            num, cnt = heapq.heappop(heap)
            current_num = -num
            use = min(cnt, k)
            result = (result * pow(current_num, use, mod)) % mod
            k -= use

        return result