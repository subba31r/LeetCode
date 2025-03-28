# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #As this is a binary search tree we could check p and q values with the root value
        #if p and q are less than root value we check only left half and if greater we
        #check right half as this is a BST
        if root is None:
            return None
        #if root value is greater than both p and q val the both p and q will
        #be in the left side of the tree as BST maintains the property 
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        return root
        
        