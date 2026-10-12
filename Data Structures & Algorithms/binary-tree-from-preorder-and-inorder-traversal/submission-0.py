class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # 建立 HashMap，记录每个节点的值在 inorder 中的位置
        # 例如 inorder = [2, 1, 3, 4]
        # index = {2: 0, 1: 1, 3: 2, 4: 3}
        # 这样可以 O(1) 找到 root 在 inorder 中的位置
        index = {val: i for i, val in enumerate(inorder)}

        # preIndex 表示当前应该读取 preorder 中的哪个节点
        # 因为 preorder 的顺序是 Root -> Left -> Right
        # 所以每次读取的元素都是当前子树的 root
        preIndex = 0

        # left 和 right 表示当前子树在 inorder 中的范围
        # 注意：不是 preorder 的范围
        def dfs(left, right):
            nonlocal preIndex

            # 如果 left > right
            # 说明当前子树没有任何节点
            # 因此返回 None
            if left > right:
                return None

            # 取出 preorder 中的当前元素
            # 这个元素就是当前子树的 root
            rootVal = preorder[preIndex]

            # 指针向后移动一位
            # 下一次 DFS 就会读取 preorder 的下一个元素
            preIndex += 1

            # 创建当前子树的根节点
            root = TreeNode(rootVal)

            # 找到 root 在 inorder 中的位置
            # mid 左边的元素属于左子树
            # mid 右边的元素属于右子树
            mid = index[rootVal]

            # 递归构建左子树
            # 左子树的 inorder 范围是 [left, mid - 1]
            # 必须先构建左子树，因为 preorder 是 Root -> Left -> Right
            root.left = dfs(left, mid - 1)

            # 递归构建右子树
            # 右子树的 inorder 范围是 [mid + 1, right]
            root.right = dfs(mid + 1, right)

            # 左右子树都构建完成后
            # 返回当前子树的根节点
            return root

        # 从整个 inorder 数组开始构建二叉树
        # 初始范围是 [0, len(inorder) - 1]
        return dfs(0, len(inorder) - 1)