# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #using recursion
        if root == None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left,right)+1


        #using queue approach
        # if root==None:
        #     return 0
        # l = 0
        # queue = [root]
        # while queue:
        #     l += 1
        #     n = len(queue)
        #     for i in range(0,len(queue)):
        #         q = queue.pop(0)
        #         if q.left:
        #             queue.append(q.left)
        #         if q.right:
        #             queue.append(q.right)
        # return l

        