# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.res = [0]

        def path(curSum,root,li):
            if root is None:
                return

            curSum = curSum + root.val
            li.append(root.val)
            if curSum == targetSum:  
                self.res[0] += 1

            path(curSum,root.left,li)
            path(curSum,root.right,li)
            li.pop(-1)    
        
        def dfs(root):
            if not root:
                return
            path(0,root,[])
            dfs(root.left)
            dfs(root.right)
            
        # path(0,root,[])
        dfs(root)
        return self.res[0]
