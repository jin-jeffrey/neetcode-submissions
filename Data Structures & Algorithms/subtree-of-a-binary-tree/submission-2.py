# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # traverse until root and subroot nodes are the same

        def checkSubtree(rootNode, subRootNode):
            if rootNode == None and subRootNode == None:
                return True
            elif rootNode == None or subRootNode == None or rootNode.val != subRootNode.val:
                return False

            left = checkSubtree(rootNode.left, subRootNode.left)
            if not left:
                return False
            right = checkSubtree(rootNode.right, subRootNode.right)
            if not right:
                return False
            
            return True

        nodes = [root]

        while nodes:
            node = nodes.pop()
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
            if checkSubtree(node, subRoot):
                return True
        return False

