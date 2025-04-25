class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # https://leetcode.com/problems/sliding-window-maximum/solutions/6367749/notes-for-myself
        q = deque()
        res = []

        for i in range(0,len(nums)):
            if q and i-k>=0 and nums[i-k] == q[0]:
                q.popleft()
            
            while q and q[-1]<nums[i]:
                q.pop()
            q.append(nums[i])

            if i>= k-1:
                res.append(q[0])
        return res
