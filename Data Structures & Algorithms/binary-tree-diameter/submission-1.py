# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # consider each node as the pivot point
        # find the longest depth left and longest depth right
        # check if the sum is greater than the current maximum, if so set it
        # return the greatest length left or right for each node
        if not root:
            return 0
        
        self.current_max = 0

        def checkLongestLeg(self, node):
            if not node:
                return 0
            else:
                left_max = checkLongestLeg(self, node.left)
                right_max = checkLongestLeg(self, node.right)
                self.current_max = max(left_max + right_max, self.current_max)
                return 1 + max(left_max, right_max)

        checkLongestLeg(self, root)
        return self.current_max



