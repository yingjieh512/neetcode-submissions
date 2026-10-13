class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:

        # 用一个 list 保存 DFS 遍历得到的节点
        res = []

        def dfs(node):

            # 如果当前节点为空
            # 我们也要把空节点记录下来
            # 否则 Deserialize 时无法恢复树的结构
            if not node:
                res.append("N")
                return

            # Preorder: Root -> Left -> Right

            # 先保存当前节点的值
            # 因为最后要拼接成字符串，所以转换成 str
            res.append(str(node.val))

            # 然后遍历左子树
            dfs(node.left)

            # 最后遍历右子树
            dfs(node.right)

        # 从根节点开始 DFS
        dfs(root)

        # 用逗号连接所有元素，生成字符串
        return ",".join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:

        # 将字符串拆成 list
        # 例如 "1,2,N,N,3,N,N"
        # 变成 ["1", "2", "N", "N", "3", "N", "N"]
        vals = data.split(",")

        # 用 index 记录当前读到第几个元素
        # 类似你上一道 Construct Binary Tree 使用的 preIndex
        index = 0

        def dfs():
            nonlocal index

            # 如果当前元素是 "N"
            # 说明当前位置没有节点
            if vals[index] == "N":

                # index 向后移动
                index += 1

                # 返回空节点
                return None

            # 当前元素不是 N
            # 说明需要创建一个 TreeNode
            # int() 将字符串转换成整数
            node = TreeNode(int(vals[index]))

            # 当前节点已经处理完了
            # index 指向下一个元素
            index += 1

            # 根据 Preorder 的顺序
            # 先递归构建左子树
            node.left = dfs()

            # 再递归构建右子树
            node.right = dfs()

            # 返回构建完成的节点
            return node

        # 从第一个元素开始重建整棵树
        return dfs()