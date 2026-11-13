# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        nodes = [root]
        max_depth = 0
        while nodes:
            max_depth += 1
            children_nodes = []
            while nodes:
                current_node = nodes.pop()
                if current_node.left != None:
                    children_nodes.append(current_node.left)
                if current_node.right != None:
                    children_nodes.append(current_node.right)
            nodes = children_nodes
        return max_depth