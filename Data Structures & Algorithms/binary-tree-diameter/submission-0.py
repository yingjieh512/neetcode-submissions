class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def dfs(node):
            nonlocal result

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            result = max(result, left + right)

            return 1 + max(left, right)

        dfs(root)

        return result