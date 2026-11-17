# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # level order traversal
        # pop right and add it to the resutls list
        if not root:
            return []

        results = []
        stack = [root]
        while stack:
            new_stack = []
            for node in stack:
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
            results.append(stack.pop().val)
            stack = new_stack
        return results
