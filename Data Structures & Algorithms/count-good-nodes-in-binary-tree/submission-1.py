# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def findGoodNodes(node, path_max):
            if not node:
                return 0

            if node.val >= path_max:
                return 1 + findGoodNodes(node.left, node.val) + findGoodNodes(node.right, node.val)
            else:
                return findGoodNodes(node.left, path_max) + findGoodNodes(node.right, path_max)

        return findGoodNodes(root, root.val)