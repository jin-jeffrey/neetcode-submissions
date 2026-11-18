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
        serialized = data.split(",")
        print(data)
        if data == ["N"]:
            return
        # root = TreeNode(data[0])
        # position = 0
        # nodes = [root]
        # print(data)
        # while nodes:
        #     subnodes = []
        #     for node in nodes:
        #         if data[position + 1] != "N":
        #             node.left = TreeNode(data[position + 1])
        #             subnodes.append(node.left)
        #         if data[position + 2] != "N":
        #             node.right = TreeNode(data[position + 2])
        #             subnodes.append(node.right)
        #         position += 2
        #     nodes = subnodes
        
        return root



