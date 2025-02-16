# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root == None:
            return None
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.left = right
        root.right = left
        return root
        

        # def bfs(tr):
        #     if tr == None:
        #         return
        #     if tr.left and tr.right:
        #         tr.left, tr.right = tr.right, tr.left
        #     elif tr.right:
        #         tr.left, tr.right = tr.right, None
        #     elif tr.left:
        #         tr.left, tr.right = None, tr.left
        #     bfs(tr.left)
        #     bfs(tr.right)
        #     return tr
        # return bfs(root)
