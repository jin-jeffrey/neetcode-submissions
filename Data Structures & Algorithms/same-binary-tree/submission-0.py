# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def compareTree(pnode, qnode):
            if not pnode and not qnode:
                return True

            if not pnode or not qnode:
                return False            

            if pnode.val != qnode.val:
                return False

            left = compareTree(pnode.left, qnode.left)
            if not left:
                return False
            right = compareTree(pnode.right, qnode.right)
            if not right:
                return False
            return True

        return compareTree(p, q) 

