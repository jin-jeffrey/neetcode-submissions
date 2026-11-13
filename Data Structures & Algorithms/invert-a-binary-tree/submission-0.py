# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        head = root

        stack = [head]

        while stack:
            current = stack.pop()
            if not current:
                break
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
            temp = current.left
            current.left = current.right
            current.right = temp

        return head