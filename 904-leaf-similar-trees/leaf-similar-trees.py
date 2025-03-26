# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def postOrder(root,l):
            if not root:
                return
            postOrder(root.left,l)
            postOrder(root.right,l)
            if not root.left and not root.right:
                l.append(root.val)
            return l
        l1 = postOrder(root1,[])
        l2 = postOrder(root2,[])
        
        return l1 == l2