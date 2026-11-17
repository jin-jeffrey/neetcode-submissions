# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def checkValidBST(node, lt, gt):
            if not node:
                return True
            if node.val < lt and node.val > gt:
                return checkValidBST(node.left, node.val, gt) and checkValidBST(node.right, lt, node.val)
            else:
                return False
            

        return checkValidBST(root, float('inf'), float('-inf'))