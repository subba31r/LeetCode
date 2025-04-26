class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        n = 8
        res = [0]*n
        res = [1,1,4,2,1,1,0,0]
        stack = [] -> for idx
        stack = [6,7] cur->

        """
        n = len(temperatures)
        res=[0]*n
        stack = [0]
        for i in range(1,n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return res
