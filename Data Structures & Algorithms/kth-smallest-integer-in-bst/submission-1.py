# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # build ordered list and return the k-1 index

        def buildTree(node):
            if not node:
                return []
            
            left = buildTree(node.left)
            left.append(node.val)
            left.extend(buildTree(node.right))

            return left
        
        return buildTree(root)[k-1]