class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        cur = root

        while cur:
            if val < cur.val:
                if cur.left is None:
                    cur.left = TreeNode(val)
                    break
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = TreeNode(val)
                    break
                cur = cur.right

        return root