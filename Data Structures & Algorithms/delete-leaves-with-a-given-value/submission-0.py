class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        if not root:
            return None

        # 先处理左子树
        root.left = self.removeLeafNodes(root.left, target)

        # 再处理右子树
        root.right = self.removeLeafNodes(root.right, target)

        # 最后检查当前节点
        if not root.left and not root.right and root.val == target:
            return None

        return root