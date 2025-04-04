# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        que = [root]
        res = 0
        curLevel = 0
        maxSum = float("-inf")
        while que:
            n = len(que)
            curLevel += 1
            cur = 0
            for i in range(0,n):
                q = que.pop(0)
                cur = cur + q.val
                if q.left:
                    que.append(q.left)
                if q.right:
                    que.append(q.right)
            if cur > maxSum:
                maxSum = cur
                res = curLevel
        return res