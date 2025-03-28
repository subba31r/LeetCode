# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        #brute force - dfs on all nodes and dfs on every node path
        # self.res = [0]

        # def path(curSum,root,li):
        #     if root is None:
        #         return

        #     curSum = curSum + root.val
        #     li.append(root.val)
        #     if curSum == targetSum:  
        #         self.res[0] += 1

        #     path(curSum,root.left,li)
        #     path(curSum,root.right,li)
        #     li.pop(-1)    
        
        # def dfs(root):
        #     if not root:
        #         return
        #     path(0,root,[])
        #     dfs(root.left)
        #     dfs(root.right)
            
        # # path(0,root,[])
        # dfs(root)
        # return self.res[0]
        #

        #optimized is to keep track of prefix sum
        prefixSum = {0:1}
        def dfs(root,cur):
            if root is None:
                return 0
            cur = cur+root.val
            total = prefixSum.get(cur-targetSum,0) #count no.of paths ending at the current node
            prefixSum[cur] = prefixSum.get(cur,0)+1
            total += dfs(root.left,cur)
            total += dfs(root.right,cur)

            prefixSum[cur] -= 1 #backtrack to remove the current cumulative sum from hashmap
            return total
        return dfs(root,0)

