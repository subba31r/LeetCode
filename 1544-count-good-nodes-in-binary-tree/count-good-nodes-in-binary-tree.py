# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #num is the max number that we had seen so far
    def countGoodNodes(self, root, num,count):
        if root == None:
            return 0
        if root.val >= num:
            num = root.val#updating the num with the max num that we had
            #seen so far in the path
            count[0] = count[0] + 1
        self.countGoodNodes(root.left,num,count)
        self.countGoodNodes(root.right,num, count)
        return count[0]

    def goodNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        count = [0]
        return self.countGoodNodes(root,root.val,count)