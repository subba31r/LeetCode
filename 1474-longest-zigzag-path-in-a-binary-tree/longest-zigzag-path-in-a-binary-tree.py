# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root,st,count):
            if not root:
                return
            self.res = max(self.res,count)
            dfs(root.left,"left",count+1 if st == "root" or st == "right" else 1)
            dfs(root.right,"right",count+1 if st == "root" or st == "left" else 1)
        dfs(root,"root",0)
        return self.res