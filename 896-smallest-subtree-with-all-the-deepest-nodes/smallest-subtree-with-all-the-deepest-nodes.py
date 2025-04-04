# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        depth = {None: -1}
        def dfs(root, parent=None):
            if not root:
                return
            depth[root] = depth[parent] + 1
            dfs(root.left,root)
            dfs(root.right,root)
        dfs(root)
        max_depth = max(depth.values())

        def res(root):
            if not root:
                return
            if depth.get(root,None) == max_depth:
                return root
            L, R = res(root.left), res(root.right)
            return root if L and R else L or R

        return res(root)