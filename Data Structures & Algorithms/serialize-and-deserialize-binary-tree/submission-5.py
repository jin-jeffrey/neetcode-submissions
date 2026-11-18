# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = ""
        nodes = [root]

        while nodes:
            temp_nodes = []
            for node in nodes:
                if not node:
                    result += "N,"
                else:
                    result += str(node.val) + ","
                    temp_nodes.append(node.left)
                    temp_nodes.append(node.right)
            nodes = temp_nodes
        return result
            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        serialized = data[:-1].split(",")
        if serialized == ["N"]:
            return None
        
        root = TreeNode(serialized[0])
        nodes = [root]
        pos = 0

        while nodes:
            subnodes = []

            for node in nodes:
                left = serialized[pos + 1]
                right = serialized[pos + 2]
                if left != "N":
                    left_node = TreeNode(left)
                    subnodes.append(left_node)
                    node.left = left_node
                if right != "N":
                    right_node = TreeNode(right)
                    subnodes.append(right_node)
                    node.right = right_node
                pos += 2
            nodes = subnodes

        return root



