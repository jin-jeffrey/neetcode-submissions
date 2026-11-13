# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        balanced = True
        def check_balance(node):
            nonlocal balanced
            # find max depth of left and right and ensure that it is within 1 at each step
            if not node:
                return 0

            left = check_balance(node.left)
            right = check_balance(node.right)

            if abs(left - right) > 1:
                balanced = False
 
            return 1 + max(left, right)

        check_balance(root)
        return balanced