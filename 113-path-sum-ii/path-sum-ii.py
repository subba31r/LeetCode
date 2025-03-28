# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []

        def path(curSum,root,li):
            if root is None:
                return

            curSum = curSum + root.val
            li.append(root.val)
            if curSum == targetSum and root.left==None and root.right==None:  
                self.res.append(li.copy())

            
            path(curSum,root.left,li)
            path(curSum,root.right,li)
            li.pop(-1)    
        
        path(0,root,[])
        return self.res