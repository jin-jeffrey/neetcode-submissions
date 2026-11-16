# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = [[root.val]]

        previous_level = [root]
        while previous_level:
            next_level = []
            result_level = []
            for i in range(len(previous_level)):
                node = previous_level[i]
                if node.left:
                    next_level.append(node.left)
                    result_level.append(node.left.val)
                if node.right:
                    next_level.append(node.right)
                    result_level.append(node.right.val)
            previous_level = next_level
            if result_level:
                result.append(result_level)
        return result