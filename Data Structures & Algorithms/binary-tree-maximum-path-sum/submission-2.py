# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # find max path at every node by considering:
        # max of the left, right, left + right + middle,
        maxPathSum = float('-inf')

        def findPathSum(node):
            nonlocal maxPathSum
            if not node:
                return 0
            
            left = findPathSum(node.left)
            right = findPathSum(node.right)
            # want to return the single maximum path sum through a node so it can be used to determine
            # if it is the leg that attributes to the maximum path sum
            maxPathSum = max(maxPathSum, left + right + node.val)
            return max(0, left + node.val, right + node.val)

        findPathSum(root)
        return maxPathSum
