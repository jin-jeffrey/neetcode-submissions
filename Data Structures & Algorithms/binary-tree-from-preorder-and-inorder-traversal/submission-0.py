class Solution:
    def buildTree(
        self, preorder: List[int], inorder: List[int]
    ) -> Optional[TreeNode]:
        inorder_index = {value: i for i, value in enumerate(inorder)}

        def build(pre_start, in_start, size):
            if size == 0:
                return None

            root_value = preorder[pre_start]
            root = TreeNode(root_value)

            root_in_index = inorder_index[root_value]
            left_size = root_in_index - in_start

            root.left = build(
                pre_start + 1,
                in_start,
                left_size
            )
            root.right = build(
                pre_start + 1 + left_size,
                root_in_index + 1,
                size - left_size - 1
            )

            return root

        return build(0, 0, len(preorder))