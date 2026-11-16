# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # at every step, check if p and q are both in the left, both in the right, or on separate sides
        # if separate sides, return the current node
        # if same side, dig deeper
        # if p or q is the current node then return this node

        # function to check which side of the tree p and q are in
        def findNode(node, compareNode):
            if not node:
                return False
            if node.val == compareNode.val:
                return True
            if findNode(node.left, compareNode):
                return True
            if findNode(node.right, compareNode):
                return True
            return False
        
        while True:
            if root.val == p.val or root.val == q.val:
                return root
            p_left = findNode(root.left, p)
            q_left = findNode(root.left, q)
            print(root.val, p_left, q_left)
            if p_left and q_left:
                root = root.left
            elif not p_left and not q_left:
                root = root.right
            else:
                return root