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

        def check_balance(node):
            # find max depth of left and right and ensure that it is within 1 at each step
            if not node:
                return 0

            left = check_balance(node.left)
            if left == -1:
                return -1
            right = check_balance(node.right)
            if right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return False if check_balance(root) == -1 else True