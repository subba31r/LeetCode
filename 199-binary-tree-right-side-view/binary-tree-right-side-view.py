# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return []
        q = [root]
        res = [root.val]
        while q:
            if not q:
                return
            quelen = len(q)
            for i in range(quelen):
                r = q.pop(0)
                if r.left:
                    q.append(r.left)
                if r.right:
                    q.append(r.right)
            if len(q)>0:
                res.append(q[-1].val)
        return res
            

        