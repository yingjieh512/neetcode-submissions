class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # 记录整棵树中找到的最大路径和
        # 初始化为负无穷，因为树中的节点可能全部是负数
        res = float("-inf")

        def dfs(node):
            nonlocal res

            # 如果当前节点为空，返回 0
            # 表示空节点不能提供任何路径贡献
            if not node:
                return 0

            # 递归计算左子树能够提供的最大路径和
            # 如果左子树的贡献是负数，就不要这条路径
            # 因为负数只会让我们的路径和变小
            left = max(dfs(node.left), 0)

            # 递归计算右子树能够提供的最大路径和
            # 同样，如果贡献是负数，就选择 0
            right = max(dfs(node.right), 0)

            # 计算经过当前节点的最大路径和
            # 路径可以是：
            # 左子树 -> 当前节点 -> 右子树
            currentSum = node.val + left + right

            # 更新整棵树的最大路径和
            # 注意：这条完整路径不一定能继续延伸到父节点
            res = max(res, currentSum)

            # 返回当前节点能够提供给父节点的最大路径和
            # 只能选择左边或者右边的一条路径
            # 因为一条合法路径不能出现分叉
            return node.val + max(left, right)

        # 从根节点开始 DFS
        dfs(root)

        # 返回整棵树中的最大路径和
        return res