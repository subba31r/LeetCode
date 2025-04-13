# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left,key)
        elif key > root.val:
            root.right = self.deleteNode(root.right,key)
        else:
            #when no children
            if not root.left and not root.right:
                return None
            
            #when there is one chile
            if not root.left or not root.right:
                return root.left if root.left else root.right
            
            #when there are two children
            temp = root.left
            while temp.right:
                temp = temp.right
            root.val = temp.val
            root.left = self.deleteNode(root.left,temp.val)
        return root