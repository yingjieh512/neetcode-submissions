class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return None

        # 找到要删除的节点
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            # 没有左子树
            if not root.left:
                return root.right

            # 没有右子树
            if not root.right:
                return root.left

            # 两个子树都存在
            cur = root.right

            # 找右子树最小的节点
            while cur.left:
                cur = cur.left

            # 替换当前节点的值
            root.val = cur.val

            # 删除原来那个后继节点
            root.right = self.deleteNode(root.right, cur.val)

        return root