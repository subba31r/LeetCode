class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []

        def solve(idx, cursum):
            if idx>=len(candidates) or cursum >= target:
                if cursum == target:
                    res.append(cur.copy())
                return
            cur.append(candidates[idx])
            solve(idx,cursum+candidates[idx])
            cur.pop()
            solve(idx+1,cursum)

        solve(0,0)
        return res














        # res = []

        cur = []
        def solve(idx,cursum):
            if idx >= len(candidates) or cursum >= target:
                if cursum == target:
                    res.append(cur.copy())
                return
            #considering the choice of taking the same element
            cur.append(candidates[idx])
            solve(idx,cursum + candidates[idx])

            #considering the choice of not taking the element
            cur.pop()
            solve(idx+1,cursum)
        solve(0,0)
        return res
        

        
        