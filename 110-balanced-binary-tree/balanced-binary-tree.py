# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return 0, True
            lh, lb = height(root.left)
            rh, rb = height(root.right)
            balance = lb and rb and abs(lh-rh)<=1
            return 1+max(lh,rh), balance
        _,b = height(root)
        return b




        # def height(root):
        #     if root == None:
        #         return 0, True
        #     leftHeight, leftBalanced = height(root.left)
        #     rightHeight, rightBalanced = height(root.right)
        #     balanced = leftBalanced and rightBalanced and abs(leftHeight - rightHeight) <= 1
        #     return 1 + max(leftHeight,rightHeight), balanced
        
        # _, balanced = height(root)
        # return balanced