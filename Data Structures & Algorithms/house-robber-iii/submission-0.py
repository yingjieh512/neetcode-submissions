class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return (0, 0)

            left = dfs(node.left)
            right = dfs(node.right)

            # 不偷当前节点
            skip = max(left) + max(right)

            # 偷当前节点
            take = node.val + left[0] + right[0]

            return (skip, take)

        return max(dfs(root))